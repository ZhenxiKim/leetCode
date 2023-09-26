num_list = set(range(1,10001))
create_number = set()

for num in num_list:
    for c in str(num):
        num += int(c)
    create_number.add(num)

answer = sorted(num_list - create_number)

for a in answer:
    print(a)