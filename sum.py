def sum_user_numbers(num_prompts=5):
    total_sum = 0
    for _ in range(num_prompts):
        while True:
            try:
                number = float(input("Please enter the number: "))
                total_sum += number
                break
            except ValueError:
                print("Wrong Input, Please enter the number: ")
    return total_sum

result = sum_user_numbers()
print(f"The sum of the numbers is: {result}")
