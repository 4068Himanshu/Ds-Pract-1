# Python Program to find Factorial of a Number Using Recursive And Iterative Function.
def recur_factorial(n):

    if n == 1:

        return n

    else:

        return n*recur_factorial(n-1)



num=int(input("Enter the number: "))



print("factorial of ",num," (recursive): ",end="")

print(recur_factorial(num))



def iter_factorial(n):

    factorial=1

    if int(n) >= 1:

        for i in range (1,int(n)+1):

            factorial = factorial * i

        return factorial

  

num=int(input("Enter the number: "))



print("factorial of ",num," (iterative): ",end="")

print(iter_factorial(num))
