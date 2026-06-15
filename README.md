# Higher Lower Game

## Project Overview

This is a simple Python terminal game where the player compares two famous people and guesses who has more followers.

The game continues until the player gives a wrong answer.

## Features

* Randomly selects two accounts
* Player chooses A or B
* Checks if the answer is correct
* Keeps track of score
* Ends the game when the answer is wrong

## Technologies Used

* Python
* Functions
* Loops
* Dictionaries
* Lists
* Random Module

## How to Run

```bash
python main.py
```

## Example Output

```text
WELCOME TO HIGHER LOWER GAME!!!!

Compare A : Akshay Kumar, a Bollywood actor

VS

Against B : Janhvi Kapoor, a Bollywood actress

who has more followers? Type 'A' or 'B': a

you are right! Current score 1
```

## Logic Used

### 1. Select Random Accounts

```python
account_b = random.choice(data)
```

A random account is selected from the dataset.

### 2. Display Account Information

The function:

```python
format_data(account)
```

shows:

* Name
* Description

Example:

```text
Akshay Kumar, a Bollywood actor
```

### 3. Take User Input

```python
guess = input("who has more followers? Type 'A' or 'B': ")
```

The player chooses A or B.

### 4. Compare Followers

The program gets follower counts from both accounts and checks the answer using:

```python
check_answer()
```

### 5. Update Score

If the answer is correct:

```python
score += 1
```

The score increases by 1.

### 6. End Game

If the answer is wrong:

```python
game_conti = False
```

The game stops and displays the final score.

## What I Learned

* Working with dictionaries and lists
* Creating and using functions
* Using while loops
* Taking user input
* Using the random module
* Writing game logic
* Tracking score in a program

## Future Improvements

* Add a logo using ASCII art
* Clear the screen after each round
* Add difficulty levels
* Show follower difference after each round
* Add more accounts

## Author

Madhumita Bhunya
