import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


def view_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")


def add_to_order(current_order, drink_code, quantity):
    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    current_order.append(
        {
            "code": drink_code,
            "name": DRINK_MENU[drink_code]["name"],
            "price": DRINK_MENU[drink_code]["price"],
            "quantity": quantity
        }
    )

    logging.info(f"Added {quantity} of {drink_code} to order")


def calculate_total(order):
    total = 0

    for item in order:
        total += item["price"] * item["quantity"]

    return total


def view_order(order):
    if not order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print("Mã SP | Tên đồ uống          | Đơn giá  | Số lượng | Thành tiền")
    print("-" * 64)

    for item in order:
        subtotal = item["price"] * item["quantity"]

        print(
            f"{item['code']:<5} | "
            f"{item['name']:<20} | "
            f"{item['price']:,} | "
            f"{item['quantity']:<8} | "
            f"{subtotal:,} VNĐ"
        )

    print("-" * 64)
    print(f"Tổng tiền cần thanh toán: {calculate_total(order):,} VNĐ")


def checkout(order):
    if not order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total(order)

    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).strip().lower()

    if confirm == "y":
        order.clear()
        logging.info("Checkout successful")
        print("Thanh toán thành công.")
        print("Giỏ hàng đã được làm trống.")

    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")

    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")