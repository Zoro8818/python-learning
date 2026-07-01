# 原始代码：

order_text = " A:100, B:abc, , C:200, D, E: "

order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0

for order in order_list:
    clean_record = order.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":",1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)
            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
        else:
            invalid_count += 1

print(valid_customer_list)
print(valid_amount_list)
print(invalid_count)