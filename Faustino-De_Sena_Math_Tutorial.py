import math
import random


print("----- James M. De Sena -----")
print("----- Ron Dominic E. Faustino -----\n")
print("Mathematical Operation Tutorial\n")
print("Please Input Specific Operation: \n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division")

choice = int(input("Choice: "))  #User choice for Math Tutorial   
userScore = 0

if choice == 1:

    numProblems = int(input("\nHow many problems? ")) #number of loops for the question
    print("\n")
    for x in range (numProblems):  #loop for the problem
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        answer = int(input("what is the sum of {}.0 and {}.0: " .format(num1 ,num2)))
        answer = num1 + num2 
        if answer == answer:
            print("Correct Answer\n")
            userScore+=1
        else:
            print("Wrong Answer\n")
    print("Score: {}/{}" .format(userScore,numProblems)) #printing of user score
        
elif choice == 2:

    numProblems = int(input("\nHow many problems? "))
    print("\n")
    for x in range (numProblems):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        answer = int(input("what is the difference of {}.0 and {}.0: " .format(num1 ,num2)))
            
        if num1 < num2:
            answer = num2 - num1 
        else:
            answer = num1 - num2
        if answer == answer:
            print("Correct Answer\n")
            userScore+=1
    else:
        print("Wrong Answer\n")
    print("Score: {}/{}" .format(userScore,numProblems))
        
elif choice == 3:

    numProblems = int(input("\nHow many problems? "))
    print("\n")
    for x in range (numProblems):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        answer = int(input("what is the product of {}.0 and {}.0: " .format(num1 ,num2)))
            
        answer = num1 * num2 

        if answer == answer:
            print("Correct Answer\n")
            userScore+=1
        else:
            print("Wrong Answer\n")
    print("Score: {}/{}" .format(userScore,numProblems))
        
elif choice == 4:

    numProblems = int(input("\nHow many problems? "))
    print("\n")
    for x in range (numProblems):
        num1 = random.randint (0,9)
        num2 = random.randint (0,9)
        answer = float(input("what is the quotient of {}.0 and {}.0: " .format(num1 ,num2)))
            
    if num1 < num2:
        answer = num2 / num1 
    else:
        answer = num1 / num2
    if answer == answer:
        print("Correct Answer\n")
        userScore+=1
    else:
        print("Wrong Answer\n")
    print("Score: {}/{}" .format(userScore,numProblems))

else:
    print("\nWrong Input, Please Try Again")
        
