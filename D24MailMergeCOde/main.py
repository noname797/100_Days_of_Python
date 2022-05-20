import re

with open("Input/Names/invited_names.txt") as file:
    content = file.read()

INVITEES = content.split('\n')

for i in INVITEES:
    path = f"Output/letter_for_{i}.txt"
    with open(path, mode='w') as file:

        with open("Input/Letters/starting_letter.txt") as writer:

            contents = writer.read()
            file.write(re.sub('\[name]', i, contents))
