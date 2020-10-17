def search4vowels(phrase: str) -> set:
     return set('aeiou').intersection(set(phrase))

def search4letters(word,letters):
    x= set(word).intersection(set(letters))
    if x == set():
         return str("nothing")
    else:
         return x