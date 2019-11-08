#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on November 2019
# This program uses nested loops
# To print out all possible RGB combinations


def main():
    # This function Calculates all RGB combinations
    red_counter = 0
    blue_counter = 0
    green_counter = 0

    # process and output
    for red_counter in range(0, 256):
        for blue_counter in range(0, 256):
            for green_counter in range(0, 256):
                print("RGB ({0}, {1}, {2})".format(red_counter, blue_counter,
                                                   green_counter))


if __name__ == "__main__":
    main()
