#!/usr/bin/env python3
# Created by: Gustav I
# Created on: March 31, 2025
# This program determines if user input is a leap year.


def main():
    # Gets year input
    try:
        user_year = int(input("Enter a year: "))
    #Nested if statement seeing if year is divisible by 4, 100, 400.
        if user_year % 4 == 0:
            if user_year % 100 == 0:
                if user_year % 400 == 0:
                    print(f"{user_year} is a leap year.")
                else:
                    print(f"{user_year} is not a leap year.")
            else:
                print(f"{user_year} is a leap year.")
        else:
            print(f"{user_year} is not a leap year.")
    #Try catch making sure program doesn't crash
    except ValueError:
        print("Invalid input. Please enter a valid year.")

    #Calling the function
if __name__ == "__main__":
    main()
