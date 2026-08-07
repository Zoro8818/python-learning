record_list = [
    "营业执照,已上传,25",
    "法人身份证,未上传,8",
    "安全生产许可证,已上传,40",
    "财务报表,上传中,18",
    "授权委托书,已上传,abc",
    "技术方案,,32",
    "项目业绩证明,已上传,55",
    "保密协议,已上传,12",
    "税务证明,已上传,"
]

valid_record_list = []	            #所有有效资料记录列表
uploaded_record_list = []	        #已上传电子版资料列表
not_uploaded_record_list = []	    #未上传电子版资料列表
large_file_list = []	        #文件大小不少于 20MB 的资料列表
small_file_list = []	        #文件大小少于 20MB 的资料列表
invalid_count = 0	            #无效资料数量
total_file_size = 0	            #所有有效资料文件大小总和
highest_file_name = ""
highest_file_size= 0	        #当前最大的文件大小
lowest_file_name = ""
lowest_file_size = 0            #当前最小的文件大小

for record in record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
        continue

    material_name = parts[0].strip()
    upload_status = parts[1].strip()
    size_text = parts[2].strip()

    if (
        material_name == ""
        or upload_status == ""
        or size_text == ""
    ):
        invalid_count += 1
        continue

    if upload_status != "已上传" and upload_status != "未上传":
        invalid_count += 1
        continue

    if not size_text.replace(".", "", 1).isdigit():
        invalid_count += 1
        continue

    file_size = float(size_text)

    cleaned_record = material_name + "," + upload_status + "," + size_text
    valid_record_list.append(cleaned_record)

    total_file_size += file_size

    if len(valid_record_list) == 1:
        highest_file_size = file_size
        highest_file_name = material_name

        lowest_file_size = file_size
        lowest_file_name = material_name

    else:
        if file_size > highest_file_size:
            highest_file_size = file_size
            highest_file_name = material_name

        if file_size < lowest_file_size:
            lowest_file_size = file_size
            lowest_file_name = material_name

    if upload_status == "已上传":
        uploaded_record_list.append(material_name)
    else:
        not_uploaded_record_list.append(material_name)

    if file_size >= 20:
        large_file_list.append(material_name)
    else:
        small_file_list.append(material_name)

print("招投标电子资料上传检查报告")
print("=" * 32)

print("原始记录数量:", len(record_list))
print("有效记录数量:", len(valid_record_list))
print("无效记录数量:", invalid_count)

print()

print("已上传资料数量:", len(uploaded_record_list))
print("未上传资料数量:", len(not_uploaded_record_list))
print("大文件数量:", len(large_file_list))
print("小文件数量:", len(small_file_list))

print()

print("已上传资料:", uploaded_record_list)
print("未上传资料:", not_uploaded_record_list)
print("大文件资料:", large_file_list)
print("小文件资料:", small_file_list)

print()

print("所有有效文件大小总和:", total_file_size, "MB")
print("最大文件:", highest_file_name, highest_file_size, "MB")
print("最小文件:", lowest_file_name, lowest_file_size, "MB")