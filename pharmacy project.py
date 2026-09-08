import pandas as pd
# 1. Create Pharmacy Inventory Dataset

data = {
    "Medicine_ID": list(range(101, 151)),

    "Medicine_Name": [
        "Paracetamol", "Amoxicillin", "Cetirizine", "Ibuprofen",
        "Azithromycin", "Vitamin C", "Omeprazole", "Metformin",
        "Aspirin", "Pantoprazole", "Diclofenac", "Levocetirizine",
        "Ciprofloxacin", "Doxycycline", "Calcium", "Vitamin D3",
        "Montelukast", "Atorvastatin", "Losartan", "Amlodipine",
        "Glimepiride", "Insulin", "Ranitidine", "ORS",
        "Antacid Gel", "Clotrimazole", "Fluconazole", "Amoxicillin",
        "Naproxen", "Tramadol", "Cetirizine", "Paracetamol",
        "Azithromycin", "Metformin", "Vitamin B12", "Iron Tablets",
        "Folic Acid", "Hydroxychloroquine", "Salbutamol",
        "Budesonide", "Loratadine", "Rabeprazole", "Mefenamic Acid",
        "Domperidone", "Ondansetron", "Albendazole",
        "Acyclovir", "Prednisolone", "Hydrocortisone", "Insulin"
    ],

    "Category": [
        "Painkiller", "Antibiotic", "Antihistamine", "Painkiller",
        "Antibiotic", "Supplement", "Antacid", "Diabetes",
        "Painkiller", "Antacid", "Painkiller", "Antihistamine",
        "Antibiotic", "Antibiotic", "Supplement", "Supplement",
        "Antihistamine", "Cholesterol", "Blood Pressure", "Blood Pressure",
        "Diabetes", "Diabetes", "Antacid", "Supplement",
        "Antacid", "Antifungal", "Antifungal", "Antibiotic",
        "Painkiller", "Painkiller", "Antihistamine", "Painkiller",
        "Antibiotic", "Diabetes", "Supplement", "Supplement",
        "Supplement", "Other", "Respiratory", "Respiratory",
        "Antihistamine", "Antacid", "Painkiller", "Digestive",
        "Digestive", "Antiparasitic", "Antiviral", "Steroid",
        "Steroid", "Diabetes"
    ],

    "Quantity": [
        100, 25, 80, 10, 5, 150, 60, 20, 75, 15,
        40, 12, 30, 18, 120, 90, 55, 70, 45, 35,
        8, 10, 65, 200, 50, 25, 14, 22, 60, 9,
        95, 130, 7, 28, 85, 110, 45, 16, 75, 32,
        48, 20, 13, 42, 27, 100, 19, 24, 11, 6
    ],

    "Price": [
        2.5, 8.0, 3.0, 4.5, 10.0, 1.5, 5.0, 6.0,
        2.0, 7.5, 4.0, 3.5, 9.0, 6.5, 2.5, 5.5,
        4.5, 12.0, 8.0, 6.0, 5.0, 25.0, 4.0, 1.5,
        6.0, 7.0, 15.0, 8.5, 5.5, 11.0, 3.0, 2.5,
        10.0, 6.0, 9.0, 4.0, 2.0, 14.0, 8.0, 18.0,
        3.5, 6.5, 4.5, 5.0, 9.0, 3.0, 12.0, 5.5,
        7.0, 25.0
    ],

    "Expiry_Date": [
        "2027-05-20", "2026-10-15", "2027-01-10", "2026-09-01",
        "2026-08-15", "2028-03-20", "2027-11-30", "2026-12-10",
        "2027-06-25", "2026-11-18", "2027-02-15", "2026-10-05",
        "2027-04-12", "2026-09-20", "2028-01-15", "2027-09-30",
        "2027-05-10", "2028-02-20", "2027-08-15", "2027-12-05",
        "2026-08-25", "2027-03-15", "2026-07-30", "2028-05-20",
        "2027-10-10", "2026-11-25", "2027-06-18", "2027-01-30",
        "2028-04-15", "2026-10-30", "2027-07-20", "2028-02-15",
        "2026-08-10", "2027-12-20", "2028-03-10", "2027-09-15",
        "2026-09-05", "2027-05-25", "2028-01-10", "2027-11-15",
        "2026-10-20", "2027-08-30", "2026-08-05", "2028-04-20",
        "2027-02-10", "2026-12-25", "2027-06-30", "2028-03-15",
        "2026-09-10", "2027-04-25"
    ],

    "Supplier": [
        "ABC Pharma", "MedSupply", "HealthCare Ltd", "ABC Pharma",
        "MedSupply", "HealthCare Ltd", "ABC Pharma", "MedSupply",
        "ABC Pharma", "HealthCare Ltd", "MedSupply", "ABC Pharma",
        "MedSupply", "HealthCare Ltd", "ABC Pharma", "MedSupply",
        "HealthCare Ltd", "ABC Pharma", "MedSupply", "HealthCare Ltd",
        "ABC Pharma", "MedSupply", "HealthCare Ltd", "ABC Pharma",
        "MedSupply", "HealthCare Ltd", "ABC Pharma", "MedSupply",
        "HealthCare Ltd", "ABC Pharma", "MedSupply", "HealthCare Ltd",
        "ABC Pharma", "MedSupply", "HealthCare Ltd", "ABC Pharma",
        "MedSupply", "HealthCare Ltd", "ABC Pharma", "MedSupply",
        "HealthCare Ltd", "ABC Pharma", "MedSupply", "HealthCare Ltd",
        "ABC Pharma", "MedSupply", "HealthCare Ltd", "ABC Pharma",
        "MedSupply", "HealthCare Ltd"
    ]
}

