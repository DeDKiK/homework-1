str_1 = "this is sreing"
int_1 = 1
flt = 1
bul = True

lst = [1, 2, 3]

tpl = (1, 2, 3)

dict = {"key":"value", "man":"is good"}

nope = None 

if int_1 == flt:
    print("good")
    
if "this" in str_1:
    print("yes")
    
print(bul == 4)

num_str = 125
print(str(num_str))

message = 'Hi, my name is Python!'
message.replace('i','1')
redactedMessage = message.replace('y','O')

print(redactedMessage)

split_test = ("This is a splt test")
split_test = split_test.split()
print(split_test)

string_join = " ".join(split_test)
print(string_join)

print(len(string_join))


list_append = [1, 2, 3]
list_extend = [4, 5, 6]

list_append.append(4)
list_append.append(5)
list_extend.extend([7, 8, 9])
print(list_append)
print(list_extend)

print(list_extend.index(6))
print(len(list_append))


dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}

print(dict_test['car'], dict_test['where'])

print(dict_test.keys(), dict_test.values())

print(dict_test.items())

