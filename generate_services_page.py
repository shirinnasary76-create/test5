import base64
import json
import os

with open('/home/user/src/site-config.json', encoding='utf-8') as settings_file:
    desktop_viewport_width = int(json.load(settings_file).get('display', {}).get('desktopWidth', 1360))

os.makedirs('/home/user/services', exist_ok=True)

def to_data_uri(path, mime):
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    return f"data:{mime};base64,{b64}"

font_regular = to_data_uri('/home/user/public/fonts/Vazirmatn-Regular.woff2', 'font/woff2')
font_medium = to_data_uri('/home/user/public/fonts/Vazirmatn-Medium.woff2', 'font/woff2')
font_bold = to_data_uri('/home/user/public/fonts/Vazirmatn-Bold.woff2', 'font/woff2')
font_extrabold = to_data_uri('/home/user/public/fonts/Vazirmatn-ExtraBold.woff2', 'font/woff2')
font_black = to_data_uri('/home/user/public/fonts/Vazirmatn-Black.woff2', 'font/woff2')

img_hero = to_data_uri('/home/user/public/assets/services-hero.jpg', 'image/jpeg')
img_about = to_data_uri('/home/user/public/assets/about-bg.jpg', 'image/jpeg')
img_card1 = to_data_uri('/home/user/public/assets/card-1.jpg', 'image/jpeg')
img_card2 = to_data_uri('/home/user/public/assets/card-2.jpg', 'image/jpeg')
img_card3 = to_data_uri('/home/user/public/assets/card-3.jpg', 'image/jpeg')
img_card4 = to_data_uri('/home/user/public/assets/card-4.jpg', 'image/jpeg')
img_sub1 = to_data_uri('/home/user/public/assets/subservice-1.jpg', 'image/jpeg')
img_sub2 = to_data_uri('/home/user/public/assets/subservice-2.jpg', 'image/jpeg')
img_sub3 = to_data_uri('/home/user/public/assets/subservice-3.jpg', 'image/jpeg')
img_sub4 = to_data_uri('/home/user/public/assets/subservice-4.jpg', 'image/jpeg')
img_sub5 = to_data_uri('/home/user/public/assets/subservice-5.jpg', 'image/jpeg')
img_logo = to_data_uri('/home/user/public/assets/logo-mark.png', 'image/png')
img_logo_text = to_data_uri('/home/user/public/assets/logo-text.png', 'image/png')
img_logo_full = to_data_uri('/home/user/public/assets/logo-full.png', 'image/png')
img_logo_lightbg = to_data_uri('/home/user/public/assets/logo-lightbg.png', 'image/png')

img_1001 = to_data_uri('/home/user/public/assets/srv-1001.jpg', 'image/jpeg')
img_1002 = to_data_uri('/home/user/public/assets/srv-1002.jpg', 'image/jpeg')
img_1003 = to_data_uri('/home/user/public/assets/srv-1003.jpg', 'image/jpeg')
img_1004 = to_data_uri('/home/user/public/assets/srv-1004.jpg', 'image/jpeg')

with open('/home/user/src/styles.css', 'r', encoding='utf-8') as f:
    base_styles = f.read()

# Pool of visual assets with varied crops & lighting filters so slide cards look rich and distinct
VISUAL_POOL = [
    (img_card1, "center center", "contrast(1.06) saturate(1.08)"),
    (img_sub1, "center center", "contrast(1.05) saturate(1.1)"),
    (img_sub2, "center center", "contrast(1.08) brightness(1.02)"),
    (img_sub4, "center center", "contrast(1.06) saturate(1.05)"),
    (img_sub5, "center center", "contrast(1.05) saturate(1.08)"),
    (img_hero, "right center", "contrast(1.08) saturate(1.12)"),
    (img_about, "left center", "contrast(1.06) brightness(1.04)"),
    (img_card2, "center center", "contrast(1.06) saturate(1.1)"),
    (img_sub3, "center center", "contrast(1.07) saturate(1.06)"),
    (img_card3, "center center", "contrast(1.08) saturate(1.1)"),
    (img_card4, "center center", "contrast(1.06) saturate(1.08)"),
    (img_hero, "left center", "contrast(1.05) hue-rotate(-8deg)"),
]
SLIDE_ICONS = {
    # ---------------- Industry (صنعت - 12) ----------------
    "sodor-javaz-tasis": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10M7 12h10M7 16h6"/></svg>',
    "parvane-bahrebardari-sanat": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18V3H3z"/><path d="M5 7h2M9 7h2M5 11h2M9 11h2M7 15h4"/></svg>',
    "parvane-farsh-dastbaft": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16M6 4l4 8M10 4l4 8M14 4l4 8M18 4l4 8"/></svg>',
    "mojavez-tozi-kala-dokhani": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
    "mojavez-tozi-bedone-karkhane": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="12" rx="2"/><path d="M3.5 14.5v-2L12 4l8.5 8.5v2M12 4v16"/></svg>',
    "parvane-tarahi-montazh-asansor": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="6" height="16"/><rect x="15" y="8" width="6" height="12"/><path d="M9 4V20M9 12H15"/></svg>',
    "parvane-fanni-mohandesi": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9.09A10 10 0 014 14.17c0 2.74 2.34 5.08 5.09 5.08"/></svg>',
    "parvane-tahghigh-tosee-rd": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3l-5 5 5 5M15 3l5 5-5 5M3 16l5-5 5 5"/></svg>',
    "javaz-tasis-fanni-mohandesi": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v18H3z"/><path d="M12 7l-5 5 5 5M9 9l6-6"/></svg>',
    "kharid-mavad-avali-bourse": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 13v6M12 3v18M18 18l-6-6M6 18l6-6"/></svg>',
    "pishnahad-code-isic": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><path d="M5 5L19 5L12 19L5 5Z"/></svg>',
    "javaz-ramzarz-digital": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M12 8l4 4M12 16l4-4"/></svg>',

    # ---------------- Mining (معدن - 11) ----------------
    "parvane-bahrebardari-madan": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M3 12h18"/><path d="M6 6l6 6M18 6l-6 6M6 18l6-6M18 18l-6-6"/></svg>',
    "govahi-kashf-madan": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/></svg>',
    "mojavez-behdasht-madan": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3 6 3 2-3 2 3h4a2 2 0 012 2z"/><path d="M9 11h6v8H9z"/></svg>',
    "tamdid-parvane-madani": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h5v5M19 4h-5v5M4 19h5v-5M19 19h-5v-5M12 12a3 3 0 100-6 3 3 0 000 6z"/></svg>',
    "ersal-amar-cadastre": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="21"/><line x1="17" y1="3" x2="17" y2="15"/><line x1="22" y1="3" x2="22" y2="9"/><line x1="7" y1="3" x2="7" y2="18"/><line x1="3" y1="3" x2="3" y2="12"/></svg>',
    "sabt-mahdode-madani": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 9 21 9 12 3"/><path d="M3 9v12h18V9z"/><path d="M7 9v6M17 9v6M9 11h6"/></svg>',
    "bargozari-gharardad-masool-fanni": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="6 9 12 15 18 9"/></svg>',
    "bargozari-tarh-madani": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2H3l7 7 5-5 5 5H21zM7 7h10v10H7z"/></svg>',
    "sabt-mashin-alat-madani": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="10" rx="2"/><path d="M5 17H9m10 0h4m-7 0v4M19 17v4"/><circle cx="7" cy="19" r="2"/><circle cx="17" cy="19" r="2"/></svg>',
    "pardakht-tabsare-madan": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 8V12M12 16L12 16"/></svg>',
    "salahiyat-fanni-mali-madan": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 16h6l-3-3z"/><path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/></svg>',

    # ---------------- Trade (تجارت - 10) ----------------
    "kart-bazargani": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="7" y2="10"/><line x1="1" y1="14" x2="7" y2="14"/></svg>',
    "sabt-sefaresh": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 7 12 11 8 7"/><path d="M21 12V6a2 2 0 00-2-2H6a2 2 0 00-2 2v14a2 2 0 002 2h12a2 2 0 002-2z"/></svg>',
    "tarkhis-kala": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8v13c0 1.1-.9 2-2 2H5c-1.1 0-2-.9-2-2V8zM7 8h14v11H7zM16 3h2l-4 4-4-4h2z"/></svg>',
    "sodor-tamdid-token": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
    "ijad-paye-haghighi-hoghoghi": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v18H3z"/><path d="M3 15h18M12 3v18"/></svg>',
    "ijad-code-naghsh": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>',
    "darkhast-shenase": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 8l8 8"/></svg>',
    "sabt-anbar": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8V7c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8z"/><polyline points="16 7 12 11 8 7"/><rect x="9" y="10" width="6" height="6"/></svg>',
    "ersal-amar-tejarat": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="21"/><line x1="17" y1="3" x2="17" y2="15"/><line x1="22" y1="3" x2="22" y2="9"/><line x1="7" y1="3" x2="7" y2="18"/><line x1="3" y1="3" x2="3" y2="12"/></svg>',
    "amar-tolid": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>',

    # ---------------- Engineering (فنی و مهندسی - 5) ----------------
    "structural-design": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M12 3v18M3 15h18M6 6l6 6M18 6l-6 6"/></svg>',
    "industrial-shed": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 15V8c0-1.1.9-2 2-2h14c1.1 0 2 .9 2 2v7M3 15h18"/><path d="M7 15l5 5 5-5"/></svg>',
    "surveying": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v20M2 12h20M8 8l8 8"/></svg>',
    "interior-design": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l1.5 1.5L18 13z"/></svg>',
    "building-contractor": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M12 3v18M3 15h18M6 6l6 6M18 6l-6 6"/><path d="M6 15h12v4H6z"/></svg>',

    # ---------------- Registration (ثبتی، مالی و توسعه کسب‌وکار - 7) ----------------
    "company-registration": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "brand-registration": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5a2 2 0 012-2h1a2 2 0 012 2v1a2 2 0 012 2h1a2 2 0 01-2 2H7a2 2 0 01-2-2V6a2 2 0 01-2-2z"/></svg>',
    "feasibility-study": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/><path d="M13 14H3M13 6H3M7 10l6 4"/></svg>',
    "auditing-services": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3a6 6 0 016 6v1"/><path d="M8 21v-3a4 4 0 00-4-4H5a4 4 0 00-4 4v3M13 7h8M13 7H5"/></svg>',
    "engineering-design-calculation": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6l5 5M12 12l-5 5M12 18l-5-5"/></svg>',
    "content-production": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
    "license-consulting": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><path d="m16 3.13-4 4L8 7z"/><path d="M12 17l2 2 4-4"/></svg>',
}



