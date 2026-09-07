#!/usr/bin/env python3
"""Synchronize a GitHub user's public stars into this repository."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_URL = "https://api.github.com/users/{username}/starred"
ACCEPT = "application/vnd.github.star+json"
USER_AGENT = "xiaolu-github-stars/1.0"
ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "stars.json"
README_FILE = ROOT / "README.md"


class SyncError(RuntimeError):
    """A user-facing synchronization failure."""


def _next_link(link_header: str | None) -> str | None:
    if not link_header:
        return None
    for part in link_header.split(","):
        match = re.match(r'\s*<([^>]+)>;\s*rel="([^"]+)"', part)
        if match and match.group(2) == "next":
            return match.group(1)
    return None


def fetch_starred_repositories(
    username: str,
    token: str | None = None,
    opener: Callable[..., Any] = urlopen,
) -> list[dict[str, Any]]:
    """Fetch every page of public stars, including starred_at metadata."""
    query = urlencode({"per_page": 100, "page": 1, "sort": "created", "direction": "desc"})
    url: str | None = f"{API_URL.format(username=username)}?{query}"
    results: list[dict[str, Any]] = []

    while url:
        headers = {
            "Accept": ACCEPT,
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(url, headers=headers)
        try:
            with opener(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
                if not isinstance(payload, list):
                    raise SyncError("GitHub API returned an unexpected response instead of a list.")
                results.extend(payload)
                url = _next_link(response.headers.get("Link"))
        except HTTPError as exc:
            remaining = exc.headers.get("X-RateLimit-Remaining")
            reset = exc.headers.get("X-RateLimit-Reset")
            detail = f"GitHub API request failed with HTTP {exc.code}: {exc.reason}."
            if exc.code == 403 and remaining == "0":
                reset_text = "unknown"
                if reset and reset.isdigit():
                    reset_text = datetime.fromtimestamp(int(reset), timezone.utc).isoformat()
                detail += f" API rate limit exhausted; reset time: {reset_text}. Set GITHUB_TOKEN to increase the limit."
            raise SyncError(detail) from exc
        except URLError as exc:
            raise SyncError(f"Network error while contacting GitHub API: {exc.reason}") from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise SyncError(f"GitHub API returned invalid JSON: {exc}") from exc

    return results


def normalize(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    repositories: list[dict[str, Any]] = []
    for item in items:
        repo = item.get("repo", item)
        owner = repo.get("owner") or {}
        repositories.append(
            {
                "name": repo.get("name"),
                "full_name": repo.get("full_name"),
                "owner": owner.get("login"),
                "description": repo.get("description"),
                "html_url": repo.get("html_url"),
                "homepage": repo.get("homepage"),
                "language": repo.get("language"),
                "topics": sorted(repo.get("topics") or []),
                "stargazers_count": repo.get("stargazers_count"),
                "forks_count": repo.get("forks_count"),
                "archived": bool(repo.get("archived", False)),
                "created_at": repo.get("created_at"),
                "updated_at": repo.get("updated_at"),
                "pushed_at": repo.get("pushed_at"),
                "starred_at": item.get("starred_at"),
            }
        )
    repositories.sort(key=lambda repo: (repo.get("starred_at") or "", repo.get("full_name") or ""), reverse=True)
    return repositories


def build_document(username: str, repositories: list[dict[str, Any]], generated_at: str) -> dict[str, Any]:
    return {
        "metadata": {
            "username": username,
            "total_count": len(repositories),
            "generated_at": generated_at,
            "source": f"https://github.com/{username}?tab=stars",
        },
        "repositories": repositories,
    }


def render_readme(document: dict[str, Any]) -> str:
    metadata = document["metadata"]
    repositories = document["repositories"]
    languages = Counter(repo["language"] for repo in repositories if repo["language"])
    topics = Counter(topic for repo in repositories for topic in repo["topics"])

    def table(counter: Counter[str], limit: int = 15) -> str:
        rows = ["| 名称 | 数量 |", "| --- | ---: |"]
        rows.extend(f"| {name} | {count} |" for name, count in counter.most_common(limit))
        return "\n".join(rows) if len(rows) > 2 else "暂无数据。"

    recent_rows = ["| 仓库 | 描述 | Star 时间 |", "| --- | --- | --- |"]
    for repo in repositories[:10]:
        description = (repo["description"] or "").replace("|", "\\|").replace("\n", " ")
        recent_rows.append(
            f"| [{repo['full_name']}]({repo['html_url']}) | {description} | {repo['starred_at'] or '未知'} |"
        )
    if len(recent_rows) == 2:
        recent = "暂无数据。"
    else:
        recent = "\n".join(recent_rows)

    return f"""# xiaolu-github-stars

自动同步 GitHub 用户 [{metadata['username']}](https://github.com/{metadata['username']}) 的公开 Star 收藏，生成结构化 JSON，便于其他工具和 AI 读取与分析。

- 当前收藏总数：**{metadata['total_count']}**
- 数据最后更新时间（UTC）：**{metadata['generated_at']}**
- 数据文件：[`data/stars.json`](data/stars.json)

## 最近 Star 的项目

{recent}

## 常见编程语言

{table(languages)}

## 常见 Topics

{table(topics)}

## 本地同步

需要 Python 3.9 或更高版本，不依赖第三方包：

```powershell
python sync_stars.py
```

读取公开 Stars 时无需登录。也可以设置环境变量 `GITHUB_TOKEN` 来提高 GitHub API 请求限额：

```powershell
$env:GITHUB_TOKEN = "your-token"
python sync_stars.py
```

Token 不应写入仓库。同步脚本会遍历 GitHub API 返回的全部分页，并以原子替换方式写入数据；请求失败或返回空结果时不会覆盖已有数据。

## 自动同步

GitHub Actions 每天运行一次，也支持在 Actions 页面手动触发。工作流使用仓库自带的 `GITHUB_TOKEN`，仅授予提交同步结果所需的 `contents: write` 权限，并且只在文件实际发生变化时提交。

## 第一版范围

当前仅同步全部 starred repositories。GitHub Star Lists 分类不属于第一版功能。
"""


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def sync(username: str, data_file: Path = DATA_FILE, readme_file: Path = README_FILE) -> bool:
    items = fetch_starred_repositories(username, os.environ.get("GITHUB_TOKEN"))
    repositories = normalize(items)
    if not repositories:
        raise SyncError("GitHub API returned zero starred repositories; existing files were left unchanged.")
    names = [repo["full_name"] for repo in repositories]
    if any(name is None for name in names) or len(names) != len(set(names)):
        raise SyncError("API result contains missing or duplicate full_name values; existing files were left unchanged.")

    if data_file.exists():
        try:
            existing = json.loads(data_file.read_text(encoding="utf-8"))
            if existing.get("repositories") == repositories:
                print(f"Already up to date: {len(repositories)} stars.")
                return False
        except (OSError, json.JSONDecodeError, AttributeError):
            pass

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    document = build_document(username, repositories, generated_at)
    json_text = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
    readme_text = render_readme(document)
    atomic_write(data_file, json_text)
    atomic_write(readme_file, readme_text)
    print(f"Synchronized {len(repositories)} stars for {username}.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default="nichenlu5", help="GitHub username (default: nichenlu5)")
    args = parser.parse_args()
    try:
        sync(args.username)
    except SyncError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
