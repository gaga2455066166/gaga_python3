float_str = input()
int_str = input()
str_str = input()
print('%.02f' % float(float_str))
print('%e %E %.2f%%' % (float(float_str), float(float_str), float(float_str)*100))
print(bin(int(int_str)).replace('0b', ''), end=" ")
print(hex(int(int_str)).replace('0x', ''))
print(str_str.strip().upper())
print('%20s' % str_str.strip())
str_format = "{str0:*^20s}".format(str0=str_str.strip())
print(str_format)
# print('%f + %d = %f' % (float(float_str), int(int_str), float(float_str) + int(int_str)))
print('{} + {} = {}'.format(float(float_str), int(int_str), float(float_str) + int(int_str)))
