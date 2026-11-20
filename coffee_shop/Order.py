
from Menu import menu



orders = []


def add_order():

    product = input("نام محصول را وارد کنید: ").strip().lower()


    if product not in menu:
        print("این محصول در منوی کافه وجود ندارد!")
        return


    try:
        quantity = int(input("تعداد مورد نظر را وارد کنید: "))

        if quantity <= 0:
            print("تعداد باید بیشتر از صفر باشد!")
            return

    except ValueError:
        print("لطفا تعداد را به صورت عدد صحیح وارد کنید!")
        return

    
    order = {
        "name": product,
        "price": menu[product],
        "quantity": quantity
    }

    orders.append(order)

    print("سفارش با موفقیت ثبت شد.")

def show_orders():

    if not orders:
        print("هنوز هیچ سفارشی ثبت نشده است.")
        return

    print("\n========== Registered Orders ==========")

    for index, order in enumerate(orders, start=1):

        print(f"\nسفارش شماره {index}")
        print(f"نام محصول: {order['name']}")
        print(f"قیمت واحد: {order['price']:,} تومان")
        print(f"تعداد: {order['quantity']}")
        print("-" * 35)
