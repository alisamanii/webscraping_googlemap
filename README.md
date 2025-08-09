# webscraping_googlemap

📍 **استخراج اطلاعات مکان‌ها از Google Maps با Python**

### **توضیح کلی**

این پروژه با استفاده از کتابخانه‌های **Camoufox** و **BeautifulSoup**، قادر است به صورت خودکار مکان‌های موجود در **Google Maps** را جستجو کرده، لینک‌ها و اطلاعات آن‌ها را استخراج کرده و در یک فایل متنی ذخیره کند.

### **مراحل اجرای پروژه**

1. **مرحله اول – استخراج لینک‌ها از Google Maps**

   * وارد صفحه جستجوی Google Maps می‌شود.
   * اسکرول خودکار برای بارگذاری لیست مکان‌ها انجام می‌دهد.
   * عنوان و لینک هر مکان را استخراج می‌کند.
   * از ثبت لینک‌های تکراری جلوگیری می‌شود.

2. **مرحله دوم – استخراج جزئیات مکان‌ها**

   * با رفتن به صفحه هر مکان، اطلاعات زیر را دریافت می‌کند:

     * عنوان مکان
     * زیرعنوان یا توضیح کوتاه
     * امتیاز کاربران
     * تعداد نظرات
     * دسته‌بندی مکان
     * آدرس کامل
     * شماره تماس
     * ساعت کاری (روزانه)
     * تصویر اصلی مکان
     * مختصات جغرافیایی (در صورت موجود بودن در لینک)

3. **مرحله سوم – ذخیره اطلاعات**

   * تمام داده‌ها به صورت ساختارمند در یک فایل متنی (`places_info.txt`) ذخیره می‌شوند.
   * برای هر مکان یک بلوک جداگانه شامل تمام جزئیات ذخیره می‌شود.

### **پیش‌نیازها**

قبل از اجرای پروژه، کتابخانه‌های زیر باید نصب شوند:

```bash
pip install camoufox beautifulsoup4
```

### **روش اجرا**

```bash
python main.py
```

---

## **English Description**

### **Project Title**

📍 **Google Maps Places Data Scraper with Python**

### **Overview**

This project uses **Camoufox** and **BeautifulSoup** to automatically search locations on **Google Maps**, scrape their links and detailed information, and store them in a text file.

### **Project Workflow**

1. **Step 1 – Extract Links from Google Maps**

   * Navigates to the Google Maps search page.
   * Performs auto-scrolling to load more results.
   * Extracts the title and link of each place.
   * Prevents duplicate entries.

2. **Step 2 – Extract Place Details**

   * Visits each place’s page to extract:

     * Place title
     * Subtitle/short description
     * User rating
     * Number of reviews
     * Category
     * Full address
     * Phone number
     * Opening hours (daily)
     * Main image URL
     * Geographical coordinates (if available in URL)

3. **Step 3 – Save Data**

   * All data is stored in a structured format in a text file (`places_info.txt`).
   * Each place’s data is saved in a separate block for better readability.

### **Requirements**

Install the following Python packages before running the script:

```bash
pip install camoufox beautifulsoup4
```

### **Run the Script**

```bash
python main.py
```

---

اگر بخواهی می‌توانم همین متن را مستقیماً به شکل **README.md** برای گیت‌هابت آماده کنم تا فقط کپی و پیست کنی.
آیا می‌خواهی آن را آماده کنم؟
