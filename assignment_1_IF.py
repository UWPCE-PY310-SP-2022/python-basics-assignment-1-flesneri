#Question 1
my_string = "Hello"
my_integer = 10
my_float = 3.14

#Question 2
int1 = 20
int2 = 30
int3 = int1 + int2 
# The expected value of int_result is 50
print(int3)
print()

#Question 3
float1 = 20.6
float2 = 52.8
float3 = float1 + float2
# The expected valie of float_result is 73.4
print(float3)
print()

#Question 4
string1 = "french"
string2 = "fry"
string3 = string1 + string2 
# The result of string3 will be frenchfry
print(string3)
print()

#Question 5
int_float_add = int1 + float1
# The value of int_float_add will be 40.6
print(int_float_add)
# The type of int_float_add will be a float
print()

#Question 6
# int_string_add = int1 + string1
# The value of int_string_add will be error
# print(int_string_add)
# The output value was an error because there was an illegal 
# additon of an integer and string

#Question 1a
print(type(my_string))
print(type(my_integer))
print(type(my_float))
print()

#Question 2a
string4 = "28"
print(type(string4))
int4 = int(string4)
print(type(int4))
print()

#Question 3a 
float4 = round(5 * 7.654321 , 3)
print(float4)
print()

#Question 4a
my_name = input("Enter Your Name:")
print(my_name)
print()

#Question 5a
favorite_number = input("Enter your favorite number:")
print(favorite_number)
# The type of favorite_number will be a string.
print(type(favorite_number))
# The type of favorite_value is a string because the 
# input function reads arguments in as strings
# and stores it as a string.
print()

#Question 6a
number1 = input("Enter a number:")
number2 = input("Enter a number:")
sum1 = number1+ number2
# The value of sum1 will be string number_1 + string number2
print(sum1)
# The output value was the combination of number1 and number2 becasue
# it was the addition of two strings and not two integers since the 
# input function reads in arguments as strings.
number1_int = int(number1)
number2_int = int(number2)
sum2 = number1_int + number2_int
print(sum2)
print()