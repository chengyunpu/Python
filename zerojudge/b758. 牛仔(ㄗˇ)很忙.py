h,m=map(int,input().split())
print("%02d:%02d" %(((h+2+((m+30)>=60))%24),((m+30)%60)))