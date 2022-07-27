print("Welcome to my quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Awesome! Let the games begin! :)")

score = 0

answer = input("What is the most beautiful color? ").lower()
if answer == "blue":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the most beautiful city? ").lower()
if answer == "nairobi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the best pc game? ").lower()
if answer == "cod":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What right? ").lower()
if answer == "wrong":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your ultimate score is " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")