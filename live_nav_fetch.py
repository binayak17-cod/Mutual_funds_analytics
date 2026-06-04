import requests
import pandas as pd
import json
import os

def fetch_scheme_nav(scheme_code, output_filename):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching data from: {url}...")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            
            # Extract historical tracking data array from the JSON payload
            nav_data = json_data.get('data', [])
            
            if nav_data:
                # Convert the array into a structured Pandas DataFrame
                df = pd.DataFrame(nav_data)
                
                # Append the scheme identifier code to track it easily downstream
                df['scheme_code'] = scheme_code
                
                # Create the target directory path cleanly if it doesn't exist
                os.makedirs("data/raw", exist_ok=True)
                output_path = os.path.join("data/raw", f"{output_filename}.csv")
                
                # Export to CSV without preserving the index column layout
                df.to_csv(output_path, index=False)
                print(f"✅ Success! Saved {len(df)} records to {output_path}\n")
            else:
                print(f"❌ Error: No payload data found for scheme code {scheme_code}.")
        else:
            print(f"❌ HTTP Error: Received status code {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred during network call: {e}")

if __name__ == "__main__":
    # 1. This keeps your Step 4 HDFC fetch working
    fetch_scheme_nav(125497, "hdfc_top_100_live")
    
    # 2. This is a dictionary mapping the 5 new scheme codes to their file names
    key_schemes = {
        119551: "sbi_bluechip_live",
        120503: "icici_bluechip_live",
        118632: "nippon_large_cap_live",
        119092: "axis_bluechip_live",
        120841: "kotak_bluechip_live"
    }
    
    print("================ FETCHING TASK 5 KEY SCHEMES ================")
    
    # 3. This loop goes through the dictionary and runs your fetch function for each fund
    for code, filename in key_schemes.items():
        fetch_scheme_nav(code, filename)