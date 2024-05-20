import random

print("Let's play Pig Game!")

# To get random number
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Getting input of players
while True:
    players = input("Enter the number of Players (2 - 6): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 6:
            break
        else:
            print("Must be between 2-6!")
    else:
        print("Invalid, Try Again!")

max_score = 50
players_list = [0 for _ in range(players)]

while max(players_list) < max_score:
    for player in range(players):
        print("\nPlayer number ", player + 1, "turn has just started!\n")
        print("Your current score is: ", players_list[player], "\n")
        current_score = 0
        while True:
            should_roll = input("Do you want to roll? (y)")

            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                current_score = 0
                print("\nYou rolled 1! Your turn is over.\n")
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your current score is: ", current_score)

        players_list[player] += current_score
        print("Your total score is: ", players_list[player])

max_score = max(players_list)
winner = players_list.index(max_score)
print("\nPlayer ", winner + 1, "won the game!")

