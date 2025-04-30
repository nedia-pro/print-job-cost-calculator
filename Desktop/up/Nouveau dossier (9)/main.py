import pandas as pd

# 🔹 إدخال تفاعلي
orders_file = input("📥 أدخل اسم ملف الطلبات (مثلاً orders.csv): ").strip()
output_file = input("📤 أدخل اسم ملف الإخراج (مثلاً final_quote.xlsx): ").strip()

# 📄 قراءة الملفات
try:
    orders = pd.read_csv(orders_file)
    paper_prices = pd.read_csv("paper_prices.csv")
    printing_costs = pd.read_csv("printing_costs.csv")
    delivery_costs = pd.read_csv("delivery_costs.csv")
except FileNotFoundError as e:
    print(f"❌ خطأ: الملف غير موجود - {e}")
    exit()

# 📦 حساب التكلفة
def calculate_cost(row):
    try:
        paper = paper_prices[paper_prices["PaperType"] == row["PaperType"]].iloc[0]
        printing = printing_costs[printing_costs["Sides"] == row["Sides"]].iloc[0]

        quantity = row["Quantity"]
        weight_per_sheet = paper["WeightPerSheet_g"]
        cost_per_kg = paper["CostPerKg"]

        total_weight_kg = (weight_per_sheet * quantity) / 1000
        paper_cost = total_weight_kg * cost_per_kg
        printing_cost = (quantity / 1000) * printing["CostPer1000"]

        delivery_row = delivery_costs[
            (delivery_costs["WeightKg_Min"] <= total_weight_kg) & 
            (delivery_costs["WeightKg_Max"] >= total_weight_kg)
        ].iloc[0]
        delivery_cost = delivery_row["DeliveryCost"]

        total = paper_cost + printing_cost + delivery_cost
        return pd.Series([paper_cost, printing_cost, delivery_cost, total])
    except Exception as e:
        print(f"⚠️ خطأ في حساب SKU {row['SKU']}: {e}")
        return pd.Series([0, 0, 0, 0])

# 🧠 تطبيق الحسابات
orders[["PaperCost", "PrintingCost", "DeliveryCost", "TotalCost"]] = orders.apply(calculate_cost, axis=1)

# 💾 إخراج النتائج
orders.to_excel(output_file, index=False)

# 📊 ملخص
print("✅ تم إنشاء الملف بنجاح!")
print(f"📁 الملف: {output_file}")
print(f"🧾 عدد الطلبات: {len(orders)}")
print(f"💰 مجموع التكاليف: {orders['TotalCost'].sum():.2f} دينار/€/$ (حسب العملة)")
