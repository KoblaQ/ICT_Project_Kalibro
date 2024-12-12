import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env.

import prompts # Import prompts
import base64

GENAI_API_KEY = os.getenv("GENAI_API_KEY") #Load API key from .env
genai.configure(api_key = GENAI_API_KEY) # Set the API key
model = genai.GenerativeModel("gemini-1.5-flash") # Initialize the generative model

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

image_path = ".\images\screenshot_1.png" # Path to the image (Refactor this to take image from webpage)
base64_image = encode_image(image_path) # Get the base64 string
prompt = prompts.prompt2 # Set the system prompt

response = model.generate_content([base64_image ,prompt]) # Generate response

print(response)
print("End of LARGE RESPONSE")
print(response.text) # Print the response
print("End of SMALL RESPONSE")
