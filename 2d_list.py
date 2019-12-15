#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program finds the average of all elements in a 2d list


import random


def calculator(dimensional_list, rows, columns):
    # this finds the average of all elements in a 2d list

    total = 0
    for row_value in dimensional_list:
        for single_value in row_value:
            total += single_value
    total = total/(rows*columns)

    return total


def main():
    # this function places random integers into a 2D list
    dimensional_list = []

    # Input
    rows = (input("How many rows would you like: "))
    columns = (input("How many columns would you like: "))
    try:
        # Process
        rows = int(rows)
        columns = int(columns)
        for rows_loop in range(0, rows):
            temp_column = []
            for column_loop in range(0, columns):
                random_int = random.randint(1, 50)
                temp_column.append(random_int)

                # Output 1
                print("Random Number " + str(rows_loop + 1) + ", "
                      + str(column_loop + 1) + " is " + str(random_int))
            dimensional_list.append(temp_column)
            print("")

        # Output 2
        averaged = calculator(dimensional_list, rows, columns)
        print("The average of the random numbers is: {0} ".format(averaged))

    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