# ==============================================================================
# 5 STACKED HORIZONTAL BANNER + SLIDER SECTIONS
# Alternating backgrounds:
# 1. Navy  (صنعت — 12 slides)
# 2. White (معدن — 11 slides)
# 3. Navy  (تجارت — 10 slides)
# 4. White (فنی و مهندسی — 5 slides)
# 5. Navy  (ثبتی، مالی و توسعه کسب‌وکار — 7 slides)
# ==============================================================================
SIX_SHOWCASE_BANDS = [
    {
        "id": "group-industry",
        "theme": "navy",  # 1. سورمه‌ای
        "overline": "خدمات تخصصی بخش اول",
        "icon_svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10l2.1 2.1M19.1 4.9l-2.1 2.1m-10 10l-2.1 2.1"/></svg>',
        "title": "صنعت و مجوزهای تولید",
        "desc": "راهبری کامل امور صنعتی از صدور جواز تأسیس و پیشنهاد کد ISIC تا اخذ پروانه بهره‌برداری، تحقیق و توسعه و سهمیه بورس کالا.",
        "btn_text": "درخواست مشاوره صنعت",
        "feature_img": img_1001,
        "feature_alt": "خدمات تخصصی صنعت و کارخانجات تولیدی",
        "slides": [
            {
                "slug": "sodor-javaz-tasis",
                "title": "صدور جواز تأسیس",
                "sub": "ثبت درخواست در سامانه بهین‌یاب، تعیین ظرفیت و اخذ موافقت اصولی احداث واحد تولیدی.",
                "meta": "مجوز راه‌اندازی صنعت",
                "img": img_card1,
                "pos": "center center"
            },
            {
                "slug": "parvane-bahrebardari-sanat",
                "title": "پروانه بهره‌برداری",
                "sub": "تکمیل مستندات فنی، هماهنگی بازدید کارشناسی و صدور مجوز رسمی شروع تولید کارخانه.",
                "meta": "بهره‌برداری رسمی",
                "img": img_sub1,
                "pos": "center center"
            },
            {
                "slug": "parvane-farsh-dastbaft",
                "title": "صدور پروانه فرش دست‌بافت",
                "sub": "اخذ مجوزهای مشاغل خانگی و کارگاه‌های متمرکز و غیرمتمرکز تولید فرش دست‌بافت.",
                "meta": "صنایع فرش و نساجی",
                "img": img_sub5,
                "pos": "center center"
            },
            {
                "slug": "mojavez-tozi-kala-dokhani",
                "title": "مجوز توزیع کالای دخانی",
                "sub": "پیگیری استعلامات قانونی و اخذ مجوز رسمی عاملیت و پخش سراسری یا استانی کالای دخانی.",
                "meta": "مجوز پخش و توزیع",
                "img": img_card3,
                "pos": "left center"
            },
            {
                "slug": "mojavez-tozi-bedone-karkhane",
                "title": "مجوز توزیع بدون کارخانه",
                "sub": "اخذ مجوز تولید قراردادی (ظرفیت خالی کارخانه‌ها) برای صاحبان برند بدون نیاز به تملک خط تولید.",
                "meta": "تولید بدون کارخانه",
                "img": img_sub2,
                "pos": "center center"
            },
            {
                "slug": "parvane-tarahi-montazh-asansor",
                "title": "پروانه طراحی و مونتاژ آسانسور",
                "sub": "تشکیل پرونده فنی، تأمین الزامات مهندسی و اخذ پروانه رسمی طراحی و مونتاژ آسانسور.",
                "meta": "صنایع فلزی و آسانسور",
                "img": img_card4,
                "pos": "center center"
            },
            {
                "slug": "parvane-fanni-mohandesi",
                "title": "صدور پروانه فنی و مهندسی",
                "sub": "ارزیابی توانمندی تخصصی شرکت‌ها و اخذ پروانه خدمات فنی و مهندسی از وزارت صمت.",
                "meta": "پروانه تخصصی صمت",
                "img": img_sub4,
                "pos": "center center"
            },
            {
                "slug": "parvane-tahghigh-tosee-rd",
                "title": "پروانه تحقیق و توسعه (R&D)",
                "sub": "مستندسازی فعالیت‌های پژوهشی واحدهای صنعتی و اخذ گواهی و پروانه تحقیق و توسعه.",
                "meta": "تحقیق و توسعه صنعتی",
                "img": img_about,
                "pos": "center center"
            },
            {
                "slug": "javaz-tasis-fanni-mohandesi",
                "title": "جواز تأسیس فنی و مهندسی",
                "sub": "اخذ مجوز تأسیس مراکز و واحدهای خدمات فنی، طراحی صنعتی و مهندسی پیشرفته.",
                "meta": "جواز واحد مهندسی",
                "img": img_hero,
                "pos": "right center"
            },
            {
                "slug": "kharid-mavad-avali-bourse",
                "title": "خرید مواد اولیه از بورس",
                "sub": "ثبت‌نام در بهین‌یاب، تعیین سهمیه مصرف و اخذ کد معاملاتی خرید مواد اولیه از بورس کالا.",
                "meta": "سهمیه بورس کالا",
                "img": img_sub3,
                "pos": "center center"
            },
            {
                "slug": "pishnahad-code-isic",
                "title": "پیشنهاد کد ISIC",
                "sub": "بررسی دقیق محصولات و فرآیند تولید و تعیین کد آیسیک استاندارد در سامانه‌های صنعتی.",
                "meta": "کدگذاری محصولات",
                "img": img_sub1,
                "pos": "left center"
            },
            {
                "slug": "javaz-ramzarz-digital",
                "title": "صدور جواز رمز ارز دیجیتال",
                "sub": "اخذ جواز تأسیس و پروانه بهره‌برداری قانونی مزارع استخراج رمزارز با انشعاب و تجهیزات مجاز.",
                "meta": "فناوری و رمزارز",
                "img": img_hero,
                "pos": "left center"
            }
        ]
    },
    {
        "id": "group-mining",
        "theme": "white",  # 2. سفید
        "overline": "خدمات تخصصی بخش دوم",
        "icon_svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M3 20L10 6L15 15L18 10L22 20H3Z"/></svg>',
        "title": "معدن و سامانه کاداستر",
        "desc": "انجام کلیه امور فنی، حقوقی و سامانه‌ای معادن؛ از ثبت محدوده اکتشافی و گواهی کشف تا پروانه بهره‌برداری و صلاحیت فنی و مالی.",
        "btn_text": "درخواست مشاوره معدن",
        "feature_img": img_1002,
        "feature_alt": "خدمات تخصصی معدن، اکتشاف و استخراج",
        "slides": [
            {
                "slug": "parvane-bahrebardari-madan",
                "title": "صدور پروانه بهره‌برداری معدن",
                "sub": "تدوین طرح بهره‌برداری و پیگیری اخذ مجوز رسمی استخراج ذخایر معدنی از سازمان صمت.",
                "meta": "بهره‌برداری معادن",
                "img": img_card2,
                "pos": "center center"
            },
            {
                "slug": "govahi-kashf-madan",
                "title": "صدور گواهی کشف",
                "sub": "مستندسازی عملیات اکتشافی، گزارش پایانی اکتشاف، تعیین ذخیره قطعی و صدور گواهی کشف.",
                "meta": "اکتشاف و تعیین ذخیره",
                "img": img_sub3,
                "pos": "center center"
            },
            {
                "slug": "mojavez-behdasht-madan",
                "title": "صدور مجوز بهداشت",
                "sub": "پیگیری استعلامات زیست‌محیطی، ایمنی کار و اخذ مجوز بهداشت حرفه‌ای محدوده‌های معدنی.",
                "meta": "ایمنی و بهداشت معدن",
                "img": img_sub2,
                "pos": "center center"
            },
            {
                "slug": "tamdid-parvane-madani",
                "title": "تمدید پروانه‌های معدنی",
                "sub": "تکمیل مدارک عملکردی و پیگیری تمدید پروانه‌های اکتشاف و بهره‌برداری پیش از انقضا.",
                "meta": "تمدید مجوزهای معدنی",
                "img": img_card1,
                "pos": "center center"
            },
            {
                "slug": "ersal-amar-cadastre",
                "title": "ارسال آمار کاداستر",
                "sub": "ثبت و ارسال منظم گزارش‌های دوره‌ای عملکرد و میزان استخراج در سامانه کاداستر معادن.",
                "meta": "سامانه کاداستر",
                "img": img_sub5,
                "pos": "center center"
            },
            {
                "slug": "sabt-mahdode-madani",
                "title": "ثبت محدوده‌های معدنی",
                "sub": "بررسی نقاط آزاد در نقشه کاداستر، تعیین مختصات جغرافیایی و ثبت اولیه محدوده اکتشافی.",
                "meta": "ثبت محدوده جدید",
                "img": img_sub3,
                "pos": "right center"
            },
            {
                "slug": "bargozari-gharardad-masool-fanni",
                "title": "بارگذاری قرارداد مسئول فنی",
                "sub": "تنظیم و ثبت رسمی قرارداد مسئول فنی معدن و تأیید صلاحیت در درگاه تخصصی سازمان.",
                "meta": "امور مسئول فنی",
                "img": img_about,
                "pos": "center center"
            },
            {
                "slug": "bargozari-tarh-madani",
                "title": "بارگذاری طرح",
                "sub": "تهیه، تدوین و بارگذاری طرح‌های اکتشاف، استخراج و بهره‌برداری توسط کارشناسان ذی‌صلاح.",
                "meta": "طرح‌های فنی معدن",
                "img": img_sub4,
                "pos": "center center"
            },
            {
                "slug": "sabt-mashin-alat-madani",
                "title": "ثبت ماشین‌آلات معدنی",
                "sub": "ثبت مشخصات ناوگان حفاری، بارگیری و حمل‌ونقل معدنی در سامانه و پیگیری سهمیه سوخت.",
                "meta": "ناوگان و تجهیزات معدن",
                "img": img_sub1,
                "pos": "center center"
            },
            {
                "slug": "pardakht-tabsare-madan",
                "title": "پرداخت تبصره",
                "sub": "محاسبه حقوق دولتی، ثبت اظهارنامه و پیگیری فرآیند پرداخت یا تقسیط تبصره‌های معدنی.",
                "meta": "حقوق دولتی و تبصره",
                "img": img_hero,
                "pos": "center center"
            },
            {
                "slug": "salahiyat-fanni-mali-madan",
                "title": "صدور صلاحیت فنی و مالی",
                "sub": "تشکیل پرونده، ارزیابی امتیازات و اخذ گواهی صلاحیت فنی و مالی بهره‌برداران معدن.",
                "meta": "احراز صلاحیت معدن",
                "img": img_card2,
                "pos": "left center"
            }
        ]
    },
    {
        "id": "group-trade",
        "theme": "navy",  # 3. سورمه‌ای
        "overline": "خدمات تخصصی بخش سوم",
        "icon_svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3.5 9h17M3.5 15h17"/></svg>',
        "title": "تجارت بدون مرز و بازرگانی",
        "desc": "پوشش کامل خدمات بازرگانی داخلی و بین‌المللی در سامانه جامع تجارت؛ از صدور کارت بازرگانی و توکن تا ثبت سفارش و ترخیص کالا.",
        "btn_text": "درخواست مشاوره تجارت",
        "feature_img": img_1003,
        "feature_alt": "خدمات تخصصی تجارت، صادرات، واردات و ترخیص کالا",
        "slides": [
            {
                "slug": "kart-bazargani",
                "title": "صدور و تمدید کارت بازرگانی",
                "sub": "تشکیل پرونده در اتاق بازرگانی و سامانه جامع تجارت جهت صدور یا تمدید کارت بازرگانی.",
                "meta": "صادرات و واردات",
                "img": img_card3,
                "pos": "center center"
            },
            {
                "slug": "sabt-sefaresh",
                "title": "ثبت سفارش",
                "sub": "اخذ مجوز ثبت سفارش واردات کالاهای تجاری، مواد اولیه و ماشین‌آلات خطوط تولید.",
                "meta": "سامانه جامع تجارت",
                "img": img_hero,
                "pos": "left center"
            },
            {
                "slug": "tarkhis-kala",
                "title": "ترخیص کالا",
                "sub": "انجام تشریفات گمرکی، تنظیم اظهارنامه و پیگیری مراحل ترخیص کالا از گمرکات کشور.",
                "meta": "تشریفات گمرکی",
                "img": img_sub1,
                "pos": "center center"
            },
            {
                "slug": "sodor-tamdid-token",
                "title": "صدور و تمدید توکن",
                "sub": "اخذ و تمدید گواهی امضای الکترونیکی (توکن) جهت فعالیت در سامانه جامع تجارت و گمرک.",
                "meta": "امضای الکترونیکی",
                "img": img_sub5,
                "pos": "center center"
            },
            {
                "slug": "ijad-paye-haghighi-hoghoghi",
                "title": "ایجاد پایه حقیقی و حقوقی",
                "sub": "ثبت‌نام اولیه، احراز هویت و تشکیل پروفایل پایه اشخاص و شرکت‌ها در سامانه جامع تجارت.",
                "meta": "احراز هویت تجاری",
                "img": img_about,
                "pos": "center center"
            },
            {
                "slug": "ijad-code-naghsh",
                "title": "ایجاد کد نقش",
                "sub": "تعریف و فعال‌سازی نقش‌های تجاری، تولیدی و توزیعی متناسب با مجوزهای کسب‌وکار.",
                "meta": "فعال‌سازی نقش سامانه",
                "img": img_sub2,
                "pos": "center center"
            },
            {
                "slug": "darkhast-shenase",
                "title": "درخواست شناسه کالا",
                "sub": "ثبت مشخصات فنی کالاها و اخذ شناسه کالا جهت ثبت سفارش، تولید، انبارش یا فروش.",
                "meta": "شناسه رسمی کالا",
                "img": img_sub4,
                "pos": "center center"
            },
            {
                "slug": "sabt-anbar",
                "title": "ثبت انبار",
                "sub": "ثبت مشخصات مکانی و کد پستی انبارها و مراکز نگهداری کالا در سامانه جامع انبارها.",
                "meta": "سامانه جامع انبارها",
                "img": img_card1,
                "pos": "center center"
            },
            {
                "slug": "ersal-amar-tejarat",
                "title": "ارسال آمار",
                "sub": "ثبت مستندات خرید، فروش، حواله‌ها و موجودی کالا در زیرسامانه‌های تجاری وزارت صمت.",
                "meta": "گزارش‌های دوره‌ای تجارت",
                "img": img_sub3,
                "pos": "center center"
            },
            {
                "slug": "amar-tolid",
                "title": "آمار تولید",
                "sub": "ثبت مستندات تولید ماهانه و سالانه واحدهای صنعتی جهت حفظ سهمیه‌ها و اعتبار مجوزها.",
                "meta": "ثبت عملکرد تولید",
                "img": img_card4,
                "pos": "center center"
            }
        ]
    },
    {
        "id": "group-engineering",
        "theme": "white",  # 4. سفید
        "overline": "خدمات تخصصی بخش چهارم",
        "icon_svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M4 18C4 13 7.6 9 12 9C16.4 9 20 13 20 18H4Z"/><path d="M2 18.5H22"/></svg>',
        "title": "فنی، مهندسی و ساختمان",
        "desc": "ارائه خدمات تخصصی مهندسی از طراحی سازه و نقشه‌برداری دقیق تا ساخت سوله کارخانه، دکوراسیون داخلی و پیمانکاری کامل ساختمان.",
        "btn_text": "درخواست مشاوره مهندسی",
        "feature_img": img_1004,
        "feature_alt": "خدمات تخصصی فنی و مهندسی، سازه و سوله کارخانه",
        "slides": [
            {
                "slug": "structural-design",
                "title": "طراحی سازه ساختمان",
                "sub": "طراحی و محاسبات سازه‌های فولادی و بتنی متناسب با مشخصات پروژه و ضوابط فنی مقررات ملی.",
                "meta": "محاسبات و نقشه‌های سازه",
                "img": img_card4,
                "pos": "center center"
            },
            {
                "slug": "industrial-shed",
                "title": "طراحی و اجرای سوله کارخانه",
                "sub": "طراحی مهندسی دهانه و سازه، ساخت اسکلت فلزی و اجرای کامل سوله‌های صنعتی و تولیدی.",
                "meta": "سوله و سازه صنعتی",
                "img": img_sub4,
                "pos": "center center"
            },
            {
                "slug": "surveying",
                "title": "نقشه‌برداری",
                "sub": "برداشت توپوگرافی، تهیه اطلاعات مکانی اراضی و پیاده‌سازی دقیق محورهای اجرایی ساختمان و عمرانی.",
                "meta": "اطلاعات مکانی و عمرانی",
                "img": img_sub3,
                "pos": "center center"
            },
            {
                "slug": "interior-design",
                "title": "دکوراسیون",
                "sub": "طراحی سه‌بعدی و اجرای دکوراسیون داخلی فضاهای اداری، تجاری و ساختمانی متناسب با سبک پروژه.",
                "meta": "طراحی و معماری داخلی",
                "img": img_sub5,
                "pos": "center center"
            },
            {
                "slug": "building-contractor",
                "title": "پیمانکاری صفر تا صد ساختمان",
                "sub": "مدیریت و اجرای کامل مراحل پروژه ساختمانی از فونداسیون و اسکلت تا نازک‌کاری و تحویل نهایی.",
                "meta": "مدیریت و اجرای ساختمان",
                "img": img_sub1,
                "pos": "center center"
            }
        ]
    },
    {
        "id": "group-other-services",
        "theme": "navy",  # 6. سرمه‌ای (تغییر از سفید به سرمه‌ای)
        "overline": "خدمات تخصصی بخش ششم",
        "icon_svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v20M2 12h20"/></svg>',
        "title": "سایر خدمات",
        "desc": "خدمات متنوع و تکمیلی شامل صدور پروانه کسب اصناف، گواهی عدم سوء پیشینه، تائید پلیس اماکن، پروانه مشاغل خانگی، ثبت نام سوخت، امور مالیاتی، ثبت نام تحصیلات و مشاغل پشتیوانی خانگی.",
        "btn_text": "درخواست مشاوره سایر خدمات",
        "feature_img": img_hero,
        "feature_alt": "خدمات متنوع و تکمیلی Other Services",
        "slides": [
            {
                "slug": "sodor-parvane-kasb-asanf",
                "title": "صدور پروانه کسب اصناف",
                "sub": "اخذ پروانه کسب رسمی برای افراد و واحدهای صنایع اصنافی و تجاری در Monthly",
                "meta": "پروانه کسب اصناف",
                "img": img_card1,
                "pos": "center center"
            },
            {
                "slug": "goahi-adi-sooeh-payineh",
                "title": "گواهی عدم سوء پیشینه / کد رهگیری سامانه خود نویس",
                "sub": "اصدار گواهی عدم سوابق سوء و دریافت کد رهگیری در سامانه‌های خود نویس",
                "meta": "عدم سوء پیشینه",
                "img": img_sub1,
                "pos": "center center"
            },
            {
                "slug": "taeed-police-amaken",
                "title": "تائید پلیس اماکن",
                "sub": "دریافت تاییدیه پلیس اماکن برای محل کسب و کار و فعالیت‌های تجاری",
                "meta": "تایید پلیس اماکن",
                "img": img_sub2,
                "pos": "center center"
            },
            {
                "slug": "parvane-moshagh-khaneghi",
                "title": "پروانه مشاغل خانگی",
                "sub": "اخذ پروانه رسمی برای انجام مشاغل خانگی و کارگاه‌های کوچک خانگی",
                "meta": "مشاغل خانگی",
                "img": img_sub3,
                "pos": "center center"
            },
            {
                "slug": "sabt-nam-sookht",
                "title": "ثبت نام سوخت",
                "sub": "ثبت‌نام در سامانه تخصیص سوخت برای وسایل نقلیه و ماشین‌آلات",
                "meta": "ثبت نام سوخت",
                "img": img_sub4,
                "pos": "center center"
            },
            {
                "slug": "omorat-maliati",
                "title": "انجام امور مالیاتی",
                "sub": "مراجعه و انجام کلیه امور مالیاتی و تیکس در ادارات مربوطه",
                "meta": "امور مالیاتی",
                "img": img_sub5,
                "pos": "center center"
            },
            {
                "slug": "sabt-nam-tahsilat",
                "title": "ثبت نام تحصیلات",
                "sub": "ثبت‌نام در نظام‌های تحصیلی و آموزش عالی برایadaan و کارکنان",
                "meta": "ثبت نام تحصیلات",
                "img": img_card2,
                "pos": "center center"
            },
            {
                "slug": "moshagh-postevani-khaneghi",
                "title": "مشاغل پشتیوانی خانگی",
                "sub": "ارائه خدمات مشاغل پشتیوانی از طریق کارگاه‌های خانگی و خانوادگی",
                "meta": "مشاغل خانگی",
                "img": img_card3,
                "pos": "center center"
            }
        ]
    },
    {
        "id": "group-registration",
        "theme": "white",  # 7. سفید (تغییر از سرمه‌ای به سفید)
        "overline": "خدمات تخصصی بخش پنجم",
        "icon_svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="4" y="3" width="10" height="18"/><path d="M14 9h6v12h-6"/></svg>',
        "title": "ثبتی، مالی و توسعه کسب‌وکار",
        "desc": "پشتیبانی جامع حقوقی، ثبتی، مالی و محتوایی از شرکت‌ها؛ شامل ثبت شرکت، ثبت برند، طرح توجیهی، حسابرسی و طراحی و محاسبات.",
        "btn_text": "درخواست مشاوره کسب‌وکار",
        "feature_img": img_about,
        "feature_alt": "خدمات ثبت شرکت، ثبت برند، طرح توجیهی و حسابرسی",
        "slides": [
            {
                "slug": "company-registration",
                "title": "ثبت شرکت",
                "sub": "مشاوره انتخاب قالب حقوقی، تنظیم اساسنامه و اوراق ثبتی و پیگیری ثبت شرکت و تغییرات.",
                "meta": "امور ثبتی شرکت‌ها",
                "img": img_sub4,
                "pos": "left center"
            },
            {
                "slug": "brand-registration",
                "title": "ثبت برند و علامت تجاری",
                "sub": "استعلام تخصصی پیش از ثبت، تعیین طبقات و پیگیری مراحل قانونی تا صدور گواهی ثبت برند.",
                "meta": "مالکیت معنوی و برند",
                "img": img_about,
                "pos": "center center"
            },
            {
                "slug": "feasibility-study",
                "title": "تهیه طرح توجیهی صنعتی",
                "sub": "تدوین تخصصی طرح توجیهی فنی، مالی و اقتصادی جهت ارائه به بانک‌ها، سازمان‌ها و سرمایه‌گذاران.",
                "meta": "امکان‌سنجی فنی و مالی",
                "img": img_sub5,
                "pos": "center center"
            },
            {
                "slug": "auditing-services",
                "title": "خدمات حسابرسی",
                "sub": "بررسی اسناد و صورت‌های مالی، تنظیم گزارش‌های حسابرسی و مشاوره مالیاتی واحدهای صنعتی و تجاری.",
                "meta": "مالی و حسابرسی",
                "img": img_card1,
                "pos": "center center"
            },
            {
                "slug": "engineering-design-calculation",
                "title": "طراحی و محاسبات تخصصی",
                "sub": "انجام محاسبات فنی و مهندسی، طراحی فرآیندها و جانمایی ماشین‌آلات خطوط تولید کارخانه.",
                "meta": "طراحی و مهندسی صنعتی",
                "img": img_sub2,
                "pos": "center center"
            },
            {
                "slug": "content-production",
                "title": "تولید محتوا و خدمات محتوایی",
                "sub": "تدوین محتوای تخصصی متنی و تصویری جهت معرفی خدمات، کاتالوگ صنعتی و درگاه‌های ارتباطی.",
                "meta": "محتوای تخصصی کسب‌وکار",
                "img": img_hero,
                "pos": "right center"
            },
            {
                "slug": "license-consulting",
                "title": "مشاوره و پیگیری جامع مجوزها",
                "sub": "بررسی دقیق نوع فعالیت متقاضی، تشخیص پیش‌نیازهای قانونی و پیگیری مرحله‌به‌مرحله پرونده‌ها.",
                "meta": "پیگیری امور اداری و مجوز",
                "img": img_card3,
                "pos": "center center"
            }
        ]
    }
]

