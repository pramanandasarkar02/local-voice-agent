from faster_whisper import WhisperModel

class WhisperSTT:
    def __init__(self, model):
        self.model = WhisperModel(
            model,
            device="cpu",
            compute_type="int8"  # production-friendly
        )

    def transcribe(self, audio):
        segments, _ = self.model.transcribe(
            audio,
            language="en",          # FORCE ENGLISH
            task="transcribe",      # NO TRANSLATION
            beam_size=5,
            vad_filter=True         # removes silence/noise
        )
        return " ".join(seg.text.strip() for seg in segments)
