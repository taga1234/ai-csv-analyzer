import os
import pandas as pd
from openai import OpenAI

# Читаем CSV
df = pd.read_csv("data.csv")

# Формируем текст запроса для модели
prompt = f"""
Проанализируй данные и сделай выводы.
Данные:
{df.head(20).to_string()}
"""

# Настраиваем клиента
client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

# Запрос к модели
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message["content"])
