def is_anagram(word):
    reversed_word = ''.join(reversed(word))

    if word == reversed_word:
        print("It is an Anagram")
    else:
        print("It is not an Anagram")

is_anagram("Hola")
