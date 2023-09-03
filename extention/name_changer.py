import os, random, time


def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_user_img_path(instance, filename):
    file_time = time.localtime()
    name, ext = get_file_name_ext(filename)
    random_num = random.randint(0,99999999999999999)
    final_name = f"{file_time.tm_year}-{file_time.tm_mon}-{file_time.tm_mday}-{random_num}{ext}"

    return f"users/{final_name}"
