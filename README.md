# Shopee Customer Experience & Retention Dashboard

Data analytics project focusing on **customer experience** and **retention** on Shopee.  
This repository is part of my university term project for *Artificial Intelligence Engineering and Data Science* at Bangkok University, and is used as a portfolio piece for Data Analyst / Data Research roles.

---

## 🧩 Project Overview

The goal of this project is to:

- Understand **customer behavior** and **pain points** on Shopee Home category
- Analyze key metrics related to **customer satisfaction**, **repeat purchase**, and **order fulfillment**
- Build a **Power BI dashboard** that helps non-technical stakeholders quickly see:
  - Who are our customers?
  - Which segments are likely to churn?
  - Where are the main issues in the customer journey?

---

## 📂 Repository Structure

```text
Shopee-CX-Retention-Dashboard/
│
├─ Shopee_CX_Retention_Analysis.ipynb     # Main analysis notebook (Python)
│
├─ data/
│   ├─ shopee_home_raw.xlsx               # Raw Shopee Home orders dataset
│   ├─ shopee_home_goods_raw.xlsx         # Raw product-level data
│   └─ shopee_home_goods_transformed.xlsx # Cleaned / transformed data
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
Note: archive/ contains experimental notebooks and intermediate work.
The main workflow is inside Shopee_CX_Retention_Analysis.ipynb.

🔍 Data & Metrics
Data Sources
Exported Shopee order data from the Home category

Product-level data for analyzing category / brand performance

Transformed tables used for retention & cohort-style analysis

Key Metrics
Customer Satisfaction (CSAT) – based on ratings & review text

Repeat Purchase Rate – customers who come back to buy again

Order Fulfillment & Cancellation – success vs failed orders

Revenue by Product / Category – which items drive most value

📊 Analysis & Dashboard
In the Jupyter Notebook
The notebook covers:

Data Cleaning

Handling missing values

Fixing data types (dates, categorical values, etc.)

Merging order-level and product-level datasets

Exploratory Data Analysis (EDA)

Customer distributions (by location, spend, frequency)

Product/category performance

Time-based trends

Customer Retention

Identifying repeat vs one-time customers

Simple cohort-style views based on first purchase month

Power BI Dashboard
The Power BI dashboard (summarized in the PDF) consists of:

Overview page: high-level KPIs and trends

Customer page: segmentation and retention overview

Pain points page: cancellations, low ratings, and review insights

🛠️ Tools & Technologies
Python (pandas, numpy, matplotlib) for data cleaning and analysis

Excel / Google Sheets for initial data handling

Power BI for interactive dashboards and KPI visualization

Git & GitHub for version control and portfolio

🚀 How to Use
This repository is mainly intended as a portfolio and reference of my data analytics workflow.
If you want to explore the notebook:

Clone the repo:

bash
Copy code
git clone https://github.com/Ploy-ari/Shopee-CX-Retention-Dashboard.git
cd Shopee-CX-Retention-Dashboard
Open Shopee_CX_Retention_Analysis.ipynb in Jupyter / VS Code

Make sure you have the required Python libraries installed:

bash
Copy code
pip install pandas numpy matplotlib
👩‍💻 About Me
Ariya Raveewongpiboon (Ploy)
3rd-year student in Artificial Intelligence Engineering and Data Science, Bangkok University.
Interested in Data Research / Data Analyst roles, especially customer behavior and digital platforms.

LinkedIn: ariya-rave

GitHub: Ploy-ari

Email: ariya.raveewong@gmail.com
