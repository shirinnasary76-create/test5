#!/usr/bin/env python3
with open('/home/user/generate_services_page.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = """        slides_markup += f'''
          <a href="services/{s['slug']}/index.html" class="srv-slide-card" data-service-slug="{s['slug']}" data-service-title="{s['title']}" data-service-desc="{s['sub']}" style="--srv-title-color: var(--srv-color-{s['color_idx']});">
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
          </a>
        '''"""

new = """        # Theme-inverted card: white band → navy card, navy band → white card
        card_theme = "white" if band["theme"] == "navy" else "navy"
        slides_markup += f'''
          <a href="services/{s['slug']}/index.html" class="srv-slide-card card-theme-{card_theme}" data-service-slug="{s['slug']}" data-service-title="{s['title']}" data-service-desc="{s['sub']}">
            <div class="srv-slide-img-wrap">
              <img src="{s['img']}" alt="{s['title']}" class="srv-slide-img" style="object-position:{s['pos']};filter:{filt};" loading="lazy" />
              <div class="srv-slide-title-overlay"></div>
              <h3 class="srv-slide-title" data-editable="true">{s['title']}</h3>
            </div>
            <div class="srv-slide-footer">
              <span class="srv-slide-meta" data-editable="true">{s['meta']}</span>
              <span class="srv-slide-arrow-icon" aria-hidden="true">→</span>
            </div>
          </a>
        '''"""

if old in content:
    content = content.replace(old, new, 1)
    with open('/home/user/generate_services_page.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("REPLACED SUCCESSFULLY")
else:
    print("OLD TEXT NOT FOUND")
