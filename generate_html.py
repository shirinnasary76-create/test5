import base64
import json
from html import escape

def to_data_uri(path, mime):
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    return f"data:{mime};base64,{b64}"

font_regular = to_data_uri('/home/user/public/fonts/Vazirmatn-Regular.woff2', 'font/woff2')
font_medium = to_data_uri('/home/user/public/fonts/Vazirmatn-Medium.woff2', 'font/woff2')
font_bold = to_data_uri('/home/user/public/fonts/Vazirmatn-Bold.woff2', 'font/woff2')
font_extrabold = to_data_uri('/home/user/public/fonts/Vazirmatn-ExtraBold.woff2', 'font/woff2')
font_black = to_data_uri('/home/user/public/fonts/Vazirmatn-Black.woff2', 'font/woff2')

img_hero = to_data_uri('/home/user/public/assets/hero-bg.jpg', 'image/jpeg')
img_about = to_data_uri('/home/user/public/assets/about-bg.jpg', 'image/jpeg')
img_card1 = to_data_uri('/home/user/public/assets/card-1.jpg', 'image/jpeg')
img_card2 = to_data_uri('/home/user/public/assets/card-2.jpg', 'image/jpeg')
img_card3 = to_data_uri('/home/user/public/assets/card-3.jpg', 'image/jpeg')
img_card4 = to_data_uri('/home/user/public/assets/card-4.jpg', 'image/jpeg')
img_logo = to_data_uri('/home/user/public/assets/logo-mark.png', 'image/png')
img_logo_text = to_data_uri('/home/user/public/assets/logo-text.png', 'image/png')
img_logo_full = to_data_uri('/home/user/public/assets/logo-full.png', 'image/png')
img_logo_lightbg = to_data_uri('/home/user/public/assets/logo-lightbg.png', 'image/png')
img_circle_bg = to_data_uri('/home/user/public/assets/circle-bg.jpg', 'image/jpeg')

# Newly extracted assets from Picsart composite reference screenshot
img_ceo = to_data_uri('/home/user/public/assets/ceo-video.jpg', 'image/jpeg')
img_sub1 = to_data_uri('/home/user/public/assets/subservice-1.jpg', 'image/jpeg')
img_sub2 = to_data_uri('/home/user/public/assets/subservice-2.jpg', 'image/jpeg')
img_sub3 = to_data_uri('/home/user/public/assets/subservice-3.jpg', 'image/jpeg')
img_sub4 = to_data_uri('/home/user/public/assets/subservice-4.jpg', 'image/jpeg')
img_sub5 = to_data_uri('/home/user/public/assets/subservice-5.jpg', 'image/jpeg')
img_av1 = to_data_uri('/home/user/public/assets/avatar-1.jpg', 'image/jpeg')
img_av2 = to_data_uri('/home/user/public/assets/avatar-2.jpg', 'image/jpeg')
img_av3 = to_data_uri('/home/user/public/assets/avatar-3.jpg', 'image/jpeg')

with open('/home/user/src/styles.css', 'r', encoding='utf-8') as f:
    styles_css = f.read()

