# Import libraries
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env.

import prompts # Import prompts
import images # Import images
import base64


client = OpenAI() # Initialize the OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #Load OpenAI API key from .env
client.set_api_key(OPENAI_API_KEY) # Set the API key

prompt = prompts.prompt1 # Set the prompt

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

image_path = ".\images\screenshot_1.png" # Path to the image (Refactor this to take image from webpage)
base64_image = encode_image(image_path) # Get the base64 string

#Call the OpenAI API
def generate_openai_response(prompt, base64_image):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {
                "role": "role",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                ]
            },
        ]
    )

    output = response.choices[0].message.content
    return output

