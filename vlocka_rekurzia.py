## viemeprogramovat.sk rekurzia priklad

import turtle

def rek(n, d):
    for i in range(6):        
        forward(d)
        if n > 0:

            rek(n-1, d/2.5)
        back(d)
        right(360/6)
    
rek(1, 100)