with open('/home/user/src/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

with open('/home/user/src/site-config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

desktop_viewport_width = int(config.get("display", {}).get("desktopWidth", 1360))

CIRCLE_SVGS = {
    "content": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="9" y="12" width="30" height="22" rx="3" stroke="#ffffff" stroke-width="2.5"/>
        <polygon points="21,19 29,23 21,27" fill="#fbbf24" stroke="#fbbf24" stroke-width="1.5" stroke-linejoin="round"/>
        <path d="M16 38H32" stroke="#fbbf24" stroke-width="2.6" stroke-linecap="round"/>
      </svg>
    ''',
    "audit": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="12" y="9" width="22" height="30" rx="2.5" stroke="#ffffff" stroke-width="2.4"/>
        <path d="M17 16H29M17 21H25M17 26H22" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round"/>
        <circle cx="30" cy="30" r="6" fill="#06182e" stroke="#fbbf24" stroke-width="2.4"/>
        <path d="M34.5 34.5L38.5 38.5" stroke="#fbbf24" stroke-width="2.8" stroke-linecap="round"/>
      </svg>
    ''',
    "design_calc": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M11 36L35 12V36H11Z" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round"/>
        <path d="M23 36V29H30" stroke="#fbbf24" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M14 14L22 22M18 11L11 18" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
      </svg>
    ''',
    "feasibility": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 26L20 19L26 23L35 14M35 14H28.5M35 14V20.5" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
        <rect x="12" y="30" width="4.5" height="7" rx="1" fill="#ffffff"/>
        <rect x="19" y="26" width="4.5" height="11" rx="1" fill="#fbbf24"/>
        <rect x="26" y="28" width="4.5" height="9" rx="1" fill="#ffffff"/>
        <rect x="33" y="21" width="4.5" height="16" rx="1" fill="#fbbf24"/>
      </svg>
    ''',
    "brand": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="24" cy="21" r="10" stroke="#ffffff" stroke-width="2.5"/>
        <polygon points="24,15 26.2,19.2 30.8,19.9 27.4,23.1 28.2,27.6 24,25.4 19.8,27.6 20.6,23.1 17.2,19.9 21.8,19.2" fill="#fbbf24"/>
        <path d="M18 29.5L15 39L24 35.5L33 39L30 29.5" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    ''',
    "company": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 38H38" stroke="#fbbf24" stroke-width="2.6" stroke-linecap="round"/>
        <rect x="14" y="12" width="13" height="26" rx="1.5" stroke="#ffffff" stroke-width="2.4"/>
        <path d="M27 20H34C34.8 20 35.5 20.7 35.5 21.5V38H27V20Z" stroke="#fbbf24" stroke-width="2.3"/>
        <path d="M18 17H23M18 22H23M18 27H23" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
    ''',
    "license": '''
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M14 10H28L35 17V37C35 38.1 34.1 39 33 39H14C12.9 39 12 38.1 12 37V12C12 10.9 12.9 10 14 10Z" stroke="#ffffff" stroke-width="2.6" stroke-linejoin="round"/>
        <path d="M28 10V17H35" stroke="#ffffff" stroke-width="2.4" stroke-linejoin="round"/>
        <path d="M17 21H26M17 26H30M17 31H27" stroke="#fbbf24" stroke-width="2.6" stroke-linecap="round"/>
      </svg>
    '''
}

CARD_CATEGORY_SVGS = {
    "industry": '''
      <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="16" cy="16" r="5" stroke="currentColor" stroke-width="2.8"/>
        <circle cx="16" cy="16" r="9.2" stroke="currentColor" stroke-width="2.4" stroke-dasharray="4 2.5"/>
        <path d="M16 2.5V6.5M16 25.5V29.5M2.5 16H6.5M25.5 16H29.5M6.4 6.4L9.3 9.3M22.7 22.7L25.6 25.6M25.6 6.4L22.7 9.3M9.3 22.7L6.4 25.6" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/>
      </svg>
    ''',
    "mining": '''
      <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2.5 26.5L12.5 7.5L19.5 19.5L15.5 26.5H2.5Z" fill="currentColor"/>
        <path d="M18 26.5L23.5 14L29.5 26.5H18Z" fill="currentColor"/>
      </svg>
    ''',
    "trade": '''
      <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="16" cy="16" r="12" stroke="currentColor" stroke-width="2.5"/>
        <ellipse cx="16" cy="16" rx="5.5" ry="12" stroke="currentColor" stroke-width="2.2"/>
        <path d="M4.5 12.5H27.5M4.5 19.5H27.5" stroke="currentColor" stroke-width="2.2"/>
      </svg>
    ''',
    "engineering": '''
      <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 22C5 15.4 9.9 10 16 10C22.1 10 27 15.4 27 22H5Z" stroke="currentColor" stroke-width="2.6" stroke-linejoin="round"/>
        <path d="M13.5 10V7.5C13.5 6.7 14.2 6 15 6H17C17.8 6 18.5 6.7 18.5 7.5V10" stroke="currentColor" stroke-width="2.4"/>
        <path d="M3 22.5H29" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
      </svg>
    '''
}

WHY_SVGS = {
    "exp": '''
      <svg width="26" height="26" viewBox="0 0 28 28" fill="none">
        <circle cx="14" cy="14" r="5.5" stroke="#f59e0b" stroke-width="2.2"/>
        <path d="M14 3V6M14 22V25M3 14H6M22 14H25M6.2 6.2L8.4 8.4M19.6 19.6L21.8 21.8M21.8 6.2L19.6 8.4M8.4 19.6L6.2 21.8" stroke="#f59e0b" stroke-width="2.4" stroke-linecap="round"/>
      </svg>
    ''',
    "consult": '''
      <svg width="26" height="26" viewBox="0 0 28 28" fill="none">
        <circle cx="14" cy="14" r="6" stroke="#f59e0b" stroke-width="2.2"/>
        <circle cx="14" cy="14" r="2.2" fill="#f59e0b"/>
        <path d="M14 2.5V5.5M14 22.5V25.5M2.5 14H5.5M22.5 14H25.5M5.8 5.8L8 8M20 20L22.2 22.2M22.2 5.8L20 8M8 20L5.8 22.2" stroke="#f59e0b" stroke-width="2.3" stroke-linecap="round"/>
      </svg>
    ''',
    "partner": '''
      <svg width="26" height="26" viewBox="0 0 28 28" fill="none">
        <circle cx="14" cy="10" r="4.5" stroke="#f59e0b" stroke-width="2.2"/>
        <path d="M8.5 23L11 14.5M19.5 23L17 14.5M10 19.5L14 17L18 19.5" stroke="#f59e0b" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    ''',
    "network": '''
      <svg width="26" height="26" viewBox="0 0 28 28" fill="none">
        <circle cx="14" cy="9" r="3.5" stroke="#f59e0b" stroke-width="2.2"/>
        <circle cx="7.5" cy="19.5" r="3.2" stroke="#f59e0b" stroke-width="2.2"/>
        <circle cx="20.5" cy="19.5" r="3.2" stroke="#f59e0b" stroke-width="2.2"/>
        <path d="M11.5 11.8L9 16.5M16.5 11.8L19 16.5M10.8 19.5H17.2" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
      </svg>
    '''
}

CARD_IMAGES = {
    "01": img_card1,
    "02": img_card2,
    "03": img_card3,
    "04": img_card4
}

circles_html = ""
for idx, c in enumerate(config["serviceCircles"]):
    arc_svg = ""
    if c["arc"] == "left":
        arc_svg = '''
        <svg class="ring-arc-svg" viewBox="0 0 110 110">
          <path d="M 18 85 A 48 48 0 0 1 18 25" fill="none" stroke="#f59e0b" stroke-width="5.5" stroke-linecap="round"/>
        </svg>
        '''
    elif c["arc"] == "top-right":
        arc_svg = '''
        <svg class="ring-arc-svg" viewBox="0 0 110 110">
          <path d="M 55 5 A 50 50 0 0 1 95 28" fill="none" stroke="#f59e0b" stroke-width="5.5" stroke-linecap="round"/>
        </svg>
        '''
    active_cls = "active" if idx == 0 else ""
    preview_cls = ""
    inner_style = f"background-image: url('{img_circle_bg}');"
    inner_markup = CIRCLE_SVGS[c["id"]]
    if c.get("previewImage"):
        # Small, distinct sample photos inside the existing storyboard rings.
        preview_uri = to_data_uri('/home/user/public/assets/' + c["previewImage"], 'image/jpeg')
        preview_cls = " has-story-image"
        inner_style = "background-image:none;"
        inner_markup = f'<img src="{preview_uri}" class="service-story-image" alt="تصویر نمایشی {escape(c["title"], quote=True)}" width="320" height="320" loading="lazy" decoding="async" draggable="false" />'
    circles_html += f'''
      <div class="service-circle-item {active_cls}{preview_cls}" data-target-card="{c['targetCard']}">
        <div class="service-circle-ring">
          {arc_svg}
          <div class="service-circle-inner{preview_cls}" style="{inner_style}">
            {inner_markup}
          </div>
        </div>
        <span class="service-circle-label" data-editable="true">{c["title"]}</span>
      </div>
    '''

cards_html = ""
for card in config["industryCards"]:
    cid = card["id"]
    links_html = ""
    for item in card["items"]:
        links_html += f'''
          <li class="card-link-item">
            <a href="#service-{cid}" class="card-link-anchor">
              <span class="card-ext-icon" aria-hidden="true">
                <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                  <path d="M13 9V13C13 13.55 12.55 14 12 14H3C2.45 14 2 13.55 2 13V4C2 3.45 2.45 3 3 3H7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                  <path d="M10 2H14V6M14 2L7.5 8.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
              <span class="card-link-text" data-editable="true">{item}</span>
            </a>
          </li>
        '''

    cards_html += f'''
      <article class="industry-card" id="industry-card-{cid}">
        <div class="card-visual">
          <img src="{CARD_IMAGES[cid]}" alt="{card['title']}" class="card-visual-img" loading="lazy" />
          <div class="card-visual-gradient"></div>
          <div class="card-num-badge" aria-hidden="true">
            {CARD_CATEGORY_SVGS[card['icon']]}
          </div>
          <div class="card-title-row">
            <h3 class="card-category-title" data-editable="true">{card['title']}</h3>
          </div>
          <div class="card-subtitle-bar" title="کلیک برای باز/بسته کردن فهرست">
            <svg class="card-subtitle-chevron" viewBox="0 0 16 16" fill="none">
              <path d="M4 10L8 6L12 10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="card-subtitle-text" data-editable="true">{card['subtitle']}</span>
          </div>
        </div>
        <div class="card-links-box">
          <ul class="card-links-list">
            {links_html}
          </ul>
        </div>
        <div class="card-footer-more">
          <a href="services.html" data-switch-page="services" class="card-more-btn">
            <span data-editable="true">مشاهده همه خدمات این بخش</span>
            <svg width="13" height="13" viewBox="0 0 16 16" fill="none">
              <path d="M10 4L6 8L10 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </div>
      </article>
    '''

why_html = ""
for w in config["whyItems"]:
    why_html += f'''
      <div class="why-item">
        <div class="why-icon-circle" aria-hidden="true">
          {WHY_SVGS[w["icon"]]}
        </div>
        <div class="why-item-text">
          <h4 class="why-item-heading" data-editable="true">{w["title"]}</h4>
          <p class="why-item-sub" data-editable="true">{w["subtitle"]}</p>
        </div>
      </div>
    '''

# 5 Sub-Services Cards Data (RTL Right-to-Left matching Picsart composite screenshot)
SUB_SERVICES_DATA = [
    {
        "img": img_sub1,
        "title": "تأمین و تجهیزات کارخانه‌ها",
        "desc": "تأمین تجهیزات پیشرفته مورد نیاز صنایع و معادن",
        "target_group": "#group-industry",
        "svg": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9c.26.6.77 1.05 1.51 1H21a2 2 0 1 1 0 4h-.09c-.74.05-1.25.4-1.51 1z"/></svg>'
    },
    {
        "img": img_sub2,
        "title": "اجرای پروژه‌های صنعتی",
        "desc": "طراحی، اجرا و راه‌اندازی واحدهای صنعتی و معدنی",
        "target_group": "#group-engineering",
        "svg": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'
    },
    {
        "img": img_sub3,
        "title": "استخراج و فرآوری مواد معدنی",
        "desc": "استخراج و فرآوری حرفه‌ای مواد معدنی",
        "target_group": "#group-mining-trade",
        "svg": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 20L10 7L15 15L18 10L22 20H3Z"/></svg>'
    },
    {
        "img": img_sub4,
        "title": "تعمیرات و نگهداری تجهیزات",
        "desc": "تعمیرات تخصصی و سرویس‌های دوره‌ای تجهیزات",
        "target_group": "#group-engineering",
        "svg": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
    },
    {
        "img": img_sub5,
        "title": "خدمات مشاوره و مطالعات",
        "desc": "ارائه راهکارهای تخصصی برای پروژه‌های صنعتی",
        "target_group": "#group-financial-specialized",
        "svg": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'
    }
]

subservices_html = ""
for s in SUB_SERVICES_DATA:
    subservices_html += f'''
      <article class="subservice-card">
        <div class="subservice-img-wrap">
          <img src="{s['img']}" alt="{s['title']}" class="subservice-img" loading="lazy" />
          <div class="subservice-icon-badge" aria-hidden="true">
            {s['svg']}
          </div>
        </div>
        <div class="subservice-body">
          <h3 class="subservice-card-title" data-editable="true">{s['title']}</h3>
          <p class="subservice-card-desc" data-editable="true">{s['desc']}</p>
          <a href="services.html{s['target_group']}" data-switch-page="services" data-scroll-target="{s['target_group']}" class="subservice-more-link">
            <span data-editable="true">اطلاعات بیشتر</span>
            <span>+</span>
          </a>
        </div>
      </article>
    '''

html_doc = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width={desktop_viewport_width}, minimum-scale=0.1" />
  <title>راه‌گشا صمت | هلدینگ توسعه صنعت و معدن و تجارت</title>
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
    {styles_css}
  </style>
</head>
<body id="top">

  <!-- ====================================================================
       1. TOP HEADER / NAVIGATION BAR
       ==================================================================== -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" data-switch-page="home" class="brand-logo" aria-label="دلگشا - صفحه اصلی">
        <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
        <div class="brand-text-stack">
          <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
          <span class="brand-subtitle" data-brand-field="tagline" data-editable="true">هلدینگ توسعه صنعت و معدن و تجارت</span>
        </div>
        <img src="{img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
      </a>

      <nav class="main-nav" aria-label="منوی اصلی">
        <a href="index.html" data-switch-page="home" data-nav-key="home" class="nav-link active" data-editable="true">خانه</a>
        <a href="services.html" data-switch-page="services" data-nav-key="services" class="nav-link" data-editable="true">خدمات</a>
        <a href="about.html" data-switch-page="about" data-nav-key="about" class="nav-link" data-editable="true">درباره ما</a>
        <a href="news.html" data-switch-page="news" data-nav-key="news" class="nav-link" data-editable="true">اخبار و رویدادها</a>
        <a href="projects.html" data-switch-page="projects" data-nav-key="projects" class="nav-link" data-editable="true">پروژه‌ها</a>
        <a href="#footer" data-nav-key="contact" class="nav-link" data-editable="true">تماس با ما</a>
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

        <button type="button" class="btn-search" id="btnOpenSearch" aria-label="جستجو در سایت" title="جستجو در خدمات و مقالات">
          <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="7"></circle>
            <line x1="20" y1="20" x2="16.2" y2="16.2"></line>
          </svg>
        </button>

        <button type="button" class="btn-mobile-menu" id="btnMobileMenu" aria-label="منوی موبایل">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
            <line x1="4" y1="7" x2="20" y2="7"></line>
            <line x1="4" y1="12" x2="20" y2="12"></line>
            <line x1="4" y1="17" x2="20" y2="17"></line>
          </svg>
        </button>
      </div>
    </div>

    <div class="mobile-drawer" id="mobileDrawer">
      <a href="index.html" data-switch-page="home" data-nav-key="home" class="nav-link active">خانه</a>
      <a href="services.html" data-switch-page="services" data-nav-key="services" class="nav-link">خدمات</a>
      <a href="about.html" data-switch-page="about" data-nav-key="about" class="nav-link">درباره ما</a>
      <a href="news.html" data-switch-page="news" data-nav-key="news" class="nav-link">اخبار و رویدادها</a>
      <a href="projects.html" data-switch-page="projects" data-nav-key="projects" class="nav-link">پروژه‌ها</a>
      <a href="#footer" data-nav-key="contact" class="nav-link">تماس با ما</a>
    </div>
  </header>

  <!-- ====================================================================
       2. HERO BANNER SECTION
       ==================================================================== -->
  <section class="hero-section" style="background-image: url('{img_hero}');">
    <div class="hero-overlay"></div>

    <svg class="hero-network-svg" viewBox="0 0 380 440" fill="none" xmlns="http://www.w3.org/2000/svg">
      <line x1="0" y1="120" x2="190" y2="20" stroke="#38bdf8" stroke-width="0.8" stroke-opacity="0.4"/>
      <line x1="20" y1="220" x2="240" y2="80" stroke="#fbbf24" stroke-width="0.8" stroke-opacity="0.35"/>
      <line x1="0" y1="310" x2="180" y2="190" stroke="#38bdf8" stroke-width="0.8" stroke-opacity="0.3"/>
      <circle cx="28" cy="215" r="4" fill="#fbbf24" fill-opacity="0.7"/>
      <circle cx="110" cy="145" r="2.5" fill="#38bdf8" fill-opacity="0.6"/>
    </svg>

    <div class="hero-container">
      <div class="hero-content">
        <p class="hero-overline" id="heroOverline" data-brand-field="heroOverline" data-editable="true">راهگشا، همراه مطمئن کسب‌وکارها</p>
        <h1 class="hero-title">
          <span id="heroTitle1" data-editable="true">از مجوز تا توسعه،</span>
          <span id="heroTitle2" data-editable="true">در کنار شما هستیم</span>
        </h1>
        <p class="hero-description" id="heroBody" data-brand-field="heroBody" data-editable="true">
          با تکیه بر ارائه خدمات تخصصی در حوزه‌های صنعتی، معدنی، اداری، مالی و توسعه کسب‌وکار، مسیر رشد و موفقیت شما را هموار می‌کند.
        </p>
        <div class="hero-cta-wrap">
          <a href="#services" class="btn-hero-cta">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
            <span data-editable="true">مشاهده خدمات</span>
          </a>
        </div>
      </div>
    </div>

    <div class="hero-dots" role="tablist" aria-label="اسلایدر صفحه اصلی">
      <button type="button" class="hero-dot active" aria-label="اسلاید ۱"></button>
      <button type="button" class="hero-dot" aria-label="اسلاید ۲"></button>
      <button type="button" class="hero-dot" aria-label="اسلاید ۳"></button>
      <button type="button" class="hero-dot" aria-label="اسلاید ۴"></button>
      <button type="button" class="hero-dot" aria-label="اسلاید ۵"></button>
    </div>

    <div class="hero-bottom-step" aria-hidden="true"></div>
  </section>

  <!-- ====================================================================
       3. SPECIALIZED SERVICES STRIP ("خدمات ما")
       ==================================================================== -->
  <section class="services-strip-section" id="services">
    <div class="container services-strip-grid">
      <div class="services-intro">
        <div>
          <p class="services-overline" data-brand-field="servicesOverline" data-editable="true">خدمات ما</p>
          <h2 class="services-heading" data-editable="true">
            راهکارهای تخصصی برای<br />رشد کسب‌وکار شما
          </h2>
          <p class="services-desc" data-editable="true">
            با تکیه بر تجربه، تخصص و ارتباطات گسترده،<br />پیشرفت شما را تضمین می‌کنیم.
          </p>
        </div>
        <div class="services-all-link-wrap">
          <a href="services.html" class="services-all-link">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
            <span data-editable="true">مشاهده همه خدمات</span>
          </a>
        </div>
      </div>

      <div class="services-capsule-outer">
        <button type="button" class="carousel-nav-btn carousel-nav-prev" id="carouselPrevBtn" aria-label="قبلی">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>

        <div class="service-circles-row" id="storyboard" role="group" aria-label="استوری‌بورد خدمات">
          {circles_html}
        </div>

        <button type="button" class="carousel-nav-btn carousel-nav-next" id="carouselNextBtn" aria-label="بعدی">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>

        <div class="capsule-scrollbar-track" aria-hidden="true">
          <div class="capsule-scrollbar-thumb" id="capsuleScrollThumb"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       4. FOUR INDUSTRY SERVICE CARDS
       Exact Right-to-Left Order: ۱. صنعت | ۲. معدن | ۳. تجارت | ۴. فنی و مهندسی
       ==================================================================== -->
  <section class="industry-cards-section" id="cards">
    <div class="container">
      <div class="industry-cards-grid">
        {cards_html}
      </div>
    </div>
  </section>

  <!-- ====================================================================
       5. CEO INTRODUCTION VIDEO SECTION ("معرفی مهندس مدیرعامل")
       ==================================================================== -->
  <section class="ceo-section" id="ceo">
    <img src="{img_logo_lightbg}" alt="" class="ceo-watermark" aria-hidden="true" />
    <div class="container ceo-grid">
      <!-- Right Column: CEO Intro Text -->
      <div class="ceo-text-col">
        <h2 class="ceo-heading" data-editable="true">معرفی مهندس مدیرعامل</h2>
        <p class="ceo-paragraph" data-editable="true">
          ما در شرکت صنعت و معدن از ابتدا با تکیه به تجربه، دانش فنی و نیروی انسانی متخصص تلاش می‌کنیم تا بهترین خدمات را در حوزه صنعت و معدن ارائه دهیم.<br />
          هدف ما ایجاد ارزش پایدار برای مشتریان و جامعه است.
        </p>
        <button type="button" class="btn-ceo-video" data-open-video="true">
          <span data-editable="true">مشاهده ویدیو کامل</span>
          <span>+</span>
        </button>
      </div>

      <!-- Left Column: CEO Video Player Frame -->
      <div class="ceo-video-col">
        <div class="ceo-video-frame" data-open-video="true" title="کلیک برای پخش ویدیوی معرفی مدیرعامل">
          <img src="{img_ceo}" alt="معرفی مهندس مدیرعامل" class="ceo-video-img" loading="lazy" />
          <button type="button" class="video-play-btn" data-open-video="true" aria-label="پخش ویدیوی معرفی مدیرعامل" title="پخش ویدیو">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round">
              <polygon points="8 5 19 12 8 19 8 5" fill="currentColor" fill-opacity="0.25"></polygon>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       6. COMPREHENSIVE 5-CARD SERVICES GRID ("خدمات ما — ارائه خدمات جامع و تخصصی در صنعت و معدن")
       ==================================================================== -->
  <section class="subservices-section" id="subservices">
    <div class="container">
      <div class="subservices-header">
        <h2 class="subservices-title" data-editable="true">خدمات ما</h2>
        <p class="subservices-subtitle" data-editable="true">ارائه خدمات جامع و تخصصی در صنعت و معدن</p>
      </div>
      <div class="subservices-grid">
        {subservices_html}
      </div>
    </div>
  </section>

  <!-- ====================================================================
       7. DARK NAVY BANNER — "چرا ما را انتخاب کنید؟"
       ==================================================================== -->
  <section class="why-choose-banner">
    <div class="container">
      <div class="why-choose-grid">
        <!-- Item 1 (Far Right): پشتیبانی ۲۴ ساعته -->
        <div class="why-choose-item">
          <div class="why-choose-circle" aria-hidden="true">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M11 17a4 4 0 0 1-8 0V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2z"></path>
              <path d="M16.7 13H19a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H7"></path>
            </svg>
          </div>
          <h3 class="why-choose-item-title" data-editable="true">پشتیبانی ۲۴ ساعته</h3>
          <p class="why-choose-item-sub" data-editable="true">همیشه در کنار شما</p>
        </div>

        <!-- Item 2 (2nd from Right): تعهد به کیفیت -->
        <div class="why-choose-item">
          <div class="why-choose-circle" aria-hidden="true">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              <polyline points="9 12 11 14 15 10"></polyline>
            </svg>
          </div>
          <h3 class="why-choose-item-title" data-editable="true">تعهد به کیفیت</h3>
          <p class="why-choose-item-sub" data-editable="true">استانداردهای بین‌المللی</p>
        </div>

        <!-- Item 3 (3rd from Right): تیم متخصص -->
        <div class="why-choose-item">
          <div class="why-choose-circle" aria-hidden="true">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
          </div>
          <h3 class="why-choose-item-title" data-editable="true">تیم متخصص</h3>
          <p class="why-choose-item-sub" data-editable="true">کارشناسان مجرب و حرفه‌ای</p>
        </div>

        <!-- Item 4 (4th from Right): تجربه طولانی‌مدت -->
        <div class="why-choose-item">
          <div class="why-choose-circle" aria-hidden="true">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3"></circle>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
            </svg>
          </div>
          <h3 class="why-choose-item-title" data-editable="true">تجربه طولانی‌مدت</h3>
          <p class="why-choose-item-sub" data-editable="true">بیش از ۱۵ سال سابقه کاری</p>
        </div>

        <!-- Column 5 (Far Left): چرا ما را انتخاب کنید؟ -->
        <div class="why-choose-intro">
          <h2 class="why-choose-intro-title" data-editable="true">چرا ما را انتخاب کنید؟</h2>
          <p class="why-choose-intro-desc" data-editable="true">
            تجربه، تعهد و کیفیت، سه اصل اصلی ما در ارائه خدمات است
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       8. CUSTOMER TESTIMONIALS ("نظرات مشتریان") & ONLINE CHAT WIDGET
       ==================================================================== -->
  <section class="testimonials-section" id="testimonials">
    <div class="container">
      <div class="testimonials-top-bar">
        <h2 class="testimonials-heading-right" data-editable="true">نظرات مشتریان</h2>
        <span class="testimonials-pill-left" data-editable="true">نظرات مشتریان</span>
      </div>

      <div class="testimonials-main-grid">
        <!-- Right Column: Interactive Online Support Chat Box -->
        <div class="support-chat-card">
          <div class="support-chat-header">
            <span class="support-chat-title" data-editable="true">✕ گفتگوی آنلاین</span>
            <span class="support-bot-badge" aria-hidden="true">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
              </svg>
            </span>
          </div>
          <div class="support-chat-body" id="supportChatBody">
            <div class="support-msg-bubble" data-editable="true">
              سلام! چطور می‌توانیم در زمینه خدمات صنعتی، معدنی و تجاری به شما کمک کنیم؟
            </div>
            <div class="support-quick-btns">
              <button type="button" class="support-quick-pill" data-editable="true">مشاوره تخصصی</button>
              <button type="button" class="support-quick-pill" data-editable="true">پیگیری و اخذ مجوزها</button>
              <button type="button" class="support-quick-pill" data-editable="true">ارتباط با کارشناسان</button>
            </div>
          </div>
          <form class="support-chat-footer" id="supportChatForm">
            <button type="submit" class="support-send-btn" aria-label="ارسال پیام">➤</button>
            <input type="text" class="support-chat-input" id="supportChatInput" placeholder="پیام خود را بنویسید..." />
          </form>
        </div>

        <!-- Left Column: 3 Customer Testimonial Cards -->
        <div class="testimonials-cards-wrap">
          <div class="testimonials-cards-grid">
            <!-- Card 1: علی محمدی -->
            <article class="testimonial-card">
              <div class="testimonial-header">
                <img src="{img_av1}" alt="علی محمدی" class="testimonial-avatar" loading="lazy" />
                <div class="testimonial-author-info">
                  <h3 class="testimonial-name" data-editable="true">علی محمدی</h3>
                  <div class="testimonial-stars" aria-label="۵ ستاره">★★★★★</div>
                </div>
              </div>
              <p class="testimonial-quote" data-editable="true">
                خدمات مشاوره و پیگیری مجوزهای صنعتی بسیار سریع، دقیق و حرفه‌ای انجام شد و تیم پشتیبانی در تمام مراحل همراه ما بود.
              </p>
            </article>

            <!-- Card 2: مینا احمدی -->
            <article class="testimonial-card">
              <div class="testimonial-header">
                <img src="{img_av2}" alt="مینا احمدی" class="testimonial-avatar" loading="lazy" />
                <div class="testimonial-author-info">
                  <h3 class="testimonial-name" data-editable="true">مینا احمدی</h3>
                  <div class="testimonial-stars" aria-label="۵ ستاره">★★★★★</div>
                </div>
              </div>
              <p class="testimonial-quote" data-editable="true">
                تیم فنی و مهندسی بسیار مجرب و حرفه‌ای هستند. طراحی و تدوین طرح توجیهی ما با بالاترین کیفیت و دقت انجام گرفت.
              </p>
            </article>

            <!-- Card 3: رضا نادری -->
            <article class="testimonial-card">
              <div class="testimonial-header">
                <img src="{img_av3}" alt="رضا نادری" class="testimonial-avatar" loading="lazy" />
                <div class="testimonial-author-info">
                  <h3 class="testimonial-name" data-editable="true">رضا نادری</h3>
                  <div class="testimonial-stars" aria-label="۵ ستاره">★★★★★</div>
                </div>
              </div>
              <p class="testimonial-quote" data-editable="true">
                همکاری با این مجموعه در بخش بازرگانی و تأمین تجهیزات صنعتی تجربه‌ای عالی و مطمئن برای توسعه کارخانه ما بود.
              </p>
            </article>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Mid Copyright Bar from Composite Reference -->
  <div class="mid-copyright-strip">
    <div class="container">
      <span data-editable="true">© تمامی حقوق مادی و معنوی برای شرکت صنعت و معدن و تجارت محفوظ است</span>
    </div>
  </div>

  <!-- ====================================================================
       9. ABOUT ("معرفی دلگشا") & WHY US ("چرا دلگشا؟") SECTION
       ==================================================================== -->
  <section class="about-section" id="about" style="background-image: url('{img_about}');">
    <div class="about-overlay"></div>
    <div class="container about-grid">
      <div class="why-card">
        <h2 class="why-card-title" data-brand-field="whyTitle" data-editable="true">چرا دلگشا؟</h2>
        <div class="why-list">
          {why_html}
        </div>
      </div>

      <div class="about-content">
        <div class="about-header-with-line">
          <p class="about-overline" data-brand-field="aboutOverline" data-editable="true">معرفی دلگشا</p>
          <h2 class="about-title">
            <span data-editable="true">همراهی مطمئن</span>
            <span data-editable="true">در مسیر پیشرفت</span>
          </h2>
        </div>
        <p class="about-description" data-brand-field="aboutBody" data-editable="true">
          دلگشا با تکیه بر تجربه و دانش تخصصی، در کنار کسب‌وکارها، صنایع و سرمایه‌گذاران است تا با ارائه راهکارهای عملی و دقیق، مسیر توسعه و رشد آن‌ها را هموار کند.
        </p>
        <a href="about.html" data-switch-page="about" class="btn-about-more">
          <span data-editable="true">درباره ما بیشتر بدانید</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </a>
      </div>

      <div class="about-video-zone" aria-hidden="true"></div>
    </div>
  </section>

  <!-- ====================================================================
       10. FOOTER SECTION
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

          <a href="#footer" class="social-circle-link" aria-label="واتساپ">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="5"></rect>
              <circle cx="12" cy="12" r="4"></circle>
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

        <a href="index.html" data-switch-page="home" class="footer-logo" aria-label="دلگشا">
          <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
          <div class="brand-text-stack">
            <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
            <span class="brand-subtitle" data-brand-field="tagline" data-editable="true">هلدینگ توسعه صنعت و معدن و تجارت</span>
          </div>
          <img src="{img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
        </a>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div class="container">
        <p class="footer-copyright" data-brand-field="copyright" data-editable="true">
          © تمامی حقوق مادی و معنوی این سایت متعلق به دلگشا می‌باشد.
        </p>
      </div>
    </div>
  </footer>

  <!-- ====================================================================
       11. INTERACTIVE MODALS & CUSTOMIZATION TOOLBAR
       ==================================================================== -->
  <div class="modal-backdrop" id="serviceDetailModal" role="dialog" aria-modal="true">
    <div class="modal-card">
      <div class="modal-header">
        <div>
          <span id="serviceModalBadge" class="search-result-badge">بخش ۰۱ — صنعت</span>
          <h3 class="modal-title" id="serviceModalTitle" style="margin-top:6px;">اخذ مجوزهای صنعتی</h3>
        </div>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <p id="serviceModalDesc" style="font-size:13.8px;color:#334155;line-height:1.95;margin-bottom:18px;"></p>
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:14px 16px;margin-bottom:18px;">
        <h4 style="font-size:13px;font-weight:800;color:#09213d;margin-bottom:8px;">مراحل و خدمات اجرایی این بخش:</h4>
        <ul style="font-size:12.5px;color:#475569;line-height:1.9;padding-right:16px;list-style:disc;">
          <li>بررسی اولیه شرایط و امکان‌سنجی فنی، مالی و قانونی</li>
          <li>تکمیل و ثبت مستندات در سامانه‌های رسمی و تخصصی</li>
          <li>پیگیری مستمر اداری تا صدور نهایی مجوز یا اجرای طرح</li>
          <li>ارائه مشاوره تخصصی پس از اخذ مجوز و شروع بهره‌برداری</li>
        </ul>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="services.html" data-switch-page="services" class="btn-submit-modal" style="flex:1;text-align:center;margin-top:0;">
          ورود به صفحه جامع خدمات ↖
        </a>
        <button type="button" class="btn-submit-modal" id="btnModalBookConsult" style="flex:1;margin-top:0;background:linear-gradient(135deg,#09213d,#0d2b4e);">
          ثبت درخواست مشاوره در این حوزه
        </button>
      </div>
    </div>
  </div>

  <div class="modal-backdrop" id="consultModal" role="dialog" aria-modal="true">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">درخواست مشاوره تخصصی</h3>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <form id="consultForm">
        <div class="form-group">
          <label class="form-label" for="consultName">نام و نام خانوادگی / نام شرکت</label>
          <input type="text" id="consultName" class="form-control" placeholder="مثال: شرکت فولاد گستر..." required />
        </div>
        <div class="form-group">
          <label class="form-label" for="consultPhone">شماره تماس</label>
          <input type="tel" id="consultPhone" class="form-control" placeholder="۰۹۱۲xxxxxxx یا ۰۳۱xxxxxxxx" required />
        </div>
        <div class="form-group">
          <label class="form-label" for="consultCategory">بخش مورد نظر</label>
          <select id="consultCategory" class="form-control">
            <option value="صنعت">۰۱ - صنعت (تولید، توسعه صنعتی و حمایت از کسب‌وکارها)</option>
            <option value="معدن">۰۲ - معدن (اکتشاف، بهره‌برداری و توسعه صنایع معدنی)</option>
            <option value="تجارت">۰۳ - تجارت (بازرگانی، صادرات و واردات و توسعه بازار)</option>
            <option value="فنی و مهندسی">۰۴ - فنی و مهندسی (راهکارهای تخصصی برای توسعه بهره‌وری)</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="consultTopic">موضوع یا شرح درخواست</label>
          <input type="text" id="consultTopic" class="form-control" placeholder="موضوع مشاوره را وارد کنید..." />
        </div>
        <button type="submit" class="btn-submit-modal">ارسال درخواست مشاوره</button>
      </form>
    </div>
  </div>

  <div class="modal-backdrop" id="searchModal" role="dialog" aria-modal="true">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">جستجو در خدمات و مقالات تخصصی</h3>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <input type="search" id="searchInput" class="form-control" placeholder="جستجوی عنوان خدمت (مثال: مجوز، معدن، صادرات، ثبت برند...)" />
      <div class="search-results-list" id="searchResultsList"></div>
    </div>
  </div>

  <div class="modal-backdrop" id="videoModal" role="dialog" aria-modal="true">
    <div class="modal-card" style="max-width:640px;background:#06182e;color:#fff;border:1px solid rgba(251,191,36,0.35);">
      <div class="modal-header" style="border-bottom-color:rgba(255,255,255,0.12);">
        <h3 class="modal-title" style="color:#fff;">ویدیوی معرفی هلدینگ توسعه صنعت و معدن و تجارت</h3>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <div style="position:relative;border-radius:14px;overflow:hidden;background:url('{img_ceo}') center/cover;height:300px;display:flex;align-items:center;justify-content:center;">
        <div style="position:absolute;inset:0;background:rgba(4,18,34,0.76);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;text-align:center;">
          <img src="{img_logo_full}" alt="لوگو راه‌گشا صمت" style="height:84px;width:auto;object-fit:contain;margin-bottom:14px;" />
          <h4 style="font-size:22px;font-weight:900;color:#fbbf24;margin-bottom:8px;">از مجوز تا توسعه، در کنار شما هستیم</h4>
          <p style="font-size:13.5px;color:#e2e8f0;max-width:460px;line-height:1.9;">
            ارائه خدمات تخصصی در ۴ محور کلیدی: صنعت، معدن، تجارت و خدمات فنی و مهندسی. تلفن تماس دفتر مرکزی: ۰۹۱۷۷۰۵۶۰۶۳
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Floating Quick Brand Switcher & Live Editor Toolbar -->
  <div class="designer-toolbar" aria-label="نوار ابزار سفارشی‌سازی">
    <a href="services.html" class="toolbar-btn" style="background:linear-gradient(135deg,#fbbf24,#f4810b);color:#051527;font-weight:900;" title="ورود به صفحه جامع خدمات">📋 صفحه جامع خدمات</a>
    <span class="toolbar-label">نام برند:</span>
    <button type="button" class="toolbar-btn active" data-brand-btn="delgosha" title="نمایش با نام دلگشا (مطابق تصویر مرجع)">دلگشا (تصویر مرجع)</button>
    <button type="button" class="toolbar-btn" data-brand-btn="rahgosha" title="نمایش با نام هلدینگ راه‌گشا">هلدینگ راه‌گشا</button>
    <button type="button" class="toolbar-btn" id="btnToggleLogoLayout" title="تغییر چیدمان لوگو بین حالت افقی هدر و حالت عمودی کامل">لوگو: افقی (هدر)</button>
    <button type="button" class="toolbar-btn" id="btnToggleEdit" title="ویرایش مستقیم تمام متون صفحه با کلیک">✎ ویرایش متن‌ها</button>
  </div>

  <div class="toast-msg" id="toastMsg" role="status" aria-live="polite"></div>

  <script>
    {app_js}
  </script>
</body>
</html>
'''

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)

with open('/home/user/public/index.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)

print("Generated full 10-section /home/user/index.html! Size:", len(html_doc))
