from script_processor import (
    split_script,
    generate_prompts
)

from image_generator import (
    generate_images
)

from voice_generator import (
    generate_voice
)

from video_builder import (
    build_video
)

from config import INPUT_DIR

import os


def process(
    language,
    voice
):

    script_path = os.path.join(
        INPUT_DIR,
        f"script_{language}.txt"
    )

    with open(
        script_path,
        "r",
        encoding="utf-8"
    ) as f:

        script = f.read()

    print("[INFO] Dividiendo escenas")

    scenes = split_script(script)

    print("[INFO] Generando prompts")

    prompts = generate_prompts(scenes)

    print("[INFO] Generando imágenes")

    image_paths = generate_images(prompts)

    print("[INFO] Generando voz")

    audio_path = generate_voice(
        script,
        language,
        voice
    )

    print("[INFO] Construyendo video")

    build_video(
        scenes,
        image_paths,
        audio_path,
        language
    )


def main():

    process(
        "es",
        "es-AR-ElenaNeural"
    )

    print("[INFO] Short generado")


if __name__ == "__main__":
    main()