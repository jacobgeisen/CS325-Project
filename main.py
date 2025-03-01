# Jacob Geisen - 800732301

from models.phi import Phi
from models.tinyLlama import TinyLlama

def extract_kword(response):
    # Convert the response to lowercase and split into tokens
    tokens = response.lower().strip().split()
    # Check for one of the expected words
    for token in tokens:
        if token in ["positive", "negative", "neutral"]: # if token is in array, it is a key word (p/n/n) and is returned
            return token
    # No keywords found: return indication of error
    return "No sentiment found"

def evaluate_headline(model, headline):
    prompt = ( #prompt to be passed to each model
        f"Classify the sentiment of the following headline as one word only: neutral, negative, or positive.\n"
        f"Do not include any additional text. Respond with only one word.\n\n"
        f"Headline: \"{headline}\""
    )
    # Passing prompt to model to generate a response
    raw_response = model.generate(prompt)
    # Extracting the key word
    return extract_kword(raw_response)

# Read headlines from input.txt file
with open("input.txt", "r") as file:
    headlines = [line.strip() for line in file if line.strip()]

# Initializing the models
phi = Phi()
tinyLlama = TinyLlama()

# Getting evaluation for each headline from each model
results = {
    "Phi-1.5": [evaluate_headline(phi, headline) for headline in headlines],
    "TinyLlama": [evaluate_headline(tinyLlama, headline) for headline in headlines]
}

# Saving the results to responses.txt
with open("responses.txt", "w") as file:
    for model_name, sentiments in results.items():
        file.write(f"{model_name} -------------\n")
        for headline, sentiment in zip(headlines, sentiments):
            file.write(f"Headline: {headline}\nResponse: {sentiment}\n\n")

print("Responses generated and saved to responses.txt")