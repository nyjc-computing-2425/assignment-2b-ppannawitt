num = input('Enter a number (decimal only): ')
# type your code here
ind = -1;
for i in range(len(num)):
  if (num[i]=='.'):
    ind = i
    break
dp = len(num) - ind -1


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
