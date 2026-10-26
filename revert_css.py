#!/usr/bin/env python3
with open('/home/user/generate_services_page.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_css_start = '/* Individual Slide Card - Image Filled with Title Overlay (matching reference image style) */'
old_css_end = '/* 4. 5-STEP PROCESS SECTION ("مسیر دریافت خدمات") */'

import re

pattern = re.compile(
    r'/\* Individual Slide Card - Image Filled.*?\n\n/\* 4\. 5-STEP PROCESS SECTION',
    re.DOTALL
)

new_css = '''/* Individual Vertical Slide Card - Image Top + Title Below (RTL) */
.srv-slide-card {
  flex: 0 0 146px;
  width: 146px;
  min-height: 272px;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s ease, border-color 0.3s ease;
  cursor: pointer;
}

.srv-band.theme-navy .srv-slide-card {
  background: linear-gradient(180deg, #072241 0%, #041529 100%);
  border: 1px solid rgba(56, 189, 248, 0.16);
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.38);
}

.srv-band.theme-navy .srv-slide-card:hover {
  transform: translateY(-6px);
  border-color: var(--orange-400);
  box-shadow: 0 16px 34px rgba(0, 0, 0, 0.55), 0 0 18px rgba(251, 191, 36, 0.2);
}

.srv-band.theme-white .srv-slide-card {
  background: var(--white);
  border: 1px solid #cbd5e1;
  box-shadow: 0 10px 24px rgba(6, 24, 46, 0.08);
}

.srv-band.theme-white .srv-slide-card:hover {
  transform: translateY(-6px);
  border-color: var(--orange-500);
  box-shadow: 0 18px 34px rgba(6, 24, 46, 0.15);
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
  transition: transform 0.45s ease;
}

.srv-slide-card:hover .srv-slide-img {
  transform: scale(1.07);
}

/* Bottom gradient fade on card photo into card body */
.srv-band.theme-navy .srv-slide-img-fade {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(4, 21, 41, 0) 45%, rgba(4, 21, 41, 0.96) 100%);
  pointer-events: none;
}

.srv-band.theme-white .srv-slide-img-fade {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(6, 24, 46, 0) 55%, rgba(6, 24, 46, 0.45) 100%);
  pointer-events: none;
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

/* 4. 5-STEP PROCESS SECTION ("مسیر دریافت خدمات") */'''

content = pattern.sub(new_css, content)

with open('/home/user/generate_services_page.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS REVERTED SUCCESSFULLY")
