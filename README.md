# xiaolu-github-stars

自动同步 GitHub 用户 [nichenlu5](https://github.com/nichenlu5) 的公开 Star 收藏，生成结构化 JSON，便于其他工具和 AI 读取与分析。

- 当前收藏总数：**124**
- 数据最后更新时间（UTC）：**2026-10-09T09:14:31Z**
- 数据文件：[`data/stars.json`](data/stars.json)

## 最近 Star 的项目

| 仓库 | 描述 | Star 时间 |
| --- | --- | --- |
| [yanirs/established-remote](https://github.com/yanirs/established-remote) | A list of established remote companies | 2026-10-06T02:19:50Z |
| [engineerapart/TheRemoteFreelancer](https://github.com/engineerapart/TheRemoteFreelancer) | Listing of community-curated resources to find topical remote freelance & contract work for software developers, web designers, and more! | 2026-10-06T02:19:43Z |
| [greatghoul/remote-working](https://github.com/greatghoul/remote-working) | 收集整理远程工作相关的资料 | 2026-10-06T02:19:37Z |
| [remoteintech/remote-jobs](https://github.com/remoteintech/remote-jobs) | Source for remoteintech.company — a community-maintained directory of remote-friendly tech companies | 2026-10-06T02:19:30Z |
| [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | Toonflow 是开源 AI 创作平台，融合无限画布、AI Agent 与可视化工作流，支持图像生成、视频生成、智能分镜及短剧创作。支持本地部署、自由接入模型，提供跨平台桌面端，并可通过 MCP 与插件扩展创作能力。Open-source AI creative platform with an infinite canvas, AI agents and visual workflows for image generation, video generation and filmmaking, with a canvas-based approach similar to LibTV and TapNow. | 2026-10-06T02:18:21Z |
| [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama) | 🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video" | 2026-10-06T02:18:15Z |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) |  | 2026-10-06T02:18:03Z |
| [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | 支持小红书自动发布、自动评论、自动检索的 Skill。支持 OpenClaw、Codex、CC 等 | 2026-10-06T02:17:51Z |
| [geekjourneyx/md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill) | 面向 AI Agent 的微信公众号创作与发布 CLI：Markdown 排版、AI 配图、预览与草稿创建；支持由浏览器 Agent 保存知乎、CSDN、头条未发布草稿。 | 2026-10-06T02:17:44Z |
| [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload) | 自动化上传视频到社交媒体：抖音、小红书、视频号、tiktok、youtube、bilibili | 2026-10-06T02:17:37Z |

## 常见编程语言

| 名称 | 数量 |
| --- | ---: |
| Python | 30 |
| TypeScript | 22 |
| Jupyter Notebook | 11 |
| JavaScript | 5 |
| HTML | 4 |
| C | 4 |
| Vue | 3 |
| Go | 3 |
| PHP | 3 |
| MDX | 2 |
| Rust | 2 |
| CSS | 2 |
| Ruby | 1 |
| VHDL | 1 |
| Jinja | 1 |

## 常见 Topics

| 名称 | 数量 |
| --- | ---: |
| ai | 23 |
| llm | 19 |
| python | 15 |
| chatgpt | 15 |
| awesome | 14 |
| machine-learning | 13 |
| ai-agents | 12 |
| openai | 11 |
| prompt-engineering | 10 |
| awesome-list | 10 |
| deep-learning | 9 |
| artificial-intelligence | 8 |
| open-source | 7 |
| agent | 7 |
| mcp | 7 |

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
