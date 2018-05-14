import random


class GAME:
    def __init__(self):
        print("Let's play flashgame!")
        self.flashcard = []
        self.correctA = 0

    def inputQandA(self):
        while True:
            question = str(input("Your question: "))
            answer = str(input("Your answer: "))
            self.flashcard.append([question, answer, -1])
            if input("Continue? Yes, enter 1. No, enter 0. ") == "1":
                continue
            else:
                break

    def test(self):
        answerN = 0
        while True:
            q_a_number = random.randint(0, len(self.flashcard)-1)
            if self.flashcard[q_a_number][2] == -1:
                enterA = str(input("What is the correct answer for {}? ".format(self.flashcard[q_a_number][0])))
                if enterA == self.flashcard[q_a_number][1]:
                    self.flashcard[q_a_number][2] = 1
                    self.correctA += 1
                    answerN += 1
                else:
                    self.flashcard[q_a_number][2] = 0
                    answerN += 1
            if answerN == len(self.flashcard):
                break

    def printResult(self, verbose=False):
        if verbose:
            for i in range(len(self.flashcard)):
                if self.flashcard[i][2] == 1:
                    print("Question ({}): Correct".format(self.flashcard[i][0]))
                elif self.flashcard[i][2] == 0:
                    print("Question ({}): Incorrect".format(self.flashcard[i][0]))
        print("Total number of the correct answers: {} out of {}".format(self.correctA, len(self.flashcard)))


J = GAME()
J.inputQandA()
J.test()
J.printResult()
J.printResult(verbose=True)
