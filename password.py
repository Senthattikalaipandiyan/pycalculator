import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbols="!@#$%^&*()/?]{[}"
all= lower+upper+number+symbols
length=int(input("Enter length of password you want:"))
password= "".join(random.sample(all,length))
print("The password is",password)
