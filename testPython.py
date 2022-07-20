#Task 1: Write a program that converts from hours to minutes or minutes to hours depending on the user's choice.
type = "minutes"
number = 120

conversion = [number, type]
time = conversion[0]
if conversion[1] == ("minutes"):
    print (time / 60, "hours")
elif conversion[1] == "hours":
    print (time * 60, "minutes")
else:
     print ("Please specify minutes or hours")

