#!/usr/bin/env python3

import hashlib

# Set up data
x1 = bytes.fromhex(''.join('01' for i in range(16)))
x2 = bytes.fromhex(''.join('02' for i in range(16)))
x3 = bytes.fromhex(''.join('03' for i in range(16)))
x4 = bytes.fromhex(''.join('04' for i in range(16)))
x5 = bytes.fromhex(''.join('05' for i in range(16)))
x6 = bytes.fromhex(''.join('06' for i in range(16)))
x7 = bytes.fromhex(''.join('07' for i in range(16)))
x8 = bytes.fromhex(''.join('08' for i in range(16)))

# Make hashes
md5 = hashlib.md5(); md5.update(x1);  y1 = md5.digest()
md5 = hashlib.md5(); md5.update(x2);  y2 = md5.digest()
md5 = hashlib.md5(); md5.update(x3);  y3 = md5.digest()
md5 = hashlib.md5(); md5.update(x4);  y4 = md5.digest()
md5 = hashlib.md5(); md5.update(x5);  y5 = md5.digest()
md5 = hashlib.md5(); md5.update(x6);  y6 = md5.digest()
md5 = hashlib.md5(); md5.update(x7);  y7 = md5.digest()
md5 = hashlib.md5(); md5.update(x8);  y8 = md5.digest()

md5 = hashlib.md5(); md5.update(y1);  md5.update(y2)
y9  = md5.digest()
md5 = hashlib.md5(); md5.update(y3);  md5.update(y4)
y10 = md5.digest()
md5 = hashlib.md5(); md5.update(y5);  md5.update(y6)
y11 = md5.digest()
md5 = hashlib.md5(); md5.update(y7);  md5.update(y8)
y12 = md5.digest()

md5 = hashlib.md5(); md5.update(y9);  md5.update(y10)
y13 = md5.digest()
md5 = hashlib.md5(); md5.update(y11); md5.update(y12)
y14 = md5.digest()

md5 = hashlib.md5(); md5.update(y13); md5.update(y14)
y15 = md5.digest()

print("3-Layer MD5 Merkle Tree")
print("#"*72)
print()
print("Data")
print()
print('x1 = %s' % (x1.hex()))
print('x2 = %s' % (x2.hex()))
print('x3 = %s' % (x3.hex()))
print('x4 = %s' % (x4.hex()))
print('x5 = %s' % (x5.hex()))
print('x6 = %s' % (x6.hex()))
print('x7 = %s' % (x7.hex()))
print('x8 = %s' % (x8.hex()))
print()
print()

print("Merkle Tree")
print()
print('y1  = md5(x1)')
print('    = %s' % (y1.hex()))
print('y2  = md5(x2)')
print('    = %s' % (y2.hex()))
print('y3  = md5(x3)')
print('    = %s' % (y3.hex()))
print('y4  = md5(x4)')
print('    = %s' % (y4.hex()))
print('y5  = md5(x5)')
print('    = %s' % (y5.hex()))
print('y6  = md5(x6)')
print('    = %s' % (y6.hex()))
print('y7  = md5(x7)')
print('    = %s' % (y7.hex()))
print('y8  = md5(x8)')
print('    = %s' % (y8.hex()))
print()

print('y9  = md5(y1 ||y2 )')
print('    = %s' % (y9.hex()))
print('y10 = md5(y3 ||y4 )')
print('    = %s' % (y10.hex()))
print('y11 = md5(y5 ||y6 )')
print('    = %s' % (y11.hex()))
print('y12 = md5(y7 ||y8 )')
print('    = %s' % (y12.hex()))
print()

print('y13 = md5(y9 ||y10)')
print('    = %s' % (y13.hex()))
print('y14 = md5(y11||y12)')
print('    = %s' % (y14.hex()))
print()

print('y15 = md5(y13||y14)')
print('    = %s' % (y15.hex()))
print()