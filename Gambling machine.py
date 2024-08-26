import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3


symbol_counter = {
    "A": 2,
    "B": 4,
    "C": 8,
    "D": 10,
}
symbol_value = {
    "A": 7,
    "B": 3,
    "C": 6,
    "D": 4,
}

def check_winnings(coloumns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloumn in coloumns:
            symbol_check = coloumn[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)

    return winnings, winning_line



def get_slot_mach_spin(rows,cols,symbol):
    all_symbols = []
    for symbol, symbol_counter in symbol.items():
        for _ in range(symbol_counter):
            all_symbols.append(symbol)

# define the coloumn list
    columns = []
    # generate the coloumn for everyone that we have
    for _ in range(cols):
        # then the rest of the code picks random values for each row
        coloumn = []
        current_symbols = all_symbols[:]
        # then loop through the numbers we need to generate which will be equal to the rows
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)

        columns.append(coloumn)
    
    return columns

def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i, coloumn in enumerate(coloumns):
            if i != len(coloumns) - 1:
                print(coloumn[row], end=" | ")
            else:
                print(coloumn[row], end="")

        print()


def deposit():
    while True:
        money = input("What would you like to deposit? $")
        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
                print("Amount has to be more than 0.")

        else:
            print("Please input a number.")

    return money

def get_number():
    while True:
        lines = input("Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please type in a valid number of lines")

        else:
            print("Please input a number.")
            
    return lines

def get_bets():
    while True:
        money = input("What would you like to Bet on each line? $")
        if money.isdigit():
            money = int(money)
            if MIN_BET <= money <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

        else:
            print("Please input a number.")

    return money

def spins(balance_account):
    lines = get_number()
    while True:
        bet = get_bets()
        total_bet = bet * lines

        if total_bet > balance_account:
          print(f"You do not have enough to bet that amount of money, your current balance is: ${balance_account} ")  
          
        else:
            break


    print(f"You are betting ${bet} on {lines} lines. You're total bet is equal to: ${total_bet}")

    slots = get_slot_mach_spin(ROWS, COLS, symbol_counter)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You have won ${winnings}.")
    print(f" You won on", * winning_line)
    return winnings - total_bet

def main():
    balance_account = deposit()
    while True:
        print(f"Your current balance is ${balance_account}")
        answer = input("Press enter to spin again (Enter Q to quit)")
        if answer == "q":
            break
        balance_account += spins(balance_account)

    print(f"You have made ${balance_account}")
    

main()