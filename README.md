# AI-Powered YouTube Blog Generator using CrewAI and Ollama

This project demonstrates an autonomous agent-based pipeline that uses YouTube video content to generate informative and engaging blog posts. It leverages **CrewAI**, **Ollama LLMs**, and the **YoutubeChannelSearchTool** to mimic the collaborative workflow of a human research and writing team.

---

## 🎯 Project Objective

> Automate blog writing by combining YouTube content analysis with LLM-driven agents for research and content creation, specifically targeting technical topics in AI, Data Science, and GenAI.

---

## 🧠 How It Works

- **Blog Researcher Agent**: Searches for and analyzes videos on a specified topic from a YouTube channel.
- **Blog Writer Agent**: Summarizes the research and generates a blog post in markdown format.

The agents work collaboratively via CrewAI to simulate human-like task delegation and execution.

---

## 🛠️ Tech Stack

- 🧠 **[CrewAI](https://github.com/joaomdmoura/crewAI)** – Autonomous multi-agent orchestration
- 🦙 **Ollama LLM** – Local large language models (e.g., `gemma2-9b-it`)
- 📺 **YoutubeChannelSearchTool** – Retrieves video data from specified YouTube channels
- 🐍 **Python 3.10+**

---

## 📁 Folder Structure

📦 YouTube-Blog-Generator/
├── agents.py # Defines the Researcher and Writer agents
├── crew.py # Creates the Crew and kicks off the pipeline
├── tasks.py # Task descriptions and expected outputs
├── tools.py # YouTube search tool setup
└── new-blog-post.md # Output blog post (auto-generated)
