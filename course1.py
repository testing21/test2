#   Lets get started in Python by working with numbers
#   This Python code is written by Sasan Najar.

print (3+2)
print (3**2)
print (3%2)
print (15/4)

print ((23+32+64)/3)
print (float(16/7))

manila_pop = 1780148
manila_area = 16.56
manila_pop_density = manila_pop/manila_area


print (manila_pop)

print (manila_pop_density)

manila_pop += 1675

print (manila_pop)

manila_pop += 2000

print (manila_pop)


full_name = "charlotte hippopotamus turner"

print (full_name.upper())


def cylinder_vol(height, radius):
	pi = 3.14159
	return height * pi * radius ** 2


print (cylinder_vol(10, 3))


def printgreeting():
	print('hello world')


printgreeting()


return_value = print("I wish to register a comlaint.")
print("Finished calling function")
print(return_value)


def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))


print_testcase(10, 30000)


def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


print (readable_timedelta(365))


def which_prize(points):

    if points <= 50:
        prize_name = "wooden rabbit"
    elif points <= 150:
        prize_name = "no prize"
    elif points <= 180:
        prize_name = "wafer-thin mint"
    elif points <= 200:
        prize_name = "penguin"
    else:
        print("chk later")

    return ("COngratulations! you have won a {}!".format(prize_name))



print (which_prize(20))


altitude = 1000
speed = 250
propulsion = "propeller"

def test(altitude, speed, propulsion):
    if (altitude < 1000) and (speed > 100):
        print (1)
        return True
    elif (propulsion == "jet" or propulsion == "turboprop") and (speed < 300) and (altitude > 20000):
        print (2)
        return True
    elif not (speed > 400) and (propulsion == "propeller"):
        print (3)
        return True
    elif (altitude > 500 and speed > 100) or not (propulsion == "propeller"):
        print (4)
        return True

print (test(1000, 250, "propeller"))


def punctuate(sentence, type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create.
                "exclamation", "question" and "aside" are known values.
    """
    if type == "exclamation":
        sentencePunct = sentence + "!"
    elif type == "question":
        sentencePunct = sentence + "?"
    elif type == "aside":
        sentencePunct = "(" + sentence + ".)"
    else:
        sentencePunct = sentence + "."
    return sentencePunct


print (punctuate ("why this happened", "question"))