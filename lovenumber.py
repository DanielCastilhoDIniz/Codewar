print("The Love Calculator is calculating your score...")
name1 = "David Beckham"

name2 = "Victoria Beckham"
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = (name1+name2).upper()
first_number = 0
second_number = 0
for letter in "TRUE":
    if letter in names:
        first_number += names.count(letter)

for letter in "LOVE":
    if letter in names:
        second_number += names.count(letter)

score = str(first_number)+str(second_number)
score_number = int(score)

print(score_number)
if (score_number >= 40) and (score_number <= 50):
    print(f"Your score is {score}, you are alright together.")
elif (score_number < 10) or (score_number > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
else:
     print(f"Your score is {score}.")
