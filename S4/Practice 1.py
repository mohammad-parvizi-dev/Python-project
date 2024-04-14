# 1. جریمه‌های مربوط به هر کد تخلف را ثبت کنید.
# در این برنامه، شما به عنوان مسئول پارکینگ، وظیفه دارید جریمه‌های مربوط به هر کد تخلف را ثبت کنید.
# برای انجام این کار، باید از رانندگان کد تخلف و مبلغ جریمه را دریافت کنید.
# 2. جریمه مربوط به یک کد تخلف خاص را برای یک ماشین مشخص محاسبه کنید.
# پس از ثبت جریمه‌ها،
# این برنامه به شما امکان می‌دهد تا جریمه مربوط به یک کد تخلف خاص را برای یک ماشین مشخص محاسبه کنید.
# 3. نام ماشین را وارد کنید.
# این تابع نام ماشین را از کاربر دریافت می‌کند.
# 4. برنامه اصلی
# این تابع وظیفه اصلی برنامه را بر عهده دارد. در این تابع، ابتدا جریمه‌ها از کاربر دریافت و ذخیره می‌شوند. سپس، از کاربر خواسته می‌شود تا نام ماشین و کد تخلف مورد نظر را وارد کند. در نهایت، جریمه مربوط به آن کد تخلف برای آن ماشین محاسبه و چاپ می‌شود.


#توضیحات بیشتر در این لینک
#https://docs.google.com/document/d/1CqTEttKK7x8pnQU5ZhWwzNoyUTl2RebTGKGjKLDZMbs/edit?usp=sharing
# ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※         
def get_penalty_codes():
    """
    این تابع کدهای جریمه را به همراه مبلغ جریمه آنها از کاربر دریافت می کند و در یک دیکشنری ذخیره می کند.

    ورودی:
        هیچ

    خروجی:
        دیکشنری حاوی کدهای جریمه به عنوان کلید و مبالغ جریمه به عنوان مقادیر
    """
    codes = {}  # دیکشنری برای ذخیره کدها و جریمه ها
    while True:
        code = input("Please enter the code or type 'end': ")  # دریافت کد جریمه از کاربر
        if code == "end":  # بررسی شرط خروج از حلقه
            break
        elif code in codes:  # بررسی تکراری بودن کد جریمه
            print("***This code is duplicated. Please enter another code.***")
        else:
            try:  # تبدیل مقدار ورودی جریمه به عدد اعشاری
                amount = float(input("Please enter the penalty amount: "))
            except ValueError:  #  در صورت نامعتبر بودن مقدار جریمه
                print("***Invalid input. Please enter a number.***")
            else:  # ذخیره کد و جریمه در دیکشنری
                codes[code] = amount

    return codes  #  برگرداندن دیکشنری حاوی کدها و جریمه ها

def calculate_penalty(codes):
    """
    این تابع جریمه خودرو را با توجه به کد جریمه و تعداد دفعات تخلف محاسبه می کند.

    ورودی:
        codes: دیکشنری حاوی کدهای جریمه و مبالغ جریمه

    خروجی:
        هیچ (اما جریمه کل را به کاربر نمایش می دهد)
    """
    code_to_check = input("Enter the code you want to calculate: ")  # دریافت کد جریمه از کاربر
    if code_to_check in codes:  # بررسی وجود کد جریمه در دیکشنری
        try:  # تبدیل مقدار ورودی تعداد دفعات تخلف به عدد صحیح
            num_defenses = int(input("How many times has the penalty occurred?: "))
        except ValueError:  # در صورت نامعتبر بودن مقدار تعداد دفعات تخلف
            print("***Invalid input. Please enter an integer.***")
        else:  # محاسبه جریمه کل و نمایش آن به کاربر
            total_penalty = codes[code_to_check] * num_defenses
            print("Total penalty for your car:", total_penalty)
    else:  # در صورت عدم وجود کد جریمه در دیکشنری
        print("***Entered code not found.***")

def get_car_name():
    """
    این تابع نام خودرو را از کاربر دریافت می کند.

    ورودی:
        هیچ

    خروجی:
        نام خودرو به عنوان رشته
    """
    car_name = input("Please enter the car name: ")
    return car_name

def main():
    """
    این تابع اصلی برنامه است که وظایف کلی سیستم را مدیریت می کند.

    ورودی:
        هیچ

    خروجی:
        هیچ (اما تعامل با کاربر و نمایش خروجی ها را انجام می دهد)
    """
    codes = get_penalty_codes()  # دریافت کدهای جریمه و ذخیره در دیکشنری
    check_again = "y"  # متغیری برای کنترل ادامه یا توقف برنامه
    while check_again.lower() == "y":  # حلقه برای بررسی جریمه چندین خودرو
        car_name = get_car_name()  # دریافت نام خودرو
        print("Calculate penalty for", car_name)  # نمایش نام خودرو
        calculate_penalty(codes, car_name)  # محاسبه جریمه برای خودرو
        check_again = input("Do you want to check another car? y/n: ")  # پرسیدن برای بررسی جریمه خودروی دیگر

main()  # اجرای تابع اصلی در صورت اجرای مستقیم اسکریپت
