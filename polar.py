#how to obtain modulus and phase angle of an input complex number
import cmath
c = input('Enter your complex number')
z = complex(c)
print(z)
a = cmath.phase(z)
m = abs(z)
print('modulus={}'.format(m))
print('phase angle={}'.format(a))


