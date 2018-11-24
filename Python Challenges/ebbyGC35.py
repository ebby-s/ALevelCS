import os

question1 = input("Player 1 enter a question: ")
ans1 = input("Player 1 enter the answer: ")
os.system('cls')

question2 = input("Player 2 enter a question: ")
ans2 = input("Player 2 enter the answer: ")
os.system('cls')

player2_ans = input("Player 2 answer this: {0} ".format(question1))
print("correct answer: ",ans1,"\n","your answer: ",player2_ans)

player1_ans = input("Player 1 answer this: {0} ".format(question2))
print("correct answer: ",ans2,"\n","your answer: ",player1_ans)
