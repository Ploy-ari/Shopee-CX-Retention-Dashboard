# Shopee Customer Experience & Retention Dashboard

Data analytics project focusing on **customer experience** and **retention** on Shopee (Home category).  
This repository is part of my term project in *Artificial Intelligence Engineering and Data Science* at Bangkok University, and also serves as a portfolio piece for **Data Research / Data Analyst** roles.

---

## 🧩 Project Overview

The main goals of this project are to:

- Understand **customer behavior** and **pain points** on Shopee Home  
- Analyze key metrics related to **customer satisfaction**, **repeat purchase**, and **order fulfillment**  
- Build a **dashboard** that helps non-technical stakeholders quickly see:  
  - Who are our customers?  
  - Which segments are at risk of churn?  
  - Where are the main issues in the customer journey?  

The analysis is implemented in Python and visualized via an interactive dashboard (Power BI), with a slide deck summarizing the main findings.

---

## 📂 Repository Structure

```text
Shopee-CX-Retention-Dashboard/
│
├─ Shopee_CX_Retention_Analysis.ipynb     # Main analysis notebook
│
├─ data/
│   ├─ shopee_home_raw.xlsx               # Raw Shopee Home orders dataset
│   ├─ shopee_home_goods_raw.xlsx         # Raw product-level dataset
│   └─ shopee_home_goods_transformed.xlsx # Cleaned / transformed tables
│
├─ reports/
│   └─ Shopee_CX_Retention_Presentation.pdf  # Slide deck used for presentation
│
├─ assets/
│   └─ shopee_figure.png                  # Sample chart / logo used in report
│
└─ archive/
    ├─ shopee_review_analysis_colab.ipynb
    ├─ shopee_review_analysis_colab_full.ipynb
    ├─ shopee_review_analysis_colab_thai.ipynb
    └─ shopee_review_analysis_colab.py
archive/ contains experimental notebooks and intermediate work.
The main workflow is inside Shopee_CX_Retention_Analysis.ipynb.

