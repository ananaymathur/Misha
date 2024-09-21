import speech_recognition as sr
import sounddevice as sd
import numpy as np

class Listener:
    def __init__(self):
        """
        Initializes the speech recognizer.
        """
        self.recognizer = sr.Recognizer()

    def listen(self, duration=5, sample_rate=16000):
        """
        Capture voice input from the user and convert it to text.

        :param duration: Duration of the recording in seconds.
        :param sample_rate: Sample rate for the recording in Hz.
        :return: The recognized command as a string.
        """
        print("Listening...")
        try:
            # Record audio using sounddevice
            recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
            sd.wait()  # Wait until the recording is finished

            # Convert the recording to bytes suitable for speech recognition
            audio_data = np.int16(recording * 32767).tobytes()

            # Create an AudioData object for recognition
            audio = sr.AudioData(audio_data, sample_rate, 2)

            # Recognize speech using Google Speech Recognition
            command = self.recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            # Handle unintelligible speech
            return ""
        except sr.RequestError as e:
            # Handle errors during the recognition request
            print(f"Could not request results; {e}")
            return ""
    
    def is_stop_command(self, command):
        """
        Checks if the user's command indicates a desire to stop the bot.

        :param command: The recognized command string.
        :return: True if the command is a stop command, False otherwise.
        """
        stop_commands = ["stop", "exit", "quit", "goodbye", "shut down", "terminate"]
        return any(stop_phrase in command for stop_phrase in stop_commands)

