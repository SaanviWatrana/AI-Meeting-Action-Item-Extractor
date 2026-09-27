# 📋 AI Meeting Action-Item Extractor

An AI-powered meeting assistant that extracts structured action items from meeting transcripts using a Large Language Model (LLM). The system preprocesses transcripts, identifies tasks, owners, deadlines, statuses, and confidence scores, validates the extracted information, and evaluates the results against annotated ground truth.

> **Developed as Project 2 for the BharatSkillz AI Internship.**

---

## Problem Statement

Meeting transcripts often contain important action items that are difficult to track manually. Team members may miss assigned tasks, deadlines, or ownership details, leading to reduced productivity.

This project automates the extraction of actionable tasks from meeting transcripts while preserving structured information that can be validated and evaluated.

---

## Project Objective

Build an AI/NLP pipeline that converts meeting transcripts into structured action items containing:

- Task
- Owner
- Deadline
- Status
- Confidence

The project focuses on **information extraction**, not meeting summarization.

---

## Features

- Extracts action items using **Qwen2.5-0.5B-Instruct**
- Preserves speaker information during preprocessing
- Produces structured JSON output
- Validates extracted information
- Evaluates predictions against annotated ground truth
- Simple Streamlit interface with sample transcripts and file upload support

---

## Project Architecture

```text
Meeting Transcript
        │
        ▼
Preprocessing
(Speaker & Sentence Segmentation)
        │
        ▼
Qwen2.5-0.5B-Instruct
(LLM Information Extraction)
        │
        ▼
Structured JSON Output
        │
        ▼
Validation Module
        │
        ▼
Evaluation Module
        │
        ▼
Streamlit Interface
```

---

## Folder Structure

```text
ai-meeting-action-item-extractor/
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
│   │   ├── meeting_001.txt
│   │   ├── meeting_002.txt
│   │   ├── meeting_003.txt
│   │   ├── meeting_004.txt
│   │   └── meeting_005.txt
│   │
│   └── annotations/
│       └── ground_truth.json
│
└── .venv/
```

---

## Dataset

The project uses **five meeting transcripts** stored in:

```text
data/raw/
```

Each transcript has corresponding annotated ground truth stored in:

```text
data/annotations/ground_truth.json
```

Each annotation includes:

- Task
- Owner
- Deadline
- Status

These annotations are used to evaluate model performance.

---

## Preprocessing

The preprocessing pipeline performs:

- Transcript loading
- Speaker identification
- Sentence segmentation
- Speaker-aware statement preservation

### Example

**Input**

> Priya: Rahul, please fix the validation issue by Friday.

**Processed Output**

```json
{
  "speaker": "Priya",
  "text": "Rahul, please fix the validation issue by Friday."
}
```

---

## AI Model

### Selected Model

**Qwen2.5-0.5B-Instruct**

### Why this model?

- Lightweight enough for CPU execution
- Instruction-tuned for structured extraction tasks
- Generates structured JSON output
- Suitable for an internship-scale implementation

### Limitations

Like many LLMs, the model may occasionally:

- assign an incorrect owner
- infer an incorrect status
- extract an extra task from contextual statements

These behaviors are intentionally measured during evaluation rather than hidden.

---

## Information Extraction

The model extracts:

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

## Validation

The validation module checks for:

- Missing owners
- Missing deadlines
- Duplicate tasks
- Unexpected status values
- Confidence normalization

### Example

```text
Status: In Progress
↓
Normalized to:
Status: in progress
```

---

## Evaluation Methodology

Predictions are compared against annotated ground truth.

The evaluator measures:

- Overall Accuracy
- Task Accuracy
- Owner Accuracy
- Deadline Accuracy
- Status Accuracy

### Sample Evaluation Output

| Metric | Score |
|--------|------:|
| Overall Accuracy | 0.58 |
| Task Accuracy | 0.67 |
| Owner Accuracy | 0.67 |
| Deadline Accuracy | 1.00 |
| Status Accuracy | 0.00 |

### Example Error Analysis

| Task | Expected Owner | Predicted Owner |
|------|---------------|----------------|
| Fix validation issue | Rahul | Rahul |
| Update API documentation | Ananya | Ananya |
| Add automated login tests | Rahul | Vikram |

This demonstrates how the evaluation module identifies genuine model errors instead of masking them.

---

## Streamlit Interface

The application allows users to:

- Select one of five sample meeting transcripts
- Upload a custom transcript
- Extract structured action items
- View validation results

---

## Screenshots

### Home Screen

![Home Screen](assets/home.png)

### Extraction Results

![Extraction Results](assets/results.png)

### Evaluation Results

![Evaluation Results](assets/evaluation.png)

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core development |
| Hugging Face Transformers | LLM integration |
| Qwen2.5-0.5B-Instruct | Information extraction |
| PyTorch | Model inference |
| Streamlit | User interface |
| Pandas | Data handling |
| RapidFuzz | Duplicate detection |

---

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/ai-meeting-action-item-extractor.git
cd ai-meeting-action-item-extractor
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

## Running the Project

### Run the extraction pipeline

```bash
python model_extractor.py
```

### Launch the Streamlit interface

```bash
streamlit run app.py
```

---

## Example Workflow

1. Select `meeting_001` from the dropdown.
2. Click **Extract Action Items**.
3. View the extracted tasks.
4. Review validation results.
5. Compare predictions with annotated ground truth.

---

## Future Improvements

Potential future enhancements include:

- stronger owner resolution
- improved status classification
- larger annotated datasets
- optimized prompting for higher extraction accuracy
- batch transcript evaluation

---

## Learning Outcomes

This project demonstrates practical experience with:

- Large Language Models (LLMs)
- NLP information extraction
- Prompt engineering
- Data preprocessing
- Validation pipelines
- Model evaluation
- Streamlit application development
- Git/GitHub project organization

---

## Project Status

**Completed as part of the BharatSkillz AI Internship.**

The project successfully implements an end-to-end AI workflow for meeting action-item extraction, including preprocessing, LLM-based information extraction, validation, evaluation, and a working Streamlit interface.