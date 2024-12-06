SAMPLE_Letter = "Mail Merge Project Start/Input/Letters/starting_letter.txt"
NAMES = "Mail Merge Project Start/Input/Names/invited_names.txt"
NEW_LETTER ="Mail Merge Project Start/Output/ReadyToSend/"
# with open(SAMPLE_Letter, "r") as letter:
#     print(letter.read())


def getting_sample(path):
    with open(path, "r") as letter:
        content = letter.read()
    return content

def inviting_letter(path, name):
    with open(path, "r") as letter:
        read_text = letter.read()
        content = read_text.replace("[name]", name)
    return content
    

def names_list(path, line_number):
    with open(path, "r") as names:
        name =names.readlines() 
        name = name[line_number].strip()
    return name


for a in range(7):
    name = names_list(path=NAMES, line_number=a)
    
    new_letter = inviting_letter(path=SAMPLE_Letter, name=name)
    new_file = f"{NEW_LETTER}{name}.txt"
    
    with open(new_file, "w") as newLetter:
        newLetter.write(new_letter)







    

