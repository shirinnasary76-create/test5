import base64
import os
import json

os.makedirs('/home/user/src', exist_ok=True)

def to_data_uri(path, mime):
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    return f"data:{mime};base64,{b64}"

# Load fonts as data URIs so offline iframe preview in Arena renders Vazirmatn 100% natively
font_regular = to_data_uri('/home/user/public/fonts/Vazirmatn-Regular.woff2', 'font/woff2')
font_medium = to_data_uri('/home/user/public/fonts/Vazirmatn-Medium.woff2', 'font/woff2')
font_bold = to_data_uri('/home/user/public/fonts/Vazirmatn-Bold.woff2', 'font/woff2')
font_extrabold = to_data_uri('/home/user/public/fonts/Vazirmatn-ExtraBold.woff2', 'font/woff2')
font_black = to_data_uri('/home/user/public/fonts/Vazirmatn-Black.woff2', 'font/woff2')

# Load extracted & cleaned reference images as data URIs
img_hero = to_data_uri('/home/user/public/assets/hero-bg.jpg', 'image/jpeg')
img_about = to_data_uri('/home/user/public/assets/about-bg.jpg', 'image/jpeg')
img_card1 = to_data_uri('/home/user/public/assets/card-1.jpg', 'image/jpeg')
img_card2 = to_data_uri('/home/user/public/assets/card-2.jpg', 'image/jpeg')
img_card3 = to_data_uri('/home/user/public/assets/card-3.jpg', 'image/jpeg')
img_card4 = to_data_uri('/home/user/public/assets/card-4.jpg', 'image/jpeg')
img_logo = to_data_uri('/home/user/public/assets/logo-emblem.png', 'image/png')
img_circle_bg = to_data_uri('/home/user/public/assets/circle-bg.jpg', 'image/jpeg')

