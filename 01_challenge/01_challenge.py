"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python

The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""

def fizzbuzz(max_num):
    "This method implements FizzBuzz"
    
    # adding some redundant declarations on purpose
    # we will make our script 'tighter' in one of coming exercises
    three_multiple = 'fizz'
    five_multiple = 'buzz'
    nbr_three = 3
    nbr_five = 5 

    # Google for 'range in python' to see what it does
    for iteration_value in range(1,max_num):
        # % or modulo division gives you the remainder 
        if iteration_value%nbr_three==0 and iteration_value%nbr_five==0:
            print(iteration_value,three_multiple+five_multiple)
        elif iteration_value%nbr_three==0:
            print(iteration_value,three_multiple)
        elif iteration_value%nbr_five==0:
            print(iteration_value,five_multiple)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)
