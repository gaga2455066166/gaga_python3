def check_id_data(n):
    var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    var_id = ['1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2']
    n = str(n)
    sum = 0
    for i in range(0, 17):
        sum += int(n[i]) * var[i]
    sum %= 11
    print(var_id[sum])


a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = input().split()
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = eval(a), eval(b), eval(c), eval(d), eval(e), eval(f), eval(g), eval(
    h), eval(i), eval(j), eval(k), eval(l), eval(m), eval(n), eval(o), eval(p), eval(q)
n = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j) + str(k) + str(l) + str(
    m) + str(n) + str(o) + str(p) + str(q)

check_id_data(n)
