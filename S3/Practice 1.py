# در این برنامه، شما لیستی از داده‌ها را به صورت تعاملی از کاربر دریافت می‌کنید.
# کاربر می‌تواند هر گونه داده‌ای را که می‌خواهد به لیست اضافه کند، اما مقادیر تکراری مجاز نیستند.

# برنامه تا زمانی که کاربر "end" را وارد نکند، به جمع‌آوری داده‌ها ادامه می‌دهد.
# در نهایت، لیست نهایی داده‌ها به همراه پیامی به کاربر نمایش داده می‌شود.


#توضیحات بیشتر در این لینک
#https://docs.google.com/document/d/11SkbYE78BjFU5wiy98r5s8QiNFezVcYGGXy4p70JGBc/edit?usp=sharing
# ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※         
dataList = []  # لیستی برای ذخیره داده‌های ورودی کاربر

getNewData = input("add new data: ")  # دریافت داده جدید از کاربر

while getNewData != "end":  # تا زمانی که کاربر "end" را وارد نکند، ادامه دهید
    if getNewData in dataList:  # بررسی وجود داده در لیست
        print("This data already exists. Please enter a new one.")  # پیام خطا در صورت وجود داده تکراری
        getNewData = input("add neeeewwww data (•_•): ")  # درخواست مجدد برای داده جدید
    else:
        dataList.append(getNewData)  # اضافه کردن داده جدید به لیست
        print("Data added successfully!")  # پیام موفقیت
        getNewData = input("add new data: ")  # درخواست مجدد برای داده جدید

print("your data (ﾟvﾟ)ノ :\n"+ str(dataList))  # نمایش لیست نهایی داده‌ها به کاربر


