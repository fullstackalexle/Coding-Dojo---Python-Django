print("Hello World!")

x = "Hello Python"
print(x)
y = 42
print(y)

string = "World"

# 1. TASK: print "Hello World"
print( f"Hello {string}" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "Hello", name )	# with a comma
print( "Hello" + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello", name )	# with a comma
# print( "Hello" + name )	# with a +	-- this one should give us an error!
print( "Hello" + str(name) )
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

txt = "hello, and welcome to my world!"

x = txt.istitle()

print(x)
