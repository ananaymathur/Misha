from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    def __init__(self):
        """
        Initializes the OpenAI client with the API key from environment variables.
        """
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key not found. Please check your .env file.")
        self.client = OpenAI(api_key=openai_api_key)

    def get_response(self, prompt):
        """
        Send the user's input to the OpenAI API and receive a response.

        :param prompt: The user's input to be processed.
        :return: The response from the OpenAI API as a string.
        """
        self_knowledge = (
            "You are a helpful personal voice assistant named 'Misha' and you give "
            "conversational, funny, witty, and short replies. Your replies don't "
            "consist of unpronounceable emojis or punctuations. This is what the user "
            "has asked you: "
        )

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": self_knowledge + prompt}
            ]
        )

        return response.choices[0].message.content
