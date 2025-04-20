import time
#şimdi burada yapılan şey 2 fonksiyon çalışırken yukarıdan aşağı inen script mantığı fakat bir web sitesi düşün bir tuşa basılınca diğer işlemlerin beklemesi
# pekte doğru olmaz yani ilk fonksiyonun değere 5 saniye de dönerken biz niye 10 saniye bekliyorruz bunun için async kullanacağız.

def my_func_1():
    print("1. fonksyion başlıyor")
    time.sleep(5)
    print("1. fonksiyon bitti ")
    return 5

def my_func_2():
    print("2. fonksyion başlıyor")
    time.sleep(5)
    print("2. fonksiyon bitti ")
    return 10


if __name__ == "__main__":
    X = my_func_1()
    y = my_func_2()


    print(f"1.fonksiyonumuzun döndürüğü değer {X}")
    print(f"2.fonksiyonumuz döndürdüğü değer {y}")



