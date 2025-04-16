def separate_even_odd(*args):
    odd_numbers = []
    even_numbers = []
    for num in args:
        if isinstance(num,int):
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)
        else:
            print(f"Warning: Wrong Argument '{num}'. Integer is a must")
    return odd_numbers, even_numbers

input_string = input("Enter numbers separated by Spaces: ")
number_strings = input_string.split()

numbers = []
for num_str in number_strings:
    try:
        num = int(num_str)
        numbers.append(num)
    except ValueError:
        print (f"Warning: '{num_str}' is not valid integer and will be ignored")
odds, evens = separate_even_odd(*numbers)
print (f"Odd Numbers: {odds}")
print (f"Even Numbers: {evens}")
