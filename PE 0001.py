import sys
import time
start_time = time.clock()


#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
sum = 0
for number in range(3,1000):
  if( number % 3 == 0 or number % 5 == 0 ):
    sum+=number
stop_time = str(time.clock() - start_time) + " seconds"
print sum
print stop_time



with open(sys.argv[0] + ".out", "w") as answer:
  answer.write(str(sum))
  answer.write('\n')
  answer.write(stop_time)
