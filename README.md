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

---


🔍 Data & Metrics
Data Sources

Exported Shopee order data from the Home category

Product-level data for analyzing category / brand performance

Transformed tables used for retention & cohort-style analysis

Key Metrics

Customer Satisfaction (CSAT) – based on star ratings & review text

Repeat Purchase Rate – customers who come back to buy again

Order Fulfillment & Cancellation – success vs failed orders

Revenue by Product / Category – which items drive most value

📊 Analysis Workflow

The main notebook Shopee_CX_Retention_Analysis.ipynb includes:

Data Cleaning

Fixing data types (dates, numeric fields, categories)

Handling missing values and inconsistent labels

Merging order-level and product-level datasets

Exploratory Data Analysis (EDA)

Customer distributions (location, spending, purchase frequency)

Product / category performance

Time-based trends (daily / monthly orders and revenue)

Customer Retention & Segmentation

Identifying one-time vs repeat customers

Simple cohort-style views based on first purchase month

Highlighting segments with high churn risk

Insights & Recommendations

Summarizing key pain points in the customer journey

Suggesting actions to improve satisfaction & retention

📊 Dashboard & Presentation

Although the interactive Power BI file is not included here, the main views and KPIs are summarized in:

reports/Shopee_CX_Retention_Presentation.pdf

The dashboard is structured around:

Overview page – high-level KPIs and trends

Customer page – segmentation and retention overview

Pain points page – cancellations, low ratings, and review insights

These pages are designed to be readable by business stakeholders without deep technical knowledge.

🛠️ Tools & Technologies

Python: pandas, numpy, matplotlib

Jupyter / VS Code for notebook-based analysis

Excel / Google Sheets for initial data handling

Power BI for dashboard creation and KPI visualization

Git & GitHub for version control and portfolio management

🚀 How to Run the Notebook

This repository is mainly intended as a portfolio and reference of my data analytics workflow.
If you want to explore or reproduce the analysis:

Clone the repository

git clone https://github.com/Ploy-ari/Shopee-CX-Retention-Dashboard.git
cd Shopee-CX-Retention-Dashboard


Create and activate a Python environment (optional but recommended)

python -m venv venv
.\venv\Scripts\activate      # on Windows
# source venv/bin/activate   # on macOS / Linux


Install required libraries

pip install pandas numpy matplotlib


Open the notebook

Open Shopee_CX_Retention_Analysis.ipynb in Jupyter Notebook / JupyterLab / VS Code

Run the cells step by step to reproduce the analysis

👩‍💻 About Me

Ariya Raveewongpiboon (Ploy)
3rd-year student in Artificial Intelligence Engineering and Data Science, Bangkok University.
Interested in Data Research Analyst / Data Analyst roles, especially around customer behavior, e-commerce, and digital platforms.

LinkedIn: ariya-rave

GitHub: Ploy-ari

Email: ariya.raveewong@gmail.com


---

## 2️⃣ วิธีเอาไปใส่ใน GitHub / VS Code แบบละเอียด

ทำบนเครื่องเหมือนเดิมในโฟลเดอร์โปรเจกต์ `Shopee-CX-Retention-Dashboard`

### ขั้นตอนใน VS Code

1. เปิด VS Code  
2. ไปที่ `File → Open Folder...` แล้วเลือกโฟลเดอร์  
   `Shopee-CX-Retention-Dashboard`
3. ที่แถบด้านซ้าย ดับเบิลคลิกที่ไฟล์ `README.md` ให้เปิดขึ้นมา
4. ในไฟล์ `README.md`:
   - กด `Ctrl + A` เพื่อเลือกข้อความทั้งหมด
   - กด `Delete` เพื่อลบเนื้อหาเดิมออก
5. กลับมาหน้าจอแชตนี้  
   - ลากเมาส์เลือกข้อความในกรอบ `markdown` ด้านบน  
     ตั้งแต่บรรทัด `# Shopee Customer Experience & Retention Dashboard`  
     จนถึงบรรทัดสุดท้าย `Email: ...`  
     (อย่า copy ตัว ```markdown กับ ``` นะ)
   - กด `Ctrl + C` เพื่อคัดลอก
6. กลับไปที่ VS Code ในไฟล์ `README.md`  
   - กด `Ctrl + V` เพื่อวางเนื้อหาใหม่ลงไป
7. กด `Ctrl + S` เพื่อบันทึกไฟล์

---

### ขั้นตอนอัปเดตขึ้น GitHub

เปิด Terminal ใน VS Code (หรือ PowerShell ที่โฟลเดอร์นี้) แล้วพิมพ์:

```bash
git status
git add README.md
git commit -m "Update README with project overview and structure"
git push
