#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()
    print(names)

with open('./Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()

    for i in names:

        stripped_name = i.strip()

        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f'./Output/ReadyToSend/letterFor{stripped_name}.txt', 'w') as complete_letter:
            complete_letter.write(new_letter)
