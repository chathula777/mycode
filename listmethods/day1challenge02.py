 
#!/usr/bin/env python3
import random

icecream = ["flavors", "salty"] 

tlgclass = ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

icecream.append(99)

print(icecream)

random_student = int(random.random() * len(tlgclass) )

select_student = input(f"Select a student between 0 and {len(tlgclass) -1}: ")

print(f"You had {icecream[2]} {icecream[0]} to pick from and {tlgclass[int(select_student)]} chose to be {icecream[1]}")
