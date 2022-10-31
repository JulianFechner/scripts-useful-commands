#!/usr/bin/env python3
# Copyright (c) 2022 Julian Fechner

import sys

print("This program counts something and deducts a given percentage.")
print("In this version it counts the worked overtime and deducts the already paid overtime.")

def main():
    # The while-Loop is used to let a user start again, should he want to change an entered value.
    while True:
        print("Enter normal work hours.")
        nor_week = input("Normal week: ")

        print("Enter percentage to deduct.")
        per = input("Percentage: ")

        deductedhours = float(nor_week)/float(per)
        limit = float(nor_week) + float(deductedhours)

        print("Enter hours for the weeks of the month.")
        week1 = input("Week 1: ")
        week2 = input("Week 2: ")
        week3 = input("Week 3: ")
        week4 = input("Week 4: ")

        print("Normal week: " + nor_week)
        print("Percentage: " + per)
        print("Hours that will be deducted: " + str(deductedhours) + ".")
        print("Hours to this limit will not be counted as overwork: " + str(limit) + ".")
        print("Week 1: " + week1)
        print("Week 2: " + week2)
        print("Week 3: " + week3)
        print("Week 4: " + week4)

        overall = float(week1) + float(week2) + float(week3) + float(week4)
	# Gives out the entered values.
        print("Overall: " + str(overall) + ".")

	# Let's a user check for mistakes.
        print("Are the entered values correct?")
        answer = str(input("y/n: "))

        if answer == "y":
            print("Continuing...")
        elif answer == "n":
            continue   
        else:
            print("Goodbye!")
            break

        # Let's the user check for mistakes.
        print("Would you like to add more weeks?")
        answer2 = str(input("y/n: "))
        moreweeks = input("more weeks: ")

        # Should the user want to enter more values for more weeks, he can do so.
        for overtime in str(moreweeks):
            if float(moreweeks) >= float(limit):
                ot_moreweeks = float(moreweeks) - float(deductedhours)
                print(ot_moreweeks)
            elif float(moreweeks) <= float(limit):
                print("Not enough hours!")
            else:
                break

        for overtime in str(week1):
            # If the given number is greater than the given limit, the given percentage is deducted.
            if float(week1) >= float(limit):
                ot_week1 = float(week1) - float(nor_week)
                print(ot_week1)
                break
            # If the given number is lesser than the given limit, initial value is given.
            elif float(week1) <= float(limit):
                print(week1)
                print("Not enough hours!")
            else:
                break

        for overtime in str(week2):
            if float(week2) >= float(limit):
                ot_week2 = float(week2) - float(deductedhours)
                print(ot_week2)
                break
            elif float(week2) <= float(limit):
                print(week2)
                print("Not enough hours!")
            else:
                break

        for overtime in str(week3):
            if float(week3) >= float(limit):
                ot_week3 = float(week3) - float(deductedhours)
                print(ot_week3)
                break
            elif float(week3) <= float(limit):
                print(week3)
                print("Not enough hours!")
            else:
                break

        for overtime in str(week4):
            if float(week4) >= float(limit):
                ot_week4 = float(week4) - float(deductedhours)
                print(ot_week4)
                break
            elif float(week4) <= float(limit):
                print(week4)
                print("Not enough hours!")
            else:
                break

        sys.exit()
        
if __name__ == '__main__':
	main()
