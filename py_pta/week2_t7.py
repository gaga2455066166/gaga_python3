a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = input().split(" ")
# print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
a0 = int(a)
b0 = int(b)
c0 = int(c)
d0 = int(d)
e0 = int(e)
f0 = int(f)
g0 = int(g)
h0 = int(h)
i0 = int(i)
j0 = int(j)
k0 = int(k)
l0 = int(l)
m0 = int(m)
n0 = int(n)
o0 = int(o)
p0 = int(p)
q0 = int(q)
# 7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2。
total0 = a0 * 7 + b0 * 9 + c0 * 10 + d0 * 5 + e0 * 8 + f0 * 4 + g0 * 2 + h0 * 1 \
         + i0 * 6 + j0 * 3 + k0 * 7 + l0 * 9 + m0 * 10 + n0 * 5 + o0 * 8 + p0 * 4 + q0 * 2
# print(total0)
remainder = total0 % 11
check = (12 - remainder) % 11
print(check)
