a,b,c=map(int,input().split())
d=b**2-4*a*c
if(d>0):
        print("Two different roots x1=%d , x2=%d" % (((-b+(b**2-4*a*c)**0.5)/2*a),((-b-(b**2-4*a*c)**0.5)/2*a)))
elif(d==0):
        print("Two same roots x=%d" % (((-b+(b**2-4*a*c)**0.5)/(2*a))))
else:
        print("No real root")