"""Project-domain portfolio built exclusively from existing site capabilities.

These are not completed-project case studies. No client, completion date,
project size or track-record metric is invented. Images are conceptual.
"""
from pathlib import Path
from html import escape
from collections import Counter
import json

ROOT = Path('/home/user')
CATEGORIES = {
    'engineering': 'مهندسی و ساختمان',
    'industry': 'صنعت و تولید',
    'mining': 'معدن و طرح‌های فنی',
    'studies': 'مطالعات و توسعه',
}
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


def build_projects_content(gsp):
    records = json.loads((ROOT / 'src/projects-data.json').read_text(encoding='utf-8'))
    assert len({record['slug'] for record in records}) == len(records)
    images = {}
    for record in records:
        slug = record['slug']
        assert record['category'] in CATEGORIES
        assert all(service in gsp.all_dedicated_services for service in record['serviceSlugs']), slug
        image_path = ROOT / 'public/assets' / record['image']
        assert image_path.exists(), image_path
        images[slug] = gsp.to_data_uri(str(image_path), 'image/jpeg')
        record['categoryLabel'] = CATEGORIES[record['category']]
        record['conceptual'] = True
        record['caseStudy'] = False
        if record.get('summaryFrom'):
            record['summary'] = gsp.all_dedicated_services[record['summaryFrom']]['desc']
        record['serviceLinks'] = [
            {'slug': service, 'title': gsp.all_dedicated_services[service]['title'],
             'href': f'services/{service}/index.html'}
            for service in record['serviceSlugs']
        ]
        page = record.get('sourcePage', 'services')
        record['source'] = {
            'page': page, 'hash': record['sourceTarget'], 'label': record['sourceSection'],
            'href': ('index.html' if page == 'home' else 'services.html') + record['sourceTarget'],
        }
    counts = Counter(r['category'] for r in records)

    def card(record):
        slug = record['slug']
        url = 'projects.html?project=' + slug
        return f'''
        <article class="prj-card" data-project-id="{slug}" data-project-category="{record['category']}">
          <a class="prj-card-image" href="{url}" data-project-slug="{slug}" tabindex="-1" aria-hidden="true"><img src="{images[slug]}" alt="تصویر مفهومی {escape(record['title'])}" width="1200" height="805" loading="lazy"></a>
          <div class="prj-card-body"><div class="prj-card-overline"><span class="prj-card-category">{record['categoryLabel']}</span><span class="prj-card-kind">حوزه خدمات</span></div>
            <h3 data-editable="true"><a href="{url}" data-project-slug="{slug}">{escape(record['title'])}</a></h3>
            <p class="prj-card-description" data-editable="true">{escape(record['summary'])}</p>
            <div class="prj-card-footer"><span>{escape(record['focus'])}</span><a href="{url}" data-project-slug="{slug}">معرفی حوزه <span aria-hidden="true">←</span></a></div>
          </div>
        </article>'''

    buttons = ''.join(
        f'<button type="button" data-project-filter="{category}" aria-pressed="false">{label} <span>{str(counts[category]).translate(FA)}</span></button>'
        for category, label in CATEGORIES.items()
    )
    content = (ROOT / 'src/projects-page.html').read_text(encoding='utf-8')
    for token, value in {
        '@@PROJECT_HERO_IMAGE@@': images['industrial-shed'],
        '@@PROJECT_COUNT_FA@@': str(len(records)).translate(FA),
        '@@PROJECT_FILTERS@@': buttons,
        '@@PROJECT_CARDS@@': ''.join(card(record) for record in records),
    }.items():
        content = content.replace(token, value)
    assert '@@' not in content
    detail = (ROOT / 'src/project-detail.html').read_text(encoding='utf-8')
    return content, detail, {r['slug']: r for r in records}, images
