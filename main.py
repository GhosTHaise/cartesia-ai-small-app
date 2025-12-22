from cartesia import Cartesia
import os
from dotenv import load_dotenv
import sounddevice as sd
import numpy as np
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])
llm = ChatGroq(model="llama-3.3-70b-versatile")

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
            

question = "Comment gagner du temps en étant en vacances ?"
template = """You are a helpful assistant that answers questions and return only the answer in french.

{question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm | StrOutputParser() | RunnableLambda(speak_stream) | RunnableLambda(play_stream)

result = chain.invoke({"question": question})
