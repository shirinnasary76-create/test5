"""News-page templates and explicitly labelled demonstration content.

No sample entry is a verified news item or an announced real-world event.
Replace src/news-data.json with approved copy to publish real content.
"""
from pathlib import Path
from html import escape
from collections import Counter
import json

ROOT = Path('/home/user')
TOPICS = {
    'industry': ('صنعت و تولید', 'group-industry'),
    'mining': ('معدن و کاداستر', 'group-mining'),
    'trade': ('تجارت و بازرگانی', 'group-trade'),
    'engineering': ('فنی و مهندسی', 'group-engineering'),
    'registration': ('ثبتی و مالی', 'group-registration'),
    'other': ('سایر خدمات', 'group-other-services'),
}
KINDS = {'news': 'خبر', 'event': 'رویداد', 'guide': 'مقاله و راهنما'}
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
CALENDAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 2v6m10-6v6M3 11h18m-14 4h3m4 0h3m-10 3h3"/></svg>'


def build_news_content(gsp):
    records = json.loads((ROOT / 'src/news-data.json').read_text(encoding='utf-8'))
    assert len({r['slug'] for r in records}) == len(records)
    images = {r['slug']: gsp.to_data_uri(str(ROOT / 'public/assets' / r['image']), 'image/jpeg') for r in records}
    for r in records:
        r['topicLabel'], r['bandId'] = TOPICS[r['topic']]
        r['kindLabel'] = KINDS[r['kind']]
        r['sample'] = True
    counts = Counter(r['topic'] for r in records)

    def link(r):
        return 'news.html?article=' + r['slug']

    def card(r):
        slug = r['slug']
        footer_meta = 'رویداد نمونه' if r['kind'] == 'event' else str(r['minutes']).translate(FA) + ' دقیقه مطالعه'
        action = 'جزئیات رویداد' if r['kind'] == 'event' else 'ادامه مطلب'
        return f'''
          <article class="nw-card" data-nw-id="{slug}" data-nw-card-kind="{r['kind']}" data-nw-card-topic="{r['topic']}">
            <a class="nw-card-image-link" href="{link(r)}" data-news-slug="{slug}" tabindex="-1" aria-hidden="true"><img src="{images[slug]}" alt="تصویر مفهومی {escape(r['topicLabel'])}" loading="lazy" width="600" height="300"></a>
            <div class="nw-card-body"><div class="nw-card-labels"><span class="nw-kind-badge" data-kind="{r['kind']}">{r['kindLabel']}</span><span class="nw-card-topic">{r['topicLabel']}</span></div>
              <h3 data-editable="true"><a href="{link(r)}" data-news-slug="{slug}">{escape(r['title'])}</a></h3>
              <p class="nw-card-description" data-editable="true">{escape(r['excerpt'])}</p>
              <div class="nw-card-footer"><span>{CLOCK}{footer_meta}</span><a href="{link(r)}" data-news-slug="{slug}">{action}<span aria-hidden="true">←</span></a></div>
              <p class="nw-card-draft">محتوای نمونه • پیش‌نویس</p>
            </div>
          </article>'''

    featured = records[0]
    feature = f'''
      <article class="nw-feature-card" aria-labelledby="nwFeatureTitle">
        <div class="nw-feature-copy"><div class="nw-feature-kicker"><span aria-hidden="true"></span> مطلب منتخب</div><span class="nw-kind-badge" data-kind="{featured['kind']}">{featured['topicLabel']}</span>
          <h2 id="nwFeatureTitle" data-editable="true"><a href="{link(featured)}" data-news-slug="{featured['slug']}">{escape(featured['title'])}</a></h2>
          <p data-editable="true">{escape(featured['excerpt'])}</p>
          <div class="nw-feature-footer"><span>محتوای نمونه · {str(featured['minutes']).translate(FA)} دقیقه مطالعه</span><a href="{link(featured)}" data-news-slug="{featured['slug']}">مطالعه مطلب <span aria-hidden="true">←</span></a></div>
        </div>
        <a class="nw-feature-photo" href="{link(featured)}" data-news-slug="{featured['slug']}" tabindex="-1" aria-hidden="true"><img src="{images[featured['slug']]}" alt="تصویری مفهومی از فعالیت صنعتی" width="600" height="600" fetchpriority="high"></a>
      </article>'''
    events = '\n'.join(f'''
        <a href="{link(r)}" data-news-slug="{r['slug']}"><span class="nw-event-icon" aria-hidden="true">{CALENDAR}</span><div class="nw-event-text"><h3>{escape(r['title'])}</h3><p>{escape(r['eventType'])} • محتوای نمونه</p><span>زمان برگزاری: پس از اعلام</span></div></a>'''
        for r in records if r['kind'] == 'event')
    topic_buttons = '\n'.join(f'<button type="button" data-nw-topic="{key}" aria-pressed="false"><span>{value[0]}</span><span>{str(counts[key]).translate(FA)}</span></button>' for key, value in TOPICS.items())
    options = '\n'.join(f'<option value="{key}">{value[0]}</option>' for key, value in TOPICS.items())
    content = (ROOT / 'src/news-page.html').read_text(encoding='utf-8')
    replacements = {
        '@@NEWS_FEATURE@@': feature, '@@NEWS_TOPIC_OPTIONS@@': options,
        '@@NEWS_CARDS@@': '\n'.join(card(r) for r in records),
        '@@NEWS_EVENTS@@': events, '@@NEWS_TOPICS@@': topic_buttons,
    }
    for token, value in replacements.items():
        content = content.replace(token, value)
    assert '@@' not in content
    article_template = (ROOT / 'src/news-article.html').read_text(encoding='utf-8')
    return content, article_template, {r['slug']: r for r in records}, images
