message = "Learning Generative & Agentic AI!";

print(message);

print(type(message));

print(id(message)); # Physical Address

print(dir(message)); # All Methods & Attributes

print([i for i in dir(message) if "__" not in i]); # Important Methods & Attributes

num = 45;

print(num, type(num));

num = -45.5;

print(num, type(num));

num = 2/2;

print(num, type(num));

complex_data = 44j; # In Complex Type Only Use Word "J"

print(complex_data, type(complex_data));

check = True;

print(check);

name = "sAbrina CarpenTer";

print(name.title());

print(name.upper());

print(name.lower());

name = "A" + "H" + "M" + " X";

print(name);

print(9 + \
      10 + \
      6); # Backslash Means Logic Continue The In Next Line

strIndex = "Ahmed Shaykh";

print(strIndex[6]);

print(strIndex[-4].upper());

strSlice = "Ahmed Saleem Shaikh";

print(strSlice[0:5:1]);

val = 0.0;

print(val, type(val));

print(bool(val), type(bool(val)));

boolVal = True;

print(boolVal, int(boolVal), type(int(boolVal)));

implicitType = 4/2;

print(implicitType, type(implicitType));

multiStr = """Imran Khan
Is The Only Leader
Of Pakistan""";

print(multiStr);

first_name = "Imran";

last_name = "Khan";

full_name = f"{first_name} {last_name}";

print(full_name);

mess = f"{full_name.upper()} ZINDABAD!";

print(mess);

print(mess.title());

name = "Ahmed Saleem Shaikh";

artistName = "AHM X";

age = 25;

skills = "Full Stack Developer, AI Engineer & Music Producer";

religion = True;

visaCard = f"""
My Name: {name}
My Artist Name: {artistName}
My Age: {age}
My Skills: {skills}
My Religion Is Islam: {religion}
""";

print(visaCard);

total = f"""
Totals: {3 + 5 + 8}
""";

print(total);

message = input("What Is Your Name: ");

print(f"Nice To Meet You {message}");

# Arithmetic Operators

num = 2 + 3;

print(num);

num = 2 * 3;

print(num);

num = 3 / 2;

print(num);

num = 4 ** 4; # Exponentiation Operator

print(num);

a = 11;

b = 3;

print(a % b); # Modulus Operator Give Reminder

print(12 / 3); # Normal Division Operator Value Return In Float

print( 12 // 3); # Floor Division Operator Value Return In Integer

print(14.8 / 3);

print(14.8 // 3);

print(17 // 3);

# Assignment Operators

a = 7;

a = a + 2;

print(a);

a += 1;

print(a);

x = 5;

x -= 3;

print(x);

x = 5;

print(x);

x %= 3;

print(x);

x = 5;

x /= 3;

print(x);

x = 5;

x //= 3;

print(x);

x = 5;

x **= 3;

print(x);

# Comparison Operators

a = 7;

b = "7";

print(a == b);

print(a == int(b));

print(a != b);

a = 67;

b = 49;

print(a < b);

print(a > b);

print(a >= b);

a = "A";

b = "B";

print(a <= b);

print(12 >= 12);

print(ord("A")); # ASCII Code (A = 65 TO Z = 90)

print(chr(65)); # (a = 97 To z = 122 & 0 = 48 TO 9 = 57)

# Logical Operators

print(12 > 20 and 123 > 100 and 34 == 34 and 45 < 90);

print(12 > 20, 123 > 100, 34 == 34, 45 < 90);

print(True and True and True and True);

print(True and True and False and True);

print(12 != 12 or 23 == 45 or 67 == 56 or 10 > 5);

print(12 != 12, 23 == 45, 67 == 56, 10 > 5);

print(True or True or True or True);

print(False or False or False or True);

print(False or False or False or False);

print(not False); # Reverse Boolean Value

print(not 12 == 12);

a = 6;

if a > 10: # Indentation
    print("I will do task A");

else:
    print("I will do task B");

if True:
    print("Imran Khan Zindabad");

else:
    print("Hello World!");

print("Hello World!") if False else print("Imran Khan Zindabad");

if True:
    print("True");

print("1");

print("2");

if False:
    print("True");

print("3");

print("4");

if True:
    print("True Block");

elif False:
    print("Elif Logic 1");

elif False:
    print("Elif Logic 2");

elif False:
    print("Elif Logic 3");

else:
    print("Final Else Block");

if False:
    print("True Block");

elif True:
    print("Elif Logic 1");

elif False:
    print("Elif Logic 2");

elif False:
    print("Elif Logic 3");

else:
    print("Final Else Block");

if False:
    print("True Block");

elif False:
    print("Elif Logic 1");

elif False:
    print("Elif Logic 2");

elif False:
    print("Elif Logic 3");

else:
    print("Final Else Block");

print("Learning Python");

money = int(input("Please Provide Me The Money: "));

if money >= 300:
    print("I will take Zinger Roll");

elif money >= 180:
    print("I will take Drink");

elif money >= 60:
    print("I will take Tea");

else:
    print("I will take anything i want");

per = int(input("Enter Your Percentage: "));

grade = None;

if per >= 80:
    grade = "A+";
elif per >= 70:
    grade = "A";
elif per >= 60:
    grade = "B";
elif per >= 50:
    grade = "C";
elif per >= 40:
    grade = "D";
elif per >= 33:
    grade = "E";
else:
    grade = "Fail";

print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");

per = int(input("Enter Your Percentage: "));

grade = None;

if per >= 0: # Logical Error
    grade = "Fail";
elif per >= 33:
    grade = "E";
elif per >= 40:
    grade = "D";
elif per >= 50:
    grade = "C";
elif per >= 60:
    grade = "B";
elif per >= 70:
    grade = "A";
else:
    grade = "A+";

print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");

per = float(input("Enter Your Percentage: "));

grade = None;

if (per >= 0) and (per < 33):
    grade = "Fail";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 33) and (per < 40):
    grade = "E";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 40) and (per < 50):
    grade = "D";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 50) and (per < 60):
    grade = "C";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 60) and (per < 70) :
    grade = "B";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 70) and (per < 80) :
    grade = "A";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >=80 )and (per < 100):
    grade = "A+";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
