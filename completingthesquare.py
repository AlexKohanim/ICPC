x, y = [0]*3, [0]*3
for i in range(3):
    x[i], y[i] = map(int, input().split())

d1 = ((x[1] - x[0])**2 + (y[1] - y[0])**2)**(0.5)
d2 = ((x[2] - x[0])**2 + (y[2] - y[0])**2)**(0.5)
d3 = ((x[1] - x[2])**2 + (y[1] - y[2])**2)**(0.5)
print(d1, d2, d3)

b = min(d1, d2, d3)
a = max(d1, d2, d3)
h = (b**2 - 0.25*(a**2))**(0.5)

print("h:",h)

e1, f1 = (x[2] - x[0]) + (x[2] - x[1]), (y[2] - y[0]) + (y[2] - y[1])
e2, f2 = (x[1] - x[0]) + (x[1] - x[2]), (y[1] - y[0]) + (y[1] - y[2])
e3, f3 = (x[0] - x[1]) + (x[0] - x[2]), (y[0] - y[1]) + (y[0] - y[2])

print(e1, f1)
print(e2, f2)
print(e3, f3)

#[-7, -3]
#[3, -7]

# h = sqrt(b**2 - 0.25(a**2))

# (x1 - x) **2 + (x2 - x)**2 = b

# x = (foil_mid / 4) +/- sqrt((rhs - foil_Constant) - (foil_mid**2 / 4))
