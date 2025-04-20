from fastapi import FastAPI ,Body # body burada bir database içinde post etmek için kullanıyor amatörce daha çok pydantic kullanıyor.
"""
  ->>> fastapi diyor ki kral sen async kullanmasanda olr ben onu kendim yapıyor zaten diyor.
  ->>>her bir / sonra söylediğimiz şeyler bizim için bir endpointtir yani kemalbaz.com/kursları-göster  kemalbaz.com/kurs-ekle gibi 
  bunların hepsi endpointtir ve bunlar birer fonksiyon olarak tanımlarız.
  ->>>uvicorn main:app --reload cmd satırına yazdığımız bu kod sanki gerçek web sitesinde gibi çalıştıracak bu yazdıklarımzı 
  son sırada bulunan --reload ise bi şey değişirse tekrar tekrar yazdırmaya gerek kalmadan değişiklik olunca direkt çalıştırıyor .
  ->>>kısa kısa notlar : pip freeze neler yüklü hangi kütüphane araç onu gösterir. 
  ->>>eğer ki bizim kendi 127.0.0.1:8000/docs bu şekilde sunucumuza yazarsak bize dosyalarımızı döndürür yani kullandığımız bütün methodları fastapi ile gelir 
  """

app =  FastAPI()


# bu bizim örnek veritabanımızdır sanki böyle bir veritabanımız varmış gibi düşün
courses_db = [
    {'id': '1', 'instructor': 'atil', 'title': 'python', 'category': 'development'},
    {'id': '2', 'instructor': 'musta', 'title': 'java', 'category': 'development'},
    {'id': '3', 'instructor': 'kemal', 'title': 'c', 'category': 'development'},
    {'id': '4', 'instructor': 'cemil', 'title': 'c++', 'category': 'development'},
    {'id': '5', 'instructor': 'zerda', 'title': 'c#', 'category': 'development'},
    {'id': '6', 'instructor': 'gül', 'title': 'js', 'category': 'geliştirici'}
]
@app.get("/") # yani burası kısa kemalbaz.com sitesindeyken gözükmek yapay zekayı açmak istedi biz o zaman kemalbaz.com/yapay-zeka ' ya yönlendirmek için kullanırız bunu
async def hello_world():
        return{"message":"zerda hanm çok güzelsiniz"}


@app.get("/hello") # yani burası kısa kemalbaz.com sitesindeyken gözükmek yapay zekayı açmak istedi biz o zaman kemalbaz.com/yapay-zeka ' ya yönlendirmek için kullanırız bunu
async def hello_world():
        return{"message":"hello world"}


@app.get("/courses") # yani bize courses_db'nin içindeki tüm verileri getirir json formatı ile.
async def get_all():
    return courses_db


# şimdi biz burada yaptıklarımızla sadece database'in hepsini getirdik şimdi ise id=5 olan ya da işte python kursu veren gibi sınıflandırcaz
# bunu ise  PATH , QUERY bu ikisi ile yapıyoruz.

# Burası şu anda PATH parametreleri ile yapıyoruz.

@app.get("/courses/{courses_title}") # burada yazdığımız {} course_title ı değişken olarak getirebilmemizi sağlıyor
async def get_course(courses_title: str):
    for course in courses_db:
        if course.get('title') == courses_title:
            return course


# bu fonksiyon çalışmıyor
@app.get("/courses/{courses_id}") # burada yazdığımız {} course_title ı değişken olarak getirebilmemizi sağlıyor
async def get_courses_id(courses_id: int):
    for course in courses_db:
        if course.get('id') == courses_id:
            return course


# ŞİMDİ BURADA ÇOK ÖNEMLİ BİR ŞEY VAR EĞER AYNI PATH YANİ AYNI YOL ÜZERİNE İKİ ŞEY YAZARSAN ÜSTTEKİNİ ALIR HEP FASTAPI YANİ ALTTAKİNİ ALMAZ
# YANİ BURADA AŞAĞIDAKİ GİBİ PATH YOLUNU DEĞİŞTİRMEMİZ GEREK ÇAKIŞMAMASI İÇİNNNN !!!!


@app.get("/courses/users/{courses_id}") # burada yazdığımız {} course_title ı değişken olarak getirebilmemizi sağlıyor
async def get_courses_id(courses_id: int):
    for course in courses_db:
        if course.get('id') == courses_id:
            return course




# KATEgory == kategory
# BURADA İSE QUERY İLE SORGU YAPILANDIRACAĞIZ

@app.get("/courses/") # yani burada / sonrasına query getirecez ? koyarak bu
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold(): # buradaki casefold ne gelirse hepsini al büyük küçük eşite gibi
            courses_to_return.append(course)
    return courses_to_return


# BURADA İSE ŞİMDİ HEM PATH YOLU İLE HEMDE QUERY İLE YAPACAĞIZ

@app.get("/courses/{instructor}/")
async def get_instructor(instructor: str,category: str): # İF İÇERİSİNE AND İLE İKİ KOŞUL EKLEYEREK İKİLİ KULLANIYORUZ
    courses_to_instructor = []
    for course in courses_db:
        if course.get('instructor').casefold() == instructor.casefold() and course.get('category').casefold() == category.casefold():
            courses_to_instructor.append(course)


    return courses_to_instructor


# POST İŞLEMİ YAPIYORUZ BURADA BASİT BİR KOD İLE

@app.post("/courses/create_courses")
async def create_courses(new_course=Body()): # BURADA KULLANDIĞIMIZ İŞTE YUKARIDA EKLEDİĞİMİZ BODY KÜTÜPHANESİDİR.
    courses_db.append(new_course)



# PUT İŞLEMİ YANİ UPDATE İŞLEMİ YAPIYORUZ BURADA

@app.put("/courses/update_courses")
async def update_courses(update_course=Body()):
    for course in range(len(courses_db)):
        if courses_db[course].get("id") == update_course.get("id"):
            courses_db[course] = update_course


# DELETE İŞLEMLERİMİZİ YAPTIK BURADA 

@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            courses_db.pop(index)
            break


