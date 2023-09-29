import numpy as np
import devide
import psum

x = 33
y = 25
z_1 = psum.PSum.sum(x, y)
z_2 = devide.Divide.divide(x, y)
print(f"sum and divide are respectivily: {z_1} , {z_2}")