FAQ_ITEMS = [
    {
        "cat": "صنعت و مجوزها",
        "q": "برای دریافت جواز تأسیس چه مدارکی لازم است؟",
        "a": "برای اشخاص حقیقی مدارک هویتی (شناسنامه، کارت ملی و وضعیت نظام وظیفه) و برای اشخاص حقوقی اساسنامه، آگهی تأسیس، روزنامه رسمی، آخرین تغییرات شرکت و مدارک هویتی صاحبان امضا به همراه مشخصات طرح تولیدی، فهرست ماشین‌آلات و کد ISIC محصول موردنیاز است."
    },
    {
        "cat": "صنعت و مجوزها",
        "q": "تفاوت جواز تأسیس و پروانه بهره‌برداری چیست؟",
        "a": "جواز تأسیس مجوز موافقت اولیه برای احداث واحد تولیدی، تخصیص زمین در شهرک‌های صنعتی و نصب ماشین‌آلات است؛ اما پروانه بهره‌برداری پس از اتمام ساخت‌وساز، نصب تجهیزات، تأمین نیروی انسانی و تولید آزمایشی صادر می‌شود و مجوز رسمی شروع بهره‌برداری و تولید واحد صنعتی است."
    },
    {
        "cat": "صنعت و مجوزها",
        "q": "طرح توجیهی صنعتی چه کاربردی دارد؟",
        "a": "طرح توجیهی صنعتی ابعاد فنی، بازار و مالی پروژه را به صورت مستند بررسی می‌کند تا توجیه‌پذیری اجرای طرح مشخص شود. این سند برای اخذ جواز تأسیس، پذیرش در شهرک‌های صنعتی، جذب سرمایه‌گذار و بررسی پرونده‌های تسهیلات بانکی کاربرد مستقیم دارد."
    },
    {
        "cat": "ثبتی و کسب‌وکار",
        "q": "ثبت شرکت و ثبت برند چه تفاوتی دارند؟",
        "a": "ثبت شرکت به معنای ایجاد یک شخصیت حقوقی رسمی (مانند سهامی خاص یا با مسئولیت محدود) برای فعالیت قانونی کسب‌وکار است؛ در حالی که ثبت برند (علامت تجاری) برای حفاظت قانونی از نام و نشان تجاری محصولات یا خدمات شما در برابر استفاده سایرین انجام می‌شود."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "طراحی سازه ساختمان شامل چه مراحلی است؟",
        "a": "شامل بررسی نقشه‌های معماری و مشخصات ژئوتکنیکی زمین، انتخاب سیستم سازه‌ای متناسب با پروژه، بارگذاری و تحلیل سازه بر اساس ضوابط فنی و مقررات ملی ساختمان، طراحی مقاطع و اتصالات، و در نهایت تهیه نقشه‌های اجرایی سازه و دفترچه محاسبات است."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "برای طراحی و اجرای سوله صنعتی چه اطلاعاتی لازم است؟",
        "a": "ابعاد زمین، عرض دهانه و طول سوله، ارتفاع مفید موردنیاز، نوع کاربری صنعتی یا انبارداری، نیاز به جرثقیل سقفی و ظرفیت آن، و شرایط اقلیمی محل اجرا (بار باد و برف) از اطلاعات اصلی برای طراحی و اجرای سوله کارخانه هستند."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "نقشه‌برداری در پروژه‌های ساختمانی چه کاربردی دارد؟",
        "a": "نقشه‌برداری برای برداشت وضع موجود زمین، تعیین دقیق حدود و مختصات ملک، تهیه نقشه‌های توپوگرافی، محاسبه احجام عملیات خاکی و پیاده‌سازی دقیق محورهای فونداسیون، ستون‌ها و ترازهای اجرایی ساختمان در طول پروژه به کار می‌رود."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "پیمانکاری صفر تا صد ساختمان شامل چه خدماتی می‌شود؟",
        "a": "شامل برنامه‌ریزی، هماهنگی و اجرای مراحل پروژه ساختمانی از آماده‌سازی کارگاه، عملیات خاکی و فونداسیون تا اجرای اسکلت، سفت‌کاری، تأسیسات مکانیکی و برقی، نازک‌کاری و تکمیل پروژه مطابق با قرارداد و محدوده خدمات مورد توافق با کارفرما است."
    },
    {
        "cat": "عمومی و مشاوره",
        "q": "چگونه می‌توان درخواست مشاوره ثبت کرد؟",
        "a": "شما می‌توانید از طریق دکمه «درخواست مشاوره» در هدر سایت یا فرم ثبت درخواست در همین صفحه، موضوع فعالیت و شماره تماس خود را وارد کنید و یا در ساعات پاسخگویی (۸ الی ۱۶) با شماره ۰۹۱۷۷۰۵۶۰۶۳ تماس بگیرید."
    }
]

