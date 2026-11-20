
menu = {
    "coffee": 250000,
    "tea": 150000,
    "cake": 300000
}


def show_menu():

    print("\n========== Coffee Menu ==========")

    for product, price in menu.items():
        print(f"{product:<15} : {price:,} تومان")

    print("=================================")
