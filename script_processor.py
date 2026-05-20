from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def split_script(script):

    lines = script.splitlines()

    scenes = [
        line.strip()
        for line in lines
        if line.strip()
    ]

    return scenes


def generate_prompts(scenes):

    prompts = []

    for i, scene in enumerate(scenes):

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un experto generando prompts "
                        "cinematográficos para imágenes verticales "
                        "de videos cortos estilo documental."
                    )
                },
                {
                    "role": "user",
                    "content": f"""
Convierte esta escena en un prompt visual cinematográfico.

Escena:
{scene}

Reglas:
- Formato vertical 9:16
- Cinematic
- Ultra detailed
- Dramatic lighting
- Sin texto
- Imagen realista
- Estilo documental
- Solo responde el prompt
"""
                }
            ]
        )

        prompt = response.choices[0].message.content.strip()

        prompts.append(prompt)

        print(f"[INFO] Prompt generado {i+1}")

    return prompts

