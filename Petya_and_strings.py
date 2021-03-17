word1 = input()
word2 = input()
word1_greater = 0
word2_greater = 0

index = 0
if (len(word1) > 0 and len(word1) < 101) and (len(word2) > 0
                                              and len(word2) < 101):

    while index <= len(word1) - 1 and index <= len(word2) - 1:
        for letter in word1:
            if letter.lower() < word2[index].lower():
                word2_greater = word2_greater + 1
            if letter.lower() > word2[index].lower():
                word1_greater = word1_greater + 1
            index += 1

    if word1_greater < word2_greater:
        print(-1)

    elif word1_greater == word2_greater:
        print(0)

    else:
        print(1)
