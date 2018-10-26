# --------------------------------------------------------------------------------------------------------------#
# Loops
# --------------------------------------------------------------------------------------------------------------#
# For Loop
stuffs = ["Darth", "Luke", "Yoda", "Chewbacca", "Han"]
for stuff in stuffs:
    print(stuff)

# While Loop
x = 0
y = 10
while x < y:
    print(str(x) + "/" + str(y))
    x += 1

print("We Made It!")
# Nested Loop (Using the 2 above)
x = 0
y = 10
stuffs = ["Darth", "Luke", "Yoda", "Chewbacca", "Han"]
while x < y:
    for stuff in stuffs:
        print(stuff + str(x))

    x += 1
# --------------------------------------------------------------------------------------------------------------#