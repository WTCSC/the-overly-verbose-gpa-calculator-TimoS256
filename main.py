gpas = []
totalGrades = []

def getgpa(list):
    out = 0
    count = 0
    for x in list:
        out = out+x
        count += 1
    return out/count

def getgrades():
    gpa = float()
    grades = []
    count = float(input("How many grades would you like to enter? (more than 5):"))
    print(count)
    while count > 0:
        grades.append(float(input("Enter a grade (0.0-4.0):")))
        count -= 1
    gpa = getgpa(grades)
    gpas.append(round(gpa,3))
    totalGrades.append(grades)


print("Hello and welcome to this normal gpa calculator! "
      "it will tell you your average grade among all of your classes, and definetely not waste your time!"
      "you must enter the grade of each class as a number between 0 and 4, grade weights will not be taken into account."
      "Your grade will then be calculated by taking the average of the list of grades. this means adding each value and dividing by the amount of values."
      "Go ahead and input them now, you must have at least 5 grades between 0 and 4, decimal points expected.")

sem = float(input("How many semesters would you like to enter? (at least 1):"))

while sem > 0:
    getgrades()
    sem -= 1

for x in range(0,len(gpas)):
    print(f'Your gpa for semester {x+1} is {gpas[x]}')

goalselect = input('Would you like to set a goal gpa? (y/n) \n >')
if goalselect == 'y':
    selection = int(input("Which semester would you like to set a goal gpa? "))
    goal = float(input("Enter a goal gpa: "))
    templist = [totalGrades[selection - 1]]
    index = 0
    found = False
    for x in range(0,len(templist)):
        templist = totalGrades[selection - 1]
        templist[index] = 4
        index += 1
        print(templist)
        print(getgpa(templist))
        if getgpa(templist) >= goal:
            print(f" -If you get your class #{index} grade up to a 4.0, You'll meet your goal!")
            print("Congradulations and good luck on getting that 4!")
            found = True
    if found == False:
        print("I couldn't find a way to meet your goal by improving only one grade, you might have to get multiple up.")

