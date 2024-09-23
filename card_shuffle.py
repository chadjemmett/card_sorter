class Deck():

    # In python __init__ is a constructor in python.
    # Self is Python's keyword that refers to the instance of class
    def __init__ (self, imported_deck):
        self.shuffled_deck  = imported_deck
        self.card_list = []
        self.deck_id  = 0

        self.face_values = {
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

    # A double underscore designates the method as a private method.
    # Each method does one thing. It updates or changed the data in the card_list praperty of the class.
    def  __process_deck(self):
        random_deck = open(self.shuffled_deck, 'r')
        for line in random_deck.readlines():
            suit, value = line.split('of')[1].strip(), line.split('of')[0].strip()
            self.card_list.append({'value': value, 'suit': suit })
        random_deck.close()
    
    def __index_values(self):
        for hash in self.card_list:
            hash['value'] = self.face_values[hash['value']]
   
    def  __sort(self):
        self.card_list.sort(key=lambda hash: (hash['suit'], hash['value']))

    def __reindex(self):
        inverse_dict = {v: k for k, v in self.face_values.items()}
        for card_values  in self.card_list:
            card_values['value'] = inverse_dict[card_values['value']]

    def __write_to_file(self):
        file = open(f"Sorted-{self.shuffled_deck}", "w")
        file_data = ""
        for line  in self.card_list:
            file_data += f"{line['value']} of {line['suit']}\n"

        file.write(file_data)
        file.close()
        return f"Sorted-{self.shuffled_deck}"

    # the user only needs to do  two things. Provide an existing text file  of  shuffled cards. And call sort on the
    # object
    def sort(self):
        self.__process_deck()
        self.__index_values()
        self.__sort()
        self.__reindex()
        return self.__write_to_file()

d = Deck("shuffled_deck.txt")
print(d.sort())

