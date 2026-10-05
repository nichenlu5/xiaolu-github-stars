# xiaolu-github-stars

自动同步 GitHub 用户 [nichenlu5](https://github.com/nichenlu5) 的公开 Star 收藏，生成结构化 JSON，便于其他工具和 AI 读取与分析。

- 当前收藏总数：**104**
- 数据最后更新时间（UTC）：**2026-10-05T09:13:21Z**
- 数据文件：[`data/stars.json`](data/stars.json)

## 最近 Star 的项目

| 仓库 | 描述 | Star 时间 |
| --- | --- | --- |
| [Sens-Wear/python-sdk](https://github.com/Sens-Wear/python-sdk) | Python SDK for connecting to SensWear hardware over BLE. | 2026-10-05T07:13:34Z |
| [Sens-Wear/hardware](https://github.com/Sens-Wear/hardware) |  | 2026-10-05T07:13:22Z |
| [Sens-Wear/firmware](https://github.com/Sens-Wear/firmware) | Firmware of the Sens Wear wearable platform. | 2026-10-05T07:13:08Z |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | The best ChatGPT that $100 can buy. | 2026-10-05T07:10:03Z |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning | 2026-10-05T07:09:47Z |
| [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | Standard Open Arm 100 | 2026-10-05T07:09:29Z |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. | 2026-10-05T07:07:57Z |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. | 2026-10-05T07:07:42Z |
| [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent. | 2026-10-05T07:07:25Z |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all | 2026-09-30T11:32:58Z |

## 常见编程语言

| 名称 | 数量 |
| --- | ---: |
| Python | 25 |
| TypeScript | 19 |
| Jupyter Notebook | 11 |
| HTML | 4 |
| C | 4 |
| JavaScript | 4 |
| Go | 2 |
| Rust | 2 |
| CSS | 2 |
| Java | 1 |
| Vue | 1 |
| VHDL | 1 |
| PHP | 1 |
| MDX | 1 |
| Jinja | 1 |

## 常见 Topics

| 名称 | 数量 |
| --- | ---: |
| ai | 21 |
| llm | 17 |
| chatgpt | 14 |
| awesome | 14 |
| machine-learning | 13 |
| python | 13 |
| ai-agents | 11 |
| openai | 11 |
| prompt-engineering | 10 |
| awesome-list | 10 |
| deep-learning | 9 |
| artificial-intelligence | 8 |
| agent | 7 |
| mcp | 7 |
| gpt | 7 |

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
