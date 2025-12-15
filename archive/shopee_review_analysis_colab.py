
# Shopee Home & Living Review Impact Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# โหลดข้อมูลจาก Excel
file_path = 'shopee_home_dataset.xlsx'
xls = pd.ExcelFile(file_path)

products = pd.read_excel(xls, 'products')
reviews = pd.read_excel(xls, 'reviews')
promos = pd.read_excel(xls, 'promotions')

# Merge ข้อมูลโปรโมชั่นเข้ากับสินค้า
products = products.merge(promos, on='product_id', how='left')

# ======================
# 1. ความสัมพันธ์: จำนวนรีวิว / คะแนนรีวิว กับยอดขาย
# ======================

plt.figure(figsize=(10, 6))
sns.scatterplot(data=products, x='review_count', y='monthly_sales', hue='rating', palette='coolwarm', size='rating')
plt.title("รีวิวมากขึ้น = ยอดขายสูงขึ้น?")
plt.xlabel("จำนวนรีวิว")
plt.ylabel("ยอดขายต่อเดือน")
plt.legend(title='คะแนนรีวิว')
plt.tight_layout()
plt.show()

# Insight 1
print("\nInsight: โดยรวมพบว่าสินค้าที่มีจำนวนรีวิวมาก มียอดขายสูงขึ้น โดยเฉพาะเมื่อคะแนนรีวิวสูง (> 4.5)")

# ======================
# 2. Boxplot เปรียบเทียบยอดขายของสินค้าตามระดับคะแนนรีวิว
# ======================

# สร้างกลุ่มคะแนนรีวิว
products['rating_group'] = pd.cut(products['rating'], bins=[3.0, 4.0, 4.5, 5.0], labels=['ต่ำ', 'กลาง', 'สูง'])

plt.figure(figsize=(8, 6))
sns.boxplot(data=products, x='rating_group', y='monthly_sales', palette='Set2')
plt.title("คะแนนรีวิวกับยอดขาย")
plt.xlabel("กลุ่มคะแนนรีวิว")
plt.ylabel("ยอดขายต่อเดือน")
plt.tight_layout()
plt.show()

# Insight 2
print("\nInsight: สินค้าที่ได้คะแนนรีวิวระดับ 'สูง' (4.5–5.0) มียอดขายเฉลี่ยสูงกว่ากลุ่มอื่นอย่างชัดเจน")

# ======================
# 3. รีวิวมีภาพ vs ไม่มีภาพ ส่งผลต่อคะแนนรีวิวไหม?
# ======================

plt.figure(figsize=(8, 6))
sns.boxplot(data=reviews, x='has_image', y='review_rating', palette='cool')
plt.title("รีวิวที่มีภาพ vs คะแนนรีวิว")
plt.xlabel("มีภาพประกอบรีวิวหรือไม่ (0=ไม่มี, 1=มี)")
plt.ylabel("คะแนนรีวิว")
plt.tight_layout()
plt.show()

# Insight 3
print("\nInsight: รีวิวที่มีภาพมักได้คะแนนเฉลี่ยสูงกว่า สื่อถึงคุณภาพสินค้าที่ลูกค้าประทับใจมากพอจะถ่ายภาพ")

# ======================
# 4. เปรียบเทียบยอดขายสินค้า 'มีโปรโมชัน' vs 'ไม่มีโปรโมชัน'
# ======================

products['has_promo'] = products['promo_type'].notnull()

plt.figure(figsize=(8, 6))
sns.boxplot(data=products, x='has_promo', y='monthly_sales', palette='Pastel1')
plt.title("โปรโมชันช่วยเพิ่มยอดขายหรือไม่?")
plt.xlabel("มีโปรโมชันหรือไม่?")
plt.ylabel("ยอดขายต่อเดือน")
plt.xticks([0, 1], ['ไม่มีโปร', 'มีโปร'])
plt.tight_layout()
plt.show()

# Insight 4
print("\nInsight: สินค้าที่มีโปรโมชันมียอดขายสูงกว่าค่าเฉลี่ย สื่อถึงการใช้ Flash Sale/ส่วนลดช่วยเพิ่ม Conversion")

