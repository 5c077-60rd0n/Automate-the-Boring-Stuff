# Automate the Boring Stuff Scripts

## Chapter 1

`hello.py`

```python
# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')
my_name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
```

## Chapter 2

`exit_example.py`

```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```

`five_times_while.py`

```python
print("My name is")
i = 0
while i < 5:
    print('Scotty Five Times (' + str(i) + ')')
    i = i + 1
```

`five_times.py`

```python
print('My name is')
for i in range(5):
    print('Scotty Five Times (' + str(i) + ')')
```

`guess_the_numbers`

```python
# This is a guess the number game.
import random
secret_number = random.randint(1, 20)
print('I am thinking about a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break   # This condition is the gorrect guess!

if guess == secret_number:
    print('Good job! You guessed the number is ' +
          str(guesses_taken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secret_number))
```

`how_many_guests.py`

```python
name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
num_of_guests = int(input())
if num_of_guests:
    print('Be sure to have enough room for all of your guests.')
print('Done')
```

`infinate_loop.py`

```python
while True:
    print('Infinate loop!')
```

`little_kid.py`

```python
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
```

`print_random.py`

```python
import random
for i in range(5):
    print(random.randint(1, 10))
```

`rps_game.py`

```python
import random
import sys

print('ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()  # Quit the program.
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Break out of the player input loop.
        print('Type one of r, p, s or q.')

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is as tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
```

`swordfish.py`

```python
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```

`vampire.py`

```python
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not and undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
```

`vampire2.py`

```python
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
```

`your_name.py`

```python
name = ''
while name != 'your name':
    print('Please type in your name.')
    name = input()
print('Thank you!')
```

`your_name2.py`

```python
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
```
