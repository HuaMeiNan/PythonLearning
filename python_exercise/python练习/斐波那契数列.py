def fie(t):
    a = 0
    b = 1
    for i in range(t):
        a,b = b, a+b
        print(a)

print(fie(6))
print('-'*50)
