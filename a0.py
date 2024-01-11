user_int = int(input())
num_spaces = 0
for i in range(user_int):
    if i == 0:
        print('+-+')
        print('| |')
        print('+-+-+')
    elif i == (user_int - 1):
        num_spaces = '  ' * (i)
        print(f'{num_spaces}| |')
        print(f'{num_spaces}+-+')
    else:
        num_spaces = '  ' * (i)
        print(f'{num_spaces}| |')
        print(f'{num_spaces}+-+-+')