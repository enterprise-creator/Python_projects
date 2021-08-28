import random
pwd_len = int(input('Enter the length of your password: '))
s = []
for i in range (65 , 91):

    s.append(chr(i))

for i in range(97 , 123):

    s.append(chr(i))

for i in range(10): 
    s.append(str(i))


s.extend(['!' , "@" , '#', '$', "%", "^","&", '*','(',')'])

print( "".join(random.sample(s,pwd_len)))
