while True:
    a = int(input("Введите натуральное число"))
    if a < 1:
        print("Вы ввели неккоректные данные. Попробуйте еще раз.")
    else : break
kol = 0
temp = a
while temp > 0 :
    temp = temp // 10
    kol = kol + 1
temp = a
i = 0
while i < kol :
    mas[i] = temp // 10 ** (kol - i + 1)
    temp %= 10 ** (kol - i + 1)
    # 345 3