print("Password should be:")
print("* The alphabets must be between [a-z]\n* At least one alphabet should be of Upper Case [A-Z]\n* At least 1 number or digit between [0-9].")
print("* At least 1 character from [ _ or @ or $ ].")
l_alphabets=list('abcdefghijklmnopqrstuvwxyz')
u_alphabets="abcdefghijklmnopqrstuvwxyz"
u_alphabets=list(u_alphabets.upper())
numbers=list('1234567890')
character=list('_@$')
u=0
l=0
n=0
c=0
a=''
true=0
while true==0:
    if(len(a)>8):
        for i in a:
            if i in l_alphabets:
                l = 1
                continue
            else:
                continue
        for i in a:
            if i in u_alphabets:
                u = 1
                continue
            else:
                continue
        for i in a:
            if i in numbers:
                n = 1
                continue
            else:
                continue
        for i in a:
            if i in character:
                c = 1
                continue
            else:
                continue
        if(l==u==n==c==1):
            print("Valid Password")
            break
        else:
            print("Invalid Format")
            a = list(input("enter your password:"))
            continue

    else:
        print("* Minimum 8 Characters.")
        a = list(input("enter your password:"))
        continue