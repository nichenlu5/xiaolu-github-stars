import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError

import sync_stars


class FakeResponse:
    def __init__(self, payload, link=None):
        self.payload = json.dumps(payload).encode()
        self.headers = {"Link": link} if link else {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None

    def read(self):
        return self.payload


def api_item(full_name="owner/repo", starred_at="2026-01-01T00:00:00Z"):
    owner, name = full_name.split("/")
    return {
        "starred_at": starred_at,
        "repo": {
            "name": name, "full_name": full_name, "owner": {"login": owner},
            "description": "description", "html_url": f"https://github.com/{full_name}",
            "homepage": None, "language": "Python", "topics": ["example"],
            "stargazers_count": 1, "forks_count": 0, "archived": False,
            "created_at": "2020-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
            "pushed_at": "2026-01-01T00:00:00Z",
        },
    }


class SyncStarsTests(unittest.TestCase):
    def test_fetch_follows_next_link(self):
        responses = [
            FakeResponse([api_item("a/one")], '<https://api.github.test/page=2>; rel="next", <x>; rel="last"'),
            FakeResponse([api_item("b/two")]),
        ]
        calls = []

        def opener(request, timeout):
            calls.append(request.full_url)
            return responses.pop(0)

        result = sync_stars.fetch_starred_repositories("user", opener=opener)
        self.assertEqual(2, len(result))
        self.assertEqual("https://api.github.test/page=2", calls[1])

    def test_generated_json_parses_and_full_names_are_unique(self):
        repos = sync_stars.normalize([api_item("a/one"), api_item("b/two")])
        document = sync_stars.build_document("user", repos, "2026-01-01T00:00:00Z")
        parsed = json.loads(json.dumps(document, ensure_ascii=False))
        names = [repo["full_name"] for repo in parsed["repositories"]]
        self.assertEqual(len(names), len(set(names)))

    def test_empty_result_does_not_overwrite_existing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / "data.json"
            readme = Path(directory) / "README.md"
            data.write_text('{"valid": true}\n', encoding="utf-8")
            readme.write_text("existing\n", encoding="utf-8")
            with patch("sync_stars.fetch_starred_repositories", return_value=[]):
                with self.assertRaises(sync_stars.SyncError):
                    sync_stars.sync("user", data, readme)
            self.assertEqual('{"valid": true}\n', data.read_text(encoding="utf-8"))
            self.assertEqual("existing\n", readme.read_text(encoding="utf-8"))

    def test_network_error_does_not_overwrite_existing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / "data.json"
            readme = Path(directory) / "README.md"
            data.write_text('{"valid": true}\n', encoding="utf-8")
            readme.write_text("existing\n", encoding="utf-8")
            with patch("sync_stars.fetch_starred_repositories", side_effect=sync_stars.SyncError("network")):
                with self.assertRaises(sync_stars.SyncError):
                    sync_stars.sync("user", data, readme)
            self.assertEqual('{"valid": true}\n', data.read_text(encoding="utf-8"))
            self.assertEqual("existing\n", readme.read_text(encoding="utf-8"))

    def test_fetch_reports_network_error(self):
        def opener(request, timeout):
            raise URLError("offline")
        with self.assertRaisesRegex(sync_stars.SyncError, "Network error"):
            sync_stars.fetch_starred_repositories("user", opener=opener)


if __name__ == "__main__":
    unittest.main()
