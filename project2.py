import random

"""
python has built-in library, offical document link @ https://docs.python.org/3/library/index.html
here is a simple example to demo how to use module 'random'.
"""
def guess_number(start, end):
    """
    let user to guess a integer number belonging to the range [start, end].
    """
    # generate one secret number first, and then let users try to guess it.
    secret_number = random.randint(start, end)
    user_input_number = -1
    
    print(f"lets guess the number between {start} and {end} !")

    # keep loop until user guess the corrected number successfully
    while user_input_number != secret_number:
        user_input_number = int(input("try your number > "))

        if user_input_number < secret_number:
            print("too small, try big number !")
        elif user_input_number > secret_number:
            print("too big, try small number !")

    print(f"congras ! you guess the correct number {secret_number} successfully !")

# now, it is time to play !
guess_number(0, 100)


# TBD, change the above code to score for each round.
#   if one can guess the number with attempts [1, 5] which means <= 5  attempts, score 'A',
#   if one can guess the number with attempts [6, 10], score 'B'.
#   if one can guess the number with attempts [11, 15], score 'C'.
#   if one can guess the number with attempts [16, 20], score 'D'.
#   if one can guess the number with attempts [21, 30], score 'E'.
#   if one fails to guess the number within 30 attempts, score 'F' and quit.
