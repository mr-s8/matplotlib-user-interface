import matplotlib.pyplot as plt

xValues = []
yValues = []


def is_number(s):  # defining a function that checks wether s is a number (float or integer) or not
    try:
        a = float(s)
    except:
        return False
    if type(a) == float:
        return True


counter = 1
print("Put in d for an x value when you are done")
while True:
    while True:
        x = input("x value " + str(counter) + ": ")  # ask for x value
        if is_number(x) == False and x != "d":  # checks if input is not a number and not d
            print("Only int or float pls")  # if so tell user to try again
        else:  # if x is a number or d break
            break
    if x == "d":  # if x is d getting values is done
        break
    else:  # if its an number append x to the list
        xValues.append(x)

    while True:
        y = input("y value " + str(counter) + ": ")  # ask for y value
        if is_number(y) == False:  # if input is not a number try again (we dont ask if its d this time, because if we were able to stop after typing in a value for x, the list for the x values would be longer than the list for the y values)
            print("Only int or float pls")  # tell user to try again
        else:
            yValues.append(y)  # append y to list if input is a number
            break  # break to go to inputting x value again
    counter += 1

print(xValues)
print(yValues)


xLabel = input("Put in the label for your x-values: ")  # getting label names
yLabel = input("Put in the label for your y-values: ")

f = open("Coordinates.txt", "a")  # opening or creating file to store the data

f.write("\n(" + xLabel + " / " + yLabel + ")\n")

counter2 = 0
for x in xValues:
    f.write("(" + x + " / " + yValues[counter2] + ")\n")
    counter += 1
f.close()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.Axes.set_xticks(xValues)
plt.plot(xValues, yValues, marker=".", markersize=8)
plt.show()

# things to add:
# check if given input is an integer or a float otherwise repeat input and also check for d after wrong input -done
# specify plot ticks mby to get curves and stuff  ..important  -specify ticks w maxvalue and stuff
# add different chart types?
# markersize?
# eif heftige pyplot funtktionen geben
# different modes with function and values
