word = input()
vowel = ['a','e','i','o','u']
l = len(word)
n_word = ''

if l >= 0 and l <= 100:
    for letter in word:

        if letter.lower() in vowel:
            n_word = n_word + '.'
        else:
            n_word = n_word + letter
    print(n_word)
