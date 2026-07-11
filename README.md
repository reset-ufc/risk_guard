# 🎓 RiskGuard: A Card-Based Serious Game for Enhancing Education on Security Patterns and Software Vulnerabilities in Web Systems

This repository contains the analysis supporting the paper “RiskGuard: A Card-Based Serious Game for Enhancing Education on Security Patterns and Software Vulnerabilities in Web Systems”. It compares the effectiveness and impact of the RiskGuard educational game against a traditional lecture-based approach in the context of Web Application Security, with a particular focus on Software Vulnerabilities and Security Patterns.

## 📁 Repository Structure

- **`data_en/`** — anonymized study data in **English** (CSV). These are the files the notebooks read.
  - `experiment_Anon.csv`: group assignment (control/experimental) with course and academic performance (IRA)
  - `IMI_TradictioalLecture_Anon.csv`: IMI responses from the traditional lecture
  - `IMI_RiskGuard_Anon.csv`: IMI responses from the RiskGuard session
  - `KnowledgeAssessment_pre_Anon.csv` / `KnowledgeAssessment_post_Anon.csv`: knowledge test results (pre/post)
  - `CharacterizationForm_Anon.csv`: characterization form responses

- **`data_csv/`** — the same anonymized data in the **original Portuguese** (CSV), with the same structure as `data_en/`.

- **`notebooks/`**  
  - `RQ1.ipynb`: analysis for RQ1 (learning outcomes)
  - `RQ2.ipynb`: analysis for RQ2 (motivation)
  - `stratify.py`: helper used to build the stratified experimental/control split
  - `codebook_RQ3_standardized.xlsx` / `codebook_RQ3_standardized_en.xlsx`: RQ3 qualitative codebook (Portuguese / English) — thematic coding of the feedback responses

- **`figures/`**  
  - `boxplots_imi_control_x_exp.pdf`: IMI subscale comparison — control vs. experimental
  - `boxplots_imi_pre_x_post.pdf`: IMI subscale comparison — pre- vs. post-game (experimental)
  - `ira_boxplot.pdf`: academic performance (IRA) distribution by group

- **`game_material/`** : contain the cards, and game rules 

- **`study_artifacts/`** : contain the main study artifacts

> **Data, language & anonymization.** Participants are identified only by anonymized IDs (`P1`, `P2`, …), consistent across RQ1, RQ2 and RQ3. Group assignments are derived directly from the published anonymized files, so the notebooks run without any private mapping module. The data are provided in English (`data_en/`) and in the original Portuguese (`data_csv/`).

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

### **RQ1 — To what extent does the adoption of RiskGuard as an educational instrument support students’ learning of security patterns and software vulnerabilities?**

To answer RQ1, we tested two hypotheses:  
- **H₀:** There is no significant difference in participants’ learning between the two approaches (with and without RiskGuard).  
- **H₁:** There is a significant difference in learning outcomes between the two approaches.

**Learning Measurement:**  
Learning was measured through two *Knowledge Assessment Questionnaires*: one after the traditional lecture and another after the RiskGuard session. Each form contained 12 multiple-choice questions. Learning gain was calculated as the difference between post-game and post-lecture scores (ranging from –12 to +12).  
We also computed the **normalized gain (g)** = (Post – Pre) / (Max – Pre), with *Max = 12*, allowing a relative measure of learning improvement.

We controlled for two moderating factors:  
- **Experience Level:** Participants were grouped as *Less-experienced* or *More-experienced* based on self-reported familiarity with security concepts.  
- **Academic Performance (IRA):** Participants were classified as *High IRA* or *Low IRA* according to institutional academic performance indices.

We further examined whether learning gains differed by **experience level** (Less- vs. More-experienced), by **academic performance** (Low vs. High IRA), and by a combined **experience × performance profile** (compared with the Kruskal–Wallis test). Normality was checked with the Shapiro–Wilk test; independent-group comparisons used **Welch’s** *t*-test, paired comparisons used the paired *t*-test / Wilcoxon signed-rank test, and the Mann–Whitney U test was used as the non-parametric alternative. Effect sizes are reported via Cohen’s *d* or rank-biserial correlation.

### **RQ2 — How does the use of RiskGuard influence students’ motivation to learn about security patterns and software vulnerabilities?**

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

Each IMI subscale (INT, CMP, EFF, VAL, PRS) had its own hypothesis pair (H₀/H₁) to identify specific motivational effects. Normality was checked with the Shapiro–Wilk test, using **Welch’s** *t*-test / paired *t*-test where appropriate and **Mann–Whitney U / Wilcoxon** otherwise. Significance was evaluated at α = 0.05, and *p*-values across the five subscales were adjusted with the **Holm–Bonferroni** correction to control the family-wise error rate (the composite *overall motivation* score is reported separately).

This analysis triangulates motivational data across both experimental and control conditions to ensure that observed differences are attributable to RiskGuard rather than external classroom effects.

### **RQ3 — What are students’ perceptions of the effectiveness of RiskGuard as a learning instrument for security patterns and software vulnerabilities?**

RQ3 explores participants’ perceptions of the RiskGuard experience through a **feedback questionnaire** with six open-ended questions covering satisfaction, engagement, real-world applicability, ease of use, physical vs. digital format, and suggested improvements.

Responses from the experimental group were analyzed with **qualitative thematic coding**: each answer was assigned a category and subcategory, consolidated into a codebook (`notebooks/codebook_RQ3_standardized*.xlsx`, provided in Portuguese and English). This qualitative evidence complements the quantitative results of RQ1 and RQ2 with participants’ own accounts of what worked and what could be improved.

## 📊 Objective

The objective is to assess whether the **RiskGuard game-based approach** enhances **learning** (RQ1) and **motivation** (RQ2) compared to a **traditional lecture**, and to understand how participants **perceive** the experience (RQ3).  
Together, these analyses provide insights into how game-based learning can impact both cognitive and affective dimensions of web security education.

## ⚙️ Requirements

This project uses Python and standard data science libraries. To run the notebooks, install:

- Python 3.10+
- pandas
- numpy
- scipy
- statsmodels
- matplotlib 
- seaborn
- openpyxl
- ipykernel

You can install dependencies with:

```bash
pip install -r requirements.txt
```

---

