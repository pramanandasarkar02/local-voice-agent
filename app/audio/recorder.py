import sounddevice as sd
import numpy as np

def record(seconds=4, rate=16000):
    audio = sd.rec(
        int(seconds * rate),
        samplerate=rate,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    audio = np.squeeze(audio)

    # normalize (important for Whisper)
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val

    return audio
