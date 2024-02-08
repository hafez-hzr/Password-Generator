import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spch=['!', '#', '$', '&', '*', '_', '|', ';', ':','<', '>', ',', '.', '?', '/']
len_alpha=int(input('Enter the length of alphabets: '))
len_num=int(input('Enter the length of numbers: '))
len_spch=int(input('Enter the length of special characters: '))
pw=[]
for i in range(len_alpha):
    pw+=(random.choice(letters))
for i in range(len_num):
    pw+=(random.choice(numbers))
for i in range(len_spch):
    pw+=(random.choice(spch))
random.shuffle(pw)
password=''.join(random.sample(pw,(len_num+len_spch+len_alpha)))
print(f'Password: {password}')