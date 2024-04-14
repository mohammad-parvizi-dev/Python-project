# یک ارایه دوبعدی طراحی کنید 
# داده های دریافتی رو سوال بپرسید از کاربر که لیست داخلی هست یا نه 
#با END لیست اصلی بسته میشود و با end لیست داخلی بسته میشود



#توضیحات بیشتر در این لینک
#https://docs.google.com/document/d/1rZiQtTroI0ayhzRGktSyMP008L1L62zxHr6mYu2E4GU/edit?usp=sharing
# ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※         
dataList = []  # لیستی برای ذخیره داده‌های ورودی

getNewData = input("add new data: ")  # دریافت داده جدید از کاربر

while getNewData != "END":  # حلقه تا زمانی که کاربر "END" را وارد کند
    flagD = input("this data is list? y/n: ")  # پرسش از کاربر که آیا داده ورودی لیست است یا خیر

    if flagD == "n":  # اگر داده ورودی لیست نباشد
        dataList.append(getNewData)  # اضافه کردن داده به لیست اصلی

    elif flagD == "y":  # اگر داده ورودی لیست باشد
        dataListNew = []  # لیست جدید برای ذخیره داده‌های لیست

        while getNewData != "end":  # حلقه تا زمانی که کاربر "end" را برای لیست داخلی وارد کند
            dataListNew.append(getNewData)  # اضافه کردن داده به لیست داخلی
            getNewData = input("add new data to list or type 'end' to back: ")  # دریافت داده جدید برای لیست داخلی

        dataList.append(dataListNew)  # اضافه کردن لیست داخلی به لیست اصلی

    getNewData = input("add new data or type 'END' to finish: ")  # دریافت داده جدید یا "END" برای اتمام

print("your data is:\n" + str(dataList))  # چاپ لیست نهایی

