from cartesia import Cartesia
import os
from dotenv import load_dotenv
import sounddevice as sd
import numpy as np
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import threading

# ─────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────
load_dotenv()

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])
llm = ChatGroq(model="llama-3.3-70b-versatile")

stop_event = threading.Event()
current_audio_thread = None

# ─────────────────────────────────────────────
# Text-to-Speech (Cartesia)
# ─────────────────────────────────────────────
def speak_stream(text: str):
    return client.tts.bytes(
        model_id="sonic-3",
        transcript=text,
        voice={
            "mode": "id",
            "id": "36532b82-ce6c-43d7-bdf3-2183e414966c"
        },
        output_format={
            "container": "raw",
            "sample_rate": 44100,
            "encoding": "pcm_f32le",
        },
    )

# ─────────────────────────────────────────────
# Audio playback (interruptible)
# ─────────────────────────────────────────────
def play_stream(chunk_iter, stop_event: threading.Event):
    stream = sd.OutputStream(
        samplerate=44100,
        channels=1,
        dtype="float32"
    )

    leftover = b""

    with stream:
        for chunk in chunk_iter:
            if stop_event.is_set():
                break

            data = leftover + chunk
            valid_length = (len(data) // 4) * 4

            if valid_length == 0:
                leftover = data
                continue

            audio_bytes = data[:valid_length]
            leftover = data[valid_length:]

            audio = np.frombuffer(audio_bytes, dtype=np.float32)
            stream.write(audio)

# ─────────────────────────────────────────────
# Speak controller (stop + restart)
# ─────────────────────────────────────────────
def speak(text: str):
    global current_audio_thread

    # Stop previous audio
    if current_audio_thread and current_audio_thread.is_alive():
        stop_event.set()
        current_audio_thread.join()

    stop_event.clear()

    audio_stream = speak_stream(text)

    current_audio_thread = threading.Thread(
        target=play_stream,
        args=(audio_stream, stop_event),
        daemon=True
    )
    current_audio_thread.start()

# ─────────────────────────────────────────────
# LangChain (TEXT ONLY)
# ─────────────────────────────────────────────
prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant that answers questions and return only the answer in french.

{question}
"""
)

chain = prompt | llm | StrOutputParser()

# ─────────────────────────────────────────────
# Interactive loop
# ─────────────────────────────────────────────
print("💬 Tape ton message (Ctrl+C pour quitter)\n")

try:
    while True:
        question = input("👤 Vous : ")

        if not question.strip():
            continue

        answer = chain.invoke({"question": question})

        print(f"\n🤖 Assistant : {answer}\n")
        speak(answer)

except KeyboardInterrupt:
    stop_event.set()
    print("\n👋 Au revoir !")
