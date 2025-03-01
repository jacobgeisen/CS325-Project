# Jacob Geisen - 800732301

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class TinyLlama:
    def __init__(self):         # Loading tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        self.model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

    def generate(self, text):
        tokens = self.tokenizer(text, return_tensors="pt")                  # Converting text into tokens
        output = self.model.generate(**tokens, max_length=100)              # Generating response
        return self.tokenizer.decode(output[0], skip_special_tokens=True)   # Decoding response