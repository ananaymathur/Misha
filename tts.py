import pyttsx3

class TextToSpeech:
    def __init__(self):
        """
        Initializes the text-to-speech engine.
        """
        self.engine = pyttsx3.init()
        
        # Reducing the speach rate to 150
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        """
        Convert text to speech and output it using the TTS engine.

        :param text: The text to be spoken.
        """
        self.engine.say(text)
        self.engine.runAndWait()
