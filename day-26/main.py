# new_list = [new_item for item in list //if ] <-- LIST COMPREHENSION

numbers = [1,2,3]
names = ["carlos", "karla", "patricio"]
new_numbers = [i+1 for i in numbers]
print(new_numbers)

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() // if}
new_dict = {student:100 for student in names}

print(new_dict)

# for(index, row) in dataframe.iterrows(): print(row.student)
