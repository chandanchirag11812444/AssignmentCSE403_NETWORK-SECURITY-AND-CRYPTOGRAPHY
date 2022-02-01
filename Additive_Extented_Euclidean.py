#Our Target is To find the value of t which will be the muliplicative inverse of b .
#Actually the Extended Euclidean algorithm find the multiplicative inverse of b in Zn when n and b are given and gcd(n,b)=1
#so the multiplicative inverse of b is the value of t .
from re import A


def ExtendedEA(r1, r2):
    s1=1
    s2=0
    t1=0
    t2=1
    q=0
    t=0
    s=0
    r=0
    print("r1\t r2\t q\t r\t s1\t s2\t s\t t1\t t2\t t\t")
    print("______________________________________________________________________________________")
    while r2>0:
        print(r1,'\t', r2,'\t', q,'\t',r,'\t', s1,'\t', s2,'\t', s,'\t', t1,'\t', t2,'\t', t,'\t')
        q=r1//r2
        r=r1-q*r2
        r1=r2
        r2=r


        s=s1-q*s2
        s1=s2
        s2=s


        t=t1-q*t2
        t1=t2
        t2=t
    return r1,s1,t1    
#Coding Part 
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
if a < b:
    temp=a
    a=b
    b=temp

gcd, s, t=ExtendedEA(a, b)
print("gcd of ",a, "&", b,"is", gcd)
if(t < 0):
    t=t+a
print("The value of s :",s," and t is ",t)

if(gcd==1):
    print(" The inverse of ",b, " in Z",a, " is:",t)







    