else:
    print("Error 404");

records = ["Revealed", "Spinnin", "Armada", "STMPD"];

print(records);

for record in records:
    print(record);

records = ["Revealed", "Spinnin", "Armada", "STMPD"];

i: int = 0;

while i < len(records):
    print(records[i]);
    i += 1;

for i in range(0, 21, 2):
    print(i);

for i in range(-1, -16, -1):
    print(i);

num = int(input("Which Table You Want: "));

for i in range(num, (num * 10) + 1, num):
    print(i);

name = "Ahmed Saleem Shaikh";

print(len(name)); # Calculate String Value

for i in range(len(name)):
    print(name[i]);

username = "AHM X MUSIC";

for i in username:
    print(i);

for i in range(21):
    if i == 15:
        print(f"Break Statement Is Executed In {i}");
        break;
    print(i);

for i in range(31):
    if i == 15:
        print(f"Continue Statement Is Executed In {i}");
        continue;
    print(i);

for i in range(21):
    if i == 15:
        print("Break Statement Is Executed");
        break; # If Break Will Execute
    print(i);
else: # Else Will Not Execute
    print("Break Statement Is Not Executed");

for i in range(21):
    if i == 22:
        print("Break Statement Is Executed");
        break;
    print(i);
else:
    print("Break Statement Is Not Executed");

n = int(input("Which Table Print You Want: "));

for i in range(1,11):
    print(f"{n} * {i} = {n * i}");

n = int(input("Which Number Get Sum You Want: "));

sum = 0;

for i in range(1, n + 1):
    sum = sum + i;

print(f"Your Sum Is {sum}");

n = int(input("Which Number Get Factorial You Want: "));

fact = 1;

for i in range(1, n + 1):
    fact = fact * i;

print(f"Your Factorial Is {fact}");

n = int(input("Which Number Get Factors You Want: "));

for i in range(1, n + 1):
    if n % i == 0:
        print(i);

name = "AHMED";

revNam = "";

for i in range(len(name)-1, -1, -1):
    revNam = revNam + name[i];

print(revNam);

stringValue = "P@#yn26at^&i5ve";

chars = 0;

digits = 0;

symbol = 0;

for i in stringValue:
    if i.isdigit():
        digits += 1;
    elif i.isalpha():
        chars += 1;
    else:
        symbol += 1;

print(f"""Your Digits are {digits}
Your Alphabets are {chars}
Your Special Or Symbols Characters are {symbol}""");

print(dir(stringValue));

a = 1;

while a <= 30:
    print(a);
    a = a + 1;

flag = True;

number = 0;

while flag:
    print(f"No. {number}");
    number += 1;
    if number == 10:
        break;

