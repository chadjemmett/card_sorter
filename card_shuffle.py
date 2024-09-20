
random_deck = open('shuffled_deck.txt', 'r')

shuffled_deck = []

for line in random_deck.readlines():
    suit, value = line.split('of')[1].strip(), line.split('of')[0].strip()
    shuffled_deck.append({'value': value, 'suit': suit })


face_values = {
        'Ace': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10,
        'Jack': 12, 
        'Queen': 13, 
        'King': 14, 
    }
# Note:  this is a list comprehension in Python. It allows you to invert your existing hash table.

inverse_dict = {v: k for k, v in face_values.items()}

# replace strings with integers.
for hash in shuffled_deck:
    hash['value'] = face_values[hash['value']]

# note: lambda is an anonymous function in python. In it we pick out the key to the value we want to sort by.
shuffled_deck.sort(key=lambda hash: (hash['suit'], hash['value']))

# a string to output the same format we got in.
sorted_deck = ""

for hash in shuffled_deck:
    sorted_deck += f"{inverse_dict[hash['value']]} of {hash['suit']}\n"

print(sorted_deck)

random_deck.close()

sorted = open('sorted_deck.txt', 'w')
sorted.write(sorted_deck)
sorted.close()

