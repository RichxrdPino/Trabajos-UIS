n = int(input("número a revisar:"))
div=0
for i in range(2, n):
    if n%i == 0:
        div=div+1
if div>0:
    print("no es primo")
else: 
    print("es primo")