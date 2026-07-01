consume_text = " 张三:1500, 李四:0, 王五:300, , 赵六:abc, 钱七:800, 错误数据, :200, 孙八: "

consume_list = consume_text.split(",")

high_consume_customer_list = []
normal_consume_customer_list = []
zero_consume_customer_list = []

high_consume_count = 0
normal_consume_count = 0
zero_consume_count = 0
for record in consume_list:
   clean_record = record.strip()

   if clean_record == "":
        continue
   elif ":" not in clean_record:
      continue
   else:
      parts = clean_record.split(":", 1)
      customer = parts[0].strip()
      amount_text_item = parts[1].strip()

      if customer == "" or amount_text_item == "":
         continue
      elif amount_text_item.replace(".", "", 1).isdigit():
         amount = float(amount_text_item)

         if amount >= 1000:
            high_consume_customer_list.append(customer)
            high_consume_count += 1
         elif amount > 0:
            normal_consume_customer_list.append(customer)
            normal_consume_count += 1
         else:
            zero_consume_customer_list.append(customer)
            zero_consume_count += 1
      else:
         continue

print("高消费客户列表: ", high_consume_customer_list)
print("高消费客户数量: ", high_consume_count)
print("普通消费客户列表: ", normal_consume_customer_list)
print("普通消费客户数量: ", normal_consume_count)
print("零消费客户列表: ", zero_consume_customer_list)
print("零消费客户数量: ", zero_consume_count)



