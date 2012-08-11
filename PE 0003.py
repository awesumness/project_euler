import sys
import time
import math
start_time = time.clock()


# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
n_1=600851475143
answer=int(math.sqrt(n_1))
if( answer % 2 == 0 ):
  answer += 1
prime = False
while( 1 < answer and not prime):
  answer -= 2
  if n_1 % answer == 0:
    checkPrime = 3
    prime = True
    while( prime and checkPrime < (math.sqrt(answer)+1) ):
      if( answer % checkPrime == 0):
        prime = False
      checkPrime += 2
stop_time = str(time.clock() - start_time) + " seconds"
print answer
print stop_time



with open(sys.argv[0] + ".out", "w") as answer:
  answer.write(str(answer))
  answer.write('\n')
  answer.write(stop_time)
