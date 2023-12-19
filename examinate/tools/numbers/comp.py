
n = int(input('Enter number: '))


def sumofdigits(n):
    sum = 0
    for digit in str(n): 
        sum += int(digit)      
    return sum

print("sum number is" ,sumofdigits(n))

def ispal(number):
    
    str_number = str(number)
    
    return str_number == str_number[::-1]


input_number = int(input("Enter a number: "))
result = ispal(input_number)

print(f"{input_number} is a palindrome: {result}")


