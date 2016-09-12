import requests


def get_url(page):
    url = "http://shopicruit.myshopify.com/products.json?page=" + str(page)
    response = requests.get(url)
    data = response.json()
    return data


def get_product(data):
    if len(data['products']) != 1:
        print ("len of product ", len(data['products']))
        return data['products']


# def get_total(data):
#     total = 0
#     if len(data['products']) != 1:
#         total = 0
#         # print("return len of items", len(data['products']))
#         for x in range(2):
#             # print(data['products'][0]['variants'][x]['price'])
#             price = data['products'][0]['variants'][x]['price']
#             price = float(price)
#             total += price
#
#         # print(data['products'][0]['variants'][0]['price'])
#             print(round(total, 2))
#     return total

def main():
    
    page = 1
    data = get_url(page)
    invalid = True
    print(get_product(data))
    while invalid:
        if len(get_product(data)) != 0:
            page += 1
            data = get_url(page)
            print("yes")
        else:
            print("no")
            invalid = False



if __name__ == '__main__':
    main()