# Write editable site configuration file
site_config = {
    "defaultBrand": "delgosha",
    "brands": {
        "delgosha": {
            "name": "دلگشا",
            "tagline": "هلدینگ توسعه صنعت و معدن و تجارت",
            "heroOverline": "دلگشا، همراه مطمئن کسب‌وکارها",
            "heroTitleLine1": "از مجوز تا توسعه،",
            "heroTitleLine2": "در کنار شما هستیم",
            "heroBody": "دلگشا با ارائه خدمات تخصصی در حوزه‌های صنعتی، معدنی، اداری، مالی و توسعه کسب‌وکار، مسیر رشد و موفقیت شما را هموار می‌کند.",
            "servicesOverline": "خدمات دلگشا",
            "aboutOverline": "معرفی دلگشا",
            "aboutBody": "دلگشا با تکیه بر تجربه و دانش تخصصی، در کنار کسب‌وکارها، صنایع و سرمایه‌گذاران است تا با ارائه راهکارهای عملی و دقیق، مسیر توسعه و رشد آن‌ها را هموار کند.",
            "whyTitle": "چرا دلگشا؟",
            "email": "info@delgosha.ir",
            "copyright": "© تمامی حقوق مادی و معنوی این سایت متعلق به دلگشا می‌باشد."
        },
        "rahgosha": {
            "name": "راه‌گشا",
            "tagline": "هلدینگ توسعه صنعت و معدن و تجارت",
            "heroOverline": "راه‌گشا، همراه مطمئن کسب‌وکارها",
            "heroTitleLine1": "از مجوز تا توسعه،",
            "heroTitleLine2": "در کنار شما هستیم",
            "heroBody": "راه‌گشا با ارائه خدمات تخصصی در حوزه‌های صنعتی، معدنی، اداری، مالی و توسعه کسب‌وکار، مسیر رشد و موفقیت شما را هموار می‌کند.",
            "servicesOverline": "خدمات راه‌گشا",
            "aboutOverline": "معرفی راه‌گشا",
            "aboutBody": "راه‌گشا با تکیه بر تجربه و دانش تخصصی، در کنار کسب‌وکارها، صنایع و سرمایه‌گذاران است تا با ارائه راهکارهای عملی و دقیق، مسیر توسعه و رشد آن‌ها را هموار کند.",
            "whyTitle": "چرا راه‌گشا؟",
            "email": "info@delgosha.ir",
            "copyright": "© تمامی حقوق مادی و معنوی این سایت متعلق به هلدینگ راه‌گشا می‌باشد."
        }
    },
    "navItems": [
        {"label": "خانه", "href": "#top", "active": True},
        {"label": "خدمات", "href": "#services", "active": False},
        {"label": "درباره ما", "href": "#about", "active": False},
        {"label": "اخبار و رویدادها", "href": "#cards", "active": False},
        {"label": "پروژه‌ها", "href": "#projects", "active": False},
        {"label": "تماس با ما", "href": "#footer", "active": False}
    ],
    "serviceCircles": [
        {"id": "content", "title": "تولید محتوا", "arc": "left", "targetCard": "04"},
        {"id": "audit", "title": "حسابرسی", "arc": "none", "targetCard": "03"},
        {"id": "design_calc", "title": "طراحی و محاسبات", "arc": "none", "targetCard": "04"},
        {"id": "feasibility", "title": "طرح توجیهی", "arc": "none", "targetCard": "01"},
        {"id": "brand", "title": "ثبت برند", "arc": "none", "targetCard": "03"},
        {"id": "company", "title": "ثبت شرکت", "arc": "none", "targetCard": "03"},
        {"id": "license", "title": "جواز", "arc": "top-right", "targetCard": "01"}
    ],
    "industryCards": [
        {
            "num": "۰۱",
            "id": "01",
            "title": "صنعت",
            "subtitle": "تولید، توسعه صنعتی و حمایت از کسب‌وکارها",
            "icon": "industry",
            "items": [
                "صدور جواز تاسیس",
                "پروانه بهره برداری",
                "صدور پروانه فرش دست بافت",
                "صدور مجوز توزیع کالای دخانی",
                "صدور مجوز توزیع بدون کارخانه",
                "صدور پروانه طراحی و منتاج آسانسور",
                "صدور پروانه فنی و مهندسی",
                "صدور پروانه تحقیق و توسعه (R&D)",
                "صدور جواز تاسیس فنی و مهندسی",
                "خرید مواد اولیه از بورس",
                "پیشنهاد کد isic",
                "صدور جواز رمز ارز دیجیتال"
            ]
        },
        {
            "num": "۰۲",
            "id": "02",
            "title": "معدن",
            "subtitle": "اکتشاف، بهره‌برداری و توسعه صنایع معدنی",
            "icon": "mining",
            "items": [
                "صدور پروانه بهره برداری",
                "صدور گواهی کشف",
                "صدور مجوز بهداشت",
                "تمدید پروانه های معدنی",
                "ارسال آمار کاداستر",
                "ثبت محدوده های معدنی",
                "بارگذاری قراردادهای مسئول فنی",
                "بارگذاری طرح",
                "ثبت ماشین آلات معدنی",
                "پرداخت تبصره",
                "صدور صلاحیت فنی و مالی"
            ]
        },
        {
            "num": "۰۳",
            "id": "03",
            "title": "تجارت",
            "subtitle": "بازرگانی، صادرات و واردات و توسعه بازار",
            "icon": "trade",
            "items": [
                "صدور و تمدید توکن",
                "ایجاد پایه حقیقی و حقوقی",
                "ایجاد کد نقش",
                "درخواست شناسه",
                "ارسال آمار",
                "ثبت انبار",
                "آمار تولید",
                "ثبت سفارش",
                "صدور و تمدید کارت بازرگانی",
                "ترخیص کالا"
            ]
        },
        {
            "num": "۰۴",
            "id": "04",
            "title": "فنی و مهندسی",
            "subtitle": "راهکارهای تخصصی برای توسعه بهره‌وری",
            "icon": "engineering",
            "items": [
                "طراحی سازه ساختمان",
                "طراحی و اجراء سوله کارخانه",
                "نقشه برداری",
                "دکوراسیون",
                "پیمانکاری صفر تا صد ساختمان"
            ]
        }
    ],
    "whyItems": [
        {"title": "تجربه و تخصص", "subtitle": "سال‌ها تجربه در حوزه صنعت", "icon": "exp"},
        {"title": "مشاوره حرفه‌ای", "subtitle": "راهکارهای عملی و کاربردی", "icon": "consult"},
        {"title": "همراهی بلندمدت", "subtitle": "در تمام مسیرهای شما", "icon": "partner"},
        {"title": "شبکه گسترده ارتباطات", "subtitle": "در دسترس به فرصت‌های جدید", "icon": "network"}
    ],
    "contact": {
        "address": "شیراز بلوار چهل مقام ، کوچه ۱۱ جنب سازمان صنعت و معدن و تجارت",
        "addressLabel": "آدرس دفتر مرکزی",
        "email": "info@delgosha.ir",
        "emailLabel": "پست الکترونیک",
        "phone": "۰۹۱۷۷۰۵۶۰۶۳",
        "phoneHours": "(پاسخگویی ۸ الی ۱۶)"
    }
}

with open('/home/user/src/site-config.json', 'w', encoding='utf-8') as f:
    json.dump(site_config, f, ensure_ascii=False, indent=2)

print("Saved site-config.json")
