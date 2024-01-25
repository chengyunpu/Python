a,b,c=map(int,input().split())
j=max(a,b,c)
if(j*j==a*a+b*b+c*c-j*j):
    print("right triangle")
elif(j*j>a*a+b*b+c*c-j*j):
    print( "obtuse triangle")
else :
    print("acute triangle")