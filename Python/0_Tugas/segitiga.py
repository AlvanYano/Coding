input_user = 20

for i in range(input_user):
    for j in range(input_user-i):
        print("*", end='')
    if i == input_user-1:
        break
    print()


for i in range(input_user):
    for j in range(i):
        print("*", end='')
    print()

print()

for i in range(input_user):

    if i == 0:
        for j in range(input_user-i):
            print("*", end='')

    elif i > input_user-2:
        for k in range(input_user-i):
            print("*", end='')

    else:
        print("*", end='')
        for k in range(input_user-i-2):
            print(" ", end='')

        print("*", end='')

    print()
