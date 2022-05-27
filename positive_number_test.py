user_no = input("Enter number: ")

try:
    user_no = float(user_no)
    print('Congrats')
    
    if user_no >= 0:
        print('Number is positive')

    if user_no < 0:
        print('Number is negative')

except:
    print('This is not a number')    
