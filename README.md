```bash
    pip install git+https://github.com/CAYTU/caytu_ai.git
```

```python
from maliba_ai import ASR

# Initialize the transcriber
transcriber = ASR(model_id = "MALIBA-AI/maliba-asr") 

# Transcribe an audio file
result = transcriber.transcribe_audio("path/to/your/audio.wav")
print(result)