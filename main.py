# brocode interest Calc
# youtube: https://youtu.be/4wGuB3oAKc4?si=lxTLGReij-3bE9D7&t=1083


# assigning 3 vars for user to fill in
principle = 0
rate = 0
time = 0

while principle <= 0:
    # using float because of the decimals
    principle = float(input("Enter Principle amount: "))
    # this will inform user principle cant be less or equal to 0
    if principle <= 0:
        print("principle cant be less or equal to 0")

while rate <= 0:
    # using float because of the decimals
    rate = float(input("Enter interest rate: "))
    # this will inform user principle cant be less or equal to 0
    if rate <= 0:
        print("Interest rate cant be less or equal to 0")

while time <= 0:
    # using whole numbers why we have a int
    time = int(input("Enter time in years: "))
    # this will inform user principle cant be less or equal to 0
    if time <= 0:
        print("Time cant be less or equal to 0")