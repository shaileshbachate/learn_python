print(round(54.3956), round(54.965), round(24.50), round(25.50))
print("------------------------------------------------------------------------")

a = 78.3421
b = 78.3481
c = 78.3451
d = 78.3450
e = 78.402

print(round(a, 2), round(b, 2), round(c, 2), round(d, 2), round(e, 2))  # 78.4
print("{0:.2f}".format(a), "{0:.2f}".format(b), "{0:.2f}".format(c), "{0:.2f}".format(d), "{0:.2f}".format(e))
print('%.2f' % a, '%.2f' % b, '%.2f' % c, '%.2f' % d, '%.2f' % e)

print("------------------------------------------------------------------------")

x = 34.5796
print(round(x, 2), round(78.3956, 2))
print("{:.2f}".format(x), "{:.2f}".format(78.3956), "{0:.2f}".format(78.3956))
print("%.2f"%x, "%.2f"% 78.3956)

print("------------------------------------------------------------------------")

import math
print(math.floor(78.39))    # 78
print(math.ceil(78.39))     # 79
# math.trunc() eliminates the decimal part and returns integer
print(math.trunc(78.39))    # 78
print(math.trunc(78.89))    # 78
