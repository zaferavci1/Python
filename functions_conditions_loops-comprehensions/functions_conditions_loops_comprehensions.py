# Fonksiyonlar (Functions)

## Fonksiyon Okur-Yazarlığı

#?print # bu ifade bu fonksiyonun neler yaptığını, hangi argümanları kullandığını bize anlatır.

help(print()) # help fonksiyonu da aynı işe yarar.
print("a", "b", sep="__")

## fonksiyon tanımlama

def calculate(x):
    print(x*2)

calculate(5)

## iki argümanlı

def summer(a,b):
    print(a+b)

summer(8,7)
summer(b=10, a=15)

# Docstring : bilgi notu
# docstring 3 bölümden oluşur
#  1- fonksiyonun ne yaptığı
#  2- parametreleri neler
#  3- return'ün ne olacağı
def summer(a,b):
    """
    iki parametreli toplama fonksiyonu
    :param a:int,float

    :param b:int,float

    :return:
    """
    print(a+b)



def calculate(x):
    print(x*2)

# Fonksiyonların Gövde (Statment) Bölümü

# def function_name(parametes/argumans):
#     statemnet(function body)

def say_hi(string):
    print(string)
    print("hello")
    print("hi")

say_hi("merhaba")

def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10,9)

# girilen değerleri bir liste içerisinde saklayacak fonksiyon

list_stor = []

def add_element(a, b):
    list_stor.append((a * b))
    print(list_stor)

add_element(10,3)
add_element(45,8)

# Ön tanımlı argümanlar/parameterler

def divide(a, b):
    print(a / b)

divide(4,2)

def divide(a, b = 1):
    print(a / b)

divide(8)


# En zaman fonksiyon yazılır

# varm moisture charge

# DRY - Don't Repeat Yourself
# kendini tekrar etmemen lazım bu durumdan kendini tekrar etmeye başladığını anladığında fonksiyon yaz


# Retun fonksiyonlar:

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge

type(calculate(10,50,20))


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output =(varm + moisture) / charge
    return varm, moisture, charge, output


type(calculate(10,50,20)) # calculate metodu tuple bir nesne olarak dönüş sağladı

varm, moisture, charge, output = calculate(10,50,20)