# Scoped CSS for the Comprehensive Services Page including the exact 6-Band Reference Layout
services_page_css = '''
/* ==========================================================================
   Comprehensive Services Page Scoped Styles (.srv-*)
   ========================================================================== */
.srv-breadcrumb-bar {
  background: rgba(5, 21, 39, 0.96);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding: 10px 0;
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.78);
}

.srv-breadcrumb-list {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.srv-breadcrumb-list a {
  color: var(--orange-400);
  font-weight: 700;
}

.srv-breadcrumb-list a:hover {
  text-decoration: underline;
}

/* 1. SERVICES HERO BANNER */
.srv-hero {
  position: relative;
  min-height: 360px;
  background-color: var(--navy-950);
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  padding: 44px 0 60px;
  overflow: hidden;
}

.srv-hero-backdrop {
  position: absolute;
  inset: 0;
  background:
    /* Left-side highlight for title area - professional accent without obscuring image */
    linear-gradient(90deg, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.08) 28%, rgba(245, 158, 11, 0) 55%),
    /* Dark overlay for text readability - keeps brand navy tones */
    linear-gradient(90deg, rgba(4, 18, 34, 0.82) 0%, rgba(6, 24, 46, 0.72) 45%, rgba(6, 24, 46, 0.55) 100%),
    /* Subtle radial accent */
    radial-gradient(circle at 22% 35%, rgba(245, 158, 11, 0.16) 0%, rgba(5, 21, 39, 0) 48%);
  pointer-events: none;
}

.srv-hero-grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.25fr 0.95fr;
  gap: 36px;
  align-items: center;
}

.srv-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(245, 158, 11, 0.14);
  border: 1px solid rgba(251, 191, 36, 0.45);
  color: var(--orange-400);
  font-size: 13px;
  font-weight: 800;
  padding: 6px 16px;
  border-radius: 999px;
  margin-bottom: 14px;
}

.srv-hero-h1 {
  font-size: 35px;
  font-weight: 900;
  color: var(--white);
  line-height: 1.38;
  margin-bottom: 14px;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.srv-hero-lead {
  font-size: 14.5px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.92);
  line-height: 1.95;
  margin-bottom: 24px;
  max-width: 640px;
}

.srv-hero-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}

.srv-btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, #fbbf24 0%, #f4810b 100%);
  color: var(--navy-950);
  font-size: 14px;
  font-weight: 900;
  padding: 11px 26px;
  border-radius: 999px;
  box-shadow: 0 10px 26px rgba(244, 129, 11, 0.38);
  transition: all 0.25s ease;
}

.srv-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 32px rgba(244, 129, 11, 0.55);
}

.srv-btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid rgba(251, 191, 36, 0.65);
  color: var(--white);
  font-size: 14px;
  font-weight: 800;
  padding: 10px 24px;
  border-radius: 999px;
  backdrop-filter: blur(6px);
  transition: all 0.25s ease;
}

.srv-btn-secondary:hover {
  background: var(--orange-500);
  border-color: var(--orange-500);
  color: var(--navy-950);
  transform: translateY(-2px);
}

.srv-hero-3d-showcase {
  perspective: 1100px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.srv-hero-mini-card {
  background: rgba(9, 33, 61, 0.78);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 14px;
  padding: 9px;
  backdrop-filter: blur(10px);
  box-shadow: 0 16px 34px rgba(0, 0, 0, 0.35);
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.srv-hero-mini-card:hover {
  transform: translateY(-4px);
  border-color: var(--orange-400);
}

.srv-hero-mini-card img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: 9px;
  display: block;
  margin-bottom: 7px;
}

.srv-hero-mini-card span {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-size: 11.8px;
  font-weight: 800;
  color: var(--white);
}

/* 2. QUICK FILTER & SEARCH BAR */
.srv-filter-bar-wrap {
  margin-top: -24px;
  position: relative;
  z-index: 10;
  margin-bottom: 24px;
}

.srv-filter-bar {
  background: var(--white);
  border-radius: 18px;
  padding: 14px 20px;
  box-shadow: 0 16px 42px rgba(6, 24, 46, 0.12);
  border: 1px solid #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
}

.srv-filter-pills {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.srv-filter-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: 999px;
  font-size: 12.5px;
  font-weight: 800;
  color: var(--navy-850);
  background: #f1f5f9;
  transition: all 0.2s ease;
}

.srv-filter-pill svg {
  width: 15px;
  height: 15px;
  color: var(--orange-500);
}

.srv-filter-pill:hover,
.srv-filter-pill.active {
  background: var(--navy-850);
  color: var(--orange-400);
}

.srv-inline-search {
  position: relative;
  min-width: 240px;
  flex: 1;
  max-width: 310px;
}

.srv-inline-search input {
  width: 100%;
  padding: 8px 16px;
  border-radius: 999px;
  border: 1.5px solid #cbd5e1;
  font-family: inherit;
  font-size: 12.8px;
  background: #f8fafc;
}

.srv-inline-search input:focus {
  outline: none;
  border-color: var(--orange-500);
  background: var(--white);
}

/* ==========================================================================
   3. THE 5 STACKED SHOWCASE BANDS (Matching Uploaded Reference Image!)
   Alternating Dark Navy (#031326) & Crisp White (#ffffff)
   ========================================================================== */
.srv-bands-stack {
  display: flex;
  flex-direction: column;
  gap: 0;
  width: 100%;
}

.srv-band {
  position: relative;
  width: 100%;
  min-height: 365px;
  display: flex;
  align-items: stretch;
  overflow: hidden;
  border-top: 1px solid rgba(56, 189, 248, 0.16);
  border-bottom: 1px solid rgba(56, 189, 248, 0.16);
}

/* Theme 1: Dark Navy Band */
.srv-band.theme-navy {
  background: linear-gradient(90deg, #020d1c 0%, #051930 58%, #07203d 100%);
  color: var(--white);
}

/* Theme 2: Crisp White Band */
.srv-band.theme-white {
  background: linear-gradient(90deg, #ffffff 0%, #f8fbff 60%, #eef5fc 100%);
  color: var(--navy-900);
  border-top: 1px solid #dbe4f0;
  border-bottom: 1px solid #dbe4f0;
}

.srv-band-inner {
  width: 100%;
  max-width: 1360px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 295px 255px 1fr;
  align-items: stretch;
  direction: rtl;
}

/* Zone 1 (Right): Full-Height Feature Photo — No Overlays, Filters, or Shadows */
.srv-band-photo-col {
  position: relative;
  overflow: hidden;
  min-height: 355px;
}

.srv-band-photo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform 0.6s ease;
  filter: none;
  box-shadow: none;
}

.srv-band:hover .srv-band-photo-img {
  transform: scale(1.04);
}

/* Zone 2 (Middle-Right): Category Overline, H2 Title, Description, Pill Button & Slider Controls */
.srv-band-info-col {
  padding: 34px 22px 30px 18px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  z-index: 2;
}

.srv-band-overline {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: 0.3px;
  margin-bottom: 10px;
}

.srv-band.theme-navy .srv-band-overline {
  color: #93c5fd;
}

.srv-band.theme-white .srv-band-overline {
  color: var(--orange-600);
}

.srv-band-overline svg {
  color: var(--orange-400);
  flex-shrink: 0;
}

.srv-band.theme-white .srv-band-overline svg {
  color: var(--orange-500);
}

.srv-band-h2 {
  font-size: 24px;
  font-weight: 900;
  line-height: 1.32;
  margin-bottom: 12px;
}

.srv-band.theme-navy .srv-band-h2 {
  color: var(--white);
}

.srv-band.theme-white .srv-band-h2 {
  color: var(--navy-900);
}

.srv-band-desc {
  font-size: 12.2px;
  font-weight: 500;
  line-height: 1.85;
  margin-bottom: 20px;
}

.srv-band.theme-navy .srv-band-desc {
  color: rgba(226, 232, 240, 0.86);
}

.srv-band.theme-white .srv-band-desc {
  color: var(--slate-600);
}

.srv-band-actions-row {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

/* Pill outline button matching "View All Countries ->" in the reference image */
.srv-band-pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 18px;
  border-radius: 999px;
  font-size: 11.8px;
  font-weight: 800;
  transition: all 0.25s ease;
}

.srv-band.theme-navy .srv-band-pill-btn {
  border: 1px solid rgba(148, 163, 184, 0.48);
  color: var(--white);
  background: rgba(255, 255, 255, 0.04);
}

.srv-band.theme-navy .srv-band-pill-btn:hover {
  border-color: var(--orange-400);
  background: var(--orange-500);
  color: var(--navy-950);
}

.srv-band.theme-white .srv-band-pill-btn {
  border: 1.5px solid var(--navy-850);
  color: var(--navy-850);
  background: transparent;
}

.srv-band.theme-white .srv-band-pill-btn:hover {
  border-color: var(--orange-500);
  background: var(--orange-500);
  color: var(--white);
}

/* Slider Prev/Next Navigation Buttons & Slide Count Indicator */
.srv-band-slider-nav {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 12px;
}

.srv-slide-arrow {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  font-weight: 900;
  transition: all 0.2s ease;
}

.srv-band.theme-navy .srv-slide-arrow {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.22);
  color: var(--white);
}

.srv-band.theme-navy .srv-slide-arrow:hover {
  background: var(--orange-500);
  border-color: var(--orange-500);
  color: var(--navy-950);
}

.srv-band.theme-white .srv-slide-arrow {
  background: #f1f5f9;
  border: 1px solid #cbd5e1;
  color: var(--navy-850);
}

.srv-band.theme-white .srv-slide-arrow:hover {
  background: var(--navy-850);
  border-color: var(--navy-850);
  color: var(--orange-400);
}

.srv-slide-count-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 999px;
}

.srv-band.theme-navy .srv-slide-count-badge {
  color: var(--orange-400);
  background: rgba(251, 191, 36, 0.12);
}

.srv-band.theme-white .srv-slide-count-badge {
  color: var(--navy-850);
  background: #e2e8f0;
}

/* Zone 3 (Left): Horizontal 5-Card Slider Track matching the Reference Image */
.srv-band-slider-col {
  padding: 28px 12px 28px 24px;
  display: flex;
  align-items: center;
  overflow: hidden;
  position: relative;
}

.srv-band-track {
  display: flex;
  align-items: stretch;
  gap: 12px;
  overflow-x: auto;
  scroll-behavior: smooth;
  scrollbar-width: none;
  -ms-overflow-style: none;
  padding: 6px 2px 10px;
  width: 100%;
}

.srv-band-track::-webkit-scrollbar {
  display: none;
}

/* Individual Vertical Slide Card - Image Top + Title Below (RTL) */
.srv-slide-card {
  flex: 0 0 146px;
  width: 146px;
  min-height: 272px;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), border-color 0.3s ease;
  cursor: pointer;
}

.srv-band.theme-navy .srv-slide-card {
  background: linear-gradient(180deg, #072241 0%, #041529 100%);
  border: 1px solid rgba(56, 189, 248, 0.16);
  box-shadow: none;
}

.srv-band.theme-navy .srv-slide-card:hover {
  transform: translateY(-6px);
  border-color: var(--orange-400);
  box-shadow: none;
}

.srv-band.theme-white .srv-slide-card {
  background: var(--white);
  border: 1px solid #cbd5e1;
  box-shadow: none;
}

.srv-band.theme-white .srv-slide-card:hover {
  transform: translateY(-6px);
  border-color: var(--orange-500);
  box-shadow: none;
}

/* Top Image Box of Slide Card */
.srv-slide-img-wrap {
  position: relative;
  width: 100%;
  height: 138px;
  overflow: hidden;
  background: #041527;
  flex-shrink: 0;
}

.srv-slide-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: none;
  box-shadow: none;
  transition: transform 0.45s ease;
}

.srv-slide-card:hover .srv-slide-img {
  transform: scale(1.07);
}

/* Bottom Text Box of Slide Card */
.srv-slide-body {
  padding: 11px 11px 12px;
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: space-between;
}

.srv-slide-title {
  font-size: 12.8px;
  font-weight: 900;
  line-height: 1.4;
  margin-bottom: 6px;
}

.srv-band.theme-navy .srv-slide-title {
  color: var(--white);
}

.srv-band.theme-white .srv-slide-title {
  color: var(--navy-900);
}

.srv-slide-sub {
  font-size: 10.6px;
  font-weight: 500;
  line-height: 1.68;
  margin-bottom: 10px;
  flex: 1;
}

.srv-band.theme-navy .srv-slide-sub {
  color: rgba(203, 213, 225, 0.88);
}

.srv-band.theme-white .srv-slide-sub {
  color: var(--slate-600);
}

.srv-slide-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 4px;
  padding-top: 6px;
  border-top: 1px solid rgba(148, 163, 184, 0.15);
}

.srv-band.theme-white .srv-slide-footer {
  border-top-color: #e2e8f0;
}

.srv-slide-meta {
  font-size: 9.8px;
  font-weight: 700;
}

.srv-band.theme-navy .srv-slide-meta {
  color: #93c5fd;
}

.srv-band.theme-white .srv-slide-meta {
  color: var(--orange-600);
}

.srv-slide-arrow-icon {
  font-size: 13px;
  font-weight: 900;
  line-height: 1;
  transition: transform 0.2s ease;
}

.srv-band.theme-navy .srv-slide-arrow-icon {
  color: var(--orange-400);
}

.srv-band.theme-white .srv-slide-arrow-icon {
  color: var(--navy-850);
}

.srv-slide-card:hover .srv-slide-arrow-icon {
  transform: translateX(-3px);
  color: var(--orange-500);
}

/* 4. 5-STEP PROCESS SECTION ("مسیر دریافت خدمات") */
.srv-process-section {
  padding: 52px 0;
  background: linear-gradient(180deg, #eef4fb 0%, #f6f9fc 100%);
}

.srv-process-tabs {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.srv-process-tab {
  padding: 10px 22px;
  border-radius: 999px;
  font-size: 13.5px;
  font-weight: 800;
  background: var(--white);
  color: var(--navy-850);
  border: 1.5px solid #cbd5e1;
  transition: all 0.2s ease;
}

.srv-process-tab.active {
  background: var(--navy-850);
  color: var(--orange-400);
  border-color: var(--navy-850);
  box-shadow: 0 8px 20px rgba(6, 24, 46, 0.18);
}

.srv-steps-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 18px;
  position: relative;
}

.srv-step-card {
  background: var(--white);
  border-radius: 18px;
  padding: 24px 18px;
  text-align: center;
  border: 1px solid #e2e8f0;
  box-shadow: 0 10px 28px rgba(6, 24, 46, 0.06);
  position: relative;
  transition: transform 0.25s ease;
}

.srv-step-card:hover {
  transform: translateY(-5px);
  border-color: var(--orange-450);
}

.srv-step-num {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg, #fbbf24 0%, #f4810b 100%);
  color: var(--navy-950);
  font-size: 20px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
  box-shadow: 0 6px 16px rgba(244, 129, 11, 0.35);
}

.srv-step-title {
  font-size: 15px;
  font-weight: 900;
  color: var(--navy-850);
  margin-bottom: 8px;
}

.srv-step-desc {
  font-size: 12.5px;
  font-weight: 500;
  color: var(--slate-600);
  line-height: 1.85;
}

/* 5. FAQ ACCORDION SECTION ("پرسش‌های متداول") */
.srv-faq-section {
  padding: 52px 0;
  background: var(--white);
}

.srv-faq-list {
  max-width: 920px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.srv-faq-item {
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  background: #f8fafc;
  overflow: hidden;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}

.srv-faq-item.open {
  border-color: var(--orange-450);
  background: var(--white);
  box-shadow: 0 8px 24px rgba(6, 24, 46, 0.06);
}

.srv-faq-question {
  width: 100%;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  text-align: right;
  font-size: 14.5px;
  font-weight: 800;
  color: var(--navy-850);
}

.srv-faq-cat-tag {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 999px;
  background: rgba(244, 129, 11, 0.14);
  color: var(--orange-600);
  margin-left: 8px;
}

.srv-faq-answer {
  display: none;
  padding: 0 20px 18px;
  font-size: 13.5px;
  font-weight: 500;
  color: var(--slate-700);
  line-height: 2;
  border-top: 1px solid #f1f5f9;
}

.srv-faq-item.open .srv-faq-answer {
  display: block;
}
'''

