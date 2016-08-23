# \ escape sequence is to escape a single-quote or douuble-quote
# I am 6'2\" tall." # escape double-quote inside string
# The second way is by using tripe-quotes, which is just""" and works like a string,
# but you also can put as many lines of text as you want until you type """
# again. We'll also play with these

tabby_cat = "\tI'm tabbled in." # \t means horizontale Tab (TAB)
persian_cat = "I'm split\non a line." # \n means ASCII linefeed (LF)
backslash_cat = "I'm \\ a \\ cat." # \\ means \
# \N{name} means character named name in the Unicode database
# \r means carriage return

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|","*","&"]:
		print "%s\r" % i,