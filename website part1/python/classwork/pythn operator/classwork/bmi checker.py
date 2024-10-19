weight =float(input("enter the weight in kgs"))
height =float(input("enter the height in m"))

bmi=weight/(height * height)

if bmi <18.5:
    print(bmi,"it is underweight")
elif bmi <25:
    print(bmi,"it is healthy")
elif bmi <30:
    print(bmi,"it is overweight")
else:
    print(bmi,"it is obese")