# Build HTML for the 6 Stacked Showcase Bands (Navy / White / Navy / White / Navy)
bands_html = ""
for band in SIX_SHOWCASE_BANDS:
    slides_markup = ""
    PALETTE = ["navy-600", "orange-500", "teal-500", "slate-600", "navy-800", "orange-600"]
    for idx, s in enumerate(band["slides"]):
        # Pick varied filter/crop from VISUAL_POOL if needed
        s["color_idx"] = PALETTE[idx % len(PALETTE)]
        slides_markup += f'''
          <a href="services/{s['slug']}/index.html" class="srv-slide-card" data-service-slug="{s['slug']}" data-service-title="{s['title']}" data-service-desc="{s['sub']}">
            <div class="srv-slide-img-wrap">
              <img src="{s['img']}" alt="{s['title']}" class="srv-slide-img" style="object-position:{s['pos']};" loading="lazy" />
            </div>
            <div class="srv-slide-body">
              <div>
                <h3 class="srv-slide-title" data-editable="true">{s['title']}</h3>
                <p class="srv-slide-sub" data-editable="true">{s['sub']}</p>
              </div>
              <div class="srv-slide-footer">
                <span class="srv-slide-meta" data-editable="true">{s['meta']}</span>
                <span class="srv-slide-arrow-icon" aria-hidden="true">←</span>
              </div>
            </div>
          </a>
        '''

    total_slides = len(band["slides"])
    bands_html += f'''
      <section class="srv-band theme-{band['theme']}" id="{band['id']}">
        <div class="srv-band-inner">
          <!-- Right Column: Dramatic Industrial/Engineering Feature Photo -->
          <div class="srv-band-photo-col">
            <img src="{band['feature_img']}" alt="{band['feature_alt']}" class="srv-band-photo-img" loading="lazy" />
          </div>

          <!-- Middle-Right Column: Overline + Icon, H2 Heading, Description, Pill CTA & Slider Arrows -->
          <div class="srv-band-info-col">
            <div class="srv-band-overline">
              {band['icon_svg']}
              <span data-editable="true">{band['overline']}</span>
            </div>
            <h2 class="srv-band-h2" data-editable="true">{band['title']}</h2>
            <p class="srv-band-desc" data-editable="true">{band['desc']}</p>
            <div class="srv-band-actions-row">
              <button type="button" class="srv-band-pill-btn" data-open-consult="true">
                <span data-editable="true">{band['btn_text']}</span>
                <span aria-hidden="true">←</span>
              </button>
            </div>
            <div class="srv-band-slider-nav">
              <button type="button" class="srv-slide-arrow" data-band-prev="{band['id']}" aria-label="اسلایدهای قبلی" title="مشاهده موارد قبلی">›</button>
              <button type="button" class="srv-slide-arrow" data-band-next="{band['id']}" aria-label="اسلایدهای بعدی" title="مشاهده موارد بعدی">‹</button>
              <span class="srv-slide-count-badge">{total_slides} زیرمجموعه تخصصی</span>
            </div>
          </div>

          <!-- Left Column: Horizontal 5-Card Slider Track -->
          <div class="srv-band-slider-col">
            <div class="srv-band-track" id="track-{band['id']}">
              {slides_markup}
            </div>
          </div>
        </div>
      </section>
    '''

