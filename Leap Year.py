year = int(input())
if year % 100 == 0:
    if year% 400 == 0:
        print("True")
    else:
        print("False")
elif year % 4 == 0:
    print("True")
else:
    print("False")
#Method2:

# def is_leap(year):
#     leap = False
#
#     Write your logic here
#     Write a function in Python - Hacker Rank Solution START
    # if year % 400 == 0:
    #     leap = True;
    # elif year % 4 == 0 and year % 100 != 0:
    #     leap = True;
    # return leap
# year = int(raw_input())
# print is_leap(year)
