import math
from decimal import *

getcontext().prec = 1000
# this increases the amount of decimals python will display

e = 0
for i in range(0,1000):
    e += Decimal(1/(math.factorial(i)))
e = str(e)
# this prints out e and turns it into a string. e = 1/1! + 1/2! + ... + 1/n!. Of course this is only an approximation of e, this "e"
# diverges from the real value of e near it's end. To get a better estimate, I'd need to increase the range.

def check_prime(n):
    limit = math.sqrt(n)
    limit = round(limit)
    for i in range(2,limit):

        check = (n/i).is_integer()

        if check == True:
            return False
            break

    return True
# as the name says, this function checks for primes. to check if a number is prime, you need to divide that number by every number that
# comes before it (excluding 1). If, for any of those divisions, the result is an integer, the number isnt a prime. However, you dont
# need to check every single number, you only have to check till the square root of the number, though I dont remember the reason.

for i in range(2,len(e)-10):
    number = e[i] + e[i+1] + e[i+2] + e[i+3] + e[i+4] + e[i+5] + e[i+6] + e[i+7] + e[i+8] + e[i+9]
    isnumber = check_prime(int(number))
    if isnumber == True:
        print("found a prime! it's ", number)
# this is taking every single 10 digit number in "e" and running it through the check_prime function. The way I got the numbers is
# quite awkward, I admit. I'm not checking for primes near the end of "e", however I think that's justified as the "e" I calculated
# diverges from the real value of e near the end.

