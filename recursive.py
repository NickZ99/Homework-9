def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

number = int(input("please enter number: "))
result = recursive_sum(number)
print(f"The sum from 1 to {number} is: {result}")