df = pd.DataFrame(data)

# 2. Convert Expiry Date
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

# 3. Calculate Inventory Value

df["Inventory_Value"] = df["Quantity"] * df["Price"]

# 4. Display Complete Inventory

print("\n========== PHARMACY INVENTORY ==========")
print(df.to_string(index=False))
# 5. Find Low Stock Medicines

low_stock = df[df["Quantity"] < 20]

print("\n========== LOW STOCK MEDICINES ==========")
print(
    low_stock[
        ["Medicine_Name", "Quantity", "Supplier"]
    ].to_string(index=False)
)

# 6. Find Expired Medicines

today = pd.Timestamp.today().normalize()

expired = df[df["Expiry_Date"] < today]

print("\n========== EXPIRED MEDICINES ==========")
print(
    expired[
        ["Medicine_Name", "Expiry_Date", "Quantity"]
    ].to_string(index=False)
)

# 7. Total Inventory Value

total_inventory_value = df["Inventory_Value"].sum()

print("\n========== TOTAL INVENTORY VALUE ==========")
print("₹", round(total_inventory_value, 2))

# 8. Category-wise Inventory Value

category_value = (
    df.groupby("Category")["Inventory_Value"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== CATEGORY-WISE INVENTORY VALUE ==========")
print(category_value)


# 9. Highest Value Medicine

highest_value_medicine = df.loc[
    df["Inventory_Value"].idxmax()
]

print("\n========== HIGHEST INVENTORY VALUE MEDICINE ==========")

print(
    highest_value_medicine[
        [
            "Medicine_Name",
            "Quantity",
            "Price",
            "Inventory_Value"
        ]
    ]
)

# 10. Supplier-wise Inventory Value

supplier_value = (
    df.groupby("Supplier")["Inventory_Value"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SUPPLIER-WISE INVENTORY VALUE ==========")
print(supplier_value)
# 11. Search Medicine
medicine = input("\nEnter medicine name to search: ").strip()

result = df[
    df["Medicine_Name"].str.strip().str.lower() == medicine.lower()
]

if not result.empty:
    print("\n========== MEDICINE DETAILS ==========")
    print(result.to_string(index=False))
else:
    print("\nMedicine not found in the stock.")