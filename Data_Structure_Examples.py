#--------------------------------------------------------------------------------------------------------------#
# List:
# Lists is a sequence and a basic data structure
# A list may contain strings (text) and numbers
# A list is similar to an array in other programming languages, but has additional functionality
#--------------------------------------------------------------------------------------------------------------#
# List Example
autobot_list = [ "Optimus", "Bumblebee", "Ironhide", "Bluestreak" ]

## Print Full or just Elements of a List
print(autobot_list)
print(autobot_list[1])

## Add Element to List
autobot_list.append("Hound")
print(autobot_list)

## Remove Element from List
autobot_list.remove("Bumblebee")
print(autobot_list)

## Sort List
print(autobot_list)
autobot_list.sort()
print(autobot_list)
autobot_list.reverse()
print(autobot_list)
#--------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------#
# Tuple:
# The tuple data structure is used to store a group of data
# The elements in this group are separated by a comma
# Once created, the values of a tuple cannot change (immutable)
#--------------------------------------------------------------------------------------------------------------#
# Create Empty Tuple
decepticons_tuple = ()

# Fill the Tuple with one Element (Have to have a "," at the end)
decepticons_tuple = ("Megatron",)
print(decepticons_tuple[0])

# Append to the Tuple
decepticons_tuple = decepticons_tuple + ("Soundwave", "Starscream")
or
decepticons_tuple += ("Soundwave", "Starscream")

print(decepticons_tuple[0])
print(decepticons_tuple[1])
print(decepticons_tuple[2])

# Assign Mutiple Variables at once using a Tuple
decepticon_1,decepticon_2,decepticon_3 = ("Megatron","Soundwave", "Starscream")
print(decepticon2)
#--------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------#
# Dictionary:
# A dictionary can be thought of as an unordered set of key: value pairs
#--------------------------------------------------------------------------------------------------------------#
# Create an Empty Dictionary
care_bears_dict = {}

# Populate Dictionary
care_bears_dict["Grumpy Bear"] = "Grumps"
care_bears_dict["Cheer Bear"] = "Cheers"
care_bears_dict["Share Bear"] = "Shares"

# Print Dictionary Elements
print(care_bears_dict["Grumpy Bear"])
print(care_bears_dict["Cheer Bear"])
print(care_bears_dict["Share Bear"])
#--------------------------------------------------------------------------------------------------------------#