#!/usr/bin/env python3
"""Modify generate_services_page.py to replace slide images with icons + title layout."""
import re

with open('/home/user/generate_services_page.py', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. Add SLIDE_ICONS dict after VISUAL_POOL
# ============================================================
SLIDE_ICONS_CODE = '''
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

'''

# Insert SLIDE_ICONS after VISUAL_POOL closing bracket
marker = '    (img_hero, "left center", "contrast(1.05) hue-rotate(-8deg)"),\n]'
assert marker in content, "VISUAL_POOL end marker not found!"
content = content.replace(marker, marker + SLIDE_ICONS_CODE, 1)

# ============================================================
# 2. Replace slide template with icon+title horizontal layout
# ============================================================
old_template = '''          <a href="services/{s['slug']}/index.html" class="srv-slide-card" data-service-slug="{s['slug']}" data-service-title="{s['title']}" data-service-desc="{s['sub']}">
            <div class="srv-slide-img-wrap">
              <img src="{s['img']}" alt="{s['title']}" class="srv-slide-img" style="object-position:{s['pos']};filter:{filt};" loading="lazy" />
              <div class="srv-slide-img-fade"></div>
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
          </a>'''

new_template = '''          <a href="services/{s['slug']}/index.html" class="srv-slide-card" data-service-slug="{s['slug']}" data-service-title="{s['title']}" data-service-desc="{s['sub']}" style="--srv-title-color: var(--srv-color-{s['color_idx']});">
            <div class="srv-slide-icon-wrap">
              {SLIDE_ICONS.get(s['slug'], '')}
            </div>
            <div class="srv-slide-text-col">
              <h3 class="srv-slide-title" data-editable="true">{s['title']}</h3>
              <p class="srv-slide-sub" data-editable="true">{s['sub']}</p>
            </div>
            <div class="srv-slide-footer">
              <span class="srv-slide-meta" data-editable="true">{s['meta']}</span>
              <span class="srv-slide-arrow-icon" aria-hidden="true">←</span>
            </div>
          </a>'''

assert old_template in content, "Old slide template not found!"
content = content.replace(old_template, new_template, 1)

# ============================================================
# 3. Add color index to each slide (cycle through palette colors)
#    We'll add color_idx inline by modifying the band loop section
# ============================================================
# Add color cycling before slides_markup loop
old_loop_start = '    slides_markup = ""\n    for idx, s in enumerate(band["slashes" if False else "slashes"]):'
# Find the actual loop
old_loop = '    slides_markup = ""\n    for idx, s in enumerate(band["slashes" if False else "slashes"]):'
# The actual text in file:
old_loop_actual = '    slides_markup = ""\n    for idx, s in enumerate(band["slides"]):'
new_loop = '    slides_markup = ""\n    PALETTE = ["navy-600", "orange-500", "teal-500", "slate-600", "navy-800", "orange-600"]\n    for idx, s in enumerate(band["slides"]):'
assert old_loop_actual in content, "Slide loop not found!"
content = content.replace(old_loop_actual, new_loop, 1)

# Add color_idx to the template usage (replace {s['title']} in style with color_idx)
# The template already uses {s['color_idx']} - we need to add it to each slide dict
# Instead, let's inject color_idx into each slide at loop time
old_filt_line = '        # Pick varied filter/crop from VISUAL_POOL if needed\n        _, _, filt = VISUAL_POOL[idx % len(VISUAL_POOL)]'
new_filt_line = '        # Pick varied filter/crop from VISUAL_POOL if needed\n        _, _, filt = VISUAL_POOL[idx % len(VISUAL_POOL)]\n        s["color_idx"] = PALETTE[idx % len(PALETTE)]'
assert old_filt_line in content, "Filt line not found!"
content = content.replace(old_filt_line, new_filt_line, 1)

# ============================================================
# 4. Replace CSS for .srv-slide-card and related styles
# ============================================================
old_css_start = '''/* Individual Vertical Card inside the Slider (5 cards fit side-by-side in the track!) */
.srv-slide-card {'''
old_css_end = '''.srv-slide-card:hover .srv-slide-arrow-icon {
  transform: translateX(-3px);
  color: var(--orange-500);
}'''

new_css = '''/* Individual Horizontal Slide Card - Icon Left + Title Right (RTL) */
.srv-slide-card {
  flex: 0 0 250px;
  width: 250px;
  min-height: 118px;
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  position: relative;
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s ease, border-color 0.3s ease, background 0.3s ease;
  cursor: pointer;
}

.srv-band.theme-navy .srv-slide-card {
  background: linear-gradient(180deg, #072241 0%, #041529 100%);
  border: 1px solid rgba(56, 189, 248, 0.16);
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.38);
}

.srv-band.theme-navy .srv-slide-card:hover {
  transform: translateY(-4px);
  border-color: var(--orange-400);
  box-shadow: 0 16px 34px rgba(0, 0, 0, 0.55), 0 0 18px rgba(251, 191, 36, 0.2);
}

.srv-band.theme-white .srv-slide-card {
  background: var(--white);
  border: 1px solid #cbd5e1;
  box-shadow: 0 10px 24px rgba(6, 24, 46, 0.08);
}

.srv-band.theme-white .srv-slide-card:hover {
  transform: translateY(-4px);
  border-color: var(--orange-500);
  box-shadow: 0 18px 34px rgba(6, 24, 46, 0.15);
}

/* Icon zone - fixed size on the left side of each card */
.srv-slide-icon-wrap {
  flex: 0 0 28px;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: visible;
}

.srv-slide-icon-wrap svg {
  width: 100%;
  height: 100%;
  display: block;
}

/* Text column - title on top, description below */
.srv-slide-text-col {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.srv-slide-title {
  font-size: 13px;
  font-weight: 800;
  line-height: 1.45;
  margin: 0 0 4px 0;
  display: -webkit-box;
  overflow: hidden;
}

.srv-slide-sub {
  font-size: 10.8px;
  font-weight: 500;
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  overflow: hidden;
}

/* Footer - meta + arrow on right */
.srv-slide-footer {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 6px;
  padding-top: 6px;
  border-top: 1px solid rgba(148, 163, 184, 0.15);
  width: 100%;
}

.srv-band.theme-white .srv-slide-footer {
  border-top-color: #e2e8f0;
}

.srv-slide-meta {
  font-size: 9.6px;
  font-weight: 700;
  flex: 1;
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
}'''

assert old_css_start in content, "CSS start not found!"
# Find the end of old CSS section
idx_start = content.find(old_css_start)
idx_end = content.find(old_css_end, idx_start)
if idx_end == -1:
    # Try finding just the last line
    idx_end = content.find('.srv-slide-card:hover .srv-slide-arrow-icon {', idx_start)
    if idx_end != -1:
        # Find the closing of this rule
        brace_end = content.find('\n}\n/* 4. 5-STEP', idx_end)
        if brace_end == -1:
            brace_end = content.find('\n}\n', idx_end)
        idx_end = brace_end + 3
else:
    idx_end += len(old_css_end)

content = content[:idx_start] + new_css + content[idx_end:]

with open('/home/user/generate_services_page.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications complete!")