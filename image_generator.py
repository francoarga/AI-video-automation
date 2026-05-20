import base64
import os

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_IMAGE_MODEL,
    IMAGES_DIR
)

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def generate_images(prompts):

    image_paths = []

    for i, prompt in enumerate(prompts):

        print(f"[INFO] Generando imagen {i+1}")

        result = client.images.generate(
            model=OPENAI_IMAGE_MODEL,
            prompt=prompt,
            size="1024x1792"
        )

        image_base64 = result.data[0].b64_json

        image_bytes = base64.b64decode(image_base64)

        image_path = os.path.join(
            IMAGES_DIR,
            f"scene_{i}.png"
        )

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        image_paths.append(image_path)

    return image_paths
