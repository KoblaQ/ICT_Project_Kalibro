System_Prompt = "You are a helpful assistant specializing in image analysis and design."


User_Prompt_1 = """
Analyze the uploaded image and provide a report covering the following aspects concisely:
1. Art Style: Briefly describe the artistic influences or movements observed, if any.
2. Design Style: Summarize the layout, use of elements (e.g., icons, text, imagery), and applied design principles (e.g., minimalism, modernism).
3. Image Theme and Category: Classify the image theme (e.g., community, advertisement) and category (e.g., public services, event promotion).
4. Colors: List the dominant colors and briefly note their emotional or psychological impact.
5. Sentiment: Provide the overall mood or sentiment conveyed (e.g., inviting, professional).
"""


prompt2 = """
Analyze the uploaded image and provide a JSON report covering the following aspects concisely:

1. Art Style**: Briefly describe the artistic influences or movements observed, if any.
2. **Design Style**: Summarize the layout, use of elements (e.g., icons, text, imagery), and applied design principles (e.g., minimalism, modernism).
3. **Image Theme and Category**: Classify the image theme (e.g., community, advertisement) and category (e.g., public services, event promotion).
4. **Colors**: List the dominant colors and briefly note their emotional or psychological impact.
5. **Sentiment**: Provide the overall mood or sentiment conveyed (e.g., inviting, professional).

Format the response as a JSON object, like this:
{
    "art_style": "Example response",
    "design_style": "Example response",
    "theme_category": "Example response",
    "colors": ["Color1", "Color2", ...],
    "sentiment": "Example response"
}

Keep the response concise, under 300 tokens.
"""
