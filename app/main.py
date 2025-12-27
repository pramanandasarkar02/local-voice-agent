from app.config import settings
from app.audio.recorder import record
from app.audio.player import play_wav
from app.stt.whisper_stt import WhisperSTT
from app.llm.ollama_client import OllamaClient
from app.tts.piper_tts import PiperTTS
from app.memory.conversation import Memory
from app.logger import logger

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
        print("You:", text)

        if "exit" in text.lower():
            break

        prompt = memory.context() + "\nUser: " + text
        reply = llm.chat(prompt)

        memory.add(text, reply)
        print("AI:", reply)

        wav = tts.speak(reply)
        play_wav(wav)

if __name__ == "__main__":
    main()
