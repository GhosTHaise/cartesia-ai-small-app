# cartesia-ai-small-app 🎙️🤖

## Overview

`cartesia-ai-small-app` is a lightweight Python application that demonstrates how to build a **conversational AI with real-time text-to-speech (TTS)** using **Cartesia**, **LangChain** and **Groq**.
The app generates AI responses and streams them as audio, creating an interactive voice-based experience.

This project is intended as a **small, focused example** rather than a full production system.

---

## Features

* 🧠 **Conversational AI** powered by LangChain
* 🔊 **Text-to-Speech (TTS)** using the Cartesia API
* 🎧 **Real-time audio streaming & playback**
* ⚡ **Fast dependency management with `uv`**

---

## Prerequisites

* Python **3.12+**
* [`uv`](https://github.com/astral-sh/uv) installed
* A valid **Cartesia API key**

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/GhosTHaise/cartesia-ai-small-app.git
cd cartesia-ai-small-app
```

### 2. Install dependencies with `uv`

This project does **not** use `requirements.txt`.
Dependencies are managed via `pyproject.toml`.

```bash
uv sync
```

---

## Environment Setup

Create a `.env` file at the root of the project:

```env
CARTESIA_API_KEY=your_cartesia_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

---

## Usage

Run the application:

```bash
uv run python main.py
```

The app will:

1. Generate a response from the AI
2. Convert the response to speech using Cartesia
3. Stream and play the audio in real time

---

## Tech Stack & Dependencies

Main libraries used:

* `cartesia`
* `langchain`
* `langchain-core`
* `langchain-google-genai`
* `langchain-groq`
* `numpy`
* `pydub`
* `sounddevice`
* `python-dotenv`

> Exact versions are defined in `pyproject.toml` and resolved by `uv`.

---

## Project Status

🚧 **Experimental / Demo project**
This app is designed for learning and experimentation with voice-enabled AI systems.

---

## License

MIT License
See the [LICENSE](LICENSE) file for details.

---

