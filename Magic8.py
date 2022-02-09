import random
name = ""
question = "Will I get the job?"
answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - Definitely!"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3: 
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Ask again later"
elif random_number == 5:
    answer = "Reply hazy, try again"
elif random_number == 6:
    answer = "Outlook not so good"
elif random_number == 7:
    answer = "Very doubtful"
elif random_number == 8:
    answer = "I think so!"
elif random_number == 9:
    answer = "The answer is definitely YES!"
else:
    answer = "Error"

if name == " ":
     print(question)
else:
    print(name + " asks: " + question)

if question == "":
    print("What do you want to know")
else:
     print("Magic 8-ball says: " + answer)
