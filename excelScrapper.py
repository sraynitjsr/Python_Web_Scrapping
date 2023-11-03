import pandas as pd
import requests

# This is Dummy URL
endpoint_url = "https://example.com/some-rest-endpoint"
response = requests.get(endpoint_url)

if response.status_code == 200:
    with open("downloaded_excel_file.xlsx", "wb") as file:
        file.write(response.content)
else:
    print("Failed to retrieve the Excel file from the endpoint.")

# Read the downloaded Excel file
excel_file = "downloaded_excel_file.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Output data column-wise
for column_name in df.columns:
    column_data = df[column_name]
    print(f"Column Name: {column_name}")
    print(column_data)
