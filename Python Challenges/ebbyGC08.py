def bmi(weight,height):
    bmi = weight/(height**2)
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= < bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "overweight"
    elif bmi >= 30:
        return "obese"
