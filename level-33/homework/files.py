def combine_strings(str1, str2):
    result = str1 + str2
    print(result)

combine_strings("Hello, ", "world!")
def sum_elements(num_list):
    if len(num_list) >= 4:
        result = num_list[2] + num_list[3]
        print(result)
    else:
        print("The list does not have enough elements.")

sum_elements([1, 2, 3, 4, 5])
def print_larger(num1, num2):
    larger = max(num1, num2)
    print(larger)

print_larger(10, 20)
