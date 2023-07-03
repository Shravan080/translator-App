from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    print("Translator App")
    print("----------------------")
    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'hi' for hindi): ")
    translated_text = translate_text(text, target_language)
    print("Translated text:", translated_text)

if __name__ == "__main__":
    main()
