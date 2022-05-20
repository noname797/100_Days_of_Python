# Eg of list comprehension [ val_1 if condition else val for i in list]

# without else : [i for i in numbers if i%2==0)

# Dictionary comprehension {new_key : new_value for (key,value) in dict.items() if condition)
# {student:random.randint(1,100) for student in names)

# Loop through rows in a data frame
# for (idx, row) in df.iterrows():
#     print(row)

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_dict = {}

for (idx, row) in df.iterrows():
    nato_dict[row.letter] = row.code


# OR

# nato_dict = {row.letter:row.code for (idx, row) in df.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_in = input("Enter your name : ")

for i in user_in:
    if i == ' ':
        print(" ")
    else:
        print(nato_dict[i.upper()])

# OR

# out = [nato_dict[i.upper()] for i in user_in]
# print(out)
#
