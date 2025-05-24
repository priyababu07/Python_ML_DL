import time
import math

def delayed_sqrt(x, delay_ms):
    time.sleep(delay_ms / 1000.0)  
    print(math.sqrt(x))

print("Square root after specific milliseconds:")
delayed_sqrt(16, 1000)   
delayed_sqrt(100, 500)   
delayed_sqrt(25100, 700) 
