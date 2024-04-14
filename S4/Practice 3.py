# برنامه‌ای بنویسید که از کاربر اعداد را به صورت دلخواه دریافت می‌کند تا زمانی که کاربر عبارت 
# "end" را وارد کند.
# سپس از میان اعداد وارد شده، یک عدد را به صورت تصادفی انتخاب و چاپ کند.

#توضیحات بیشتر در این لینک
#https://docs.google.com/document/d/1Gw61Vmq8zaSRiAG14WMSpJt5QR_oCwTMmQJdc2ZDD6o/edit?usp=sharing
# ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※         


import random

def add_numbers_to_list():
    """
    این تابع از کاربر اعداد را به صورت دلخواه دریافت می‌کند و در یک لیست ذخیره می‌کند.
    تا زمانی که کاربر عبارت "end" را وارد کند، فرایند دریافت عدد ادامه پیدا می‌کند.
    """
    numbers_list = []  # لیستی برای ذخیره اعداد ورودی ایجاد می‌شود
    while True:
        number_input = input("Enter a number (type 'end' to finish): ")  # دریافت عدد از کاربر
        if number_input.lower() == 'end':  # بررسی اینکه آیا کاربر عبارت "end" را وارد کرده است
            break  # اگر کاربر عبارت "end" را وارد کرده باشد، از حلقه خارج می‌شویم
        try:
            number = int(number_input)  # تبدیل عدد ورودی به عدد صحیح
            numbers_list.append(number)  # اضافه کردن عدد به لیست
        except ValueError:
            print("Invalid input! Please enter a valid number or 'end' to finish.")  # پیام خطا در صورت ورودی نامعتبر
    return numbers_list  # لیست اعداد را برمی‌گرداند

def get_random_element_from_list(numbers_list):
    """
    این تابع از میان لیست اعداد، یک عدد را به صورت تصادفی انتخاب و برمی‌گرداند.
    اگر لیست خالی باشد، پیامی مبنی بر خالی بودن لیست چاپ می‌کند و None را برمی‌گرداند.
    """
    if not numbers_list:  # بررسی اینکه آیا لیست خالی است
        print("The list is empty!")  # پیام چاپ در صورت خالی بودن لیست
        return None  # مقدار None را برمی‌گرداند
    random_index = random.randint(0, len(numbers_list) - 1)  # انتخاب یک عدد تصادفی از بین شاخص‌های لیست
    return numbers_list[random_index]  # عدد تصادفی انتخاب شده را برمی‌گرداند

numbers = add_numbers_to_list()  # فراخوانی تابع add_numbers_to_list برای دریافت اعداد از کاربر
random_element = get_random_element_from_list(numbers)  # فراخوانی تابع get_random_element_from_list برای انتخاب عدد تصادفی
print("Random element from the list:", random_element)  # چاپ عدد تصادفی انتخاب شده
