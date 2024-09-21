from tts import TextToSpeech
from listener import Listener
from openai_client import OpenAIClient
import sys

class VoiceChatBot:
    def __init__(self):
        """
        Initializes the VoiceChatBot class with the necessary components.
        """
        self.tts = TextToSpeech()
        self.listener = Listener()
        self.client = OpenAIClient()
        self.tts.speak("Misha bot is initializing...")

    def activate(self):
        """
        Activate the chatbot, making it start listening for commands when the
        trigger word is detected.
        """
        self.tts.speak("Misha bot is now active.")
        print("Misha bot is now active.")
        while True:
            command = self.listener.listen()
            if "misha" in command:
                
                # Check for stop commands
                if self.listener.is_stop_command(command):
                    self.tts.speak("Goodbye!")
                    print("Misha bot is shutting down.")
                    sys.exit(0)  # Exit the program gracefully
                    
                print(f"You said: {command}")
                response = self.client.get_response(command)
                print(f"Misha: {response}")
                self.tts.speak(response)

