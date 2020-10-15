def search4vowels(phrase: str) -> set:
     return set('aeiou').intersection(set(phrase))

def search4letters(word,letters):
    return set(word).intersection(set(letters))