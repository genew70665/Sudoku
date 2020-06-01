import numpy as np

# Read in the Sudoku puzzle

i = 0
sudoku_bd = np.empty(shape=(9,9),dtype=str)
print(sudoku_bd)
print('')
print(' ')
i=0
j=0
for j in range(0,9):
    for i in range(0,9):
        print("Enter your number:")
        x=input()
        sudoku_bd[j,i]=x
        i=i+1
    print(sudoku_bd)
    print(" ")
    j=j+1
    print(" ")
print(sudoku_bd)
print("Are your entries correct")
answer=input()
print (answer)

while (answer=='n'):
    print ('Go back and re-enter the data')
    print('Enter the row number that you want to change.')
    rownumber=input()
    i=rownumber
    for i in range(0,9):
        print("Enter your number:")
        x=input()
        sudoku_bd[j,i]=x
        i=i+1
    print(sudoku_bd)

# more code here

print(sudoku_bd)
print(" ")

print('Ready to solve Sudoku puzzle.')



