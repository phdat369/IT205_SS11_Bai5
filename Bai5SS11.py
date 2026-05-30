# Phân tích 
# Đề bài yêu cầu chúng ta làm 1 menu gồm có 6 chức năng
# Để làm được menu thì chúng ta cần lặp vòng lặp while và kết thúc khi người dùng nhập 6
# Chức năng đầu tiên là hiển thị danh sách bán hàng 
# Để làm chức năng này thì chúng ta cần duyệt vòng for và in ra các sản phẩm theo đúng định dạng đề bài
# Dùng câu điều kiện để cập nhật trạng thái cho từng sản phẩm 
# Chức năng thứ 2 là bán sản phẩm, đầu tiên yêu cầu người dùng nhập mã sản phẩm và số lượng mua 
# Sau đó chuẩn hóa mã , kiểm tra mã có tồn tại hay không , kiểm tra số lượng mua có vượt qua số lượng trong kho không, tính tiền sau giảm giá nếu sản phẩm đó giảm giá 
# Nếu hợp lệ hết thì trừ số lượng trong kho, tăng số lượng bán, hiển thị tổng tiền cần thanh toán 
# Chức năng thứ 3 là xử lí đổi trả, yêu cầu người dùng nhập mã sản phẩm, số lượng sau 
# Sau đó chuẩn hóa, kiểm tra mã, check số lượng có hợp lệ không, nếu hợp lệ thì bắt đầu làm các thao tác 
# Chức năng 4 là áp dụng giảm giá thì cập nhập mã giảm giá cho sản phẩm người dùng nhập, tối đa 70% 
# Chức năng cuối là nhập thêm vào kho thì yêu cầu người dùng nhập mã sản phẩm và số lượng cần nhập vào kho 
# Sau đó chuẩn hóa và check hợp lệ không, nếu xong hết thì cộng thêm vào kho 

# Viết code 

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")
    choice = input("Nhập lựa chọn: ").strip()
    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")
                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(
                        f"{index}. Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Đổi trả: {product['returned']} | "
                        f"Giảm giá: {product['discount']}% | "
                        f"Trạng thái: {status}"
                    )
        case "2":
            product_id = input(
                "Nhập mã sản phẩm khách muốn mua: "
            ).strip().upper()
            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break
            if product_found is None:
                print("Không tìm thấy sản phẩm cần bán")
                continue
            quantity_buy = input(
                "Nhập số lượng khách mua: "
            ).strip()
            if not quantity_buy.isdigit() or int(quantity_buy) <= 0:
                print("Số lượng mua không hợp lệ")
                continue
            quantity_buy = int(quantity_buy)
            if quantity_buy > product_found["quantity"]:
                print("Số lượng trong kho không đủ để bán")
                continue
            sale_price = (
                product_found["price"]
                * (100 - product_found["discount"])
                / 100
            )
            total_money = sale_price * quantity_buy
            product_found["quantity"] -= quantity_buy
            product_found["sold"] += quantity_buy
            print("Bán hàng thành công")
            print(f"Tổng tiền khách cần thanh toán: {total_money:.0f}")
        case "3":
            product_id = input(
                "Nhập mã sản phẩm khách muốn đổi/trả: "
            ).strip().upper()
            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break
            if product_found is None:
                print("Không tìm thấy sản phẩm cần đổi trả")
                continue
            quantity_return = input(
                "Nhập số lượng đổi/trả: "
            ).strip()
            if not quantity_return.isdigit() or int(quantity_return) <= 0:
                print("Số lượng đổi/trả không hợp lệ")
                continue
            quantity_return = int(quantity_return)
            if quantity_return > product_found["sold"]:
                print(
                    "Số lượng đổi/trả không được vượt quá số lượng đã bán"
                )
                continue
            refund_price = (
                product_found["price"]
                * (100 - product_found["discount"])
                / 100
            )
            refund_money = refund_price * quantity_return
            product_found["sold"] -= quantity_return
            product_found["quantity"] += quantity_return
            product_found["returned"] += quantity_return
            print("Xử lý đổi trả thành công")
            print(f"Số tiền hoàn lại: {refund_money:.0f}")
        case "4":
            product_id = input(
                "Nhập mã sản phẩm cần áp dụng giảm giá: "
            ).strip().upper()
            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break
            if product_found is None:
                print("Không tìm thấy sản phẩm")
                continue
            discount = input(
                "Nhập phần trăm giảm giá: "
            ).strip()
            if not discount.isdigit():
                print("Phần trăm giảm giá không hợp lệ")
                continue
            discount = int(discount)
            if discount < 0 or discount > 70:
                print("Phần trăm giảm giá không hợp lệ")
                continue
            product_found["discount"] = discount
            print("Cập nhật giảm giá thành công")
        case "5":
            product_id = input(
                "Nhập mã sản phẩm cần nhập thêm: "
            ).strip().upper()
            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break
            if product_found is None:
                print("Không tìm thấy sản phẩm cần nhập kho")
                continue
            quantity_import = input(
                "Nhập số lượng nhập thêm: "
            ).strip()
            if not quantity_import.isdigit() or int(quantity_import) <= 0:
                print("Số lượng nhập kho không hợp lệ")
                continue
            quantity_import = int(quantity_import)
            product_found["quantity"] += quantity_import
            print("Nhập kho thành công")
            print(f"Tồn kho mới: {product_found['quantity']}")
        case "6":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")