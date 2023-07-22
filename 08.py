#3
# test_h = int(input("Height of wall: ))
#Prime Number Checker
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It's not a prime number")

prime_checker(97)

exit()
#2
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")

greet_with(location="London", name="Jack")

exit()

#1
# functions
#function with inputs
def greet_with_name(name):
    print(f"Hellow {name}")
    print(f"How do you do {name}")

greet_with_name("suji")
#something : parameter, 123 : argument
