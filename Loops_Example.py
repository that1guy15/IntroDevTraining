#--------------------------------------------------------------------------------------------------------------#
# Loops
#--------------------------------------------------------------------------------------------------------------#
# For Loop
stuffs = [ "Darth", "Luke", "Yoda", "Chewbacca", "Han" ]

for stuff in stuffs:
	print(stuff)
	
# While Loop
x = 0
y = 10

while x < y:
	print(str(x) + "/" + str(y))
	x += 1
	
print("We Made It!")
#--------------------------------------------------------------------------------------------------------------#
# Dicts get interesting
#--------------------------------------------------------------------------------------------------------------#

stuffs = {
	"Darth": "bad",
	"Luke": "good",
	"Yoda": "good",
	"Chewbacca": "good"}

for k in stuffs:
    print(k)

# items() denotes to iterate through the dict for key and values instead of just keys
for k, v in stuffs.items():
	print("{} is a {} guy".format(k, v))

