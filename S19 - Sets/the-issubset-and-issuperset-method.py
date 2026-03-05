a = { 1, 2, 4 }
b = { 1, 2, 3, 4, 5 }

print(a.issubset(b))
print(a < b)
print(a <= b)
print(b.issubset(a))

print(b.issuperset(a))
print(b > a)
print(b >= a)
print(a.issuperset(b))