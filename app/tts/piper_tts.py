import subprocess
import uuid
import os

class PiperTTS:
    def __init__(self, voice):
        self.voice = voice

    def speak(self, text):
        out = f"/tmp/{uuid.uuid4()}.wav"

        proc = subprocess.run(
            [
                "/usr/bin/piper-tts",
                "--model", self.voice,
                "--output_file", out,
            ],
            input=text.encode("utf-8"),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        if not os.path.exists(out):
            raise RuntimeError("Piper TTS failed to generate audio")

        return out
