# put your code here.
def count_words(filename):
    f = open(filename)
    word_counts = {}
    for line in f:
        words = line.rstrip().split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0)+1
    return word_counts


def get_word_count(word, word_count):
    return word_count.get(word, 0)


counts = count_words('twain.txt')
for word in counts:
    # print(word + " " + str(get_word_count(word, counts)))
    print("{} {}".format(word, (counts[word])))
    