for i in range(5):
    num = float(input("Please enter any number:  "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
print("Done checking numbers")