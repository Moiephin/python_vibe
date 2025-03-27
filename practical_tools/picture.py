import requests
from bs4 import BeautifulSoup
import os
# 導入 requests . os
# 引用 from bs4 import BeautifulSoup

# 目標網址
url = 'https://wumanzoo.com/category/design/'

# 發送請求
response = requests.get(url)

# 解析網頁 -> 原始碼轉成可以操作的物件
# .text -> 取出 response 裡的 html 原始碼 並用 html.parser 解析
soup = BeautifulSoup(response.text, 'html.parser')

# 創建圖片保存資料夾
# os.makedirs 建立巢狀資料夾，exist_ok=True 如已存在則忽略
save_folder = '/Users/moe/Desktop/image'
os.makedirs(save_folder, exist_ok=True)

# 以 enumerate() 遍歷 soup.find_all("")
# 從 img 標籤取得其 src（圖片的來源）
# 如果 src 存在則發送請求去下載
for i, img in enumerate(soup.find_all('img')):
    img_url = img.get('src')
    # 如果有找到 img_url，直接下載
    # file_path = os.path.join(save_folder, f'image_{i+1}.jpg') 檔案命名規則
    if img_url:
        response = requests.get(img_url)
        file_path = os.path.join(save_folder, f'image_{i+1}.jpg')
        # with open(...) + .write() 把圖片的位元資料存成一個檔案（硬碟儲存）
        # wb 為二進位資料；response.content為下載下來拿到的位元組
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'image_{i+1}.jpg 下載完成！')
print("所有圖片抓取完成！")
