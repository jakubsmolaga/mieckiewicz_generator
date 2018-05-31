########### CONSTANTS ############
database_name = 'data/database_1.txt'
output_name = 'data/preprocessed_1.txt'
illegal_chars = '.,”:"-;–?!„[]1234567890'
##################################

# GET TEXT FROM DATABASE FILE
database_file = open(database_name, 'r', encoding='utf-8')
database_string = database_file.read()
database_file.close()

# FILTER OUT ILLEGAL CHARACTERS
for char in illegal_chars:
    database_string = database_string.replace(char, '')

# LOWER CASE EVERYTHING
database_string = database_string.lower()

# WRITE PROCESSED TEXT TO AN OUTPUT FILE
output_file = open(output_name, 'w', encoding='utf-8')
output_file.write(database_string)
output_file.close()