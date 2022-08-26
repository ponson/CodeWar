# from InnerModules.module1 import module1_func1

def search4vowels(word:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def search4letters(word: str, letters:str='aeiou') -> str:
    return set(letters).intersection(set(word))

print(search4vowels("How many people ever worked for BenQ more than 10 years?"))
print(search4letters("How many people ever worked for BenQ more than 10 years?", 'yearsu'))