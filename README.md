# xiaolu-github-stars

自动同步 GitHub 用户 [nichenlu5](https://github.com/nichenlu5) 的公开 Star 收藏，生成结构化 JSON，便于其他工具和 AI 读取与分析。

- 当前收藏总数：**95**
- 数据最后更新时间（UTC）：**2026-10-04T08:31:37Z**
- 数据文件：[`data/stars.json`](data/stars.json)

## 最近 Star 的项目

| 仓库 | 描述 | Star 时间 |
| --- | --- | --- |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all | 2026-09-30T11:32:58Z |
| [codeman008/Financial_freedom](https://github.com/codeman008/Financial_freedom) | Technical guide to making money and investing（最全赚钱投资指南） | 2026-09-29T15:24:51Z |
| [byoungd/up](https://github.com/byoungd/up) | An advanced guide which might benefit you a lot 🎉 . 韩先凯的人生进阶指南 人生进阶指南 离谱的人生 人生进阶 AI学习 AI指南 韩先凯的AI学习指南 英语学习指南/英语学习教程/英语学习/学英语 | 2026-09-29T09:48:00Z |
| [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 | 2026-09-29T03:37:00Z |
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the Codex harness. | 2026-09-08T14:18:43Z |
| [sandraschi/bilibili-mcp](https://github.com/sandraschi/bilibili-mcp) | Bilibili (B站) content-intelligence bridge - search, trending, video intel and transcript summarisation. Anonymous tier works; account tier via +86 cookie. | 2026-09-08T12:28:14Z |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. | 2026-09-07T08:38:59Z |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. | 2026-09-07T08:38:42Z |
| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere | 2026-09-07T08:38:07Z |
| [lissy93/dashy](https://github.com/lissy93/dashy) | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! | 2026-09-07T08:37:31Z |

## 常见编程语言

| 名称 | 数量 |
| --- | ---: |
| Python | 22 |
| TypeScript | 18 |
| Jupyter Notebook | 11 |
| JavaScript | 3 |
| HTML | 3 |
| C | 3 |
| Rust | 2 |
| CSS | 2 |
| Java | 1 |
| Vue | 1 |
| VHDL | 1 |
| PHP | 1 |
| MDX | 1 |
| Jinja | 1 |
| Kotlin | 1 |

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
| mcp | 7 |
| gpt | 7 |
| agents | 6 |

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
