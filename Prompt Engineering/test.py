from google import genai
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()  # 默认加载当前目录下的.env文件
api_key = os.environ.get("GEMINI_API_KEY")

# 检查 API 密钥是否存在
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# 创建客户端
client = genai.Client(api_key=api_key)

def set_genai_params(
    model="gemini-2.5-pro",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
):
    """设置 Google GenAI 参数"""
    genai_params = {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
    }
    return genai_params

def get_completion(params, contents):
    """从 Google GenAI 获取完成内容"""
    response = client.models.generate_content(
        model=params["model"],
        contents=contents,
        temperature=params["temperature"],
        max_tokens=params["max_tokens"],
        top_p=params["top_p"],
        frequency_penalty=params["frequency_penalty"],
        presence_penalty=params["presence_penalty"],
    )
    return response

# 设置参数
params = set_genai_params(
    model="gemini-2.5-pro",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)


# 定义要生成的内容
contents = "The Sky is "

# 获取完成内容
response = get_completion(params, contents)

# 打印响应
print(response.text)