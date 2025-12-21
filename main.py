from cartesia import Cartesia
import os
from dotenv import load_dotenv
import sounddevice as sd
import numpy as np

load_dotenv()

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

def speak_stream(text: str):
    return client.tts.bytes(
        model_id="sonic-3",
        transcript=text,
        voice={
            "mode": "id",
            "id": "6ccbfb76-1fc6-48f7-b71d-91ac6298247b",
        },
        output_format={
            "container": "raw",
            "sample_rate": 44100,
            "encoding": "pcm_f32le",
        },
    )

def play_stream(chunk_iter):
    stream = sd.OutputStream(
        samplerate=44100,
        channels=1,
        dtype="float32"
    )

    leftover = b""

    with stream:
        for chunk in chunk_iter:
            data = leftover + chunk
            valid_length = (len(data) // 4) * 4

            if valid_length == 0:
                leftover = data
                continue

            audio_bytes = data[:valid_length]
            leftover = data[valid_length:]

            audio = np.frombuffer(audio_bytes, dtype=np.float32)
            stream.write(audio)

stream = speak_stream("Hello, I am speaking to you in real time. I am so happy!")
play_stream(stream)
