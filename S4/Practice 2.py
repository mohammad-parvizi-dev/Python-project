# فرض کنید در یک پوشه تعدادی فایل با فرمت‌های مختلف (مانند txt، docx، pdf، jpg و غیره) وجود دارد. 
# شما می‌خواهید پوشه‌هایی مجزا برای هر فرمت فایل ایجاد کنید و سپس تمام فایل‌ها را به پوشه مربوطه خود منتقل کنید.
# با استفاده از زبان برنامه‌نویسی پایتون، یک برنامه بنویسید که این کار را انجام دهد.
# فایل خود پایتون شامل پوشه بندی و جابجایی فایل ها نشود
#جلوی خطاهای احتمالی هم گرفته شود

#توضیحات بیشتر در این لینک
#https://docs.google.com/document/d/1cPY5m-277enuMzFOsBBoF6PqzlSEBdrrhGavd-53VOo/edit?usp=sharing
# ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※         
import os
import glob

# لیستی از نام تمام فایل‌ها در پوشه جاری را با استفاده از glob.glob تهیه کنید
files_list = glob.glob('*.*')

# مجموعه‌ای به نام my_set برای ذخیره پسوندهای منحصربه‌فرد ایجاد کنید
my_set = set()

# برای هر فایل در لیست files_list:
for item in files_list:
    # پسوند فایل را با استفاده از .split('.') جدا کنید
    ext = item.split('.')[1]
    # پسوند را به مجموعه my_set اضافه کنید (تکراری‌ها حذف می‌شوند)
    my_set.add(ext)


def create_folders():
    # برای هر پسوند منحصربه‌فرد در my_set:
    for i in my_set:
        # اگر پسوند py نیست:
        if i != "py":
            # سعی کنید پوشه را با نام i_Files ایجاد کنید
            try:
                os.makedirs(i + '_Files')
            # اگر پوشه قبلاً وجود دارد، پیامی چاپ کنید
            except FileExistsError:
                print(f"Folder '{i}_Files' already exists.")
            # اگر خطای دیگری رخ داد، جزئیات خطا را چاپ کنید
            except Exception as e:
                print(f"Error creating folder '{i}_Files': {e}")

def move_folders():
    # برای هر فایل در لیست files_list:
    for item in files_list:
        # پسوند فایل را با استفاده از .split('.') جدا کنید
        f = item.split('.')[1]
        # اگر پسوند py نیست:
        if f != "py":
            # نام جدید فایل را با فرمت نام_فایل_در_پوشه_جدید بسازید
            new_name = f + '_Files/' + item
            # فایل را به نام جدید جابجا کنید
            os.rename(item, new_name)

create_folders()  # پوشه‌های جدید را برای هر پسوند ایجاد کنید
move_folders()   # فایل‌ها را به پوشه‌های مربوطه منتقل کنید
