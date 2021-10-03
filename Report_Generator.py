# Created by MAOGriffiths 03/10/2021
# https://github.com/griffmeg11/


import sys
filename = input("What do you want to name the file?: (Recommended DDMMYYYY - Team - Name)\n")
file = open("{}.txt".format(filename), "w")

#defining loop to write option chosen to file
def options():
    if option == "1":
        file.write("{} showed great skills with navigation, honing {} skills and making great improvements. ".format(name, gender))
        file.close()
    elif option == "2":
        file.write("{} proved that they were stronger than previously thought, pushing through the "
                   "expedition and walking longer distances than usual. ".format(name))
        file.close()
    elif option == "3":
        file.write("{} enjoyed camping in the evening, particularly cooking with the rest of {} team. ".format(name, gender))
        file.close()
    elif option == "4":
        file.write("{} enjoyed spending time with {} friends, solidifying existing relationships, and creating new "
                   "ones! {}'s communication skills improved and was a great asset to {} team. ".format(name, gender,  name,  gender))
        file.close()
    elif option == "5":
        file.write("{} pushed the team to always keep going, even when they encountered difficulties, showcasing "
                   "{} communication and empathy abilities. ".format(name, gender))
        file.close()
    elif option == "6":
        file.write("{} showed great determination and perseverance throughout, keeping {} head up when the going got "
                   "tough, this was contagious to the other team members. {}'s strength was inspiring ahd shouldn't "
                   "be overlooked. ".format(name, gender, name))
        file.close()
    elif option == "7":
        file.write("{} was a great team player, making sure that all {} friends were happy. {} supported the other "
                   "participants and kept everyone going throughout the walk! " .format(name, gender, name))
        file.close()
    elif option == "8":
        file.write("{} particularly enjoyed the independence that was given to {} throughout the expedition. {} "
                   "enjoyed spending time with friends and peers in a non-restricted environment and demonstrated "
                   "a mature and responsible attitude. ".format(name, gender, name))
        file.close()
    elif option =="9":
        file.write("{} mentioned being in the outdoors was exciting and enjoyed the exploration, "
                   "seeing new areas they wouldn't usually be able to see. ".format(name))
    else:
        file.close()
        print("choose a number from the choices above")
        sys.exit("The report has been recorded in {}.txt".format(filename))

# asking name of student and gender
name = input("Name of student?:\n")
gender = input("Gender?: f/m/t\n")
if gender == 'f':
    gender = "her"
elif gender == 'm':
    gender = "his"
elif gender == 't':
    gender = "their"
else:
    print("Please enter one of the above options (female,male,they/them")
    sys.exit("The report has been recorded in {}.txt".format(filename))

# asks first option then starts loop
option = input("Where did they do well? Pick from the options: (one at a time)\n"
      "1: Map and compass/Navigation\n"
      "2: Fitness\n"
      "3: Trangias/Campcraft\n"
      "4: Teamwork/Friendship\n"
      "5: Pusher?\n"
      "6: Strength/Perseverance/Determination\n"
      "7: Motivator\n"
      "8: Independence\n"
      "9: Exploration\n")

options()
cont = input("Did they do anything else well?: y/n ")


while cont == "y":
    file = open("{}.txt".format(filename), "a")
    print("\n1: Map and compass/Navigation\n"
      "2: Fitness\n"
      "3: Trangias/Campcraft\n"
      "4: Teamwork/Friendship\n"
      "5: Pusher?\n"
      "6: Strength/Perseverance/Determination\n"
      "7: Motivator\n"
      "8: Independence\n"
      "9: Exploration\n")
    option = input("What else did they do well?")
    options()
    cont = input("Did they do anything else well?: y/n ")
else:
    file = open("{}.txt".format(filename), "a")
    file.write("{} performed very well over the expedition, and shows good skills for the next award should they choose to continue with their award. Well done!".format(name))
    file.close()
    with open("{}.txt".format(filename), "r") as text_file:
        contents = text_file.read()
    print(contents)
    sys.exit("The report has been recorded in {}.txt".format(filename))
