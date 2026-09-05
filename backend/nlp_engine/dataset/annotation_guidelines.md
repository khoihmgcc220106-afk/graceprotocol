# Phonological Error Annotation Guidelines

## 1. Objective
Identify, categorize, and tag regional phonetic spelling errors in raw Vietnamese text to train the NLP normalization engine.

## 2. Methodology
*   Annotators must strictly map identified errors to the predefined IDs in `taxonomy.json`.
*   Data must be split into `train/` (80%) and `eval/` (20%) directories in JSONL format.

## 3. Data Structure Example
Each annotated record must follow this format:
`{"original": "con châu", "corrected": "con trâu", "error_ids": ["tr_ch_confusion"]}`