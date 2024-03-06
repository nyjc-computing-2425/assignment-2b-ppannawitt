num = input('Enter a number (decimal only): ')
# type your code here
index = num.find('.') 
remaining = num[index+1:]
dp = len(remaining)


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
