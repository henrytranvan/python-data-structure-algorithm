product = {
    "name": "One",
    "weight": 417,
    "cost": 10,
    "price": 1
}

def price_list(products):
    for item in range(0,len(products)):
        products[item]["price"] = products[item]["cost"] / products[item]["weight"]


def greedy(products, weight):
    for item in range(0, len(products)):
        products[item]["selected"] = weight // products[item]["weight"]
        weight -= products[item]["selected"] * products[item]["weight"]

prds = [
    {
        "name": "One",
        "weight": 15,
        "cost": 30,
        "price": 0
    },
    {
        "name": "two",
        "weight": 10,
        "cost": 25,
        "price": 0
    },
    {
        "name": "three",
        "weight": 2,
        "cost": 2,
        "price": 0
    },

    {
        "name": "two",
        "weight": 4,
        "cost": 7,
        "price": 0
    }
]

price_list(prds)

sorted_prds = sorted(prds, key=lambda i: i['price'], reverse=True)

greedy(sorted_prds, 37)

print(sorted_prds)