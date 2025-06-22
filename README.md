---
title: First Agent Template
emoji: ⚡
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 5.23.1
app_file: app.py
pinned: false
tags:
- smolagents
- agent
- smolagent
- tool
- agent-course
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# 🤖 Simple Agent Project

Welcome to the **Simple Agent Project** — an elegant and modular simple AI agent system powered by [SmolAgents](https://github.com/huggingface/smol-agents), capable of solving complex tasks using structured reasoning, tool use, and code execution. Designed with usability and extensibility in mind, this project features a dynamic Gradio-based interface, plug-and-play tools, and a powerful HuggingFace model backend.

---

## ✨ Features

- 🔁 **Multi-Step Reasoning** with an agent that can plan, execute code, and invoke tools.
- 🌐 **Web Search Tool** via DuckDuckGo for live queries.
- 🧭 **Webpage Reader Tool** to fetch and parse web pages in Markdown.
- 📅 **Time and Weather Tools** for real-time timezone and temperature queries.
- 🖼️ **Image Generation** support using HuggingFace tool hub.
- 🎯 **Gradio UI Integration** with step-wise conversational tracing.
- 📦 Modular structure — easily extensible with custom tools.

---

## 🧠 Project Structure

```bash
.
├── app.py                  # Main entrypoint - defines tools, loads agent, and launches Gradio UI
├── Gradio_UI.py           # Elegant multi-step UI for interaction using Gradio
├── tools/final_answer.py        # Defines a final answer tool to conclude tasks
├── tools/visit_webpage.py       # Tool to visit a URL and extract readable markdown content
├── tools/web_search.py          # Tool for DuckDuckGo web search queries
├── requirements.txt       # Python dependencies
├── agent.json             # Agent configuration (tools, model, prompts, rules)

```

---

## 🧰 Built-in Tools

| Tool Name         | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `web_search`      | Search the web using DuckDuckGo                                             |
| `visit_webpage`   | Visit and parse the content of a webpage as markdown                        |
| `get_temperature` | Get real-time temperature of a given city                                   |
| `get_current_time_in_timezone` | Get local time in a specified timezone                         |
| `final_answer`    | Returns the final response to a task                                        |
| `text-to-image`   | Generates images using HuggingFace image generation API (remote tool)       |

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the App

```bash
python app.py
```

This will launch a Gradio interface where you can interact with your agent conversationally.

---

## 🌈 Sample Tasks

Try asking the agent:

- "What is the current temperature in Tokyo?"
- "Find the age of the Pope and raise it to the power of 0.36"
- "Search for latest news on Mars exploration"
- "Generate an image of a futuristic AI-powered city"
- "What’s the current time in New York?"

---

## 🛠️ Under the Hood

### 🧠 Agent Model
- Powered by [`Qwen/Qwen2.5-Coder-32B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
- HuggingFace API wrapper (`HfApiModel`) with streaming and code execution.

### 💬 Prompt Planning Logic
- Configured in `agent.json` with step-by-step templates, planning logic, and reasoning strategy.
- Structured prompt system encourages:
  - Thought → Code → Observation → Final Answer loops

---

## 🖼️ UI Highlights

- 💬 Chat-based interface with message tracking
- ⚙️ Shows tool usage logs, execution reasoning, and token statistics
- 📁 Supports file uploads (PDF, DOCX, TXT)
- 🧵 Maintains step context and memory

---

## 🔧 Customize or Extend

### Adding Your Own Tool

You can add custom tools easily by subclassing `Tool`. Example:
```python
from smolagents.tools import Tool

class MyTool(Tool):
    name = "my_tool"
    description = "Describe what your tool does here."
    inputs = {'input1': {'type': 'string', 'description': 'Your input'}}
    output_type = "string"

    def forward(self, input1: str) -> str:
        # Your logic
        return "Output result"
```

Then add it in `app.py` to the agent's tools list.

---

## 📜 License

This project is licensed under the Apache 2.0 License. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.

---

## 🌟 Acknowledgements

Built using:

- 🤖 [SmolAgents](https://github.com/huggingface/smol-agents)
- 🌐 [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)
- 🧾 [Markdownify](https://pypi.org/project/markdownify/)
- 🔥 [Gradio](https://gradio.app/)
- 🧠 [Qwen Model on HuggingFace](https://huggingface.co/Qwen)

