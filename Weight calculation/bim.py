from math import *
length  = float(input("Please enter the length in metres : "))
weight  = int(input("Please enter weight in kg : "))



result = weight / (length * length)

if result < 16:
    print("Severe weight loss")
elif result > 16 and result < 18:
    print("Weight loss")
elif result > 18 and result < 25:
    print("Healthy weight")
elif result > 25 and result < 30:
    print("Increase in weight")
else:
    print("Excessive obesity")