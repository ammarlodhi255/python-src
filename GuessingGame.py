
nums = [1, 2, 3, 4]
nums.sort(reverse = True)

for index, num in enumerate(nums):
    print(f"nums[{index}] = {num}")

#Guessing game
value = 78
guess = int(input("Enter your guess: "))
guesses_left = 4

while(guess != value and guesses_left > 0):
    print(f'Incorrect guess, {guesses_left} guesses left')
    guess = int(input("Enter your guess: "))
    guesses_left -= 1

if guess == value: print("Correct guess!!")
else: print("You lost")
