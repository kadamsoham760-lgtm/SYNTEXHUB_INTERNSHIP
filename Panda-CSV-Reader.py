import importlib
import pandas as pd
from pathlib import Path

print("===== Pandas CSV Reader & Basic Analysis =====")


try:
    importlib.import_module("openpyxl")
    excel_available = True
except ModuleNotFoundError:
    excel_available = False
    print("\nNote: openpyxl is not installed, Excel export will be skipped.")
    print("Install it with: pip install openpyxl")


script_dir = Path(__file__).resolve().parent
file_name = script_dir / "students.csv"   # CSV file in the same folder as this script

if not file_name.exists():
    raise FileNotFoundError(f"CSV file not found: {file_name}")

df = pd.read_csv(file_name)

print("\nDataset Loaded Successfully!")


print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nColumn Data Types:")
print(df.dtypes)

print("\nDataset Shape:")
print(df.shape)

print("\n===== Summary Statistics =====")

print("\nCount:")
print(df.count())

print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nMinimum Values:")
print(df.min())

print("\nMaximum Values:")
print(df.max())

print("\nDetailed Statistics:")
print(df.describe())


print("\n===== Selected Columns =====")

selected_columns = df[['Name', 'Marks']]
print(selected_columns)


print("\n===== Students Scoring More Than 80 =====")

filtered_data = df[df['Marks'] > 80]
print(filtered_data)


print("\n===== First 3 Rows =====")

subset = df.iloc[0:3]
print(subset)

output_dir = script_dir
csv_path = output_dir / "top_students.csv"
excel_path = output_dir / "top_students.xlsx"

filtered_data.to_csv(csv_path, index=False)

print(f"\nFiltered data saved as '{csv_path.name}'")


if excel_available:
    filtered_data.to_excel(excel_path, index=False)
    print(f"Filtered data saved as '{excel_path.name}'")
else:
    print("\nExcel export skipped because openpyxl is not installed.")
    print("Install it with: pip install openpyxl")

print("\n===== Project Completed Successfully =====") 