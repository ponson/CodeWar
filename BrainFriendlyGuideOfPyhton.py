"""Display any vowels found in an asked-for word."""
def search4vowels_v1():
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


def search4vowels(word):
    vowels = set('aeiou')
    return vowels.intersection(set(word))


search4vowels("Understanding")