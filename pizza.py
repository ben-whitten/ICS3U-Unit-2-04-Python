#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can find price of a pizza.


import constants


def main():

    # Input
    diameter = int(input("Enter the diameter of the pizza (inch):"))

    # Process
    subtotal = constants.LABOR + constants.RENT + \
        (diameter*constants.COST_PER_INCH)
    total = subtotal * constants.HST

    # Output
    print("If your pizza's diameter is {0} inch,\
 the cost will be ${1:,.2f}" .format(diameter, total))


if __name__ == "__main__":
    main()
