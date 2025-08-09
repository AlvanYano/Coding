str_in = input()

new_str = []

for i in range(len(str_in)):
    new_str.append(str_in[-(i+1)])

hasil = ''.join(new_str)
