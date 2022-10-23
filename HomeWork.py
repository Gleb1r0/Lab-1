def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


print('Введите коэффицент a,b,c через пробел')
print('a b c')
a, b, c = map(float, input().split())


d = discriminant(a, b, c)
if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print(f'Ответ: x1 = {x1}, x2 = {x2}')
elif d == 0:
    x = -b / 2 * a
    print(f'Ответ: {x}')

else:
    print('Ответ: нет корней')

