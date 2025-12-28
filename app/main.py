from app.config import settings
from app.audio.recorder import record
from app.audio.player import play_wav
from app.stt.whisper_stt import WhisperSTT
from app.llm.ollama_client import OllamaClient
from app.tts.piper_tts import PiperTTS
from app.memory.conversation import Memory
from app.logger import logger
import tempfile
import os

def speak_chunks(tts: PiperTTS, text: str):
    max_chunk = 200 
    start = 0
    while start < len(text):
        chunk = text[start:start + max_chunk]
        try:
            wav_file = tts.speak(chunk)
            play_wav(wav_file)
            # os.remove(wav_file)
        except RuntimeError as e:
            logger.error(f"TTS failed for chunk: {chunk}\n{e}")
        start += max_chunk

def main():
    logger.info("Starting Local Voice Agent")

    stt = WhisperSTT(settings.whisper_model)
    llm = OllamaClient(settings.ollama_model)
    tts = PiperTTS(settings.piper_voice)
    memory = Memory()

    while True:
        print("🎤 Speak...")
        audio = record()

        text = stt.transcribe(audio)
        if not text.strip():
            continue
        print("You:", text)

        if "exit" in text.lower():
            break

        prompt = memory.context() + "\nUser: " + text
        reply = llm.chat(prompt)

        memory.add(text, reply)
        print("AI:", reply)

        # speak safely in chunks
        speak_chunks(tts, reply)

        memory.showHistory()

if __name__ == "__main__":
    main()
