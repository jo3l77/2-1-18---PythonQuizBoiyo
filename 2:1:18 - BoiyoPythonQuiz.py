# trivia quiz

print("This is a quiz that tests your knowledge on __")

'''

'''

name = input("Enter your name: ")
print("Hi there", name,"!")

print("In this quiz, I will ask you 6 questions and give you three choices. Select the correct answer out of choices A, B, or C for each question.")
print(" _____________")

# set the score of the quiz to 0

score = 0
score = int(score)

# Question 1
print("Question 1: What is the largest ocean in the world? \n")
print("A. Indian Ocean")
print("B. Pacific Ocean")
print("C. Atlantic Ocean")
print("")

Q1answer = "B" # the right answer to question 1
Q1response = input("Your answer:")

if Q1response == "B" or Q1response == 'b':
    print("Correct!", Q1answer)
    score = score + 1
elif Q1response != "B" or Q1response != 'b':
    print("Sorry, that is incorrect.")
    score = score
print(name,", your final score is", score, "out of 10.")
elif score >=4>=6:
    print("Congratulations",name ."You passed!")
