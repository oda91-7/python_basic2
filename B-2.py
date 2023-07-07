max_row = int(input("行数を入力してください: "))
max_col = int(input("列数を入力してください: "))

# list = [1, 2, 3, 4, 5, 6]
# list2 = [1, 2, 3, 4]

for kuku_1 in range(1, max_row + 1):
    for kuku_2 in range(1, max_col + 1):
        print(f"{kuku_1 * kuku_2}", end = " ")
    print()