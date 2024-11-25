passw = "password123"

if passw == "password123":
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")
    
   
day_num = 3
days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

if 1 <= day_num <= 7:
    print(f"День тижня {days[day_num -1]} ")
else:
    print("немає такого дня")
    
numbers = [1,2,3,4,5,6,7,8,9,10]
mlt_by = 2
final =[]

for i in numbers:
    final.append(mlt_by * i)
print(final)

total = 0
for i in numbers:
    total += i
print(total)


fac_num = 8

if fac_num < 0:
    print("Факторіал може бути лише з додатніх чисел")
else:
    factorial = 1
    for i in range(1, fac_num + 1):
        factorial *= i
print(f"Факторіал числа {fac_num} = {factorial}")


even_num = []
for i in range(1, 51):
    if i % 2 == 0:
        even_num.append(i)
print(even_num)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
primes = []
for num in range(1, 51):
    if is_prime(num):
        primes.append(num)
print(f"Прості числа від 1 до 50 {primes}")