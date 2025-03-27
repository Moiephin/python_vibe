# /Users/moe/Desktop/攝影/1月照片

import os
folder_path = '/Users/moe/Desktop/攝影/1月照片'
files = os.listdir(folder_path)
# os.listdir(path) → 列出指定資料夾內的所有「內容名稱」→ 回傳一個 list

files = sorted([ f for f in os.listdir(folder_path)
if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.jpg')])
# 列表生成式，遍歷 f 如果符合後方條線，生成列表
# 後方條件為 os.path.isfile 判斷是否為檔案
# os.path.join(folder_path, f) 將檔案與路徑結合
# 判斷 檔名最後為小寫的.jpg 格式

for i, file in enumerate(files):
    old_path = os.path.join(folder_path, file)
    new_name = f"不刪檔_{i+1}.jpg"
    new_path = os.path.join(folder_path, new_name)

    if os.path.exists(new_path):
        print(f"⚠️ 已存在，跳過：{new_name}")
        continue  # 跳過這個，不動它

    os.rename(old_path, new_path)
    print(f"✅ 改名成功：{file} → {new_name}")

print("\n🎉 所有檔案處理完畢！")
