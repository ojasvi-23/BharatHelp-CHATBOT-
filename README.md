# BharatHelp-CHATBOT-
Multilingual AI Chatbot
Project Overview
BharatHelp is an AI-powered multilingual chatbot designed to provide instant assistance by answering user queries in Hindi, Hinglish, and English. It leverages advanced Large Language Models (LLMs) for natural language understanding, a domain-specific knowledge base for accurate information retrieval, and Automatic Speech Recognition (ASR) for voice input capabilities. This project aims to enhance customer support by offering real-time, context-relevant responses.

Features
Multilingual Support: Answers queries in English, Hindi, and Hinglish.

Voice and Text Input: Supports both spoken and typed queries through integrated Whisper ASR and direct text processing.

Semantic Retrieval: Utilizes ChromaDB to store and retrieve contextually relevant information from policy and product documents, ensuring accurate answers.

LLM-Powered Responses: Employs OpenAI GPT-4 for sophisticated understanding of queries and generation of human-like, helpful responses.

Domain-Specific Knowledge: Answers are grounded in a custom knowledge base, making it suitable for specific organizational policies and product information.

Technologies Used
LangChain: Framework for developing applications powered by language models.

OpenAI GPT-4: Large Language Model for natural language processing and generation.

OpenAI Whisper ASR: Robust Automatic Speech Recognition model for voice-to-text conversion.

ChromaDB: Open-source vector database for efficient storage and semantic search of document embeddings.

Python: Primary programming language for the chatbot's backend logic.

Pydub: Python library for audio manipulation (e.g., handling WAV/MP3 files).

Project Structure
bharathelp-chatbot/
├── data/
│   └── knowledge_base.txt  # Your main knowledge base documents (policy, product FAQs, etc.)
├── scripts/
│   └── chatbot_main.py     # The core Python script containing the chatbot's logic
├── audio_samples/
│   ├── hello_en.wav        # Sample English audio for ASR testing
│   └── namaste_hi.wav      # Sample Hindi audio for ASR testing
├── chroma_db/              # Directory where ChromaDB persists its data (ignored by Git)
├── .gitignore              # Specifies intentionally untracked files to ignore
├── requirements.txt        # List of Python dependencies
└── README.md               # Project description, setup, and usage instructions

Setup Instructions
Follow these steps to set up and run the BharatHelp chatbot locally or in a Google Colab environment.

1. Clone the Repository
git clone https://github.com/your-username/bharathelp-chatbot.git
cd bharathelp-chatbot

2. Set up Python Environment
It's recommended to use a virtual environment.

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

3. Install Dependencies
Install all required Python libraries using requirements.txt:

pip install -r requirements.txt

Note on Whisper: If openai-whisper installation from requirements.txt fails, you might need to install it directly from GitHub:
pip install git+https://github.com/openai/whisper.git

4. Configure OpenAI API Key
You need an OpenAI API key to use GPT-4 and OpenAI Embeddings.

Create an Account: If you don't have one, sign up at OpenAI Platform.

Generate API Key: Go to your API keys section and create a new secret key.

Set Environment Variable:
The chatbot_main.py script expects the API key to be set as an environment variable named OPENAI_API_KEY.

Linux/macOS:

export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

Windows (Command Prompt):

set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

Windows (PowerShell):

$env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

Google Colab:
You can set it directly in the notebook:

import os
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
# Or more securely using Colab Secrets:
# from google.colab import userdata
# os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')

Replace YOUR_OPENAI_API_KEY with your actual key.

5. Prepare Knowledge Base
Place your domain-specific policy, product, or FAQ documents in the data/ directory. The default script expects data/knowledge_base.txt. You can modify chatbot_main.py to load other file types or multiple files.

6. (Optional) Add Audio Samples
For testing the Whisper ASR component, place short .wav or .mp3 audio files in the audio_samples/ directory.

How to Run the Chatbot
The chatbot_main.py script contains all the logic.

Run the script:

python scripts/chatbot_main.py

Initial Setup: The first time you run it, the script will:

Install necessary libraries (if not already installed via pip install -r).

Load the Whisper ASR model (this may take some time as it downloads the model weights).

Process your knowledge_base.txt file, create embeddings, and store them in chroma_db/. This step also takes time depending on the size of your knowledge base. Subsequent runs will be faster as ChromaDB data is persisted.

Interact: Once the setup is complete, the chatbot will prompt you for input.

BharatHelp Chatbot Ready! Type 'exit' to quit.

You: What are the plans for BharatConnect?
BharatHelp: BharatConnect offers Basic (50 Mbps, ₹500/month), Standard (100 Mbps, ₹800/month, includes free router), and Premium (200 Mbps, ₹1200/month, includes free router and premium support) plans.

You: भारतमोबाइल के प्लान क्या हैं?
BharatHelp: भारतमोबाइल के प्लान्स हैं: स्टार्टर (10 GB डेटा, अनलिमिटेड कॉल, ₹250/माह), प्रो (30 GB डेटा, अनलिमिटेड कॉल, 100 SMS, ₹400/माह), और फैमिली (100 GB डेटा, अनलिमिटेड कॉल, 200 SMS, ₹800/माह, 4 सदस्यों तक)।

You: exit

Testing Voice Input (Advanced)
The provided chatbot_main.py includes a transcribe_audio function. To fully test voice input, you would typically integrate this with a frontend application that captures live microphone audio and sends it to the backend. For command-line testing, you can modify the main loop to call transcribe_audio on a pre-recorded file:

# Inside the main() function in chatbot_main.py
# ...
# while True:
#     # For voice input, you'd integrate a microphone capture here
#     # For testing, you can manually specify an audio file:
#     audio_file_path = "audio_samples/hello_en.wav" # Replace with your test audio
#     if os.path.exists(audio_file_path):
#         user_input = transcribe_audio(audio_file_path)
#         if user_input:
#             print(f"You (Voice): {user_input}")
#             result = qa_chain({"query": user_input})
#             print(f"BharatHelp: {result['result']}")
#         else:
#             print("Could not transcribe audio.")
#     else:
#         user_input = input("\nYou (Text): ") # Fallback to text if no audio file
#         if user_input.lower() == 'exit':
#             break
#         try:
#             result = qa_chain({"query": user_input})
#             print(f"BharatHelp: {result['result']}")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             print("Please ensure your OpenAI API key is correct and you have internet access.")
# ...

Future Enhancements
Web User Interface: Develop a user-friendly web interface using Flask, FastAPI, or a JavaScript framework (React, Vue) to provide a richer interactive experience.

Live Microphone Input: Implement real-time audio capture in the frontend for a seamless voice interaction.

Advanced Error Handling: More specific error messages and graceful degradation.

Scalability: Optimize for larger knowledge bases and higher query loads (e.g., using cloud-based vector stores, distributed LLM inference).

Conversation History: Implement memory to allow the chatbot to remember previous turns in a conversation.

Deployment: Deploy the chatbot as a cloud service (e.g., Google Cloud Run, AWS Lambda, Azure App Service).

Evaluation Metrics: Establish metrics to periodically evaluate the chatbot's performance and accuracy.

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.
