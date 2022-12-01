# Assignment Day 3 - 1

""" You are a pilot, cruising at an altitude of 33000 ft,
you want to land your plane, to land your plane, you need
to be under 5000ft take input from the pilot, what
is your current altitude, and suggest
the pilot to go around if the altitude is more than 10K feet,
if its more than 5K suggest the pilot to land the plane
by bringing it to 1000ft """

#LETS DO IT

alt = int(input("Enter your current Attitude in feet "))
if alt >= 10000:
    print("Go around and decrease your altitude ")
elif alt >= 5000 and alt < 10000:
    print("Land the plane by bringing it to 1000 feet ")
elif alt >= 0 and alt < 5000:
    print("Make your altitude little near to 1000 feet for smooth landing ")
else :
    print("Invalid input")
	
print("ENJOY YOUR SAFE JOURNEY")



