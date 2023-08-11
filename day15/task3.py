# write a program to prompt for a score between 0.0 and 1.0 if the score is between 0.0 and 1.0, print a grade using the following table.

#if the users enters a value out of range, print a suitable error message.



percentage = float(input("Enter your percentage"))
if percentage > 1.0 or percentage < 0.0:
    print("Invalid percentage")
elif percentage >= 0.9:
    print("A")
elif percentage >= 0.8:
    print("B")
elif percentage >= 0.7:
    print("C")
elif percentage >= 0.6:
    print("D")
else:
    print("F")
