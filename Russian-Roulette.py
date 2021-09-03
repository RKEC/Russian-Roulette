import random
import os

chamber = 6
bullet = random.randint(0, chamber)
killingBullet = random.randint(0, chamber)
print(bullet , " : " , killingBullet)
if bullet == killingBullet:
    os.system("shutdown -t 0 -r -f")
