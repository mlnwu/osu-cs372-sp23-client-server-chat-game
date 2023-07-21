# Art from: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

ascii_rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

ascii_paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

ascii_scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def get_ascii(choice):
    if choice == 'r':
        print(ascii_rock)
    elif choice == 'p':
        print(ascii_paper)
    else:
        print(ascii_scissors)


def win(word, input):
    if input.lower() == "r" and word.lower() == "p":
        return "You lose :("
    elif input.lower() == "r" and word.lower() == "s":
        return "You win :)"
    elif input.lower() == "p" and word.lower() == "s":
        return "You lose :("
    elif input.lower() == "p" and word.lower() == "r":
        return "You win :)"
    elif input.lower() == "s" and word.lower() == "r":
        return "You lose :("
    elif input.lower() == "s" and word.lower() == "p":
        return "You win :)"
    else:
        return "It's a draw!"
