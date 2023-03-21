import sys

unit = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
numbers = []

def reset_numbers() -> None:
    global numbers
    numbers = [1, 2, 3]

def next_bet() -> float:
    return (numbers[0] + numbers[-1]) * unit

def win() -> None:
    global numbers
    numbers.pop(0)
    numbers.pop(-1)
    if len(numbers) < 2:
        reset_numbers()

def lose() -> None:
    global numbers
    numbers.append(numbers[0] + numbers[-1])

def print_numbers() -> None:
    global numbers
    print('numbers : ' + str(numbers))

print('############################')
print('# Start Monte Carlo Method #')
print('############################')

reset_numbers()
num_games = 1
profit = 0.0
num_win = 0
num_lose = 0

while True:
    print()
    print('game #' + str(num_games))
    print_numbers()
    bet_amount = next_bet()
    print('next bet amount : ' + str([bet_amount]))
    print('Win[(any)] or Lose[(enter)] ? : ', end='')
    num_games += 1
    result = input()
    if result.strip() != '':
        #win
        num_win += 1
        profit += bet_amount
        win()
    else:
        #lose
        num_lose += 1
        profit -= bet_amount
        lose()
    print('current profit : ' + str(profit))


