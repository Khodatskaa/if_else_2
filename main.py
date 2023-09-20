x = int(input('Enter seconds: '))

if 0 < x < 86400:
    remaining_s = 86400 - x
    h = remaining_s // 3600
    m = (remaining_s % 3600) // 60
    s = (remaining_s % 3600) % 60
    print(f"Left until midnight: {h} hours {m} minutes {s} seconds")
elif x == 86400:
    print('It is midnight')
else:
    print('Unknown operation number')
