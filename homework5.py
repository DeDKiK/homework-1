import calculator
import utilities

a = int(input("Введіть число а "))

b = int(input("Введать число b "))

calculator.multiply(a, b)
calculator.add(a, b)
calculator.substract(a, b)
calculator.divide(a, b)


numbers = list(map(int, input("Введіть числа ").split()))

utilities.calculate_avg(numbers)