# Build FAQ HTML
faq_html = ""
for idx, f in enumerate(FAQ_ITEMS):
    open_cls = "open" if idx == 0 else ""
    faq_html += f'''
      <div class="srv-faq-item {open_cls}">
        <button type="button" class="srv-faq-question">
          <span>
            <span class="srv-faq-cat-tag">{f['cat']}</span>
            <span data-editable="true">{f['q']}</span>
          </span>
          <span class="srv-faq-icon" style="color:#f59e0b;font-size:18px;font-weight:900;">{('−' if idx == 0 else '+')}</span>
        </button>
        <div class="srv-faq-answer" data-editable="true">
          {f['a']}
        </div>
      </div>
    '''

services_html_doc = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width={desktop_viewport_width}, minimum-scale=0.1" />
  <title>صفحه جامع خدمات | سایت دلگشا - هلدینگ راه‌گشا (صنعت، معدن، تجارت و فنی و مهندسی)</title>
  <meta name="description" content="خدمات تخصصی صنعت، معدن، تجارت و فنی و مهندسی در سایت دلگشا متعلق به هلدینگ راه‌گشا؛ از اخذ مجوزهای صنعتی و تجاری تا طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری و پیمانکاری ساختمان." />
  <link rel="icon" type="image/png" href="{img_logo}" />
  <style>
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_regular}') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_medium}') format('woff2');
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_bold}') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_extrabold}') format('woff2');
      font-weight: 800;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_black}') format('woff2');
      font-weight: 900;
      font-style: normal;
      font-display: swap;
    }}
    {base_styles}
    {services_page_css}
  </style>
