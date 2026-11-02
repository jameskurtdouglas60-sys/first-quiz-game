def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Please choose the correct answer:")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)






def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong Answer!")
        return 0


def display_score(correct_guesses, guesses):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("RESULTS")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("Answers: ",end='')
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ",end='')
    for i in guesses:
        print(i, end=" ")
    print()




def play_game():
    pass

questions = {
    "What is the capital of the Philippines?: ": "A",
    "How many days are there in a leap year?: ": "B",
    "Which planet is known as the Red Planet?: ": "B",
    "What is 12 × 5?: ": "C",
    "Which animal is known as the King of the Jungle?: ": "C",
    "What is the largest ocean in the world?: ": "D",
    "How many continents are there?: ": "C",
    "Which gas do plants absorb?: ": "B",
    "Who wrote Romeo and Juliet?: ": "A",
    "What is the smallest prime number?: ": "C",
}

options = [["A. Manila", "B. Cebu", "C. Davao", "D. Quezon City"],
          ["A. 364", "B. 365", "C. 366", "D. 367"],
          ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
          ["A. 50", "B. 55", "C. 60", "D. 65"],
          ["A. Tiger", "B. Elephant", "C. Lion", "D. Leopard"],
          ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
          ["A. 5", "B. 6", "C. 7", "D. 8"],
          ["A. Oxygen", "B. Carbon dioxide" ",C. Nitrogen", "D. Hydrogen"],
          ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. J.K. Rowling"],
          ["A. 0", "B. 1", "C. 2", "D. 3"]]

new_game()