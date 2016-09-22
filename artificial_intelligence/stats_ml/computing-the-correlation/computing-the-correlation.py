import sys
import math
n = int(sys.stdin.readline())

sum_x = 0
sum_y = 0
sum_z = 0
sum_x_sq = 0
sum_y_sq = 0
sum_z_sq = 0
sum_xy = 0
sum_xz = 0
sum_yz = 0

for line in sys.stdin:
    xyz = [int(num) for num in line.split()]
    x, y, z = xyz
    sum_x += x
    sum_y += y
    sum_z += z
    sum_x_sq += math.pow(x,2)
    sum_y_sq += math.pow(y,2)
    sum_z_sq += math.pow(z,2)
    sum_xy += x*y
    sum_xz += x*z
    sum_yz += y*z
    
sq_sum_x = math.pow(sum_x,2)
sq_sum_y = math.pow(sum_y,2)
sq_sum_z = math.pow(sum_z,2)

corr_xy = (n*sum_xy - sum_x*sum_y)/(math.sqrt(n*sum_x_sq - sq_sum_x) * math.sqrt(n*sum_y_sq - sq_sum_y))
corr_xz = (n*sum_xz - sum_x*sum_z)/(math.sqrt(n*sum_x_sq - sq_sum_x) * math.sqrt(n*sum_z_sq - sq_sum_z))
corr_yz = (n*sum_yz - sum_y*sum_z)/(math.sqrt(n*sum_y_sq - sq_sum_y) * math.sqrt(n*sum_z_sq - sq_sum_z))

print round(corr_xy,2)
print round(corr_yz,2)
print round(corr_xz,2)
    
