word = input()

l = len(word)

if l >= 0 and l <= 100:
    n_word = word[0] + str(l -2) + word[-1]
    print(n_word)


