print("")
total = float(input("What's your starting amount of money?: "))
daily = float(input("How much will you be adding daily?: $"))
interest = float(input("What's the daily interest you're expecting (in %): "))
days = int(input("How many days do you want to look at?: "))
print("")

for i in range(days):

    start = total + daily
    interestprint = start * interest
    total = start + interestprint

    print("Day {}: ${:,}".format(i+1, round(total,2)    ) )
