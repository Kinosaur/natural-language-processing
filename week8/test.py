dictionary = {
    "i": "je",
    "like": "aime",
    "cats": "chats",
    "not": "ne",
    "good": "bon",
}

def word_by_word_translate(english_sentence):
    return " ".join(dictionary.get(word, word) for word in english_sentence.lower().split())

print(word_by_word_translate("I do not like cats"))