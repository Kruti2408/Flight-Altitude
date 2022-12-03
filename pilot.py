# You are a pilot, cruising at an altitude of 33000 ft,
# you want to land your plane, you need
# to be under 5000ft take input from the pilot, what
# is your current altitude, and suggest
# the pilot to go around if the altitude is more than 10K feet,
# if its more than 5K suggest the pilot to land the plane
# by bringing it to 1000ft

while True:
    altitude = int(input("Please enter the altitude : "))

    if altitude >= 10000 :
        print("The altitude is greater than 10k feet ... Turn around the plane!")
    else :
        print("The altitude is less than 5k feet ... Now you can land the plane safely!")
        
