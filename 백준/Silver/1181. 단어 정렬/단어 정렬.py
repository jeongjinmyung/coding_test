N = int(input())
word_list = [input().strip() for _ in range(N)]

unique_words = set(word_list)
sorted_words = sorted(unique_words, key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)