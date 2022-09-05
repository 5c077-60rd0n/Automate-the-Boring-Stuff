def collatz(number):
    if number % 2 == 0:
        even_number = number // 2
        print(even_number)
        return even_number
    elif number % 2 == 1:
        odd_number = 3 * number + 1
        print(odd_number)
        return odd_number

response = int(input('Enter an integer: '))
while response > 1:
    response = collatz(response)

