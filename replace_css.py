#!/usr/bin/env python3
with open('/home/user/generate_services_page.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire slide card CSS section
old_css_start = '''/* Individual Vertical Slide Card - Image Top + Title Below (RTL) */
.srv-slide-card {'''

old_css_end = '''/* 4. 5-STEP PROCESS SECTION ("مسیر دریافت خدمات") */
.srv-process-section {'''

import re

# Find the CSS block between slide card start and process section
pattern = re.compile(
    r'/\* Individual Vertical Slide Card.*?\n\n/\* 4\. 5-STEP PROCESS SECTION',
    re.DOTALL
)

new_css = '''/* Individual Slide Card - Image Filled with Title Overlay (matching reference image style) */
.srv-slide-card {
  flex: 0 0 200px;
  width: 200px;
  min-height: 200px;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s ease, border-color 0.3s ease;
  cursor: pointer;
  text-decoration: none;
}

/* Theme-inverted cards: white band → navy card, navy band → white card */
.srv-slide-card.card-theme-white {
  background: var(--white);
  border: 1px solid #cbd5e1;
  box-shadow: 0 10px 24px rgba(6, 24, 46, 0.08);
}

.srv-slide-card.card-theme-white:hover {
  transform: translateY(-6px);
  border-color: var(--orange-500);
  box-shadow: 0 18px 34px rgba(6, 24, 46, 0.15);
}

.srv-slide-card.card-theme-navy {
  background: linear-gradient(180deg, #072241 0%, #041529 100%);
  border: 1px solid rgba(56, 189, 248, 0.16);
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.38);
}

.srv-slide-card.card-theme-navy:hover {
  transform: translateY(-6px);
  border-color: var(--orange-400);
  box-shadow: 0 16px 34px rgba(0, 0, 0, 0.55), 0 0 18px rgba(251, 191, 36, 0.2);
}

/* Image fills the entire card */
.srv-slide-img-wrap {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
}

.srv-slide-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform 0.45s ease;
}

.srv-slide-card:hover .srv-slide-img {
  transform: scale(1.06);
}

/* Professional highlight overlay behind title - semi-transparent dark/light based on card theme */
.srv-slide-title-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.35) 40%,
    rgba(0, 0, 0, 0.75) 100%);
  pointer-events: none;
  z-index: 1;
}

/* Card-theme-white gets a lighter overlay so white text still pops */
.srv-slide-card.card-theme-white .srv-slide-title-overlay {
  background: linear-gradient(180deg,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.25) 40%,
    rgba(0, 0, 0, 0.55) 100%);
}

/* Title positioned inside image area, bottom-left (RTL: right side) */
.srv-slide-title {
  position: absolute;
  bottom: 18px;
  left: 16px;
  right: 16px;
  font-size: 14px;
  font-weight: 800;
  line-height: 1.35;
  margin: 0;
  z-index: 2;
  color: var(--white);
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.45);
  display: -webkit-box;
  overflow: hidden;
}

/* card-theme-white → navy text for contrast */
.srv-slide-card.card-theme-white .srv-slide-title {
  color: var(--navy-900);
  text-shadow: 0 2px 8px rgba(255, 255, 255, 0.6);
}

/* Footer strip at bottom of card - meta + arrow */
.srv-slide-footer {
  position: absolute;
  bottom: 12px;
  left: 16px;
  right: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  z-index: 2;
}

.srv-slide-meta {
  font-size: 10px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.85);
  background: rgba(0, 0, 0, 0.35);
  padding: 2px 8px;
  border-radius: 4px;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.4);
}

.srv-slide-card.card-theme-white .srv-slide-meta {
  color: var(--navy-700);
  background: rgba(255, 255, 255, 0.75);
  text-shadow: none;
}

.srv-slide-arrow-icon {
  font-size: 14px;
  font-weight: 900;
  color: var(--orange-400);
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4));
  transition: transform 0.2s ease;
}

.srv-slide-card.card-theme-white .srv-slide-arrow-icon {
  color: var(--orange-600);
  filter: none;
}

.srv-slide-card:hover .srv-slide-arrow-icon {
  transform: translateX(4px);
}

/* Remove old sub-description from cards (title only, like reference image) */
.srv-slide-body, .srv-slide-sub, .srv-slide-img-fade {
  display: none !important;
}

/* 4. 5-STEP PROCESS SECTION ("مسیر دریافت خدمات") */
.srv-process-section {'''

content = pattern.sub(new_css, content)

with open('/home/user/generate_services_page.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS REPLACED SUCCESSFULLY")
