# 🎓 RiskGuard: A Card-Based Serious Game for Enhancing Education on Security Patterns and Software Vulnerabilities in Web Systems

This repository contains the analysis supporting the paper “RiskGuard: A Card-Based Serious Game for Enhancing Education on Security Patterns and Software Vulnerabilities in Web Systems”. It compares the effectiveness and impact of the RiskGuard educational game against a traditional lecture-based approach in the context of Web Application Security, with a particular focus on Software Vulnerabilities and Security Patterns.

## 📁 Repository Structure

- **`data/`**  
  - `experiment_Anon.xlsx`: Separation of experimental and control groups
  - `IMI_TradictioalLecture_Anon.xlsx`: IMI Responses from the traditional class
  - `IMI_RiskGuad_Anon.xlsx`: IMI Responses from the RiskGuard game   
  - `KnowledgeAssessment_PrePost_test_Anon.xlsx`: Learning test results (pre/post-game)  
  - `CharacterizationForm_Anon.xlsx`: Characterization form responses

- **`notebooks/`**  
  - `RQ1.ipynb`: Main Jupyter notebook for RQ1 data analysis
  - `RQ2.ipynb`: Main Jupyter notebook for RQ2 data analysis

- **`figures/`**  
  - `boxplots_imi.png`: Motivation subscale comparison plots  
  - `learning_gain_distribution.png`: Learning outcomes visualization

- **`game_material/`** : contain the cards, and game rules 

- **`study_artifacts/`** : contain the main study artifacts


## 📝 Description

The dataset includes responses from participants who attended both teaching modalities — **traditional lecture** and **lecture + RiskGuard** — and answered the **Intrinsic Motivation Inventory (IMI)** questionnaire on a 7-point Likert scale.  
The questions are grouped into the following motivational subscales:

- Interest / Engagement / Enjoyment  
- Effort / Dedication / Energy  
- Competence / Self-efficacy / Performance  
- Anxiety / Calmness / Pressure  
- Value / Utility / Importance  
- Disinterest / Demotivation  

The analysis pipeline includes:
- Data preprocessing and reliability checks  
- Visualization of IMI subscales (boxplots, histograms, descriptive statistics)  
- Learning score comparison (traditional vs. RiskGuard)  
- Statistical testing (normality, significance, and effect size)  
- Interpretation of composite and subscale results  

## 🧩 Research Questions

### **RQ1 — Does RiskGuard improve students’ learning outcomes compared to a traditional lecture format?**

To answer RQ1, we tested two hypotheses:  
- **H₀:** There is no significant difference in participants’ learning between the two approaches (with and without RiskGuard).  
- **H₁:** There is a significant difference in learning outcomes between the two approaches.

**Learning Measurement:**  
Learning was measured through two *Knowledge Assessment Forms*: one after the traditional lecture and another after the RiskGuard session. Each form contained 12 multiple-choice questions. Learning gain was calculated as the difference between post-game and post-lecture scores (ranging from –12 to +12).  
We also computed the **normalized gain (g)** = (Post – Pre) / (Max – Pre), with *Max = 12*, allowing a relative measure of learning improvement.

We controlled for two moderating factors:  
- **Experience Level:** Participants were grouped as *Less-experienced* or *More-experienced* based on self-reported familiarity with security concepts.  
- **Academic Performance (IRA):** Participants were classified as *High IRA* or *Low IRA* according to institutional academic performance indices.

Interaction effects were tested for **Group × Experience** and **Group × IRA** to examine whether the learning gains were moderated by experience or academic background. Statistical significance was verified using Shapiro-Wilk normality tests, followed by parametric or non-parametric tests (t-tests or Mann–Whitney U), with effect sizes reported via Cohen’s *d* or rank-biserial correlation.

### **RQ2 — Does the use of RiskGuard influence students’ motivation compared to traditional instruction?**

RQ2 focused on whether RiskGuard enhanced **intrinsic motivation** as measured by IMI subscales.

We tested the following general hypotheses:  
- **H₀:** There is no significant difference in motivation between RiskGuard and traditional lecture conditions.  
- **H₁:** There is a significant difference in motivation between the two conditions.

**Motivation Measurement:**  
Each IMI item was rated on a 7-point Likert scale. Reverse-coded items were adjusted as |response – 8|. Subscale scores were averaged, and the **overall motivation score** was computed as:  

> **Motivation = INT + CMP – PRS + EFF + VAL**  

where INT = Interest/Enjoyment, CMP = Perceived Competence, PRS = Pressure/Tension (inverted), EFF = Effort/Importance, VAL = Value/Usefulness.

Two comparisons were made:
1. **Within the experimental group** — traditional lecture (before RiskGuard) vs. lecture + RiskGuard (after game).  
2. **Between groups** — experimental (with RiskGuard) vs. control (only traditional lecture).  

Each IMI subscale (INT, CMP, EFF, VAL, PRS) had its own hypothesis pair (H₀/H₁) to identify specific motivational effects. Statistical significance was evaluated at 95% confidence (α = 0.05).

This analysis triangulates motivational data across both experimental and control conditions to ensure that observed differences are attributable to RiskGuard rather than external classroom effects.

## 📊 Objective

The objective is to assess whether the **RiskGuard game-based approach** enhances **learning** (RQ1) and **motivation** (RQ2) compared to a **traditional lecture**.  
Together, these analyses provide insights into how game-based learning can impact both cognitive and affective dimensions of web security education.

## ⚙️ Requirements

This project uses Python and standard data science libraries. To run the notebooks, install:

- Python 3.10+
- pandas
- numpy
- scipy
- matplotlib 
- seaborn
- openpyxl

You can install dependencies with:

```bash
pip install -r requirements.txt
```

---

