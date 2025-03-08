a = [1, 2, 3]
b = a  # b trỏ cùng địa chỉ với a

print(id(a))  # In địa chỉ bộ nhớ của a
print(id(b))  # In địa chỉ bộ nhớ của b (sẽ giống với id(a))

print(a)
print(b)

b[1]= 4
print(a)
print(b)

c = tuple()