import os
import csv

# 此python檔用來載入化學物清單 並轉換為txt檔

def load_and_save_txt(input_folder, output_path):
    data = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            
            with open(file_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    data.append(row)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as txt_file:
            for item in data:
                txt_file.write(f"化學物名稱: {item['化學物名稱']}\n")
                txt_file.write(f"中文名稱: {item['中文名稱']}\n")
                txt_file.write(f"風險等級: {item['風險等級']}\n")
                txt_file.write(f"PubChem CID: {item['PubChem CID']}\n")
                txt_file.write(f"CAS No.: {item['CAS No.']}\n")
                txt_file.write(f"危害組別: {item['危害組別']}\n")
                txt_file.write(f"危害名稱: {item['危害名稱']}\n")
                txt_file.write(f"危害等級: {item['危害等級']}\n")
                txt_file.write(f"資料來源: {item['資料來源']}\n")
                txt_file.write(f"可信度: {item['可信度']}\n")
                txt_file.write(f"危害分類是否清楚: {item['危害分類是否清楚']}\n")
                txt_file.write(f"適用地區: {item['適用地區']}\n")
                txt_file.write(f"適用產業: {item['適用產業']}\n")
                txt_file.write(f"是否具強制性？: {item['是否具強制性？']}\n")
                txt_file.write(f"清單連結: {item['清單連結']}\n")
                txt_file.write(f"註解: {item['註解']}\n")
                txt_file.write(f"額外註解: {item['額外註解']}\n")
                txt_file.write(f"預測值: {item['預測值']}\n")
                txt_file.write("\n")
        print(f".txt file successfully saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

input_folder = './chemical_data'
output_file = './txt_file/Chemical.txt'

load_and_save_txt(input_folder, output_file)