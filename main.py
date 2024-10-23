import string
import keyword

#task 5/1
'''smina = input("ведіть зміну")
if smina in keyword.kwlist:
    print("False")
elif smina.isupper() or smina in string.whitespace or (smina in string.punctuation and smina != '_'):
    print("False")
elif smina.count("_") > 1:
    print ("False")
elif smina[0].isdigit():
    print("False")
else: print("True")
#task 5/2
 #while True:

    operation = input("Якщо потрібно рахувати, введіть 'Yes', якщо ні — інше: ")
    lower_operation = operation.lower()
    if lower_operation not in ['yes', 'y']:
        print("Exit")
        break
    num_one = int(input("Введіть перше число: "))
    num_two = int(input("Введіть друге число: "))
    num_oper = input("Введіть операцію ('+', '-', '*', '/'): ")
    if num_oper == '+':
        res = num_one + num_two
        print(f"Результат: {res}")
    elif num_oper == '-':
        res = num_one - num_two
        print(f"Результат: {res}")
    elif num_oper == '*':
        res = num_one * num_two
        print(f"Результат: {res}")
    elif num_oper == '/':
        if num_two != 0:
            res = num_one / num_two
            print(f"Результат: {res}")
        else:
            print("Помилка: Ділення на нуль!")
    else:
        print("Помилка: Невірна операція.")'''
 # task 5.3
hashtag = str(input("ведіть слово для hashtag: "))
cleaned_words = []
for word in hashtag.split():
    cleaned_word = ''.join(char for char in word if char not in string.punctuation)
    cleaned_words.append(cleaned_word)
hashtag = '#' + ''.join(word.capitalize() for word in cleaned_words if word)
print(hashtag)







