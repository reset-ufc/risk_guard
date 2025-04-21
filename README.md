# 🎓 Intrinsic Motivation Inventory Questionnaire | Comparative Study – Traditional Class vs. RiskGuard Game

This repository contains the initial analysis for a study comparing the effectiveness and impact of a game ("RiskGuard") to a traditional class format on the topic of **Web Application Security**, specifically focusing on **Software Vulnerabilities and Security Patterns**.

## 📁 Repository Structure

- **`data/`**  
  - `IMI_AulaTradicional.xlsx`: Responses from the traditional class  
  - `IMI_RiskGuard.xlsx`: Responses from the RiskGuard game  

- **`notebooks/`**  
  - `analysis.ipynb`: Main Jupyter notebook for data analysis  

## 📝 Description

The data consists of responses to a **7-point Likert scale questionnaire**, aimed at evaluating students' perceptions across various dimensions such as:

- Interest / Engagement / Enjoyment  
- Effort / Dedication / Energy  
- Competence / Self-efficacy / Performance  
- Anxiety / Calmness / Pressure  
- Value / Utility / Importance  
- Disinterest / Demotivation  

The analysis includes:
- Data preprocessing and normality tests  
- Visualization of the distribution of questionnaire responses using boxplots    
- Statistical comparisons between groups (traditional vs. game)  
- Effect size calculations  
- Grouping of semantically similar questions for composite interpretation  

## 📊 Objective

To investigate whether the **RiskGuard game-based approach** offers measurable benefits in terms of student engagement, motivation, and perceived learning outcomes compared to a **traditional lecture-based format**.

## ⚙️ Requirements

This project uses Python and common data science libraries. To run the notebook, make sure you have:

- Python 3.8+
- pandas
- numpy
- scipy
- matplotlib / seaborn
- openpyxl
