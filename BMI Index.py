# BMI index calculator

w = float(input("Enter your weight in KG: "))
h = float(input("Enter your height in METER: "))

BMI = float(w/(h**2))

if(BMI < 18.5):
    print("You are under-weight :-",BMI)
elif(BMI >= 18.5 and BMI <= 24.9):
    print("You are fit :-",BMI)
elif(BMI >= 25 and BMI <= 29.9):
    print("You are over- weight :-",BMI)
elif(BMI >= 30):
    print("You are a obese :-",BMI)

