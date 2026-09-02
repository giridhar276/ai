# Install first: pip install pandas openpyxl
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Meena", "John"],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Score": [85, 92, 78, 88],
    "Salary": [65000, 58000, 70000, 72000],
}
table = pd.DataFrame(data)

# Inspect and select data
print(table.head())
print("Shape:", table.shape)
print("Columns:", table.columns.tolist())
print("Scores only:\n", table["Score"])
print("Selected columns:\n", table[["Name", "Score"]])
print("IT employees:\n", table.loc[table["Department"] == "IT"])

# Add, sort and aggregate columns
table["Passed"] = table["Score"] >= 80
table["Bonus"] = table["Salary"] * 0.10
print("Sorted:\n", table.sort_values("Score", ascending=False))
print("Average score:", table["Score"].mean())
print("Department summary:\n", table.groupby("Department")["Salary"].agg(["count", "mean", "sum"]))

# Write multiple sheets to one workbook
filename = "employee_analysis.xlsx"
with pd.ExcelWriter(filename, engine="openpyxl") as writer:
    table.to_excel(writer, sheet_name="Employees", index=False)
    table.groupby("Department", as_index=False)["Salary"].sum().to_excel(
        writer, sheet_name="Department Summary", index=False
    )

# Read complete and selected Excel content
loaded = pd.read_excel(filename, sheet_name="Employees")
all_sheets = pd.read_excel(filename, sheet_name=None)
print("Loaded rows:\n", loaded)
print("Available sheets:", list(all_sheets))
