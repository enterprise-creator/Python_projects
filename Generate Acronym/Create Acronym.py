

input_string = str(input("Enter a sequence of words"))
words = input_string.split()
acronym = []
for word in words:
    acronym.append(word[0])

print(''.join(acronym))

    

