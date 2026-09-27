# 📋 AI Meeting Action-Item Extractor

<div align="center">

### AI-powered meeting transcript analysis using Qwen2.5-0.5B, Python, Hugging Face Transformers, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.14-red?style=for-the-badge&logo=pytorch)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b?style=for-the-badge&logo=streamlit)
![LLM](https://img.shields.io/badge/LLM-Qwen2.5-success?style=for-the-badge)

**Developed as Project 2 for the BharatSkillz AI Internship**

</div>

---

# 🚀 Executive Summary

Teams lose valuable follow-up tasks inside lengthy meeting transcripts.

This project solves that problem by automatically extracting **structured action items**—including task, owner, deadline, status, and confidence score—using a lightweight Large Language Model while validating and evaluating the extracted information.

Instead of generating a generic summary, the system focuses on **actionable task extraction**, making it useful for project management workflows.

---

# 📖 Project Case Study

## The Challenge

During meetings, important commitments are often buried inside long conversations.

Manual note-taking can result in:

- Missed deadlines
- Forgotten owners
- Duplicate follow-ups
- Poor task tracking

The objective was to build an AI system capable of identifying actionable commitments automatically.

---

## My Approach

I built an end-to-end NLP pipeline that:

1. Loads meeting transcripts.
2. Preserves speaker information.
3. Segments conversations into meaningful statements.
4. Uses **Qwen2.5-0.5B-Instruct** for structured information extraction.
5. Validates extracted fields.
6. Evaluates predictions against annotated ground truth.
7. Displays results through a Streamlit interface.

---

# 🏗️ System Architecture

```text
Meeting Transcript
        │
        ▼
Preprocessing
(Speaker + Sentence Segmentation)
        │
        ▼
Qwen2.5-0.5B-Instruct
        │
        ▼
Structured JSON
        │
        ▼
Validation
        │
        ▼
Evaluation
        │
        ▼
Streamlit Dashboard
```

---

# ✨ Key Features

- Speaker-aware preprocessing
- LLM-powered action-item extraction
- Structured JSON output
- Validation for missing owners and deadlines
- Duplicate task detection
- Ground truth evaluation
- Interactive Streamlit dashboard

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core development |
| Hugging Face Transformers | LLM integration |
| Qwen2.5-0.5B-Instruct | Information extraction |
| PyTorch | Model inference |
| Streamlit | Web interface |
| Pandas | Data handling |
| RapidFuzz | Duplicate detection |

---

# 📂 Project Structure

```text
AI-Meeting-Action-Item-Extractor/
│
├── app.py
├── preprocessing.py
├── model_extractor.py
├── validator.py
├── evaluator.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── home.png
│   ├── results.png
│   └── evaluation.png
│
├── data/
│   ├── raw/
│   └── annotations/
│
└── .gitignore
```

---

# 📊 Results

The project successfully extracts structured action items containing:

- Task
- Owner
- Deadline
- Status
- Confidence

### Example Output

```json
{
  "task": "Fix the validation issue",
  "owner": "Rahul",
  "deadline": "Friday",
  "status": "assigned",
  "confidence": 0.96
}
```

---

# 📈 Evaluation

The evaluation module compares predictions against annotated ground truth.

| Metric | Result |
|--------|-------:|
| Overall Accuracy | 0.58 |
| Task Accuracy | 0.67 |
| Owner Accuracy | 0.67 |
| Deadline Accuracy | 1.00 |
| Status Accuracy | 0.00 |

### Example Error Analysis

| Task | Expected | Predicted |
|------|----------|-----------|
| Fix validation issue | Rahul | Rahul |
| Update API documentation | Ananya | Ananya |
| Add automated login tests | Rahul | Vikram |

Rather than hiding mistakes, the evaluator highlights genuine model limitations.

---

# 🖥️ Application Preview

## Home Screen

![Home](assets/home.png)

---

## Extraction Results

![Results](assets/results.png)

---

## Evaluation Dashboard

![Evaluation](assets/evaluation.png)

---

# 🔄 Workflow

1. Choose one of five sample meeting transcripts.
2. Upload a custom transcript (optional).
3. Run AI extraction.
4. Generate structured JSON.
5. Validate extracted fields.
6. Compare predictions with annotated ground truth.

---

# ⚡ Installation

Clone the repository.

```bash
git clone https://github.com/SaanviWatrana/AI-Meeting-Action-Item-Extractor.git
cd AI-Meeting-Action-Item-Extractor
```

Create a virtual environment.

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Run the extraction pipeline.

```bash
python model_extractor.py
```

Launch the Streamlit app.

```bash
streamlit run app.py
```

---

# 💡 Challenges Solved

During development I worked through several practical implementation challenges:

- Preserving speaker context.
- Improving prompts for consistent JSON generation.
- Normalizing inconsistent status values.
- Building a validation pipeline.
- Evaluating outputs against annotated data.
- Optimizing the application for CPU execution.

---

# 📚 Learning Outcomes

This project strengthened my understanding of:

- Large Language Models
- NLP information extraction
- Prompt engineering
- Hugging Face Transformers
- PyTorch inference
- Validation pipelines
- Streamlit application development
- Git and GitHub workflows

---

# 🚀 Future Improvements

Potential next steps include:

- Better owner resolution
- Improved status classification
- Larger annotated datasets
- Batch transcript processing
- Higher extraction accuracy through prompt optimization

---

# 🎯 Why This Project Matters

This project demonstrates an end-to-end AI workflow—from data preprocessing and LLM-based extraction to validation, evaluation, and deployment—making it a strong portfolio project for AI, Data Analytics, and Product Management internship applications.

---

<div align="center">

### ⭐ If you found this project interesting, consider starring the repository.

Built with ❤️ using Python, Hugging Face, and Streamlit.

</div>