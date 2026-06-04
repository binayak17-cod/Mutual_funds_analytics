import pandas as pd
import os

# 1. Exact filenames from your data/raw folder
csv_files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("================ STEP 3: DATASET INSPECTION ================")
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

# 2. Corrected paths for Steps 6 & 7 matching your actual filenames
master_path = os.path.join("data", "raw", "01_fund_master.csv")
history_path = os.path.join("data", "raw", "02_nav_history.csv")

print("\n" + "="*50)
print("🎯 STEP 6: EXPLORING FUND MASTER STRUCTURE")
print("="*50)

if os.path.exists(master_path):
    df_master = pd.read_csv(master_path)
    
    print(f"🏢 Unique Fund Houses: {df_master['fund_house'].nunique()}")
    print(f"🗂️ Unique Categories: {df_master['category'].nunique()}")
    print(f"📊 Unique Sub-Categories: {df_master['sub_category'].nunique()}")
    
    risk_col = [col for col in df_master.columns if 'risk' in col.lower()]
    if risk_col:
        print(f"⚠️ Risk Grades Present: {df_master[risk_col[0]].unique()}")

    print("\n" + "="*50)
    print("🔍 STEP 7: AMFI CODE VALIDATION")
    print("="*50)
    
    if os.path.exists(history_path):
        df_history = pd.read_csv(history_path)
        
        # Determine the unique ID column key dynamically
        master_key = 'amfi_code' if 'amfi_code' in df_master.columns else 'scheme_code'
        history_key = 'amfi_code' if 'amfi_code' in df_history.columns else 'scheme_code'
        
        master_codes = set(df_master[master_key].unique())
        history_codes = set(df_history[history_key].unique())
        
        missing_in_history = master_codes - history_codes
        
        print(f"🔢 Total unique codes in Fund Master: {len(master_codes)}")
        print(f"🔢 Total unique codes in NAV History: {len(history_codes)}")
        
        if len(missing_in_history) == 0:
            print("✅ Perfect Data Integrity! All master entries exist in history datasets.")
        else:
            print(f"⚠️ Discrepancy Found: {len(missing_in_history)} codes from Master are missing in History profiles.")
            print(f"📋 Sample missing codes: {list(missing_in_history)[:5]}")
            
        # Write out your required Day 1 report markdown file
        os.makedirs("reports", exist_ok=True)
        report_path = os.path.join("reports", "data_quality_summary.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# Day 1 — Data Quality Summary Report\n\n")
            f.write(f"- **Unique Fund Houses:** {df_master['fund_house'].nunique()}\n")
            f.write(f"- **Total Master Relationship Keys:** {len(master_codes)}\n")
            f.write(f"- **Total History Tracking Keys:** {len(history_codes)}\n")
            f.write(f"- **Data Discrepancies / Missing Records:** {len(missing_in_history)}\n")
        print(f"\n📝 Summary report automatically drafted at: {report_path}")
        
    else:
        print(f"⚠️ History tracking file '{history_path}' not found. Check your folder.")
else:
    print(f"⚠️ Master file '{master_path}' not found. Check your folder.")