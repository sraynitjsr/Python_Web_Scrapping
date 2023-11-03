import pandas as pd

excel_file = "my_data.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(excel_file, sheet_name=sheet_name)

for column_name in df.columns:
    column_data = df[column_name]
    print(f"Column Name: {column_name}")
    print(column_data)
  
