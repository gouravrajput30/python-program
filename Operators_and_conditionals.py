"""operators is the concept of programing language which is used to perform operation
between two operands"""

# type of operators
"""
    1 arithmetic operators  
    ex: /,*,-,+,%,//- this is called floor division,** - this is called exponential
    division= 3/3=1.0
    floor division= 1
    exponential=3**3=27
    
    2. conditional operator/relational operator
    equal to= ==
    greater then=>
    less then=<
    greater then equal to=>=
    less then equal to =<=
    
    3. logical operator
    And- and it is used for check two condition or more then two conditions
    logic:
    condition1         condition2          result
    true        and       false            false
    false       and       true             false
    true        and       true             true
    false       and       false            false
    
    Or: if the first condition is false then also it will check for second condition
    logic:
    condition1         condition2          result
    true        or       false            true
    false       or       true             true
    true        or       true             true
    false       or       false            false
    Not: not is used for check the non equality between two operands
    
    4. membership operator:
    a type of operator which is used to check the value in the given data set
    
    in- if the given value ia present in the data set then it will return true
    not in- if the given value is not present in data set then it return true
      
"""
#  user of operators:

num1 = 2
num2 = 5
result = num1 ** 5
print(num2 < num1)

# logical operator

# user_age = int(input("Enter the age : "))
# user_gender = input("Enter the gender")

# if the age is greater then 19 then allowed for admission and is gender is male then
# if user_gender == "male" and user_age >= 19:
#     print("allowed")
# else:
#     print("Not allowed")

fruits = ["apple", "banana", "orange", "mango"]
empty_list = fruits
if fruits is not empty_list:
    print("not empty")
else:
    print("empty")

fruit = "orange"
if fruit not in fruits:
    print("fruit is present in the list")
else:
    print("fruit is not present in the list")





