my_name = 'Biyu Hua'
my_age = 30 # not a lie
my_height = 160 # cm
my_weight = 45 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "She's %d cm tall." % my_height
print "She's %d kg heavy." % my_weight
print "Actually that's too light."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
# right value replace the left one
# %s: string
# %d: decomle