</head>
<body id="top">

  <!-- ====================================================================
       1. IDENTICAL SITE HEADER (Connected to Our Designed Homepage index.html)
       ==================================================================== -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" data-switch-page="home" class="brand-logo" aria-label="بازگشت به صفحه اصلی سایت دلگشا">
        <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
        <div class="brand-text-stack">
          <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
          <span class="brand-subtitle" data-editable="true">هلدینگ توسعه صنعت و معدن و تجارت</span>
        </div>
        <img src="{img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
      </a>

      <nav class="main-nav" aria-label="منوی اصلی">
        <a href="index.html" data-switch-page="home" class="nav-link">صفحه اصلی</a>
        <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="nav-link">خدمات ما (صفحه اصلی)</a>
        <a href="#services-catalog" class="nav-link active">صفحه جامع خدمات</a>
        <a href="#group-engineering" class="nav-link">فنی و مهندسی</a>
        <a href="#service-process" class="nav-link">مسیر دریافت خدمات</a>
        <a href="#faq-section" class="nav-link">پرسش‌های متداول</a>
        <a href="#footer" class="nav-link">تماس با ما</a>
      </nav>

      <div class="header-actions">
        <button type="button" class="btn-consult" data-open-consult="true">
          <span class="btn-consult-avatar" aria-hidden="true">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 12c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm0 2c-3.33 0-10 1.67-10 5v3h20v-3c0-3.33-6.67-5-10-5z"/>
            </svg>
          </span>
          <span data-editable="true">درخواست مشاوره</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Breadcrumb Bar with Direct Internal Link to Our Designed Homepage & Services Section -->
  <nav class="srv-breadcrumb-bar" aria-label="مسیر راهنما">
    <div class="container srv-breadcrumb-list">
      <a href="index.html" data-switch-page="home">صفحه اصلی (سایت دلگشا | هلدینگ راه‌گشا)</a>
      <span>‹</span>
      <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" style="color:#93c5fd;">بخش خدمات ما در صفحه اصلی</a>
      <span>‹</span>
      <span aria-current="page">صفحه جامع خدمات تخصصی</span>
    </div>
  </nav>

  <!-- ====================================================================
       2. CINEMATIC 3D HERO BANNER (Single H1 for SEO)
       ==================================================================== -->
  <section class="srv-hero" style="background-image: url('{img_hero}');">
    <div class="srv-hero-backdrop"></div>
    <div class="container srv-hero-grid">
      <div>
        <span class="srv-hero-badge" data-editable="true">
          ✦ درگاه جامع خدمات سایت دلگشا | هلدینگ راه‌گشا
        </span>
        <h1 class="srv-hero-h1" data-editable="true">
          خدمات تخصصی صنعت، معدن، تجارت و فنی و مهندسی
        </h1>
        <p class="srv-hero-lead" data-editable="true">
          از اخذ مجوزهای صنعتی و تجاری تا طراحی و اجرای پروژه‌های ساختمانی و مهندسی، در مسیر توسعه کسب‌وکار و اجرای پروژه‌ها همراه شما هستیم.
        </p>
        <div class="srv-hero-actions">
          <a href="#services-catalog" class="srv-btn-primary">
            <span data-editable="true">مشاهده خدمات</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <polyline points="19 12 12 19 5 12"></polyline>
            </svg>
          </a>
          <a href="#contact-consult" class="srv-btn-secondary" data-open-consult="true">
            <span data-editable="true">درخواست مشاوره</span>
          </a>
        </div>
      </div>

      <!-- 3D Visual Preview Grid -->
      <div class="srv-hero-3d-showcase">
        <a href="#group-industry" class="srv-hero-mini-card">
          <img src="{img_sub1}" alt="خدمات صنعت و مجوزها" />
          <span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3"/></svg>
            صنعت و مجوزهای تولید
          </span>
        </a>
        <a href="#group-mining" class="srv-hero-mini-card">
          <img src="{img_sub2}" alt="خدمات معدن و کاداستر" />
          <span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><path d="M3 20L10 6L15 15L18 10L22 20H3Z"/></svg>
            معدن و سامانه کاداستر
          </span>
        </a>
        <a href="#group-trade" class="srv-hero-mini-card">
          <img src="{img_card3}" alt="خدمات تجارت و بازرگانی" />
          <span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/></svg>
            تجارت و بازرگانی
          </span>
        </a>
        <a href="#group-engineering" class="srv-hero-mini-card">
          <img src="{img_sub3}" alt="خدمات فنی و مهندسی" />
          <span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><path d="M4 18C4 13 7.6 9 12 9C16.4 9 20 13 20 18H4Z"/><path d="M2 18.5H22"/></svg>
            فنی، مهندسی و ساختمان
          </span>
        </a>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       3. QUICK CATEGORY FILTER & LIVE SEARCH BAR
       ==================================================================== -->
  <div class="container srv-filter-bar-wrap" id="services-catalog">
    <div class="srv-filter-bar">
      <div class="srv-filter-pills" role="navigation" aria-label="فیلتر دسته‌بندی خدمات">
        <a href="#services-catalog" class="srv-filter-pill active" data-filter-group="all">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>
          <span>همه ۵ بخش خدمات</span>
        </a>
        <a href="#group-industry" class="srv-filter-pill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3"/></svg>
          <span>صنعت (۱۲ خدمت)</span>
        </a>
        <a href="#group-mining" class="srv-filter-pill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M3 20L10 6L15 15L18 10L22 20H3Z"/></svg>
          <span>معدن (۱۱ خدمت)</span>
        </a>
        <a href="#group-trade" class="srv-filter-pill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/></svg>
          <span>تجارت (۱۰ خدمت)</span>
        </a>
        <a href="#group-engineering" class="srv-filter-pill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M4 18C4 13 7.6 9 12 9C16.4 9 20 13 20 18H4Z"/><path d="M2 18.5H22"/></svg>
          <span>فنی و مهندسی (۵ خدمت)</span>
        </a>
        <a href="#group-registration" class="srv-filter-pill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="4" y="3" width="10" height="18"/><path d="M14 9h6v12h-6"/></svg>
          <span>ثبتی، مالی و کسب‌وکار (۷ خدمت)</span>
        </a>
      </div>
      <div class="srv-inline-search">
        <input type="search" id="srvInlineSearchInput" placeholder="جستجوی سریع نام خدمت یا مجوز..." aria-label="جستجوی نام خدمت" />
      </div>
    </div>
  </div>

  <!-- ====================================================================
       4. THE 5 STACKED HORIZONTAL SHOWCASE BANDS (Navy / White / Navy / White / Navy)
       Matching the exact reference design with all sub-services & descriptions!
       ==================================================================== -->
  <main>
    <div class="srv-bands-stack">
      {bands_html}
    </div>

    <!-- ==================================================================
         5. 5-STEP SERVICE DELIVERY PROCESS ("مسیر دریافت خدمات")
         ================================================================== -->
    <section class="srv-process-section" id="service-process">
      <div class="container">
        <div class="subservices-header">
          <h2 class="subservices-title" data-editable="true">مسیر دریافت خدمات در هلدینگ راه‌گشا | دلگشا</h2>
          <p class="subservices-subtitle" data-editable="true">فرآیند شفاف، مرحله‌به‌مرحله و منظم از ثبت درخواست اولیه تا تحویل نهایی خدمت یا پروژه</p>
        </div>

        <div class="srv-process-tabs">
          <button type="button" class="srv-process-tab active" data-process-mode="licenses">
            مسیر دریافت خدمات مجوزها، صنعت، معدن و تجارت
          </button>
          <button type="button" class="srv-process-tab" data-process-mode="engineering">
            مسیر اجرایی خدمات فنی، مهندسی و پیمانکاری ساختمان
          </button>
        </div>

        <div class="srv-steps-grid" id="processStepsContainer">
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">ثبت درخواست و اعلام نیاز</h3>
            <p class="srv-step-desc" id="stepDesc1" data-editable="true">
              ثبت موضوع فعالیت یا مجوز موردنیاز از طریق فرم درخواست مشاوره یا تماس مستقیم با کارشناسان مجموعه.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">بررسی اولیه اطلاعات و مدارک</h3>
            <p class="srv-step-desc" id="stepDesc2" data-editable="true">
              بررسی مدارک هویتی، ثبتی یا فنی متقاضی، تطبیق با ضوابط قانونی و شناسایی پیش‌نیازهای سامانه مربوطه.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">مشاوره و تعیین مسیر اجرایی</h3>
            <p class="srv-step-desc" id="stepDesc3" data-editable="true">
              ارائه مشاوره تخصصی، شفاف‌سازی مراحل، زمان‌بندی، پیش‌نیازهای استعلامی و توافق بر محدوده خدمات.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">انجام یا پیگیری خدمات توافق‌شده</h3>
            <p class="srv-step-desc" id="stepDesc4" data-editable="true">
              ثبت درخواست در سامانه‌های رسمی، تدوین طرح‌ها یا نقشه‌ها و پیگیری منظم پرونده در مراجع ذی‌ربط.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">تحویل نتیجه و ارائه راهنمایی‌های لازم</h3>
            <p class="srv-step-desc" id="stepDesc5" data-editable="true">
              تحویل مجوز، پروانه، سند ثبتی یا مدارک فنی نهایی به همراه راهنمایی‌های کاربردی برای مراحل بعدی فعالیت.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================================================================
         6. REAL COLLABORATION ADVANTAGES ("مزیت‌های همکاری")
         ================================================================== -->
    <section class="about-section" id="collaboration-advantages" style="background-image: url('{img_about}');">
      <div class="about-overlay"></div>
      <div class="container about-grid">
        <div class="why-card">
          <h2 class="why-card-title" data-editable="true">مزیت‌های همکاری با ما</h2>
          <div class="why-list">
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><circle cx="12" cy="12" r="4"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">پوشش یکپارچه خدمات</h3>
                <p class="why-item-sub" data-editable="true">هماهنگی امور صنعت، معدن، تجارت، ثبت و مهندسی در یک مجموعه</p>
              </div>
            </div>
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">پیگیری منظم و مرحله‌به‌مرحله</h3>
                <p class="why-item-sub" data-editable="true">بررسی دقیق مدارک پیش از ثبت جهت جلوگیری از اتلاف زمان</p>
              </div>
            </div>
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">دانش تخصصی و تجربه اجرایی</h3>
                <p class="why-item-sub" data-editable="true">آشنایی با رویه‌های اداری، سامانه‌های تخصصی و ضوابط فنی پروژه‌ها</p>
              </div>
            </div>
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">مشاوره شفاف و کاربردی</h3>
                <p class="why-item-sub" data-editable="true">تعیین مسیر درست بر اساس شرایط واقعی متقاضی و نوع پروژه</p>
              </div>
            </div>
          </div>
        </div>

        <div class="about-content" id="contact-consult">
          <div class="about-header-with-line">
            <p class="about-overline" data-editable="true">همراهی از مجوز تا اجرا</p>
            <h2 class="about-title">
              <span data-editable="true">هماهنگی خدمات اداری،</span>
              <span data-editable="true">تجاری و مهندسی</span>
            </h2>
          </div>
          <p class="about-description" data-editable="true">
            در هلدینگ راه‌گشا (سایت دلگشا)، متقاضیان و کارفرمایان می‌توانند علاوه بر خدمات اخذ مجوزهای صنعتی، معدنی و بازرگانی، خدمات ثبت شرکت و برند، حسابرسی و همچنین خدمات فنی و مهندسی شامل طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری، دکوراسیون و پیمانکاری ساختمان را به‌صورت هماهنگ دریافت کنند.
          </p>
          <div style="display:flex;gap:12px;flex-wrap:wrap;">
            <button type="button" class="btn-about-more" data-open-consult="true">
              <span data-editable="true">ثبت درخواست مشاوره</span>
            </button>
            <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="btn-about-more" style="border-color:rgba(255,255,255,0.35);">
              <span>بازگشت به صفحه اصلی (بخش خدمات ما)</span>
            </a>
          </div>
        </div>

        <div class="about-video-zone" aria-hidden="true"></div>
      </div>
    </section>

    <!-- ==================================================================
         7. CATEGORIZED FAQ ACCORDION ("پرسش‌های متداول")
         ================================================================== -->
    <section class="srv-faq-section" id="faq-section">
      <div class="container">
        <div class="subservices-header">
          <h2 class="subservices-title" data-editable="true">پرسش‌های متداول خدمات</h2>
          <p class="subservices-subtitle" data-editable="true">پاسخ به مهم‌ترین سؤالات متقاضیان در حوزه‌های جواز تأسیس، پروانه بهره‌برداری، طرح توجیهی، ثبت برند و خدمات فنی و مهندسی</p>
        </div>
        <div class="srv-faq-list">
          {faq_html}
        </div>
      </div>
    </section>
  </main>

  <!-- ====================================================================
       8. IDENTICAL SITE FOOTER
       ==================================================================== -->
  <footer class="site-footer" id="footer">
    <div class="container">
      <div class="footer-main-row">
        <div class="footer-socials-group">
          <button type="button" class="btn-scroll-top" id="btnScrollTop" aria-label="بازگشت به بالای صفحه" title="بازگشت به بالا">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
          </button>

          <a href="index.html" data-switch-page="home" class="social-circle-link" style="width:auto;padding:0 12px;border-radius:999px;font-size:11.5px;font-weight:700;" title="صفحه اصلی سایت">
            صفحه اصلی سایت
          </a>

          <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="social-circle-link" style="width:auto;padding:0 12px;border-radius:999px;font-size:11.5px;font-weight:700;" title="بخش خدمات ما در صفحه اصلی">
            بخش خدمات ما
          </a>

          <a href="#footer" class="social-circle-link" aria-label="اینستاگرام">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </a>

          <a href="#footer" class="social-circle-link" aria-label="تلگرام">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </a>

          <a href="#footer" class="social-circle-link" aria-label="لینکدین">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
              <rect x="2" y="9" width="4" height="12"></rect>
              <circle cx="4" cy="4" r="2"></circle>
            </svg>
          </a>
        </div>

        <div class="footer-contacts-group">
          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <span class="footer-contact-primary" data-editable="true">شیراز بلوار چهل مقام ، کوچه ۱۱ جنب سازمان صنعت و معدن و تجارت</span>
              <span class="footer-contact-secondary" data-editable="true">آدرس دفتر مرکزی</span>
            </div>
            <span class="footer-contact-icon" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
            </span>
          </div>

          <div class="footer-divider" aria-hidden="true"></div>

          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <a href="mailto:info@delgosha.ir" class="footer-contact-primary" style="direction:ltr;display:inline-block;" data-editable="true">info@delgosha.ir</a>
              <span class="footer-contact-secondary" data-editable="true">پست الکترونیک</span>
            </div>
            <span class="footer-contact-icon" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
            </span>
          </div>

          <div class="footer-divider" aria-hidden="true"></div>

          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <a href="tel:09177056063" class="footer-contact-primary" data-editable="true">۰۹۱۷۷۰۵۶۰۶۳</a>
              <span class="footer-contact-secondary" data-editable="true">(پاسخگویی ۸ الی ۱۶)</span>
            </div>
            <span class="footer-contact-icon" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
            </span>
          </div>
        </div>

        <a href="index.html" data-switch-page="home" class="footer-logo" aria-label="دلگشا - صفحه اصلی">
          <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
          <div class="brand-text-stack">
            <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
            <span class="brand-subtitle" data-editable="true">هلدینگ توسعه صنعت و معدن و تجارت</span>
          </div>
          <img src="{img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
        </a>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div class="container">
        <p class="footer-copyright" data-editable="true">
          © تمامی حقوق مادی و معنوی این سایت متعلق به دلگشا (هلدینگ راه‌گشا) می‌باشد.
        </p>
      </div>
    </div>
  </footer>

  <!-- Consultation Modal -->
  <div class="modal-backdrop" id="consultModal" role="dialog" aria-modal="true">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">درخواست مشاوره تخصصی خدمات</h3>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <form id="consultForm">
        <div class="form-group">
          <label class="form-label" for="consultName">نام و نام خانوادگی / نام شرکت</label>
          <input type="text" id="consultName" class="form-control" placeholder="نام خود یا مجموعه را وارد کنید..." required />
        </div>
        <div class="form-group">
          <label class="form-label" for="consultPhone">شماره تماس</label>
          <input type="tel" id="consultPhone" class="form-control" placeholder="۰۹۱۷xxxxxxx" required />
        </div>
        <div class="form-group">
          <label class="form-label" for="consultCategory">بخش خدمات مورد نظر</label>
          <select id="consultCategory" class="form-control">
            <option value="صنعت و مجوزها">بخش اول: صنعت و مجوزهای تولید</option>
            <option value="معدن و کاداستر">بخش دوم: معدن و سامانه کاداستر</option>
            <option value="تجارت و بازرگانی">بخش سوم: تجارت و بازرگانی بین‌الملل</option>
            <option value="فنی و مهندسی">بخش چهارم: فنی، مهندسی و ساختمان</option>
            <option value="ثبتی و مالی">بخش پنجم: ثبتی، مالی و توسعه کسب‌وکار</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="consultTopic">عنوان خدمت یا شرح درخواست</label>
          <input type="text" id="consultTopic" class="form-control" placeholder="مثال: طراحی و اجرای سوله کارخانه / صدور جواز تأسیس..." />
        </div>
        <button type="submit" class="btn-submit-modal">ثبت درخواست و هماهنگی تماس</button>
      </form>
    </div>
  </div>
