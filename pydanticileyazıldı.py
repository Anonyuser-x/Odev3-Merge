from pydantic import BaseModel

# burada pydantic ile gelen veriyi istediğimiz şeylere çevirdik yani veri gelirken eğer --"name str'ye"--"price float'a"--"in_stock bool'e"-- dönmeseydi
# gelen veriyi doğru kabul etmeyecekti döndürebildiği için gelen verileri alıp döndürüğ değerleri öyle girdi.


class  Productpydantic(BaseModel):
    name : str
    price : float
    in_stock : bool



if __name__ == '__main__' :
    product_ornek = Productpydantic(name="ornekt", price="100", in_stock=True)
   # print(product_ornek.in_stock)

    external_data = {
        "name" :" laptop",
        "price" : "999.99",
        "in_stock" : "True"
    }

    product = Productpydantic(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock"),
    )

    print(product.name ,"==", type(product.name))
    print(product.price ,"==" ,type(product.price))
    print(product.in_stock , "==", type(product.in_stock))