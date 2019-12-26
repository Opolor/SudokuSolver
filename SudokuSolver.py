import logging
import time


"""
Global Variables
"""
logging.root.setLevel(logging.INFO)
sudoku = []



"""
Formats input
"""
def sudokuFormatter(filePath):
    logging.info("Beginning Formatting")
    file = open(filePath, "r")
    readfile = file.readlines()
    file.close
    
    #Creating the 2d array for the sudoku (formatting input)
    for x in range(len(readfile)):
        temp = list(readfile[x])
        try:
            temp.remove("\n")
        except Exception as identifier:
            logging.error(identifier)
        #string to int
        temp = list(map(int, temp))
        #adding temp into sudoku 2d array
        sudoku.insert(x, temp)


"""
Console Viewer
"""
def consoleViewer():
    for x in range(len(sudoku)):
        print(sudoku[x])



"""
Check if space is free
Returns False if a number already exists in given space
"""
def findNextSpace(col, row):
    for y in range((len(sudoku))):
        for x in range (len(sudoku)):
            if(sudoku[y][x] == 0):
                col = y
                row = x
                values = [y, x]
                return values
            if(y == 8 and x == 8 and sudoku[y][x] is not 0):
                values = [-1, -1]
                return values


"""
Check row  rule
Returns False if rule is broken
"""
def checkRow(num, row):
    check = True
    for x in range(len(sudoku)):
        if num == sudoku[row][x]:
            check = False
            break
        else:
            continue
    return check


"""
Check column rule
Returns False if rule is broken
"""
def checkCol(num, column):
    check = True
    for x in range(len(sudoku)):
        if num == sudoku[x][column]:
            check = False
            break
        else:
            continue
    return check


"""
Check check region (3x3) rule
Returns False if rule is broken
"""
def checkReg(num, indexcol, indexrow):

    #check
    check = True

    #array that will have 3x3 numbers and check
    arr = []

    #first 3 cols
    if(indexcol <= 2):

        if(indexrow <= 2):
            logging.info("checking region 0-2 cols, 0-2 rows")
            for y in range(3):
                for x in range(3):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

        if(indexrow >= 3 and indexrow < 6):
            logging.info("checking region 0-2 cols, 3-5 rows")
            for y in range(3, 6):
                for x in range(3):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

        else:
            logging.info("checking region 0-2 cols, 6-8 rows")
            for y in range(6, 9):
                for x in range(3):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

    #middle 3 cols
    if(indexcol >= 3 and indexcol < 6):

        if(indexrow <= 2):
            logging.info("checking region 3-5 cols, 0-2 rows")
            for y in range(3):
                for x in range(3, 6):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

        if(indexrow >= 3 and indexrow < 6):
            logging.info("checking region 3-5 cols, 3-5 rows")
            for y in range(3, 6):
                for x in range(3, 6):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

        else:
            logging.info("checking region 3-5 cols, 6-8 rows")
            for y in range(6, 9):
                for x in range(3, 6):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

    #last 3 cols
    else:
        if(indexrow <= 2):
            logging.info("checking region 6-8 cols, 0-2 rows")
            for y in range(3):
                for x in range(6, 9):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

        if(indexrow >= 3 and indexrow < 6):
            logging.info("checking region 6-8 cols, 3-5 rows")
            for y in range(3, 6):
                for x in range(6, 9):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check

        else:
            logging.info("checking region 6-8 cols, 6-8 rows")
            for y in range(6, 9):
                for x in range(6, 9):
                    arr.append(sudoku[y][x])
            for w in range(len(arr)):
                if(num == arr[w]):
                    check = False
                    break
                else:
                    continue
            return check
    #return
    return check  

"""
Solver
"""
def Sudokusolver():
    Gcol = 0
    Grow = 0
    global sudoku

    #Finds next possible position
    #If there are no more empty values returns -1 and sudoku is finished 
    values = findNextSpace(Gcol, Grow)
    if(values[0] == -1):
        return True
    else:
        Gcol = values[1]
        Grow = values[0]

    #Loops through 1 to 10 to see if numToAdd can be added 
    for numToAdd in range(1, 10):

        #Checks Rules
        if(checkCol(numToAdd, Gcol) and checkRow(numToAdd, Grow) and checkReg(numToAdd, Gcol, Grow)):
                    
            #Adds number
            sudoku[Grow][Gcol] = numToAdd
            logging.info("adding "+str(numToAdd)+" to sudoku["+str(Grow)+"]["+str(Gcol)+"]")


            #Recursion, next cell
            if(Sudokusolver()):
                return True

            #If not sets back cell
            sudoku[Grow][Gcol] = 0
                
    #Initiates Backtrack
    #If retuns false returns to call stack before and continues on line 276
    return False

"""
Main
"""
try:
    start_time = time.time()
    sudokuFormatter("./Sudoku.txt")
    if(Sudokusolver()):
        elapsed_time = time.time() - start_time
        logging.info("TIME ELAPSED: "+str(elapsed_time)+" seconds")
        consoleViewer()
        f = open("./SudokuSolution.txt", "w")
        for arr in sudoku:
            for num in arr:
                f.write(str(num))
                f.write(", ")
            f.write("\n")
        f.write("\n")
        f.write("Finished Sudoku in "+str(elapsed_time)+" seconds")
        f.close

    else:
        logging.warn("No Solution Found")
except Exception as identifier:
    logging.error(identifier)