#FlowerShop - فروشگاه گل و گیاه فروزان

فروشگاه گل و گیاه فروزان یک وب‌سایت فروشگاهی است که با استفاده از **Django** توسعه داده شده است. این پروژه با هدف ارائه بستری برای معرفی و فروش انواع گل و گیاه، مدیریت کاربران و نمایش محصولات طراحی شده است.

---

## امکانات

- صفحه اصلی زیبا و واکنش‌گرا
- نمایش محصولات
- صفحه درباره ما
- صفحه تماس با ما
- ثبت‌نام کاربران
- ورود و خروج کاربران
-  استفاده از سیستم احراز هویت پیش‌فرض Django
-رابط کاربری مدرن با Bootstrap 5

---

## تکنولوژی‌های استفاده شده

- Python 3
- Django
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- SQLite

---

## ساختار پروژه

```
FlowerShop/
│
├── core/
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py
└── db.sqlite3
```

---

## نصب و اجرا

### 1. دریافت پروژه

```bash
git clone https://github.com/YourUsername/FlowerShop.git
```

### 2. ورود به پوشه پروژه

```bash
cd FlowerShop
```

### 3. ساخت محیط مجازی

```bash
python -m venv venv
```

### 4. فعال‌سازی محیط مجازی

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 5. نصب کتابخانه‌ها

```bash
pip install -r requirements.txt
```

### 6. اعمال Migration

```bash
python manage.py migrate
```

### 7. اجرای سرور

```bash
python manage.py runserver
```

سپس مرورگر را باز کرده و وارد شوید:

```
http://127.0.0.1:8000/
```

---

## 
## صفحات پروژه

- صفحه اصلی
- محصولات
- درباره ما
- تماس با ما
- ثبت‌نام
- ورود کاربران

---

## توسعه‌های آینده

- سبد خرید
- علاقه‌مندی‌ها
- پرداخت آنلاین
-  ثبت سفارش
- امتیازدهی محصولات
- جستجوی پیشرفته
- ارسال ایمیل تأیید
- پنل کاربری

---

##توسعه‌دهنده

**Zahra Forouzan**

GitHub:
https://github.com/ZahraForouzan80

---

##License

این پروژه صرفاً جهت اهداف آموزشی و نمونه‌کار توسعه داده شده است.
