#--------------------------------------------------------------------------------------------------------------#
# If Statement
# Operands:
# - !=	not equal
# - ==	equals
# - >	greater than
# - <	smaller than
#--------------------------------------------------------------------------------------------------------------#
blah = 99
meh = 69

if blah > meh:
	print("blah is greater than meh")
elif blah < meh:
	print("blah is less than meh")
elif blah != meh:
	print("blah doesn't equal meh")
else:
	print("blah equals meh")
#--------------------------------------------------------------------------------------------------------------#
# above will never match on second elif since the logic will stop after the first match.
# Nested if statements is one way to solve this.
#--------------------------------------------------------------------------------------------------------------#

if blah > meh:
	print("blah is greater than meh")
	if blah != meh:
		print("blah doesn't equal meh")
	else:
		print("blah equals meh")
else:
	print("blah is less than meh")
