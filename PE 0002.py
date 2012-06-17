import sys
import time
start_time = time.clock()


#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

n_1=1
n_2=2
n_3=0
answer = 0
while n_2 < 4000000:
  if n_2 % 2 == 0:
    answer += n_2
  n_3=n_1+n_2
  n_1=n_2
  n_2=n_3
stop_time = str(time.clock() - start_time) + " seconds"
print answer
print stop_time



with open(sys.argv[0] + ".out", "w") as answer:
  answer.write(str(answer))
  answer.write('\n')
  answer.write(stop_time)
