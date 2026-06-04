import pandas as pd
import os

# Update this list with the exact filenames of your 10 downloaded CSVs
csv_files = [
    "fund_master.csv", 
    "nav_history.csv", 
    # Add the remaining 8 filenames here...
]

print("================ DATASET INSPECTION ================")
for file in csv_files:
    file_path = os.path.join("data/raw", file)
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"\n📄 FILE: {file}")
        print(f"📊 Shape (Rows, Columns): {df.shape}")
        print("-" * 40)
        print("🧬 Data Types:")
        print(df.dtypes)
        print("-" * 40)
        print("👀 First 3 Rows:")
        print(df.head(3))
        print("=" * 50)
    else:
        print(f"⚠️ Warning: {file} not found in data/raw/")
        