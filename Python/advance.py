# num = int(input("Enter Your Number: ")); # Exception Handling

# try:
#     print(10 / num);

# except ZeroDivisionError:
#     print("Zero Division Error!");

# print("Congratulations Your Division Is Successfully Run");

# num = input("Enter Your Number: ");

# try:
#     num = int(num);
#     print(10 / num);

# except Exception as error:
#     print(f"Sorry There Is An Error as {error}");

# else:
#     print("Good There Is No Exception");

# print("Congratulations Your Division Is Successfully Run");

# num = input("Enter Your Number: ");

# try:
#     num = int(num);
#     print(10 / num);

# except Exception as error:
#     pass;

# else:
#     print("Good There Is No Exception");

# print("Congratulations Your Division Is Successfully Run");

# num = input("Enter Your Number: ");

# try:
#     num = int(num);
#     print(10 / num);

# except Exception as error:
#     print(f"Sorry There Is An Error as {error}");

# else:
#     print("Good There Is No Exception");

# finally:
#     print("I Will Run No Matter What");

# print("Congratulations Your Division Is Successfully Run");

# age = int(input("Enter Your Number: "));

# try:

#     if age < 18:
#         raise ValueError("Sorry Your Not Eligible"); # Raise Throw Exception Error

#     else:
#         print("Welcome To The Club");

# except Exception as err:
#     print(f"An Error Occured As {err}");

# print("The Party Will Start Soon");

# data = open("./main.py");  # File Handling

# print(data);

# print(type(data));

# print(dir(data));

# print([i for i in dir(data) if "__" not in i]);

# print([i for i in dir(data) if not i.startswith("_")]);

# data = open("./main.py"); # Connectivity With File

# print(data.read());

# data.close(); # Close Connectivity

# with open("./app.txt") as file: # The With Method Automatically Close Your File After Done

#     print(type(file));

#     print(file.read());

# print("Free Palestine");

# with open("./app2.txt") as file:

#     print(file.readline()); # Read Only One Line At A Time

#     print(file.readline());

# with open("./app2.txt") as file:

#     print(file.readline(), end="");

#     print(file.readline(), end="");

# with open("./app2.txt") as file:

#     print(file.readlines());

# with open("./app2.txt", "r") as file: # By Default Is R (Read)

#     print(file.readlines()[1:3]);

# with open("./app3.txt", "w") as file: # W Is Create New File & If File Exist Remove Old Content Add New

#     file.write("Imran Khan");

# with open("./app3.txt") as file:

#     print(file.read());

# with open("./app3.txt", "r+") as file: # Read & Write Both In File

#     print(file.read());

#     file.write(" Release Imran Khan"); # After Run Write Method Cursor Go In Last

#     print("After:", file.read()); # Then It Show Blank

# with open("./app3.txt", "r+") as file:

#     print(file.read());

#     file.write(" Release Imran Khan");

#     file.seek(0); # Select Particular Value In Cursor

#     print("After:",file.read());

# with open("./app4.txt", "w") as file:

#     file.write("Free ");

# with open("./app4.txt", "a") as file: # If File Not Exist It Will Create New File & If Exist Add Content In Last Of File Not Remove Like W

#     file.write("Palestine");

# with open("./app5.txt", "x") as file: # If File Not Exist Then It Will Create New File

#     file.write("My Name Is AHM X"); # If File Exist Then Will Thorw Error

# ======================== OOP (Object Oriented Programming) ======================== #