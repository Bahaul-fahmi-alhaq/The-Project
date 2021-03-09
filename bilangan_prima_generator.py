import matplotlib.pyplot as plt
max_bil_prima = 500 #limit of the prime number
x = 0
n = 1
m = 0
bil_prima = []
while x < max_bil_prima:
    g = x/n
    p = g-int(g)
    while p == 0:
        if x == n:
            bil_prima.append(x)
            x += 1
            n = 1
            m = 0
            g = x/n
            p = g-int(g)
            continue
        m += 1
        if m<2:
            n += 1
            g = x/n
            p = g-int(g)
            continue
        else:
            x += 1
            n = 1
            m = 0
            g = x/n
            p = g-int(g)
    n += 1
    
print(bil_prima)
posisi = range(1,bil_prima[-1])
plt.plot(posisi,posisi,,'g-', label='Bilangan Real')
