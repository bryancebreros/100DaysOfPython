

import pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}

on = True

while on:
    word = input("Enter word: ").upper()
    word_list = [new_dict[letter] for letter in word]
    for i in word_list:
        print(f"{i[0]} = {i}")

