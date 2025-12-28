import subprocess
import uuid
import os
import tempfile

class PiperTTS:
    def __init__(self, voice):
        self.voice = voice

    def speak(self, text: str) -> str:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            out = tmp.name

        try:
            proc = subprocess.run(
                ["/usr/bin/piper-tts", "--model", self.voice, "--output_file", out],
                input=text.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,  
            )

            if proc.returncode != 0:
                stderr_msg = proc.stderr.decode("utf-8", errors="ignore")
                raise RuntimeError(f"Piper TTS failed: {stderr_msg}")

            if not os.path.exists(out):
                raise RuntimeError("Piper TTS did not generate an audio file.")

            return out

        except Exception as e:
            if os.path.exists(out):
                os.remove(out)
            raise e
