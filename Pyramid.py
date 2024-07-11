
print("give bottom length of pyramid: ")
usr_str = input()
x = int(usr_str) + 1

for i in range(1, x, 2):
    for j in range((x-i) // 2):
        print(" ", end = "")
    for k in range(i):
        print("*", end = "")
    print("")