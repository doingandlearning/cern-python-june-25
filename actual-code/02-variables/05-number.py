my_float = 3.74
my_int = 314

print(my_float.is_integer())

other_float = 3.0
print(other_float.is_integer())

print(int(my_float))
print(float(my_int))
print(str(my_float))
# print(int("ten"))

1 + 2
1 - 2
1 * 2
print(1 / 2)  # truediv
print(1 // 2)  # int division
print(6 % 2) # modulo 7mod2
print(2**3)  # 2 to the power of 3 (2^3)

none_data = None
print(none_data is None)
print(my_float is None)

test_variable = 12.34

int_part = int(test_variable)
dec_part = test_variable - int_part

print(int_part)
print(dec_part)


del int_part

