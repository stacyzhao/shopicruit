import requests


def get_url(page):
    url = "http://shopicruit.myshopify.com/products.json?page=" + str(page)
    response = requests.get(url)
    data = response.json()
    return data


def get_product(data):
    if len(data['products']) != 1:
        return data['products']


def get_total_per_page(data):
    total = 0
    products = data['products']
    for x in products:
        prices = x['variants']
        for y in prices:
            total += float(y['price'])
    return total


def get_total(data):
    page = 0
    total_cost = 0
    while True:
        if len(get_product(data)) != 0:
            page += 1
            data = get_url(page)
            total_cost += get_total_per_page(data)
        else:
            break
    print(round(total_cost, 2))


def main():
    page = 0
    data = get_url(page)
    get_total_per_page(data)
    get_total(data)


if __name__ == '__main__':
    main()
