"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Benáček

email: JanBenaczek@seznam.cz

discord: bejikaj

"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

delimiter = "-" * 40
asterisk = "*"

username = input("username: ")
password = input("password: ")

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

print(delimiter)

if registered_users.get(username) == password:
    print(f"Welcome to the app, {username}.")
    print("We have 3 text to be analyzed.")
    print(delimiter)

elif username not in registered_users:
    print("Unregistered user, terminating the program.")
    exit()
else:
    print("Your password is incorrect.")
    exit()

no_of_text_selection = int(input("Enter a nubmer btw. 1 and 3 to select:"))

if  0 < no_of_text_selection < 4:
    print(f"Text number {no_of_text_selection} selected.")
    
else:
    print("You picked the wrong number of text! Terminating the program.")
    exit()

print(delimiter)


text_to_count = str(TEXTS[no_of_text_selection - 1]).split()
count_of_words_in_text = len(TEXTS[no_of_text_selection - 1].split())

text_to_count_first_char = [letter[0] for letter in text_to_count]
sum_of_uppercase_first_char = sum(map(str.isupper, text_to_count_first_char))

alpha_list = [letter for letter in text_to_count if letter.isalpha()]
alpha_list_upper = sum(map(str.isupper, alpha_list))
alpha_list_lower = sum(map(str.islower, text_to_count))

digit_list = [letter for letter in text_to_count if letter.isdigit()]
count_of_digit_list = len(digit_list)
sum_of_digit_list = sum(map(int, digit_list))


print(f"There are {count_of_words_in_text} words in the selected text.")
print(f"There are {sum_of_uppercase_first_char} titlecase words.")
print(f"There are {alpha_list_upper} uppercase words.")
print(f"There are {alpha_list_lower} lowercase words.")
print(f"There are {count_of_digit_list} numeric strings.")
print(f"The sum of all the numbers {sum_of_digit_list}")

print(delimiter)
print("LEN|     OCCURENCES    |NR.")
print(delimiter) 

lenght_of_words_text = [len(word) for word in text_to_count]
lenght_dict = dict()

for count in lenght_of_words_text:
    if count not in lenght_dict:
        lenght_dict[count] = 1
    else: 
        lenght_dict[count] = lenght_dict[count] + 1
    
for key, value in sorted(lenght_dict.items()):
        print(f"{key:>2} | {value * asterisk :<17} | {value} ")
