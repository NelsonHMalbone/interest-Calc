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

total = principle * pow((1 + rate / 100), time)

# take the principle * 1 then add the rate and divide by 100 and creates a deciminal
# using the pow() function
# will rise to the power of time

print(f'Balance after {time} year/s: ${total:.2f}')
