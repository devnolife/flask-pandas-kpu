import pandas as pd
import json
import pprint

file_path = 'gowa.xlsx'
excel_data = pd.read_excel(file_path)
cleaned_data = pd.read_excel(file_path, header=4)
json_data = cleaned_data.to_json(orient="records", lines=True)
json_data = [json.loads(line) for line in json_data.splitlines()]

tps_data = []
last_kelurahan = None  
last_kecamatan = None  
seen_tps = set()

for entry in json_data:
    desa_kelurahan = entry.get("Unnamed: 3")
    kecamatan = entry.get("Unnamed: 1")
    tps_number = entry.get("Unnamed: 4")
    if desa_kelurahan and isinstance(tps_number, int):
        last_kelurahan = desa_kelurahan
    
    if kecamatan:
        last_kecamatan = kecamatan
    
    tps_key = (last_kelurahan, tps_number)

    if tps_key not in seen_tps and isinstance(tps_number, int):
        tps_data.append({
            "Kecamatan": last_kecamatan,
            "Desa/Kelurahan": last_kelurahan,
            "TPS": tps_number,
            "L": entry.get("Unnamed: 5"),
            "P": entry.get("Unnamed: 6"),
            "Total": entry.get("Unnamed: 7")
        })
        seen_tps.add(tps_key)  

filtered_tps_data = []
for entry in tps_data:
    if not ("Total" in str(entry.get("Desa/Kelurahan", "")) and entry.get("TPS") == 6):
        filtered_tps_data.append(entry)

df_tps = pd.DataFrame(filtered_tps_data)

print(df_tps.head(20))  

