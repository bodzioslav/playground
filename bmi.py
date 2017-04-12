#!/usr/bin/env python3

import argparse 
   
def bmi(weight, height):
    bmi = round(weight / pow(height, 2), 1)

    print("Your bmi is:", bmi)

    if bmi < 18.5:
        print("You're underweight")
    elif 18.5 < bmi < 24.9:
        print("You've got normal weight")
    elif 25.0 < bmi < 29.9:
        print("You're overweight")
    elif 30.0 < bmi:
        print("You're obese")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("weight", help="your weight in kilograms", type=float)
    parser.add_argument("height", help="your height in meters", type=float)
   
    args = parser.parse_args()
   
    bmi(args.weight, args.height)
