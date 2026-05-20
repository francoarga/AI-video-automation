import asyncio
import os

import edge_tts

from config import AUDIO_DIR


async def generate(text, voice, output):

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(output)


def generate_voice(
    text,
    language,
    voice
):

    output = os.path.join(
        AUDIO_DIR,
        f"narration_{language}.mp3"
    )

    asyncio.run(
        generate(
            text,
            voice,
            output
        )
    )

    return output

