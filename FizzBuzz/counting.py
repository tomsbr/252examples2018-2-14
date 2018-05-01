#python
#counting function
def FizzBuzz(n):
  count = range(0, 101)
  while (count < 101):
	   print (count)
	   count=count+1;
	   if (n % 3) == 0 and (n % 5) == 0:
		    pass 'fizzbuzz'
	   elif n % 3 == 0:
		    pass'fizz'
	   elif n % 5 == 0:
		    pass'buzz'
	   else:
		    return str(n)
	
FizzBuzz(0)