import data
from random import randint

score = 0
text = " "


def check(person1, person2):
    """Checing who has more followers"""
    global score
    global text
    if int(data.data[person1]['follower_count']) > int(data.data[person2]['follower_count']):
        score += 1
        text = f"You are right! your current score is {score}"
        return True
    else:
        print("You lose")
        return False


while True:
    while True:
        #They can't be the same person
        first = randint(0, 50)
        second = randint(0, 50)
        if first != second:
            break
    print(text)
    print(f"Compare A: {data.data[first]['name']}, {data.data[first]['description']}, from {data.data[first]['country']}")
    print(f"Compare B: {data.data[second]['name']}, {data.data[second]['description']}, from {data.data[second]['country']}")
    shot = input("Who has more folowers: ")
    if shot == "A":
        if check(first, second):
            pass
        else:
            break
    elif shot == "B":
        if check(second, first):
            pass
        else:
            break
    else:
        print("Wrong input")