class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("")
monthly = float(input("How much will you be adding monthly?: $"))
interest = float(input("What's the monthly interest you're expecting (in %): "))
years = int(input("How many years do you want to look at?: "))
print("")

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in range((years * 12) - 12):
    months.append(months[i])

yearnum = []

for i in range(years):
    for b in range(12):
        yearnum.append(i + 1)


# start
# interestprint
# total


total = 0

print("Year  \tMonth   \tInitial \tInterest \tTotal")
print("-------------------------------------------------------------------")

for i in range(years * 12):
    start = total + monthly
    interestprint = start * interest
    total = start + interestprint


    print("{}   \t{}      \t${:,}   \t${:,}    \t${:,}".format(yearnum[i], months[i], round(start,2), round(interestprint,2), round(total,2)    ))

print(bcolors.BOLD + "\nTotal after {} year(s): ${:,}\n".format(years, round(total,2)) + bcolors.ENDC)
