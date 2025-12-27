# local-voice-agent


command to install 
1. yay -S piper-tts

Download LESSAC
```bash 
curl -L -o en_US-lessac-high.onnx \
https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/high/en_US-lessac-high.onnx

curl -L -o en_US-lessac-high.onnx.json \
https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/high/en_US-lessac-high.onnx.json


```

Lamma install 
```bash 
Sudo pacman -S ollama
ollama pull llama3
```