def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num_list = input("Enter a list of numeric values those are separated by spaces\n ").split()
num_list = [int(num) for num in num_list if num.isdigit()]

if len(num_list) < 2:
    print("Please enter at least 2 numeric values\n")

result = num_list[0]
for num in num_list[1:]:
    result = gcd(result, num)

print("Greatest Common Divisor\n", result)
