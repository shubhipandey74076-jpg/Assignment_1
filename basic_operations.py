# function to add two numbers
# def add(a, b):
#     return a + b   # returns sum of a and b

# take input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# call function and print result
# print("Sum =", add(num1, num2))



# function to subtract two numbers
# def subtract(a, b):
#return a - b   # returns difference

# take input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

#  call function and print result
#  print("Difference =", subtract(num1, num2))





# # function to multiply two numbers
# def multiply(a, b):
#     return a * b   # returns product

# # take input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # call function and print result
# print("Multiplication =", multiply(num1, num2))





# # function to divide two numbers
# def divide(a, b):
#     # check if denominator is zero
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b   # returns division result

# # take input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # call function and print result
# print("Division =", divide(num1, num2))






# # create dictionary
# student = {
#     "name": "Rahul",
#     "age": 18,
#     "course": "BCA"
# }

# # print dictionary
# print("Student Details:", student)

# # access value
# print("Name:", student["name"])






# student = {}

# # add data
# n = int(input("How many students: "))

# for i in range(n):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     student[name] = age   # store in dictionary (details)

# # print dictionary
# print("\nStudent Dictionary:", student)

# #search according to your need 
# search = input("Enter name to search: ")

# if search in student:
#     print("Age =", student[search])
# else:
#     print("Student not found")






# # create empty list first
# temp = []

# n = int(input("Enter number of elements: "))

# for i in range(n):
#     num = int(input("Enter number: "))
#     temp.append(num)

# # convert list to tuple
# numbers = tuple(temp)

# print("Tuple:", numbers)

# # operations
# print("Maximum:", max(numbers))
# print("Minimum:", min(numbers))
# print("Sum:", sum(numbers))







# stack = []

# while True:
#     print("\n--- STACK MENU ---")
#     print("1. Push")
#     print("2. Pop")
#     print("3. Peek")
#     print("4. Display")
#     print("5. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         item = int(input("Enter element: "))
#         stack.append(item)
#         print("Pushed:", item)

#     elif choice == 2:
#         if len(stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Popped:", stack.pop())

#     elif choice == 3:
#         if len(stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Top element:", stack[-1])

#     elif choice == 4:
#         print("Stack:", stack)

#     elif choice == 5:
#         print("Program Ended")
#         break

#     else:
#         print("Invalid choice")





queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        queue.append(item)
        print("Enqueued:", item)

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Dequeued:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", queue[0])

    elif choice == 4:
        print("Queue:", queue)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice")