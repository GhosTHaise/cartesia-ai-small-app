# cartesia-ai-small-app

## Project Description
`cartesia-ai-small-app` is a Python-based application that leverages the Cartesia API and LangChain to provide a conversational AI experience. The app includes text-to-speech (TTS) capabilities and audio playback, making it an interactive and engaging tool.

## Features
- **Conversational AI**: Uses LangChain and Cartesia for generating responses.
- **Text-to-Speech**: Converts text responses into audio using Cartesia's TTS.
- **Audio Playback**: Streams audio responses in real-time.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GhosTHaise/cartesia-ai-small-app.git
   cd cartesia-ai-small-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Cartesia API key:
     ```env
     CARTESIA_API_KEY=your_api_key_here
     ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The app will process a predefined question and play the audio response.

## Dependencies
The project requires the following Python libraries:
- `cartesia>=2.0.17`
- `dotenv>=0.9.9`
- `langchain>=1.2.0`
- `langchain-core>=1.2.4`
- `langchain-google-genai>=4.1.2`
- `langchain-groq>=1.1.1`
- `numpy>=2.4.0`
- `pydub>=0.25.1`
- `sounddevice>=0.5.3`

## License
This project is licensed under the MIT License. See the LICENSE file for details.
