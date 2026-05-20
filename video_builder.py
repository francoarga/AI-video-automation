import os
import random

from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    CompositeVideoClip,
    concatenate_videoclips
)

from config import WIDTH, HEIGHT, OUTPUT_DIR


def apply_motion(clip, duration):

    clip = clip.resize(1.15)

    direction = random.choice([
        "left",
        "right",
        "up",
        "down"
    ])

    max_move_x = 120
    max_move_y = 80

    if direction == "left":

        start_x = 0
        end_x = -max_move_x

        start_y = 0
        end_y = 0

    elif direction == "right":

        start_x = -max_move_x
        end_x = 0

        start_y = 0
        end_y = 0

    elif direction == "up":

        start_x = 0
        end_x = 0

        start_y = 0
        end_y = -max_move_y

    else:

        start_x = 0
        end_x = 0

        start_y = -max_move_y
        end_y = 0

    animated = clip.set_position(
        lambda t: (
            start_x + (end_x - start_x)
            * (t / duration),

            start_y + (end_y - start_y)
            * (t / duration)
        )
    )

    return animated


def build_video(
    scenes,
    image_paths,
    audio_path,
    language
):

    audio = AudioFileClip(audio_path)

    total_words = sum(
        len(scene.split())
        for scene in scenes
    )

    scene_durations = []

    for scene in scenes:

        words = len(scene.split())

        duration = (
            (words / total_words)
            * audio.duration
        )

        scene_durations.append(duration)

    clips = []

    for i in range(len(scenes)):

        duration = scene_durations[i]

        img_path = image_paths[i]

        base = (
            ImageClip(img_path)
            .set_duration(duration)
            .resize(height=2200)
        )

        animated = apply_motion(
            base,
            duration
        )

        final_clip = CompositeVideoClip(
            [animated],
            size=(WIDTH, HEIGHT)
        ).set_duration(duration)

        clips.append(final_clip)

    final = concatenate_videoclips(
        clips,
        method="compose"
    )

    final = final.set_audio(audio)

    output = os.path.join(
        OUTPUT_DIR,
        f"short_{language}.mp4"
    )

    final.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"]
    )

    print(f"[INFO] Video generado: {output}")

