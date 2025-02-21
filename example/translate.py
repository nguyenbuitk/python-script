from deep_translator import GoogleTranslator

def translate_to_vietnamese(text):
    translator = GoogleTranslator(source='en', target='vi')
    translation = translator.translate(text)
    return translation

# Example usage
text_to_translate = "Hello, how are you?"
translated_text = translate_to_vietnamese(text_to_translate)
print(f"Original: {text_to_translate}")
print(f"Translated: {translated_text}")

