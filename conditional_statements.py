# age = 10

# if age <= 12:
#     print("You are still a Kid")
# elif age >= 12 and age <= 18:
#     print("You are still a Teen")

# elif age >= 18 and age <= 40:
#     print("You are now a Youth")

# else:
#     print("You are an Elder")



"""

    GO THROUGH THE ARRAY IN RANGE OF 20
    - IF AN ITEM IS DIVISIBLE BY 3 AND 5, PRINT FIZZBUZZ
    - IF IT IS DIVISIBLE BY 3, PRINT 'FIZZ'
    - IF BY 5, PRINT 'BUZZ'

"""
# nums = range(0, 20)  this works too, instead of wrting out all the numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
for num in nums:

    if num % 3 == 0 and num % 5 == 0:
        print('FIZZBUZZ')

    elif num % 3 == 0:
        print('FIZZ')

    elif num % 5 == 0:
        print('BUZZ')

    else:
        print('not fizzbuzzz')




