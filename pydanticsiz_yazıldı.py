class Product:

# burada biz name : str , price:float , in_stock:bool yazsak bile çok bir önemi olmuyor çünkü veri gelirken yine
# istediği gibi gelliyor. bizim ne yazdığımızın çok bir önemi yok


    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock


if __name__ == '__main__' :
    product_ornek = Product(name="ornekt", price="100", in_stock=True)
   # print(product_ornek.in_stock)

    external_data = {
        "name" :" laptop",
        "price" : "999.99",
        "in_stock" : "True"
    }

    product = Product(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock"),
    )

    print(product.name ,"==", type(product.name))
    print(product.price ,"==" ,type(product.price))
    print(product.in_stock , "==", type(product.in_stock))