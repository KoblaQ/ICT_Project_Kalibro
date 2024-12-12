# Import libraries
from openai import OpenAI
import os
from pydantic import BaseModel
import prompts # Import prompts
import base64
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env.



client = OpenAI() # Initialize the OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #Load OpenAI API key from .env
print(OPENAI_API_KEY)
client.api_key(OPENAI_API_KEY) # Set the API key
User_Prompt_Text = prompts.User_Prompt_1 # Set the prompt
System_Prompt_Text = prompts.System_Prompt # Set the system prompt 

# Set responseformat (TODO Modify this to get required values from the prompt)
class Kalibro_Response_Format(BaseModel):
    art_style: str
    design_style: str
    theme_category: str
    colors: list
    sentiment: str

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

image_path = ".\images\screenshot_1.png" # Path to the image (Refactor this to take image from webpage)
base64_image = encode_image(image_path) # Get the base64 string

#Call the OpenAI API
def generate_openai_response(System_Prompt_Text, User_Prompt_Text, base64_image):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": System_Prompt_Text
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": User_Prompt_Text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ]
            },
        ],
        response_format= Kalibro_Response_Format, # Set the response format
        max_tokens= 300, # Set the max tokens
        temperature= 0.7, # Adjusts creativity of the response
    )
    output = response.choices[0].message.parsed # Get the response (Modify this to get the correct values)
    return output

KalibroAnalysis = generate_openai_response(System_Prompt_Text, User_Prompt_Text, base64_image) # Call the function


# Parse response to get variables from JSON object
art_style = KalibroAnalysis.art_style
design_style = KalibroAnalysis.design_style
theme_category = KalibroAnalysis.theme_category
colors = KalibroAnalysis.colors # List of colors might come out as an array.
sentiment = KalibroAnalysis.sentiment

# Print the variables
print(f"Art Style: {art_style}")
print(f"Design Style: {design_style}")
print(f"Theme Category: {theme_category}")
print(f"Colors: {colors}")
print(f"Sentiment: {sentiment}")
# Add the response to the webpage