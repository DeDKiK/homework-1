lst = [1,2,3]
lst.append(10)
lst.append(20)
print(lst)
lst.pop(3)
print(lst)


print(sum(lst))


doubled_lst =[]

for i in lst:
    doubled_lst.extend([i, i])
print(doubled_lst)


fruits = (("яблуко", "банан", "апельсин"))

for i in fruits:
    print(i)
    
num_tpl = ((1,2,3))
num_tpl1 = ((4,5,6))

num_tpl2 = num_tpl + num_tpl1
print(num_tpl2)


sport_dict={
    "name":"Aboba",
    "age": "42",
    "team": "cool"
}
print(sport_dict)

book_dict={
    "name":"Harry Shproter",
    "age" : 2034
}

book_dict.update({"newBook":"Harry ne Shprehae","newBookAge":2035})
print(book_dict)


countries_and_capitals = {
    "Україна": "Київ",
    "США": "Вашингтон",
    "Франція": "Париж",
    "Німеччина": "Берлін",
    "Італія": "Рим",
    "Японія": "Токіо"
}

country = input("Введіть назву країни: ")

if country in countries_and_capitals:
    print(f"Столиця {country}: {countries_and_capitals[country]}")
else:
    print(False)