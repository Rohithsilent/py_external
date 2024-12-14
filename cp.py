def cp(p,r,t):
   r=r/100
   a = p*(1+r)**t
   cp = a-p
   return cp



principle = float(input("enter principle:"))
rate = float(input("enter rate:"))
time = float(input("enter time:"))

compund_interest = cp(principle,rate,time)
print(f"compound interest is:{compund_interest:.2f}")


