import requests
import os

# API access key (if required for the API call)
API_KEY = "6b827fb6d8114dc7"
SEARCH_URL = "https://www.wikiart.org/en/api/2/PaintingSearch"

# List of all art styles
art_styles = [
    "Ancient Egyptian Art", "Predynastic", "Early Dynastic", "Old Kingdom", "Middle Kingdom", "New Kingdom",
    "Amarna", "3rd Intermediate Period", "Late Period", "Ptolemaic", "2nd Intermediate Period", "Ancient Greek Art",
    "Archaic", "Classical", "Hellenistic", "Geometric", "Western Medieval Art", "Early Christian", "Early Byzantine",
    "Middle Byzantine", "Mozarabic", "Komnenian style", "Latin Empire of Constantinople", "Late Byzantine",
    "Macedonian Renaissance", "Romanesque", "Mosan art", "Gothic", "International Gothic", "Viking art", 
    "Medieval Art", "Crusader workshop", "Moscow school of icon painting", "Cretan school", "Coptic art", 
    "Novgorod school", "Kyiv school", "Vladimir school", "Galicia-Volyn school", "Pskov school", "Yaroslavl school",
    "Vologda school", "Chernihiv school", "Western Renaissance Art", "Proto Renaissance", "Early Renaissance",
    "High Renaissance", "Mannerism", "Northern Renaissance", "Renaissance", "Western Post Renaissance Art",
    "Baroque", "Tenebrism", "Rococo", "Classicism", "Neoclassicism", "Academicism", "Romanticism", "Orientalism",
    "Costumbrismo", "Biedermeier", "Neo-Rococo", "Luminism", "Realism", "Modern Art", "American Realism",
    "Naturalism", "Naïve Art", "Social Realism", "Abstract Art", "Surrealism", "Post-Impressionism", "Symbolism",
    "Metaphysical art", "Tonalism", "Impressionism", "Magic Realism", "Fantastic Realism", "Pointillism",
    "Divisionism", "Art Deco", "Precisionism", "Cloisonnism", "Regionalism", "Socialist Realism", "Fauvism",
    "Expressionism", "Cubism", "Constructivism", "Minimalism", "Contemporary Art", "Photorealism", "Graffiti Art",
    "Street Art", "Digital Art", "Fantasy Art", "Neo-Expressionism", "Pop Art", "Abstract Expressionism"
]

# Maximum number of images to download per art style
MAX_IMAGES_PER_STYLE = 50

# Function to sanitize folder names
def sanitize_folder_name(name):
    return name.replace(" ", "_").replace("/", "-").lower()

# Function to download images for a specific art style
def download_images_by_style(art_style):
    params = {
        "term": art_style,
        "imageFormat": "Large"
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(SEARCH_URL, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error {response.status_code} for art style: {art_style}")
        return

    try:
        paintings = response.json().get("data", [])

        # Create a folder for the current art style
        main_folder = "images"
        sanitized_style_name = sanitize_folder_name(art_style)
        style_folder = os.path.join(main_folder, sanitized_style_name)
        os.makedirs(style_folder, exist_ok=True)

        # Download up to MAX_IMAGES_PER_STYLE images
        for index, painting in enumerate(paintings[:MAX_IMAGES_PER_STYLE]):
            image_url = painting.get("image")
            title = painting.get("title", "unknown").replace("/", "-")
            artist = painting.get("artistName", "unknown").replace("/", "-")
            image_filename = os.path.join(style_folder, f"{title} - {artist}.jpg")

            if image_url:
                try:
                    img_data = requests.get(image_url).content
                    with open(image_filename, "wb") as img_file:
                        img_file.write(img_data)
                    print(f"Downloaded image {index + 1}/{MAX_IMAGES_PER_STYLE} for art style: {art_style}")
                except Exception as e:
                    print(f"Error downloading image: {e}")
    except Exception as e:
        print(f"Error processing response for art style: {art_style} - {e}")

if __name__ == "__main__":
    # Create the main "images" folder
    os.makedirs("images", exist_ok=True)

    # Download images for each art style
    for art_style in art_styles:
        print(f"Downloading images for art style: {art_style}")
        download_images_by_style(art_style)
