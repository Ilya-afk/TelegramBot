import json

black_list = []

with open('black_list.txt', encoding='utf-8') as r:
    for line in r:
        word = line.lower().split('\n')[0]
        if word != '':
            black_list.append(word)

with open('black_list.json', 'w', encoding='utf-8') as e:
    json.dump(black_list, e, ensure_ascii=True)
