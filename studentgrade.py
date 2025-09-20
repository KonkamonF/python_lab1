def print_mult_table(a, b):
    for i in range(a, b+1):
        for j in range(1, 13):
            if (i * j) % 2 == 0:
                print(f"{i} x {j} = {i*j}")

students = [
    {'name': 'Ploy', 'grade': 'A'},
    {'name': 'Ploy1', 'grade': 'B'},
    {'name': 'Ploy2', 'grade': 'A'},
    {'name': 'Ploy3', 'grade': 'A'}
]
print(students)
for s in students:
 if s["grade"] == "A":
   print(s["name"])

count = sum(1 for s in students if s["grade"] == "A")
print("นักเรียนที่ได้ A มี", count,"คน")
