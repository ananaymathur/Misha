# Misha Voice Chatbot

Misha is a voice-activated personal assistant built using Python, OpenAI, and various speech recognition and text-to-speech libraries. Misha listens for your voice commands, responds conversationally, and can be stopped when you ask it to. This project is designed to be modular, scalable, and easy to extend.

## Features

- **Voice Activation:** Misha activates when it hears its name.
- **Conversational AI:** Integrates with OpenAI's API to provide witty, conversational, and helpful responses.
- **Text-to-Speech:** Converts text responses into speech for a seamless interaction experience.
- **Graceful Exit:** Misha stops and exits the program when it detects stop commands like "stop", "quit", or "goodbye".
- **Modular Design:** Structured with a clear separation of concerns, making it easy to maintain and extend.

## Project Structure

```plaintext
voice_chatbot/
│
├── main.py                 # Main script to run the chatbot
├── chatbot.py              # Contains the VoiceChatBot class
├── tts.py                  # Contains the TextToSpeech class
├── listener.py             # Contains the Listener class
├── openai_client.py        # Contains the OpenAIClient class
├── requirements.txt        # List of required packages
└── .env                    # Environment file containing the OpenAI API key
```

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed. You can download Python from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ananaymathur/Misha.git
    cd Misha
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the `.env` file:**

    Create a `.env` file in the root directory of your project and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your-openai-api-key-here
    ```

### Running Misha

To start the voice chatbot, run:

```bash
python main.py
```

### Using Misha

- Say **"Misha"** to activate the chatbot.
- Speak naturally; Misha will respond based on the input it receives.
- To stop the chatbot, say **"stop"**, **"quit"**, **"exit"**, or **"goodbye"**.

## Modules Overview

### `main.py`

The entry point of the application. It initializes and activates the `VoiceChatBot`.

### `chatbot.py`

Contains the `VoiceChatBot` class, which integrates text-to-speech, listener, and OpenAI client functionalities.

### `tts.py`

Handles text-to-speech using the `TextToSpeech` class, allowing Misha to respond verbally.

### `listener.py`

Manages speech recognition using the `Listener` class. It captures audio input and converts it to text commands.

### `openai_client.py`

Contains the `OpenAIClient` class, responsible for communicating with the OpenAI API to generate responses.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new features, feel free to fork the repository and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Contact

**Your Name**  
Email: [ananaymathur@gmail.com](mailto:ananaymathur@gmail.com)  

## Acknowledgments

- [OpenAI](https://openai.com/) for their amazing AI models.
- [Python](https://www.python.org/) for providing the programming foundation.
- Libraries such as `speech_recognition`, `pyttsx3`, and `sounddevice` for making voice interaction possible.



