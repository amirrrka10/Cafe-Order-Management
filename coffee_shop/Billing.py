
from Order import orders



def calculate_total():

    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total



def calculate_discount(total):

    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount



def print_invoice():

    if not orders:
        print("هنوز هیچ سفارشی ثبت نشده است.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_price = total - discount

    print("\n========== Coffee Shop Invoice ==========")

    for order in orders:

        product_total = order["price"] * order["quantity"]

        print(f"\nمحصول: {order['name']}")
        print(f"تعداد: {order['quantity']}")
        print(f"قیمت واحد: {order['price']:,} تومان")
        print(f"مبلغ: {product_total:,} تومان")

    print("\n-----------------------------------------")
    print(f"مبلغ کل: {total:,} تومان")
    print(f"مقدار تخفیف: {discount:,.0f} تومان")
    print(f"مبلغ نهایی: {final_price:,.0f} تومان")
    print("=========================================")
