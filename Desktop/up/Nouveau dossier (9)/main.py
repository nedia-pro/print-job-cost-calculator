import pandas as pd

# 🔹 Interactive Input
orders_file = input("📥 Enter the order file name (e.g. orders.csv): ").strip()
output_file = input("📤 Enter the output file name (e.g. final_quote.xlsx): ").strip()

# 📄 Read Files
try:
    orders = pd.read_csv(orders_file)
    paper_prices = pd.read_csv("paper_prices.csv")
    printing_costs = pd.read_csv("printing_costs.csv")
    delivery_costs = pd.read_csv("delivery_costs.csv")
except FileNotFoundError as e:
    print(f"❌ Error: File not found - {e}")
    exit()

# 📦 Cost Calculation
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
        print(f"⚠️ Error calculating SKU {row['SKU']}: {e}")
        return pd.Series([0, 0, 0, 0])

# 🧠 Apply calculations
orders[["PaperCost", "PrintingCost", "DeliveryCost", "TotalCost"]] = orders.apply(calculate_cost, axis=1)

# 💾 Output results
orders.to_excel(output_file, index=False)

# 📊 Summary
print("✅ File created successfully!")
print(f"📁 File: {output_file}")
print(f"🧾 Number of orders: {len(orders)}")
print(f"💰 Total cost: {orders['TotalCost'].sum():.2f} (Currency depending on the data)")
