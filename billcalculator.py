# take food total - user input

def calculatebill(foodtotal):
    # calculate tip percentage options - 15%, 20%, 25%
    # show user those options
    print(f"15% tip on {foodtotal} is $",round((foodtotal * 0.15), 2), sep='')
    print(f"20% tip on {foodtotal} is $",round((foodtotal * 0.20), 2), sep='')
    print(f"25% tip on {foodtotal} is $",round((foodtotal * 0.25), 2), sep='')
    # ask user for tip percentage
    tippercent = int(input("Please enter the percentage number you'd like to add as a tip:"))
    tip = foodtotal * (tippercent / 100)

    # calculate total with tip
    foodplustip = round((foodtotal + tip), 2)
    print(f"Your total including tip is: $", foodplustip, sep='')

    # calculate tax
    tax = (foodtotal * 0.0875) 
    # calculate total bill
    totalbill = foodtotal + tax + tip
    print("Your total including tax and tip is: $", round(totalbill, 2), sep='')

foodtotal = float(input("How much is your food bill? "))
calculatebill(foodtotal)