# AdsBoard

AdsBoard — bu oddiy va qulay e’lonlar platformasi bo‘lib, foydalanuvchilar e’lonlarni ko‘rishi va yangi e’lon joylashi mumkin.
Loyiha **Django** framework’ida yozilgan va o‘quv / kichik loyiha sifatida mo‘ljallangan.

---

## 📌 Asosiy imkoniyatlar

* 🏠 **Home page** — oxirgi 2 ta e’lon ko‘rsatiladi
* 📃 **Ads list** — barcha e’lonlar ro‘yxati (pagination bilan)
* 🔍 **Search** — sarlavha va tavsif bo‘yicha qidirish
* 📄 **Ads detail** — e’lonning to‘liq ma’lumotlari
* ➕ **Create ad** — yangi e’lon qo‘shish
* 🧹 **Auto cleanup** — 30 kundan eski e’lonlar avtomatik o‘chiriladi

---

## ⏳ Avtomatik o‘chirish (30 kun)

* Har bir e’lon yaratilgan vaqti (`created_at`) bilan saqlanadi
* 30 kundan eski e’lonlar **database’dan butunlay o‘chiriladi**
* Tozalash **maxsus URL** orqali ishga tushiriladi:

```
/clean/
```

Natijada:

* eski e’lonlar o‘chadi
* foydalanuvchiga natija haqida xabar ko‘rsatiladi

> ⚠️ Oddiy foydalanuvchilar e’lonni o‘chira olmaydi.
> O‘chirish faqat superadmin nazoratida amalga oshiriladi.

---

## 📞 Admin bilan aloqa

Agar e’lon bo‘yicha muammo yoki savol bo‘lsa, foydalanuvchilar admin bilan quyidagi ma’lumotlar orqali bog‘lanishi mumkin:

* 📧 Email: `saparov.inbox@example.com`
* 📱 Phone: `+998-50-077-36-66`
* 📱 Phone: `+998-94-752-36-66`

---

## 🎨 Dizayn

* Hozircha **Mobile** uchun kamchiliklari bor!
* CSS fayllar alohida saqlangan (`static/css/`)
* Umumiy layout `base.html` orqali boshqariladi

---

## 🛠 Texnologiyalar

* Python 3
* Django
* HTML5
* CSS3
* PostgreSQL

---

## 🚀 Ishga tushirish

```bash
git clone <repository-url>
cd repo-name
python manage.py migrate
python manage.py runserver
```

Brauzerda oching:

```
http://127.0.0.1:8000/
```

---

## 📎 Eslatma

Bu loyiha:

* o‘quv maqsadida
* soddalik va tushunarlilikka urg‘u berib
* qo‘shimcha murakkab background tasklarsiz ishlab chiqilgan

---

## 👨‍💻 Muallif
### Mehroj Saparov

AdsBoard — Django’ni o‘rganish jarayonida yaratilgan loyiha.

