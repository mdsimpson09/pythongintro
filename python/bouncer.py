# age= 19
# isBirthday = False
# if age >= 21:
#     print("you can drink")
#     if isBirthday:
#         print("happy fucking birthday")
# elif age >= 18:
#     print ("you can come in, but can't drink")
#     if isBirthday:
#         print("here's an applejuice")
# else:
#     print("sorry kid. go home.")

    # do_if_true if CONDITION else do_if_false

    # condition ? do_if_true : do_if_false

# target = 37
# guess = None

# while guess != target:
#     guess = input("please enter a guess..")
#     if guess == 'q' or guess == 'quit':
#         break
#     guess = int(guess)

# print("all done")

# colors = ['red', 'orange', 'yellow']
# for color in colors:
#     print(color)

def greet(person):
    return f"hello there, {person}"

def divide(a,b):
    if type(a) is int and type(b) is int:
        return a/b
    return 'a and b must be integers'

#how do we define documentation so that people can run help on our own things 

def add_limited_numbers(a,b):
    """add two numbers, making sure sum caps at 100"""
    sum = a+b
    #if this required explaination, comment here
    if sum> 100:
        sum = 100
    return sum