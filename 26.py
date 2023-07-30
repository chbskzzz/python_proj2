# List Comprehension
# use : new_list = [new_item for item in list]

# Conditional List Comprehension
# use : new_list = [new_item for item in list if test]

# numbers =
# result = num for num in numbers if num % 2 == 0

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

for (index, row) in student_data_frame.interrow():
    if row.student == "bbss":
        print(row.score)