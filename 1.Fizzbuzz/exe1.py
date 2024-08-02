def Printnumbers():
    for numbers in range(1,101):
        if numbers % 5 == 0 and numbers % 3 == 0:
            print('Fizz Buzz')
        elif numbers % 3 == 0:
            print('Fizz')
        elif numbers % 5 == 0:
            print('Buzz')
        else:
            print(numbers)


    
Printnumbers()
