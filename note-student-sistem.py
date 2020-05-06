n1 = float(input("Your note in Portuguese: "))
n2 = float(input("Your math note: "))
result = (n1 + n2) / 2
if result <= 5:
    print("Your final grade is {}\n You are F!".format (result))
elif 5 < result < 6.9:
    print("Your final grade is {}\n You are D+".format (result))
elif result >= 7:
    print("Your final grade is {}\n You are A+".format(result))
