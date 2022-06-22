from bottle import request
from bs4 import BeautifulSoup
import requests
from django.contrib.auth.models import User

from price_app import models
from price_app.models import Wish_List, Amazon_Wish, Wish_list_values

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def flipkart(id1,name):
    price = '0'
    title = ""
    url = "https://www.flipkart.com"
    image = ""
    f_rating = ""

    try:
        # global flipkart
        name1 = name.replace(" ", "+")  # iphone x  -> iphone+x
        res = requests.get(f'https://www.flipkart.com/search?q={name1}', headers=headers)

        print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text, 'html.parser')
        div_type_1 = soup.find_all('div', attrs={'class': '_4ddWXP'})
        div_type_2 = soup.find_all('div', attrs={'class': '_2kHMtA'})

        if len(div_type_1) > 1:
            # New Class For Product Name
            print("div_type_1")
            for i in range(0, len(soup.select('.s1Q9rs'))):
                title = soup.select('.s1Q9rs')[i].getText().strip()
                title = title.upper()
                if name.upper() in title:
                    # New Class For Product Price
                    price = soup.select('._30jeq3')[i].getText().strip()
                    title = soup.select('.s1Q9rs')[i].getText().strip().upper()
                    url += soup.select('.s1Q9rs')[i]['href'].strip()
                    image = soup.select('._396cs4')[i + 1]['src'].strip()
                    # if image.find("placeholder_fcebae.svg") != -1:
                    #     image = "https:" + image
                    #     print(image)
                    site="Flipkart"
                    f_rating=soup.select('._3LWZlK')[0].getText().strip() + ' out of 5 stars'
                    print("Flipkart:")
                    print(title)
                    print(price)
                    print(image)
                    print(url)
                    # id1= models.User.objects.get(id=self.request.user.id)
                    # id2=id1.id
                    print(id1)
                    print(f_rating)
                    print("-----------------------")
                    flipkart_values(title,price,image,id1)
                    wish_list(title,price,image,id1,site)

                    break
                else:
                    print("Flipkart:No product 1 found!")
                    print("-----------------------")
                    title = "No product"
                    price = '-'

        elif len(div_type_2) > 1:
            print("div_type_2")
            for i in range(0, len(soup.select('._4rR01T'))):
                title = soup.select('._4rR01T')[i].getText().strip()
                title = title.upper()
                if name.upper() in title:
                    # New Class For Product Price
                    price = soup.select('._30jeq3')[i].getText().strip()
                    title = soup.select('._4rR01T')[i].getText().strip().upper()
                    url += soup.select('._1fQZEK')[i]['href'].strip()
                    image = soup.select('._396cs4')[i + 1]['src'].strip()
                    site="Flipkart"
                    f_rating=soup.select('._3LWZlK')[0].getText().strip() + ' out of 5 stars'
                    # id1= models.User.objects.get(id=self.request.user.id)
                    # id2=id1.id
                    print("Flipkart:")
                    print(title)
                    print(price)
                    print(image)
                    print(id1)
                    print(url)
                    print(f_rating)
                    print("-----------------------")
                    flipkart_values(title,price,image,id1)
                    wish_list(title,price,image,id1,site)
                    break
                else:
                    print("Flipkart:No product 2 found")
                    print("-----------------------")
                    title = "No product found"
                    price = '-'
        else:
            print("Flipkart:No product 3 found!")
            print("-----------------------")
            title = "No product found"
            price = '-'

    except:
        print("Flipkart:No product 4 found!")
        print("-----------------------")
        title = "No product1 "
        price = '0'

    product = {"title": title, "price": price, "url": url, "image": image,"id1": id1,"f_rating":f_rating, "site": "Flipkart"}
    return product


def amazon(id1,name):
    title = ""
    url = "https://www.amazon.in"
    price = "0"
    image = ""
    f_rating = ""
    # try:
    # global amazon
    name1 = name.replace(" ", "-")
    name2 = name.replace(" ", "+")
    res = requests.get(f'https://www.amazon.in/s?k={name2}', headers=headers)
    print("\nSearching in amazon:")
    soup = BeautifulSoup(res.text, 'html.parser')
    title_list = soup.select('.a-color-base.a-text-normal')
    # print(title_list)
    amazon_page_length = int(len(title_list))
    # print(amazon_page_length)
    for i in range(0, amazon_page_length):
        name = name.upper()
        title = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
        if name in title:
            title = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            price = "₹" + soup.select('.a-price-whole')[i].getText().strip()
            url += soup.select(".a-link-normal.a-text-normal")[i]['href'].strip()
            image = soup.select("div.a-section.aok-relative.s-image-fixed-height img")[i]['src'].strip()
            site = "Amazon"
            f_rating = soup.select('.a-icon-alt')[4].getText()
            print("Amazon:")
            print(title)
            print(price)
            print(url)
            print(image)
            print(f_rating)
            print("-----------------------")
            amazon_values(title,price,image,id1)
            wish_list(title,price,image,id1,site)

            break
        else:
            i += 1
            i = int(i)
            if i == amazon_page_length:
                print("amazon : No product found!")
                print("-----------------------")
                title = "No product found"
                price = '-'
                break
    # product = {"title": title, "price": price, "url": url, "image": image, "site": "Amazon"}
    # return product

    # except:
    #     print("amazon: No product found!")
    #     print("-----------------------")
    #     title = "No product found"
    #     price = '-'
    product = {"title": title, "price": price, "url": url, "image": image,"id1":id1,"f_rating":f_rating, "site": "Amazon"}
    return product


def convert(a):
    b = a.replace(" ", '')
    c = b.replace("INR", '')
    d = c.replace(",", '')
    f = d.replace("₹", '')
    g = int(float(f))
    return g


def price_comp(id1,search_string):
    filpkart_product = flipkart(id1,search_string)
    amazon_product = amazon(id1,search_string)

    if filpkart_product["price"] == '-':
        print("No product found!")
    else:
        print("\nFlipkart Price:", filpkart_product)
    if amazon_product["price"] == '-':
        print("No Product found!")
    else:
        print("\nAmazon price:", amazon_product)

    return {
        "Amazon": filpkart_product,
        "Flipkart": amazon_product,
    }


def flipkart_values(title, price, image,id1):
    wish= Wish_List()
    wish.title = title
    wish.price= price
    wish.image = image
    wish.user_id=id1
    print(title)
    print(price)
    print(id1)
    wish.save()
    return 'user/result.html'

def amazon_values(title,price,image,id1):

    amazon= Amazon_Wish()
    # amazon.user= user
    amazon.title = title
    amazon.price= price
    amazon.image = image
    amazon.user_id=id1
    amazon.save()
    return 'user/result.html'

def wish_list(title,price,image,id1,site):
    wish_lis= Wish_list_values()
    wish_lis.title= title
    wish_lis.price= price
    wish_lis.image = image
    wish_lis.user_id= id1
    wish_lis.site = site
    wish_lis.save()
    return 'user/result.html'

