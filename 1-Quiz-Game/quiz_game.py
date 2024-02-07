print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")  # Ask the user if they want to play
score = 0  # Initialize the score variable to 0

if playing != "yes":
    quit()  # If the user doesn't want to play, quit the game

print("Okay! Let's play :)")  # If the user wants to play, start the game

# answer is a variable that stores the correct answer to the question
answer = input("What does GPU stand for? ")  # Ask the user the first question
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")  # Ask the user the second question
if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does CPU stand for? ")  # Ask the user the third question
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")  # Ask the user the fourth question
if answer == "Power Supply Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does HDD stand for? ")  # Ask the user the fifth question
if answer == "Hard Disk Drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does SSD stand for? ")  # Ask the user the sixth question
if answer == "Solid State Drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print ("You got " + str(score) + " questions correct!")  # Print the final score
# i did concatenate the string and the score variable using the + operator
print ("You got " + str((score/6)*100) + "%.")  # Print the percentage score