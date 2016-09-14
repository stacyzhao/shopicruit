import requests


def get_data(page):
    url = "http://shopicruit.myshopify.com/products.json?page=" + str(page)
    response = requests.get(url)
    return response.json()


def get_total_per_page(data):
    total = 0
    for product in data["products"]:
        if product["product_type"].lower() == "watch" or product["product_type"].lower() == "clock":
            for variant in product["variants"]:
                total += float(variant["price"])
    return total


def main():
    page = 1
    total_cost = 0
    while True:
        data = get_data(page)
        # we don't know if there are more pages so check to see if this result is empty
        if len(data["products"]) == 0:
            break

        total_cost += get_total_per_page(data)
        page += 1
    print("Total cost: {}".format(round(total_cost, 2)))


if __name__ == "__main__":
    main()
