from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        if lang == 'en':
            return "English"
        else:
            return "Non-English"
    except Exception as e:
        return f"Error detecting language: {e}"

# Example usage
text_english = "This is a sample text in English."
text_non_english = "Đây là một đoạn văn mẫu bằng tiếng Việt."

print(f"Text: {text_english} - Detected: {detect_language(text_english)}")
print(f"Text: {text_non_english} - Detected: {detect_language(text_non_english)}")