val = int(input("Enter Your Number: "));

while val > 0:
    print(val % 10);
    val = val // 10;

val = int(input("Enter Your Number: "));

rev = 0;

while val > 0:
    rev = rev * 10 + val % 10;
    print(rev);
    val = val // 10;
    print(val);

print(rev);

val = int(input("Enter Your Number: "));

copy = val;

rev = 0;

while val > 0:
    rev = rev * 10 + val % 10;
    print(rev);
    val = val // 10;
    print(val);

if copy == rev:
    print("Pallindromic Number");
else:
    print("Not A Pallindromic Number");

li = [100,200,300];

index = 0;

while index < len(li):
    print(f"Current Index Is: {index} & List Value Is {li[index]}");
    index += 1;

import random;

num = random.randint(1, 10);

tries = 0;

while True:
    guess = int(input("Please Guess Your Number Between 1 To 10: "));

    if num == guess:
        tries +=1;
        print(f"Congratulations You Win & No Of Tries: {tries}");
        print(num);
        break;

    elif num < guess:
        print("Go A Little Lower");
        tries +=1;
        print(num);

    elif num > guess:
        print("Go A Little Higher");
        tries +=1;
        print(num);

    else:
        tries +=1;
        print("Something Went Wrong");

country = print("Netherlands"); # Print Is Non Return Function

print(country);

country = len("Netherlands"); # Length Is Return Function

print(country);

def ai():
    print("Artificial Intelligence");

ai();

def addNumbers(num1 , num2 = 0):
    print(num1 + num2);
    return num1 + num2;

addNumbers(56,42);

addNumbers(4);

num = lambda num1, num2 : num1 + num2;

print(num(12, 20));

def pallindrome(str):

    rev = "";

    for i in range(len(str)-1, -1, -1):
        rev = rev + str[i];
    
    if rev == str:
        print(f"{str} Is A Pallindrome");
    else:
        print(f"{str} Is Not A Pallindrome");


pallindrome("CIVIC");

pallindrome("AHM X");

listArr = ["Ahmed", "Asmir", "Jad"];

print(listArr);

print(listArr[0].upper());

print(listArr[-2]);

abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYXZ");

print(abc);

print(type(abc));

print(list("ABCDEFGH"));

for i in range(len(abc)):
    print(i, abc[i]);

abc = list("ABCDEFGH");

print(abc[1:4]); # Default List Slicing Is (Left To Right)

print(abc[:4]);

print(abc[-5:-2]);

print(abc[0:2:1]); # Step Default Value Is 1 & It Direction (Left To Right)

print(abc[0:2:]);

print(abc[0:5:2]);

print(abc[-1:-5:-1]); # Put Step Value -1 Then Reverse Direction (Right To Left)

abc = list("abcdefghijklmnopqrstuvwxyz");

print(abc[::2]);

print(abc[0::2]);

print(abc[:26:2]);

print(abc[::-1]);

print(dir(list)); # List All Methods

print([i for i in dir(list) if "_" not in i]);

help(list);

records = ["Revealed", "Spinnin", "Armada"];

print(records);

labels = ["STMPD", "Afterlife"];

records.append("Drumcode"); # Add Value In Last Of List

records.append(labels);

print(records);

records = ["Revealed", "Spinnin", "Armada"];

print(records);

labels = ["STMPD", "Afterlife"];

records.extend(labels); # All Lists Combine In One List

print(records);

records = ["Revealed", "Spinnin", "Armada"];

print(records);

records.insert(3, "STMPD"); 

print(records);

records.remove("Spinnin");

print(records);

record = records.pop(2); # Pop Remove & Store Value In Element Or Variable

print(records, "Pop Store Value:", record);

records = ["Revealed", "Spinnin", "Armada", "STMPD", "Afterlife"];

print(records.index("Afterlife"));

records = ["Revealed", "Spinnin", "Armada", "STMPD", "Afterlife", "Spinnin"];

print(records.index("Spinnin", 2));

record = list("Afterlife");

print(record);

print(record.count("e")); # Count Element

print(record.count("a"));

records = ["Revealed", "Spinnin", "Armada", "Afterlife"];

print(records);

records.sort(); # Sort In Ascending Order

print(records);

records.sort(reverse=True); # Sort In Descending Order

print(records);

records = ["Revealed", "Spinnin", "Armada", "Monstercat", "STMPD"];

del records[1:4];

print(records);

records[1] = "ASOT";

print(records);

records.reverse();

