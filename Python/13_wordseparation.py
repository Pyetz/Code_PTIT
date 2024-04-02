def word_separation(S):
    words = []
    word = ""
    for i in range(len(S)):
        if S[i] == " ":
            words.append(word)
            word = ""
        else:
            word += S[i]
    words.append(word)
    return words

def main():
    S = input()

    for word in word_separation(S):
        print(word)

main()