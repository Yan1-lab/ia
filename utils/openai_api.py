import openai
import os

def ask_openai(prompt, model="gpt-4o-mini", temperature=0.7):
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Eres un asistente médico virtual. No das diagnósticos definitivos, solo sugerencias."},
                {"role": "user", "content": prompt}
            ]
        )
        return "🔎 Revisando la base de datos...\n" + response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
