import sys

# Ensure proper encoding for Myanmar characters in terminal
sys.stdout.reconfigure(encoding='utf-8')

dictionary = {
    "i": "ကျွန်တော်",
    "you": "သင်",
    "like": "နှစ်သက်",
    "cats": "ကြောင်များ",
    "not": "မ",
    "good": "ကောင်း",
    "hello": "မင်္ဂလာပါ",
    "dogs": "ခွေးများ",
    "water": "ရေ",
    "food": "အစားအစာ",
    "thank": "ကျေးဇူး",
    "rice": "ထမင်း",
    "house": "အိမ်",
    "miss": "လွမ်း"
}

def word_by_word_translate(english_sentence):
    return " ".join(dictionary.get(word, word) for word in english_sentence.lower().split())

print(word_by_word_translate("I like cats and do not like dogs"))
print(word_by_word_translate("Hello I miss you"))