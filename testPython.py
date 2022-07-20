type = "hours"
number = 1

conversion = [number, type]
t = conversion[0]
if conversion[1] == ("minutes"):
    print (t / 60, "hours")
elif conversion[1] == "hours":
    print (t * 60, "minutes")
else:
     print ("Please specify minutes or hours")

