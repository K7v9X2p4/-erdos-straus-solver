def solve(n):
    if n%2==0:
        x=n//2
        y=z=n
        return x,y,z
    if n%3==0:
        k=n//3
        return k,6*k,6*k
    for x in range(n//4+1, (3*n)//4+1):
        num=4*x-n
        den=n*x
        y_min=(den+num-1)//num
        y_max=(2*den+num-1)//num+2
        for y in range(y_min,y_max+1):
            den_z=num*y-den
            if den_z<=0: continue
            num_z=den*y
            if num_z%den_z==0:
                return x,y,num_z//den_z
    return None

for n in [5,7,11,101,1001,10007,999999937]:
    x,y,z=solve(n)
    print(f"4/{n}=1/{x}+1/{y}+1/{z} OK={abs(1/x+1/y+1/z-4/n)<1e-12}")
