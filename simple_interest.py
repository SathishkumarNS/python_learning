names = ["yuva","dheeran", "nilavan"]
principals = [10000, 10000, 10000]
rateOfInterests = [5,6,4]
numberOfYears = [5,5,5]

i = 0
while i <= len(names) - 1:
    principle = principals[i]
    name = names[i]
    interest = rateOfInterests[i]
    numberOfYear = numberOfYears[i]
    simpleInterest = (principle * interest * numberOfYear) / 100
    print(name, "'s interest is ", simpleInterest)
    i = i + 1
