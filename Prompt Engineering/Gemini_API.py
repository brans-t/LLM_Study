import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 设置 API 密钥

# os.environ["GEMINI_API_KEY"] = "XXXXXXXXXXX"
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

load_dotenv()  # 默认加载当前目录下的.env文件
api_key = os.environ.get("GEMINI_API_KEY")
# 检查 API 密钥是否存在
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


# 创建客户端
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = "gemini-2.5-pro",
    contents = "The Sky is ",
    config = types.GenerateContentConfig(
        temperature=0.8,
        top_p=1,
        top_k=40,
        max_output_tokens=2048,
        candidate_count=1,
    )
)

print(response.text)



