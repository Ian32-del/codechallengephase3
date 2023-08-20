def positive_numbers(a, b, c):
    positive_digits = 0
    # by initializing it to 0 , meaning we shal start counting form 0
    # Used to keep track of how of the intergers are positive 
    # Basically when a interger is positive it adds a positive_count by one 

    if a > 0:
        positive_digits += 1
        # Basically when a interger is positive it adds a positive_count by one 
        # this checks if the value of a is grater than 0 , and if it is the positive_digits is triggered


    if b > 0:
        positive_digits += 1
        # so basically if the integer in b is a positive number it adds one to the positive digits  

    if c > 0:
        positive_digits += 1

    return positive_digits == 2
# this checks if only 2 intergers in the line of 3 are positive 

print(positive_numbers(2, -2, 5))
