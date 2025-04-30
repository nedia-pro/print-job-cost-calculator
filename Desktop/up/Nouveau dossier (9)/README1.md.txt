# 🖨️ Print Job Cost Calculator

A Python-based automation tool to calculate the total cost of print jobs (such as leaflets, flyers, etc.) based on a CSV file of SKUs. It processes job details like paper type, quantity, number of sides, and automatically computes material cost, weight-based delivery cost, and generates a clean Excel quote.

---

## 📦 Features

- 🔄 Import orders from CSV
- 📄 Use paper and delivery cost lookup tables
- 💡 Supports weight-based delivery logic
- 📊 Exports final quote to Excel automatically
- 🧮 Total cost summary with per-item breakdown
- 🌍 Customizable for currency and cost logic

---

## 📂 Sample Input (CSV)

| SKU        | PaperType | Quantity | Sides | WeightPerUnit |
|------------|-----------|----------|-------|----------------|
| LEAF001    | Gloss 150gsm | 1000     | 2     | 0.012          |

---

## 🛠️ How to Use

1. Place your `orders.csv` file in the same folder.
2. Run the script:

```bash
python main.py
