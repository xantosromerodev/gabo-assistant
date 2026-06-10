from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

with open(
    "prompts/system_prompt.txt",
    "r",
    encoding="utf-8"
) as file:

    system_prompt = file.read()

print("\n===== GABO ASSISTANT =====\n")
print("Escribe 'salir' para finalizar.\n")

while True:

    user_message = input("Cliente: ")

    if user_message.lower() == "salir":
        break

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    answer = response.choices[0].message.content

    print(f"\nGaby: {answer}\n")