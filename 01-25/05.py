#random.shuffle()


#FizzBuzz

#RANGE
'''
for number in range(a,b):
    print(number)
'''
total = 0
for number in range(1,101):
    total += number

print(total)

exit()
# FOR LOOP
'''
for item in list_of_items:
    #Do something to each item
'''

student_scores = [78,65,89,86,55,91,64,89]

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is : {highest_score}")

