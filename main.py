from cartesia import Cartesia
import os
from dotenv import load_dotenv

load_dotenv()

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

chunk_iter = client.tts.bytes(
	model_id="sonic-3",
	transcript="I can't wait to see what you'll create!",
	voice={
			"mode": "id",
			"id": "6ccbfb76-1fc6-48f7-b71d-91ac6298247b",
	},
	output_format={
			"container": "wav",
			"sample_rate": 44100,
			"encoding": "pcm_f32le",
	},
)

with open("voices/sonic.wav", "wb") as f:
	for chunk in chunk_iter:
		f.write(chunk)