</body>
</html>
'''

with open('/home/user/services.html', 'w', encoding='utf-8') as f:
    f.write(services_html_doc)

with open('/home/user/services/index.html', 'w', encoding='utf-8') as f:
    f.write(services_html_doc)

# Build dedicated service metadata dictionary for all 53+ slides
all_dedicated_services = {}
for band in SIX_SHOWCASE_BANDS:
    for s in band["slides"]:
        all_dedicated_services[s["slug"]] = {
            "title": s["title"],
            "cat": band["title"],
            "desc": s["sub"],
            "highlights": [
                f"بررسی تخصصی شرایط و پیش‌نیازهای «{s['title']}» توسط کارشناسان {band['title']}",
                "تکمیل مستندات، مدارک فنی و ثبت درخواست در سامانه رسمی مربوطه",
                "پیگیری مرحله‌به‌مرحله پرونده تا صدور مجوز یا تحویل نهایی پروژه",
                "ارائه مشاوره کاربردی و پشتیبانی اجرایی در تمام مراحل"
            ]
        }

for slug, info in all_dedicated_services.items():
    sdir = f"/home/user/services/{slug}"
    os.makedirs(sdir, exist_ok=True)
    hl_li = "".join([f"<li style='margin-bottom:8px;'>{h}</li>" for h in info["highlights"]])
    sub_doc = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width={desktop_viewport_width}, minimum-scale=0.1" />
  <title>{info['title']} | خدمات سایت دلگشا - هلدینگ راه‌گشا</title>
  <link rel="icon" type="image/png" href="{img_logo}" />
  <style>
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_regular}') format('woff2');
      font-weight: 400;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_bold}') format('woff2');
      font-weight: 700;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_black}') format('woff2');
      font-weight: 900;
    }}
    {base_styles}
    {services_page_css}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="../../index.html" class="brand-logo">
        <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
        <div class="brand-text-stack">
          <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
          <span class="brand-subtitle">هلدینگ توسعه صنعت و معدن و تجارت</span>
        </div>
      </a>
      <nav class="main-nav">
        <a href="../../index.html" class="nav-link">صفحه اصلی</a>
        <a href="../../index.html#subservices" class="nav-link">خدمات ما (صفحه اصلی)</a>
        <a href="../../services.html" class="nav-link active">صفحه جامع خدمات</a>
      </nav>
      <div class="header-actions">
        <a href="../../services.html" class="btn-consult"><span>بازگشت به همه خدمات</span></a>
      </div>
    </div>
  </header>

  <nav class="srv-breadcrumb-bar">
    <div class="container srv-breadcrumb-list">
      <a href="../../index.html">صفحه اصلی سایت</a>
      <span>‹</span>
      <a href="../../index.html#subservices">بخش خدمات ما (صفحه اصلی)</a>
      <span>‹</span>
      <a href="../../services.html">صفحه جامع خدمات</a>
      <span>‹</span>
      <span>{info['title']}</span>
    </div>
  </nav>

  <main class="container" style="padding:48px 24px;">
    <div style="background:#fff;border-radius:22px;padding:36px;box-shadow:0 14px 40px rgba(6,24,46,0.08);border:1px solid #e2e8f0;">
      <span class="srv-hero-badge" style="background:rgba(244,129,11,0.12);color:#ea580c;">{info['cat']}</span>
      <h1 style="font-size:32px;font-weight:900;color:#09213d;margin:10px 0 16px;">{info['title']}</h1>
      <p style="font-size:15px;color:#334155;line-height:2;margin-bottom:24px;">{info['desc']}</p>
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px;padding:22px;margin-bottom:28px;">
        <h2 style="font-size:18px;font-weight:900;color:#09213d;margin-bottom:12px;">محورهای خدمات و پیگیری‌های تخصصی این بخش:</h2>
        <ul style="padding-right:20px;list-style:disc;font-size:14px;color:#1e293b;line-height:1.9;">
          {hl_li}
        </ul>
      </div>
      <div style="display:flex;gap:14px;flex-wrap:wrap;">
        <a href="tel:09177056063" class="srv-btn-primary">تماس و مشاوره مستقیم: ۰۹۱۷۷۰۵۶۰۶۳</a>
        <a href="../../services.html" class="srv-btn-secondary" style="color:#09213d;border-color:#09213d;">بازگشت به صفحه جامع خدمات</a>
        <a href="../../index.html#subservices" class="srv-btn-secondary" style="color:#09213d;border-color:#cbd5e1;">صفحه اصلی (بخش خدمات ما)</a>
      </div>
    </div>
  </main>
</body>
</html>
'''
    with open(f"{sdir}/index.html", 'w', encoding='utf-8') as sf:
        sf.write(sub_doc)

print(f"Generated 6-Band Reference Services Page + {len(all_dedicated_services)} dedicated sub-service pages!")
