# translation.py

from transformers import MarianMTModel, MarianTokenizer

def translate_text(text: str, src_lang: str, tgt_lang: str) -> str:
    """
    Translates a given text from source language to target language.

    Parameters:
        text (str): The input text to be translated.
        src_lang (str): ISO 639-1 code of the source language (e.g., 'de', 'fr').
        tgt_lang (str): ISO 639-1 code of the target language (e.g., 'en', 'hi').

    Returns:
        translated_text (str): Translated output string.
    """

    # Define model ID based on source and target language
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"

    # Load tokenizer and model from Hugging Face
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)

    # Generate translated text
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text
