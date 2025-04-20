import asyncio
# en popüler async kütüphanesi asyncio dur
# fonksiyon yaratırken fast apide arkada çalışan mantık budur öğrenmiş olduk
# async fonksiyonları böyle yapılıyor çalıştırma mantığı aşağıda yazılı

async def fonksiyon_1():
    print ("birinci fonksiyon başladı")
    await asyncio.sleep(5) #non blocking delay simülasyonu çalışsın ama diperlerini etkilemesin diğerleri de çalışsın demektir
    print("birinci fonksiyon bitti")
    return 5

async def fonksiyon_2():
    print("ikinci fonksiyon başladı")
    await asyncio.sleep(10)  # non blocking delay simülasyonu çalışsın ama diperlerini etkilemesin diğerleri de çalışsın demektir
    print("ikinci fonksiyon bitti")
    return 10


  # if __name__ == "__main__":
  #  X = fonksiyon_1()
  #   y = fonksiyon_2()

  #   print(f"1.fonksiyonumuzun döndürüğü değer {X}")
  #   print(f"2.fonksiyonumuz döndürdüğü değer {y}")
  #   async fonksiyonlar bu şekilde çalışmaz bunlar hata verir yani bekleyemedik gibi

async def main():
    task1 = asyncio.create_task(fonksiyon_1())
    task2 = asyncio.create_task(fonksiyon_2())
#async fonksiyonları çalıştırmak için await kullanırsak bunları çalıştırmak içinde bir async fonksiyonu oluşturup orada çalıştırıyoruz ki
#daha kolay yapalım böylelikle çalışır.
#şimdi tam istediğimiz gibi olacak berabr çalışacaklar sonra bekleyecez ve hepsi çalışacak

    x = await task1
    y = await task2

    print(x)
    print(y)

if __name__ == '__main__':
    asyncio.run(main())