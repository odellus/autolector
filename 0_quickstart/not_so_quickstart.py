print("Hello, World!")

print("Hello, Types!")
# Basic types.
booleans = True
strings = 'Hello, World!'
floats = 2.5
integers = 2

print("Hello, Lists!")
example_list = []

# This is how we can see what a list can do
print(dir(example_list))

# Let's add some things to our list!
print(help(example_list.append))
example_list.append(booleans)
example_list.append(strings)
example_list.append(floats)
example_list.append(integers)

print(example_list)

# We can also make a list like this:
another_list = [True, 'Hello, World!', 2.5, 2]
print(another_list)

# We remove an item from the list as so:
print(help(another_list.pop))
x = another_list.pop(0)
# And you can see the first, zero-indexed element been removed.
print(x)
print(another_list)

# We can access their elements in a list by their index like so.
print(example_list[:3])
print(example_list[2:])
print(example_list[1:3])
print(example_list[1:-1])

print("Hello, Dictionaries!")
example_dictionary = {}

# How we set values in a dictionary.
example_dictionary['firstname'] = 'Barney'
example_dictionary['lastname'] = 'Rubble'

# Another way of initializing dictionaries.
another_dictionary = {'firstname': 'Barney', 'lastname': 'Rubble'}

# How we index dictionaries (doesn't have to be an integer!):
# We call 'firstname' the key and another_dictionary['firstname'] stores the value.
print(another_dictionary['firstname'])

# Another thing that makes dictionaries cool:
intro_conditional = 'lastname' in another_dictionary
outro_contitional = 'outro' in another_dictionary
print(intro_conditional)
print(outro_contitional)

# in works for lists too.
list_conditional = 2.5 in example_list
print(list_conditional)

# There are also sets and tuples.
# You can think of tuples as an immutable list
# And sets are dictionaries with only keys.
# Sets are uper useful for removing duplicates.
# Tuples are everywhere. We'll get to that in a minute with functions.

print("Hello, Conditionals!")

# We've seen a bit with the in operator. Let's go a bit deeper.
conditional_1 = 1 == 2
conditional_2 = 1 == 1

print(conditional_1)
print(conditional_2)

if conditional_1:
    print("The first conditional is true")
else:
    print("The first conditional is false")


if conditional_2:
    print("The second conditional is true")
else:
    print("The second conditional is false")

conditional_3 = 1 != 2
conditional_4 = 1 != 1

if conditional_3:
    print("The third conditional is true")
else:
    print("The third conditional is false")

if conditional_4:
    print("The fourth conditional is true")
else:
    print("The fourth conditional is false")

conditional_5 = True and False
conditional_6 = True or False

if conditional_5:
    print("The fifth conditional is true")
else:
    print("The fifth conditional is false")

if conditional_6:
    print("The sixth conditional is true")
else:
    print("The sixth conditional is false")

print("Hello, Iterations!")

# We're going to go over for loops.
sample_list = ['a', 'b', 'c', 'd', 'e', 34.9]
for x in sample_list:
    print(x)
    y = 3 * x
    print(y)

print(help(range))
# List comprehension, because why not. You're new.
list_comprehension = [k for k in range(100)]
print(list_comprehension)

# conditional inside comprehension
evens = [k for k in range(100) if k % 2 == 0]



# SKIP THIS. TOO MUCH!
# It has to go in front of for statement if there's an else
evens_plus_holes = [k if k % 2 == 0 else None for k in range(100) ]
print(evens)
print(evens_plus_holes)
# Works for dictionaries too:
dict_comprehension = {f'key_{k}': k for k in range(100)}
# Yuck. I had to look this up. I didn't know. Do not be discouraged.
even_odd_labels = {k:'even' if k % 2 == 0 else 'odd' for k in range(100)}
confusing = {k if k % 2 == 0 else k * 10:'even' if k % 2 == 0 else 'odd_time_ten' for k in range(100)}

print(dict_comprehension)
# and that's how you iterate over a list. Lots to cover. Not enough time.

print("Hello, Functions!")

def hello_world():
    print("Hello, World!")
hello_world()

def split_up_hello_world():
    hello_msg = "Hello, World!"
    char_list = []
    for char in hello_msg:
        char_list.append(char)
    # List comprehension is more concise if less powerful.
    # char_list = [x for x in hello_msg]
    return char_list

character_list = split_up_hello_world()
print(character_list)

# Make it generic.
def generic_split(input_str):
    return [x for x in input_str]

string_input = "Give me a string to split."
split_string = generic_split(string_input)
print(split_string)

# Scope.
a = 14
def multiply_a():
    # DON'T EVER DO THIS IF YOU CAN AT ALL HELP IT.
    global a
    a = a * 2

print(a)
multiply_a()
print(a)

# DO THIS
def double(x):
    return 2 * x
x = 10
y = double(x)
print(x, y)

# Classes! Bleh!
print("Hello, Classes!")

# Object oriented programming is bad news. State makes debugging hard.
# Functional programming is better. Give me idempotency please. 7 days a week.

# Anyway, here's a rough outline of classes.

class HelloObjects:
    def __init__(self, n_objs):
        self.n_objs = n_objs
        print(f"loaded with {self.n_objs} objects")
    def triple_objects(self):
        print(f"Tripling {self.n_objs} to {self.n_objs * 3}")
        self.n_objs *= 3
        return self.n_objs


# Instantiate the class.
hello_objects = HelloObjects(4)

n_objs = hello_objects.triple_objects()
print(n_objs)
print(hello_objects.n_objs)


class OhMyGodItsSoAnnoying(HelloObjects):
    def __init__(self, n_objs):
        super(OhMyGodItsSoAnnoying, self).__init__(n_objs)
    def quadruple_objects(self):
        self.n_objs *= 4
        return self.n_objs

smdh = OhMyGodItsSoAnnoying(13)
dir(smdh)
sigh = smdh.quadruple_objects()
print(sigh)
print(smdh.n_objs)
# And that's classes. Don't use them unless you have to.
# Only covered them because we have to use them.
