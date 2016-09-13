import requests


def get_url(page):
    url = "http://shopicruit.myshopify.com/products.json?page=" + str(page)
    response = requests.get(url)
    data = response.json()
    return data


def get_total_per_page(data):
    total = 0
    for product in data['products']:
        for variant in product['variants']:
            total += float(variant['price'])
    return total


def get_total(data):
    page = 0
    total_cost = 0
    while True:
        if len(data['products']) != 0:
            page += 1
            data = get_url(page)
            total_cost += get_total_per_page(data)
        else:
            break
    print("Total cost:", round(total_cost, 2))


def main():
    data = get_url(0)
    get_total(data)
    get_total_per_page(data)


if __name__ == '__main__':
    main()

# The total cost of all watches and clocks is $28156.04
