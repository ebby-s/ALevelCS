MyList = ["Start"]
Calories = []
for i in range (1,100):
    user = input("Waiting for next food...")
    if user == "end day":
        print(MyList,sep=",")
        sum = sum(Calories)
        print (sum)
    else:
        while True:
            New = input("Please add input:")
            Cal = input("Calorie count =")
            try:
                validcal = int(Cal)
                MyList.append(New)
                Calories.append(validcal)
                break
            except ValueError:
                print("enter integer please")


