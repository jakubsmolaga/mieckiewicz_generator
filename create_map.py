########### CONSTANTS ############
input_file_name = 'data/preprocessed_4.txt'
default_map_file = 'data/map.json'
##################################

# IMPORTS
import json

# GET TEXT FROM THE FILE
input_file = open(input_file_name, 'r', encoding='utf-8')
raw_text = input_file.read()
text_array = raw_text.split()
text_array[0] = text_array[0][1:]  # <-- getting rid of "\ufeff" char
input_file.close()

# CREATE SET OF WORDS USED
all_words_used = set()
for word in text_array:
    all_words_used.add(word)
print('length of text (in words):', len(text_array))
print('number of words used:', len(all_words_used))

# INITIALIZE THE MAP
words_map = {}
for word in all_words_used:
    words_map[word] = {}

# FILL THE MAP
for i in range(len(text_array))[1:]:
    if text_array[i] in words_map[ text_array[i-1] ]:
        words_map[ text_array[i-1] ] [ text_array[i] ] += 1
    else:
        words_map[ text_array[i-1] ] [ text_array[i] ] = 1
    
# SAVE MAP FILE
map_file = open(default_map_file, 'w', encoding='utf-8')
map_file.write( json.dumps(words_map, ensure_ascii=False) )
map_file.close()