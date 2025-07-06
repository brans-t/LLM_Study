import os
from dotenv import load_dotenv
import requests



load_dotenv()  # 默认加载当前目录下的.env文件
api_key = os.environ.get("DEEPSEEL_API_KEY")
# 检查 API 密钥是否存在
if not api_key:
    raise ValueError("DEEPSEEL_API_KEY is not set in the environment variables.")

url = "https://dpapi.cn/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-v3",
    "messages": [{"role": "user", "content": "请解释一下手机"}],
}

response = requests.post(url, headers=headers, json=data)

if response.status_code != 200:
    raise Exception(f"Error: {response.status_code}, {response.json()}")
json_data = response.json()
content = json_data["choices"][0]["message"]["content"]


print("响应结果：", content)