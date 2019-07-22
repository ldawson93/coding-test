#Question 1 - Lauretta.io coding test
'''
This program takes in a string of numbers and outputs the most likely middle value
Input restriction: 1) Six or more numbers   
                   2) Even number of numbers
                   3) Non-decreasing sequence

Example input: 123456, 12233445
'''
import statistics

def main():
    input_numbers= input("Please input six or more, even number and equal or increasing numbers(Example: 123456): ")
    input_list= list(input_numbers) 
    validate_input(input_list)
    input_list= convert_to_int(input_list)
    print(predict_middle_value(input_list))

def convert_to_int(input):
    return [int(c) for c in input]

def validate_input(input):
    assert is_all_digits(input), "There are some non-digit characters"
    assert len(input) % 2==0, "Length of input not even" 
    assert len(input) >= 6, "Length of input is less than 6"
    assert is_increasing_or_equal(input), "Input contains decreasing numbers"

def is_increasing_or_equal(input):
    for i in range(len(input)-1):
        if input[i]>input[i+1]:
            return False
    return True

def is_all_digits(input):
    for c in input:
        if not c.isdigit():
            return False
    return True
    
def predict_middle_value(input):
    return statistics.median(input)
    
if __name__ == "__main__":
    main()