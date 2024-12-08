def count_words(text):
    words = text.split(",")
    return len(words)


def count_number_of_each_word(text):
    words = text.split(",")
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
            # word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count

def count_number_of_each_word_using_default_dict(text):
    from collections import defaultdict
    words = text.split(",")
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count

print(count_words("name,23,value,42.1"))  # 4
res = count_number_of_each_word("name,23,value,42.1,name,23")  # {'name': 2, '23': 2, 'value': 1, '42.1': 1}
print(res)
print(res["name"])
# for field in res.keys():
#     print(field, res[field])
for field in ["name", "address", "age"]:
    if field in res:
        print(field, res[field])
    else:
        print(field, "not founnd:")
    print(res.get(field, 0))


# python day06/count_words.py FILE


for pair in res.items():
    print(pair)
    print(pair[0], pair[1])

for field, value in res.items():
    print(field, value)


