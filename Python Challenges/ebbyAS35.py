import random

choices = ["It is certain","Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]

while True:
    input("What is your question? ")
    print(random.choice(choices))
