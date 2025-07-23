# GPT Table Extractor 🚀

A lightweight and powerful pipeline for extracting structured tabular data from semi-structured Excel spreadsheets using **Large Language Models (LLMs)** like **OpenAI's GPT**.

This project demonstrates practical usage of GPT for real-world data extraction tasks, showcasing how LLMs can be integrated into automated data pipelines.

---

## 🔍 Overview

Working with real-world Excel files often means dealing with inconsistent formatting, missing headers, and embedded metadata. Traditional parsing methods struggle with such variability.

This tool leverages **OpenAI GPT (via ChatCompletion API)** to:

- Identify metadata blocks in spreadsheets
- Convert semi-structured tables into clean, structured JSON
- Handle multiple sheets and diverse formatting patterns

---

## ⚙️ Features

- ✅ End-to-end pipeline using OpenAI GPT
- ✅ Works with messy, real-world Excel files
- ✅ Modular Python design
- ✅ Easily extensible to other LLMs

---

## 📁 Project Structure

```
gpt-table-extractor/
├── data/                  # Input Excel files (put your files here)
├── src/                   # All source code
│   ├── config.py          # API key configuration
│   ├── gpt_extractor.py   # LLM-based block extraction
│   └── run_pipeline.py    # Main script to run
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Quick Start

1. **Install requirements**

```bash
pip install -r requirements.txt
```

2. **Add your OpenAI API key**

Set your key in an environment variable or directly in `src/config.py`.

3. **Run the pipeline**

```bash
python src/run_pipeline.py
```

You'll see extracted structured outputs for each table block, powered by GPT.

---

## 📦 Input Format

The dummy Excel (`data/dummy_data.xlsx`) includes two sheets with structured tables below a metadata row (e.g., "Main Class of Business"). You can replace this with your own file.

---

## 🤖 Powered By

- [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/guides/gpt)
- `pandas` for Excel manipulation
- `openpyxl` for spreadsheet support

---

## 💡 Use Cases

- Insurance/reinsurance profile extraction
- Financial reports parsing
- Government and policy document digitization
- Any scenario requiring **AI-assisted table extraction**

---

## 📬 Contact

Want to collaborate or extend this idea? Reach out!

