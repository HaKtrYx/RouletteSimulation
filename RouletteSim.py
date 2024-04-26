import random  # Import the random module to generate random numbers
import time  # Import the time module to add delays

# Define the initial balance and lists for different betting options
tries = int(input("Enter the number of simulations: "))
balance = 5000
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

red_count = 0
black_count = 0
green_count = 0

def place_bet():
    """
    Function to place random bets on different options.
    It updates the global variables for each bet amount.
    """
    global bet_red, bet_black, bet_even, bet_odd, bet_row1, bet_row2, bet_row3, bet_low, bet_mid, bet_high, bet_lower, bet_upper, bet, red_count, black_count, green_count
    bet_red = int(input("Amount on Red\t\t\t\t: "))
    bet_black = int(input("Amount on Black\t\t\t\t: "))
    bet_even = int(input("Amount on Even\t\t\t\t: "))
    bet_odd = int(input("Amount on Odd\t\t\t\t: "))
    bet_row1 = int(input("Amount on Row 1 (3,6,...)\t\t\t: "))
    bet_row2 = int(input("Amount on Row 2 (2,5,...)\t\t\t: "))
    bet_row3 = int(input("Amount on Row 3 (1,4,...)\t\t\t: "))
    bet_low = int(input("Amount on 1-12\t\t\t\t: "))
    bet_mid = int(input("Amount on 13-24\t\t\t\t: "))
    bet_high = int(input("Amount on 25-36\t\t\t\t: "))
    bet_lower = int(input("Amount on 1-18\t\t\t\t: "))
    bet_upper = int(input("Amount on 19-36\t\t\t\t: "))
    bet = bet_red + bet_black + bet_even + bet_odd + bet_row1 + bet_row2 + bet_row3 + bet_low + bet_mid + bet_high + bet_upper + bet_lower

def lucky_wheel():
    """
    Function to generate a random lucky number between 0 and 36.
    It prints the lucky number with a red color if it's a red number.
    """
    global lucky_number
    lucky_number = random.randint(0, 36)
    
def payout():
    """
    Function to calculate the payout based on the lucky number and the user's bets.
    It updates the global variables for the result and balance.
    """
    global result, balance, red_count, black_count, green_count
    result = 0
    
    if lucky_number != 0:
        if lucky_number in red:
            result += bet_red * 2
            red_count += 1
        else:
            result += bet_black * 2
            black_count += 1
        if lucky_number % 2 == 0:
            result += bet_even * 2
        else:
            result += bet_odd * 2
        if lucky_number < 18:
            result += bet_upper * 2
        else:
            result += bet_lower * 2
        if lucky_number % 3 == 0:
            result += bet_row1 * 3
        elif lucky_number % 3 == 2:
            result += bet_row2 * 3
        else:
            result += bet_row3 * 3
        if lucky_number >= 25:
            result += bet_high * 3
        elif lucky_number <= 12:
            result += bet_low * 3
        else:
            result += bet_mid * 3
    else:
        green_count += 1

def game():
    """
    Main function to run the game loop.
    It calls the other functions, updates the balance, and handles the game over condition.
    """
    global balance, bet, result
    
    balance = 5000
    
    for _ in range(100):
        lucky_wheel()
        if balance < bet:
            print("Your Balance is too small")
            break
        else:
            balance -= bet
            payout()
            balance += result
            
    print("Simulation complete. Final balance: {}\nRed: {} Black: {} Green: {}".format(balance, red_count, black_count, green_count))

average = 0

# Call the game function to start the game
place_bet()
for i in range(tries):
    red_count = 0
    black_count = 0
    green_count = 0
    game()
    average += balance

print("Simulation complete. Average final balance:", average / tries)