print(records);

records = ["Revealed", "Spinnin", "Armada"];

labels = records # Shallow Copy

print(labels);

labels[1] = "STMPD";

print("Records:", records);

print("Labels:", labels);

records = ["Revealed", "Spinnin", "Armada"];

print(records);

labels = records.copy(); # Deep Copy

print(labels);

labels[1] = "STMPD";

print("Records:", records);

print("Labels:", labels);

num = [1, 2, 3];

num.clear(); # Remove All Element But Object Is Remain

print(num);

l = [12,435,67,89,23,25,69];

sum = 0;

for i in l:
    sum = sum + i;

print(sum/len(l)); # Mean

letters = ("A","B","C"); # Tuple Immutable (Constant)

print(type(letters));

print(letters[0]);

print(letters[0:2]);

letters = ("Netherlands", 4, 4.0); # Reassign Value In Tuple (OverWrite)

print(letters);

for i in letters:
    print(i);

data = ("A", [1,2,3], True);

print(data);

print(data[1]);

data[1].append(20); # Because It's List

print(data);

for i in range(len(data)):
    print(data[i]);

data = { 1, 1, 4, 5, 4, 7 }; # Set Type Does Not Have Index Value

print(data); # Set Return Unique Value In Order & Not Repeat Dulipcates Value

print(type(data));

setVal = { 1, 9, 4, "Set", 5, 2, 7 };

for i in setVal:
    print(i);

setVal.clear();

print(setVal);

print(dir(set));

print([i for i in dir(set) if "__" not in i]); # Set Data Types Methods & Attributes

A = {1, 2, 3, 4, 5};

B = {3, 4, 5, 6, 7};

setData = A.union(B);

print(setData); # A | B

setData = A.intersection(B);

print(setData); # A & B

setData = A.difference(B);

print(setData); # A - B

setData = A.symmetric_difference(B);

print(setData); # A ^ B

dictData = { "fName": "Ahmed", "mName": "Saleem", "lName": "Shaikh" };

print(dictData);

print(type(dictData));

print(dictData["fName"]);

dictData["fName"] = "AHM X";

dictData["lName"] = "MUSIC";

dictData["Country"] = "Netherlands";

del dictData["mName"];

print(dictData);

nums = { 1 : 100, 2 : 200, 3 : 300, 4 : 400 };

for i in nums:
    print(i, ":", nums[i]);

print([i for i in dir(dict) if "__" not in i]);

nums.clear();

print(nums);

data = {
                            "Country": "Netherlands",
                            "Message": "Free Palestine",
                            "Learning Language": "Python"
                        };

dictdata = data; # Deep Copy

dictdata["Country"] = "Netherlands";

print(data, "Deep Copy");

print(dictdata, "Deep Copy");

data = {
                            "Country": "Netherlands",
                            "Message": "Free Palestine",
                            "Learning Language": "Python"
                        };

dictdata = data.copy(); # Shallow Copy

dictdata["Country"] = "Netherlands";

print(data, "Shallow Copy");

print(dictdata, "Shallow Copy");

print(data.get("Pakistan", "Not Available"));

print(data.get("Message", "Not Available"));

print(f"{dictdata.keys()} \n");

print(f"{dictdata.values()} \n");

print(f"{dictdata.items()}");

dictdata.pop("Message"); # Pop Remove Particular Value

print(dictdata);

dictdata.popitem(); # PopItem Remove Last Value

print(dictdata);

keys = ["fName", "mName", "lName", "Country"];

data= {};

data = data.fromkeys(keys);

print(data);

data = data.fromkeys(keys, 1);

print(data);

data= {
                            "Country": "Netherlands",
                            "Message": "Free Palestine",
                            "Language":"Python"
                        };

val = data.setdefault("Language", "TypeScript"); # If Same Index Value Exist Not Update Value

print(data);

print(val);

val2 = data.setdefault("LLM", "Empty Value"); # If Not Index Value Exist Add New Value In Object

print(data);

print(val2);

data = {
                        "fName": "Ahmed",
                        "lName": "Shaikh",
                        "Country": "Pakistan"
                    };

data2 = {
                            "Country": "Netherlands",
                            "Message": "Free Palestine",
                            "Language": "Python"
                    };

data.update(data2);

print(data);

data = {
    "fname": "Ahmed Saleem",
    "name": "Ahmed",
    "id": 44,
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2}
};

print(data);

print(data["cde"]["b"]);

print(data["cde"]);