import json

def read_file(file_name):
    lines = []
    with open(file_name) as file:
        lines = file.readlines()
        # print(lines)
        # print(type(lines).__name__)
        # print(len(lines))
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')

    return lines

def clean_words(words):
    for i in range(len(words)): 
        l = words[i].split('(')
        words[i] = l[0]

def get_word_length_map(words):
    word_length_map = dict()

    for word in words:
        word_length = len(word)
        if word_length in word_length_map:
            word_length_map[word_length].append(word)
        else:
            word_length_map[word_length] = [word]
    
    return word_length_map

def write_json_file(dictionary, file_name):
    with open(file_name, 'w') as outfile:
        json.dump(dictionary, outfile)

# found lines list at http://www-personal.umich.edu/~jlawler/wordlist.html
words = read_file('wordlist.txt')
clean_words(words)
word_length_map = get_word_length_map(words)
keys = list(word_length_map.keys())
keys.sort()
print(keys)
write_json_file(word_length_map, 'word_length_map.json')