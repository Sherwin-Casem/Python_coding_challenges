import cmath

z = complex(input())

# modulus (r)
r = abs(z)

# phase (phi)
phi = cmath.phase(z)

print(r)
print(phi)
