# Product-
#     name/title
#     price
#     ratings
#     offer
#     brand
#     inStock
#     customerReviews
#     countryOfOrigin



class Color:
    def __init__(self,name):
        self.name=name


class Manufacturer:
    def __init__(self,manufacturer_name,manufacturer_address,manufacturer_number):
        self.manufacturer_name=manufacturer_name
        self.manufacturer_address=manufacturer_address
        self.manufacturer_number=manufacturer_number

class Image:
    def __init__(self,url):
        self.url=url


class Brand:
    def __init__(self,brand_name,website):
        self.brand_name=brand_name       
        self.website=website



class Category:
    def __init__(self,name,url,description,par_category):
        self.name=name
        self.url=url
        self.description=description
        self.par_category=par_category
    def __str__(self):
        return f"{self.name}  {self.url} {self.description} {self.par_category}"



class Product:
    def __init__(self,name,price,rating,category,brand):
        self.name=name
        self.price=price
        self.rating=rating
        self.category=category
        self.brand=brand

    def __str__(self):
        return f"{self.category}{self.name}{self.price}{self.rating}{self.brand}"
    
    def display(self):   
        list=[self.category.name]    
        for cat in self.category.par_category:
            list.append(cat.name)
            for i in cat.par_category:
                list.append(i.name)        
        print("-".join(list))


def filter_products(leaf,all_products:list):
    for products in all_products:
        if products.category==leaf:
            print(products.name)


def all_products(any_node,all_products:list):
    for product in all_products:
        if any_node==product.category:
            print(product.name)
        else:
            itr=product.category.par_category
            while itr!=[]:
                if any_node==itr[0]:
                    print(product.name)
                itr=itr[0].par_category
                



b1=Brand("hujk","ghjooi.com")

electronics=Category("electronics","abavcca","fghj",[])
furnitures=Category("furnitures","hjhj","hggf",[])

mobile=Category("mobile","ghjk","hghjhjhj",[electronics])
washing_machine=Category("washing_machine1","hjj","hgff",[electronics])

android=Category("android","hjk","hjkl",[mobile])
ios=Category("ios","ghjk","hghjhjhj",[mobile]) 

sofa=Category("sofa","jkk","kjh",[furnitures])


p1=Product("redmi",100000,5,android,[b1]) 
p2=Product("realme",100000,5,android,[b1]) 
p3=Product("ios1",100000,5,ios,[b1]) 
p4=Product("whirlpool",100000,5,washing_machine,[b1]) 
p5=Product("wooden_sofa",100000,5,sofa,[b1]) 

# p1.display()
# filter_products(android,[p1,p2,p3,p4,p5])
all_products(ios,[p1,p2,p3,p4,p5])






    

