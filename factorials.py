# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program uses a while loop


def main():
    # this function uses a while loop

    # this is to keep track of how many times you go through the loop
    int_integer = input("Enter an integer: ")
    loop_counter = 1
    factorial = 1

    # input
    try:
        int_integer = int(int_integer)

        # process & output
        while loop_counter <= int_integer:
            factorial = factorial * loop_counter
            loop_counter = loop_counter + 1
        print(
            "The factorial of " + str(int_integer) + " " + "is {0}.".format(factorial)
        )

    except ValueError:
        print("That is not a valid input.")


if __name__ == "__main__":
    main()
