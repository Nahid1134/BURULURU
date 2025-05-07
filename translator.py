from deep_translator import GoogleTranslator

def translate_text(text, region):
    lang_map = {
        "USA": "en",
        "Bangladesh": "bn",
        "Korea": "ko",
        "Japan": "ja",
        "Other": "en"
    }
    target_lang = lang_map.get(region, "en")
    return GoogleTranslator(source="auto", target=target_lang).translate(text)
