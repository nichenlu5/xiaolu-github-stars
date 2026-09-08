# xiaolu-github-stars

自动同步 GitHub 用户 [nichenlu5](https://github.com/nichenlu5) 的公开 Star 收藏，生成结构化 JSON，便于其他工具和 AI 读取与分析。

- 当前收藏总数：**89**
- 数据最后更新时间（UTC）：**2026-09-08T07:18:09Z**
- 数据文件：[`data/stars.json`](data/stars.json)

## 最近 Star 的项目

| 仓库 | 描述 | Star 时间 |
| --- | --- | --- |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. | 2026-09-07T08:38:59Z |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. | 2026-09-07T08:38:42Z |
| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere | 2026-09-07T08:38:07Z |
| [lissy93/dashy](https://github.com/lissy93/dashy) | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! | 2026-09-07T08:37:31Z |
| [HeyPuter/puter](https://github.com/HeyPuter/puter) | 🌐 The Internet Computer! Free, Open-Source, and Self-Hostable. | 2026-09-07T08:37:09Z |
| [littleblack650/black_first](https://github.com/littleblack650/black_first) | 小鱼干 是一款全磁吸、模块化的开源桌宠机器人。它集成了语音识别、姿态感知、表情动画与舵机动作，支持二次开发，适合机器人爱好者、创客和学生入门嵌入式与机器人技术。/XiaoYuGan is an open‑source, fully magnetic modular desktop pet robot. It combines offline voice recognition, motion sensing, expressive animations, and servo movements, making it an ideal learning platform for embedded systems and robotics. | 2026-08-27T07:24:33Z |
| [nandland/getting-started-with-fpgas](https://github.com/nandland/getting-started-with-fpgas) | Verilog and VHDL for book | 2026-08-23T11:48:16Z |
| [STMicroelectronics/x-cube-freertos](https://github.com/STMicroelectronics/x-cube-freertos) |  X-CUBE-FREERTOS (FreeRTOS™ software expansion for STM32Cube) provides a full integration of the FreeRTOS™ kernel in the STM32Cube environment for a set of STM32 series of microcontrollers. | 2026-08-23T11:47:56Z |
| [Despacito0o/FreeRTOS](https://github.com/Despacito0o/FreeRTOS) | 【中文】 全面的 FreeRTOS + STM32 学习资源，从入门到精通。  ✅ 详细移植教程与示例项目 ✅ 开发环境配置指南 ✅ 中英双语文档  适合初学者和专业开发者，加速您的嵌入式开发之旅！  【English】 Comprehensive FreeRTOS + STM32 learning resource from basics to advanced.  ✅ Detailed tutorials with examples ✅ Development setup guides ✅ Bilingual documentation  For beginners and pros - accelerate your embedded journey! | 2026-08-23T11:47:47Z |
| [PavanMudigonda/zero-to-ai](https://github.com/PavanMudigonda/zero-to-ai) | Free AI/ML course with 950+ Jupyter notebooks — Python, deep learning, LLMs, RAG, agents, prompt engineering, fine-tuning, MLOps | 2026-08-23T11:44:52Z |

## 常见编程语言

| 名称 | 数量 |
| --- | ---: |
| Python | 21 |
| TypeScript | 17 |
| Jupyter Notebook | 10 |
| C | 3 |
| JavaScript | 2 |
| HTML | 2 |
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
| ai | 20 |
| llm | 16 |
| awesome | 14 |
| chatgpt | 13 |
| machine-learning | 12 |
| python | 11 |
| openai | 11 |
| prompt-engineering | 10 |
| awesome-list | 10 |
| ai-agents | 9 |
| deep-learning | 9 |
| artificial-intelligence | 8 |
| gpt | 7 |
| agents | 6 |
| self-hosted | 5 |

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
