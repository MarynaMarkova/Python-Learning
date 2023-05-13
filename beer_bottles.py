num = 99

while num > 0:
    if num == 1:
        print(f"{num} bottle of beer on the wall.")
        print(f"{num} bottle of beer.")
        print("Take one down, pass it around,")
        print("no more bottles of beer on the wall.")
        print("=" * 20)
    else:
        print(f"{num} bottles of beer on the wall.")
        print(f"{num} bottles of beer.")
        print("Take one down, pass it around,")
        if num != 2:
            print(f"{num-1} bottles of beer on the wall.")
        else:
            print(f"{num-1} bottle of beer on the wall.")
        print("*" * 20)
    num -= 1

# for num in range(99, 0, -1):
#     print(f"{num} bottles of beer on the wall.")
#     print(f"{num} bottles of beer.")
#     print("Take one down, pass it around,")
#     if num == 1:
#         print("no more bottles of beer on the wall.")
#         print("=" * 20)
#     else:
#         print(f"{num-1} bottles of beer on the wall.")
#         print("*" * 20)
