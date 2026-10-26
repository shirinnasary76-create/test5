"""Build all Delgosha pages with the original homepage's shared header/footer.

The main documents are self-contained (including fonts and images) and retain
in-page navigation. Dedicated service URLs also work on direct load/reload.
Run: python3 /home/user/build_all_pages.py
"""
from pathlib import Path
from html import escape
from types import SimpleNamespace
import json
import re
import runpy
import subprocess
from generate_news_content import build_news_content
from generate_projects_content import build_projects_content

ROOT = Path('/home/user')
SRC = ROOT / 'src'
source_settings = json.loads((SRC / 'site-config.json').read_text(encoding='utf-8'))
DESKTOP_WIDTH = int(source_settings.get('display', {}).get('desktopWidth', 1360))
assert 1024 <= DESKTOP_WIDTH <= 2560, 'Desktop reference width is outside the supported range.'
display_settings = {'mobileLayout': 'desktop', 'desktopWidth': DESKTOP_WIDTH}

subprocess.run(['python3', str(ROOT / 'optimize_web_assets.py')], check=True)
subprocess.run(['python3', str(ROOT / 'generate_html.py')], check=True)
gsp = SimpleNamespace(**runpy.run_path(str(ROOT / 'generate_services_page.py')))
home_raw = (ROOT / 'index.html').read_text(encoding='utf-8')
srv_raw = (ROOT / 'services.html').read_text(encoding='utf-8')
# Compact only embedded web copies; the original public source assets stay intact.
web_asset_map = json.loads((SRC / 'web-asset-map.json').read_text())
web_uri_map = {}
for original, compact in web_asset_map.items():
    mime = 'image/png' if original.endswith('.png') else 'image/jpeg'
    old_uri = gsp.to_data_uri(str(ROOT / 'public/assets' / original), mime)
    web_uri_map[old_uri] = gsp.to_data_uri(str(ROOT / 'public/assets' / compact), mime)


def extract(pattern, document):
    match = re.search(pattern, document, re.S)
    if not match:
        raise ValueError('Missing required generated section: ' + pattern[:100])
    return match.group(1).strip()


combined_css = extract(r'<style>(.*?)</style>', srv_raw)
combined_css += '\n' + (SRC / 'about-page.css').read_text(encoding='utf-8')
combined_css += '''
/* A single shared shell keeps navigation/contact details identical everywhere. */
#desktopStage { display: flex; flex-direction: column; min-height: var(--desktop-min-height, 100vh); }
#desktopStage > .site-header, #desktopStage > .site-footer { flex-shrink: 0; }
.site-page-view { width: 100%; flex: 1 0 auto; }
.site-page-view[aria-hidden="true"] { display: none; }
.designer-toolbar { width: max-content; max-width: none; white-space: nowrap; }
.designer-toolbar .toolbar-btn { flex-shrink: 0; white-space: nowrap; }
'''
shared_header = extract(r'(<header class="site-header">.*?</header>)', home_raw)
shared_footer = extract(r'(<footer class="site-footer".*?</footer>)', home_raw)
home_modals = extract(
    r'(<!-- ====================================================================\s*11\. INTERACTIVE MODALS.*?)<!-- Floating Quick Brand Switcher',
    home_raw,
)
home_script = (SRC / 'app.js').read_text(encoding='utf-8')
shell_script = (SRC / 'site-shell.js').read_text(encoding='utf-8')
news_script = (SRC / 'news-page.js').read_text(encoding='utf-8')
news_css = (SRC / 'news-page.css').read_text(encoding='utf-8')
news_content, news_article_content, news_articles, news_images = build_news_content(gsp)
projects_script = (SRC / 'projects-page.js').read_text(encoding='utf-8')
projects_css = (SRC / 'projects-page.css').read_text(encoding='utf-8')
projects_content, project_detail_content, projects, project_images = build_projects_content(gsp)
favicon_uri = gsp.to_data_uri(str(ROOT / 'public/assets/favicon.png'), 'image/png')


def strip_chrome(html):
    html = re.sub(r'<header class="site-header">.*?</header>', '', html, flags=re.S)
    html = re.sub(r'<footer class="site-footer".*?</footer>', '', html, flags=re.S)
    return html.strip()


home_content = strip_chrome(extract(
    r'<body[^>]*>(.*?)<!-- ====================================================================\s*11\. INTERACTIVE MODALS',
    home_raw,
))
services_content = strip_chrome(extract(
    r'<body[^>]*>(.*?)<!-- Consultation Modal -->', srv_raw,
))

# Catalogue metadata is unchanged. Preserve the older industrial-consulting URL too.
all_dedicated_services = dict(gsp.all_dedicated_services)
extra_path = SRC / 'extra-services.json'
if extra_path.exists():
    all_dedicated_services.update(json.loads(extra_path.read_text(encoding='utf-8')))

FA_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

def fa(value):
    return str(value).translate(FA_DIGITS)


expertise_cards = []
for index, band in enumerate(gsp.SIX_SHOWCASE_BANDS, start=1):
    expertise_cards.append(f'''
        <a href="services.html#{band['id']}" data-switch-page="services" data-scroll-target="#{band['id']}" class="ab-expertise-card">
          <div class="ab-expertise-card-top"><span class="ab-expertise-icon" aria-hidden="true">{band['icon_svg']}</span><span class="ab-expertise-index">{fa(f'{index:02d}')}</span></div>
          <h3 data-editable="true">{escape(band['title'])}</h3>
          <p data-editable="true">{escape(band['desc'])}</p>
          <div class="ab-expertise-card-link"><span>{fa(len(band['slides']))} خدمت تخصصی</span><span aria-hidden="true">←</span></div>
        </a>''')
about_content = (SRC / 'about-page.html').read_text(encoding='utf-8')
for token, value in {
    '@@ABOUT_IMAGE@@': gsp.img_sub1,
    '@@BAND_COUNT_FA@@': fa(len(gsp.SIX_SHOWCASE_BANDS)),
    '@@SERVICE_COUNT_FA@@': fa(len(gsp.all_dedicated_services)),
    '@@EXPERTISE_CARDS@@': '\n'.join(expertise_cards),
}.items():
    about_content = about_content.replace(token, value)
assert '@@' not in about_content

TITLES = {
    'home': 'دلگشا | هلدینگ توسعه صنعت و معدن و تجارت (صفحه اصلی و خدمات)',
    'services': 'صفحه جامع خدمات | سایت دلگشا - هلدینگ راه‌گشا (صنعت، معدن، تجارت و فنی و مهندسی)',
    'about': 'درباره ما | دلگشا — هلدینگ توسعه صنعت و معدن و تجارت',
    'news': 'اخبار و رویدادها | رسانه دلگشا — صنعت، معدن و تجارت',
    'projects': 'پروژه‌ها و حوزه‌های اجرایی | دلگشا — طراحی، صنعت و ساختمان',
}
DESCRIPTIONS = {
    'home': 'خدمات تخصصی صنعت، معدن، تجارت و فنی و مهندسی در سایت دلگشا متعلق به هلدینگ راه‌گشا؛ از اخذ مجوزهای صنعتی و تجاری تا طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری و پیمانکاری ساختمان.',
    'services': 'صفحه جامع خدمات دلگشا؛ خدمات صنعتی، معدنی، بازرگانی، فنی و مهندسی، سایر خدمات و امور ثبتی، مالی و توسعه کسب‌وکار.',
    'about': 'با دلگشا آشنا شوید؛ معرفی هلدینگ توسعه صنعت و معدن و تجارت، مأموریت، اصول همکاری، حوزه‌های تخصصی و مسیر همراهی با کسب‌وکارها.',
    'news': 'صفحه اخبار و رویدادهای دلگشا؛ قالبی برای خبرها، برنامه‌های تخصصی و مقالات حوزه صنعت، معدن، تجارت و توسعه کسب‌وکار. محتوای فعلی نمونه طراحی است.',
    'projects': 'معرفی حوزه‌های خدمات پروژه‌ای دلگشا؛ طراحی و اجرای سوله، سازه، نقشه‌برداری، دکوراسیون، پیمانکاری، توسعه صنعتی، مستندات معدنی، امکان‌سنجی و تجهیزات. تصاویر مفهومی هستند.',
}


def single_service_content(info=None):
    info = info or {'title': 'عنوان خدمت', 'cat': 'خدمات تخصصی', 'desc': '', 'highlights': []}
    highlights = ''.join(f'<li style="margin-bottom:8px;">{escape(h)}</li>' for h in info['highlights'])
    return f'''
    <nav class="srv-breadcrumb-bar" aria-label="مسیر راهنما">
      <div class="container srv-breadcrumb-list">
        <a href="index.html" data-switch-page="home">صفحه اصلی سایت</a><span>‹</span>
        <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices">بخش خدمات ما (صفحه اصلی)</a><span>‹</span>
        <a href="services.html" data-switch-page="services">صفحه جامع خدمات</a><span>‹</span>
        <span id="singleSrvBreadcrumbTitle" aria-current="page">{escape(info['title'])}</span>
      </div>
    </nav>
    <main class="container" style="padding:48px 24px;">
      <div style="background:#fff;border-radius:22px;padding:36px;box-shadow:0 14px 40px rgba(6,24,46,0.08);border:1px solid #e2e8f0;">
        <span class="srv-hero-badge" id="singleSrvBadge" style="background:rgba(244,129,11,0.12);color:#ea580c;">{escape(info['cat'])}</span>
        <h1 id="singleSrvTitle" style="font-size:32px;font-weight:900;color:#09213d;margin:10px 0 16px;">{escape(info['title'])}</h1>
        <p id="singleSrvDesc" style="font-size:15px;color:#334155;line-height:2;margin-bottom:24px;">{escape(info['desc'])}</p>
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px;padding:22px;margin-bottom:28px;">
          <h2 style="font-size:18px;font-weight:900;color:#09213d;margin-bottom:12px;">محورهای خدمات و پیگیری‌های تخصصی این بخش:</h2>
          <ul id="singleSrvHighlights" style="padding-right:20px;list-style:disc;font-size:14px;color:#1e293b;line-height:1.9;">{highlights}</ul>
        </div>
        <div style="display:flex;gap:14px;flex-wrap:wrap;">
          <a href="tel:09177056063" class="srv-btn-primary">تماس و مشاوره مستقیم: ۰۹۱۷۷۰۵۶۰۶۳</a>
          <a href="services.html" data-switch-page="services" class="srv-btn-secondary" style="color:#09213d;border-color:#09213d;">بازگشت به صفحه جامع خدمات</a>
          <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="srv-btn-secondary" style="color:#09213d;border-color:#cbd5e1;">صفحه اصلی (بخش خدمات ما)</a>
        </div>
      </div>
    </main>'''


def prefix_links(html, prefix):
    # All canonical links are relative, so the site also works in a subdirectory.
    return re.sub(
        r'href="((?:(?:index|services|about|news|projects)\.html|services/[^"?#]+)(?:\?[^"#]*)?(?:#[^"]*)?)"',
        lambda m: f'href="{prefix}{m.group(1)}"', html,
    )


def active_header(page):
    active_key = 'services' if page == 'single' else 'news' if page == 'article' else 'projects' if page == 'project' else page
    def nav_link(match):
        tag = match.group(0)
        tag = re.sub(r'class="nav-link(?: active)?"', 'class="nav-link"', tag)
        if f'data-nav-key="{active_key}"' in tag:
            tag = tag.replace('class="nav-link"', 'class="nav-link active" aria-current="page"')
        return tag
    return re.sub(r'<a\b[^>]*data-nav-key="[^"]+"[^>]*>', nav_link, shared_header)


TRANSPARENT_PIXEL = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'


def deduplicate_assets(html):
    assets = {}
    keys_by_uri = {}
    def asset(match):
        original_uri = match.group(0)
        uri = web_uri_map.get(original_uri, original_uri)
        key = keys_by_uri.get(uri)
        if not key:
            key = f'__ASSET_{len(assets) + 1}__'
            keys_by_uri[uri] = key
            assets[key] = uri
        return key
    html = re.sub(r'data:image/(?:jpeg|png);base64,[A-Za-z0-9+/=]{15000,}', asset, html)
    html = re.sub(
        r'src="(__ASSET_\d+__)"',
        lambda m: f'src="{TRANSPARENT_PIXEL}" data-asset="{m.group(1)}"', html,
    )
    def deferred_style(match):
        style = match.group(2)
        if '__ASSET_' not in style:
            return match.group(0)
        safe = re.sub(r'url\(\s*([\'\"]?)(__ASSET_\d+__)\1\s*\)', 'none', style)
        return f'style="{escape(safe, quote=True)}" data-asset-style="{escape(style, quote=True)}"'
    html = re.sub(r'\bstyle=([\'\"])(.*?)\1', deferred_style, html, flags=re.S)
    return html, assets


def toolbar_html():
    return '''
    <div class="designer-toolbar" aria-label="نوار ابزار ناوبری و سفارشی‌سازی">
      <a href="index.html" data-switch-page="home" data-toolbar-page="home" class="toolbar-btn" id="toolbarBtnHome">🏠 صفحه اصلی</a>
      <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="toolbar-btn" id="toolbarBtnHomeServices">✦ بخش خدمات ما</a>
      <a href="services.html" data-switch-page="services" data-toolbar-page="services" class="toolbar-btn" id="toolbarBtnServices">📋 صفحه جامع خدمات</a>
      <a href="about.html" data-switch-page="about" data-toolbar-page="about" class="toolbar-btn" id="toolbarBtnAbout">درباره ما</a>
      <a href="news.html" data-switch-page="news" data-toolbar-page="news" class="toolbar-btn" id="toolbarBtnNews">اخبار و رویدادها</a>
      <a href="projects.html" data-switch-page="projects" data-toolbar-page="projects" class="toolbar-btn" id="toolbarBtnProjects">پروژه‌ها</a>
      <button type="button" class="toolbar-btn" id="btnToggleLogoLayout" title="تغییر چیدمان لوگو">لوگو: افقی (هدر)</button>
      <button type="button" class="toolbar-btn" id="btnToggleEdit" title="ویرایش مستقیم تمام متون">✎ ویرایش متن‌ها</button>
    </div>
    <div class="toast-msg" id="toastMsg" role="status" aria-live="polite"></div>'''


def build_document(default_page='home', prefix='', service_slug=None, include_all_views=True):
    info = all_dedicated_services.get(service_slug) if service_slug else None
    title = f"{info['title']} | خدمات سایت دلگشا - هلدینگ راه‌گشا" if info else TITLES[default_page]
    description = info['desc'] if info else DESCRIPTIONS[default_page]
    views = []
    if include_all_views:
        views.extend([
            ('home', 'homePageView', home_content),
            ('services', 'servicesPageView', services_content),
            ('about', 'aboutPageView', about_content),
            ('news', 'newsPageView', news_content),
            ('article', 'newsArticlePageView', news_article_content),
            ('projects', 'projectsPageView', projects_content),
            ('project', 'projectDetailPageView', project_detail_content),
        ])
    views.append(('single', 'singleServicePageView', single_service_content(info)))
    views_markup = '\n'.join(
        f'<div id="{view_id}" class="site-page-view" style="display:{"block" if key == default_page else "none"};" aria-hidden="{"false" if key == default_page else "true"}">{content}</div>'
        for key, view_id, content in views
    )
    body_markup = f'''
    <div id="desktopViewportShell"><div id="desktopStage">
      <!-- Shared header: sourced directly from the original homepage. -->
      {active_header(default_page)}
      {views_markup}
      <!-- Shared footer: sourced directly from the original homepage. -->
      {shared_footer}
    </div></div>
    {home_modals}
    {toolbar_html()}
    '''
    body_markup = prefix_links(body_markup, prefix)
    body_markup, assets = deduplicate_assets(body_markup)
    asset_key_by_uri = {uri: key for key, uri in assets.items()}
    metadata = news_articles if include_all_views else {
        slug: {key: value for key, value in article.items() if key in ['slug', 'title', 'kind', 'kindLabel', 'topic', 'topicLabel', 'bandId']}
        for slug, article in news_articles.items()
    }
    project_metadata = projects if include_all_views else {
        slug: {key: value for key, value in project.items() if key in ['slug', 'title', 'category', 'categoryLabel', 'focus', 'conceptual', 'caseStudy']}
        for slug, project in projects.items()
    }
    page_css = combined_css + ('\n' + news_css + '\n' + projects_css if include_all_views else '')
    page_news_script = news_script if include_all_views else ''
    page_projects_script = projects_script if include_all_views else ''
    site_config = {
        'root': prefix or './', 'defaultPage': default_page, 'display': display_settings,
        'defaultSlug': service_slug, 'titles': TITLES, 'descriptions': DESCRIPTIONS,
        'services': all_dedicated_services, 'assets': assets,
        'newsArticles': metadata,
        'newsImages': {slug: asset_key_by_uri[web_uri_map.get(uri, uri)] for slug, uri in news_images.items() if web_uri_map.get(uri, uri) in asset_key_by_uri},
        'projects': project_metadata,
        'projectImages': {slug: asset_key_by_uri[web_uri_map.get(uri, uri)] for slug, uri in project_images.items() if web_uri_map.get(uri, uri) in asset_key_by_uri},
    }
    config_json = json.dumps(site_config, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <!-- Mobile uses the same layout viewport as desktop; native pinch zoom remains enabled. -->
  <meta name="viewport" content="width={DESKTOP_WIDTH}, minimum-scale=0.1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#06182e">
  <title>{escape(title)}</title>
  <link rel="icon" type="image/png" href="{favicon_uri}">
  <style>{page_css}</style>
</head>
<body id="top" data-active-page="{default_page}">
{body_markup}
<script>
window.DELGOSHA_SITE = {config_json};
{page_news_script}
{page_projects_script}
{shell_script}
{home_script}
</script>
</body>
</html>
'''


def write_page(relative_path, **options):
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    document = build_document(**options)
    path.write_text(document, encoding='utf-8')
    return len(document.encode('utf-8'))


outputs = {
    'index.html': write_page('index.html', default_page='home'),
    'services.html': write_page('services.html', default_page='services'),
    'about.html': write_page('about.html', default_page='about'),
    'news.html': write_page('news.html', default_page='news'),
    'projects.html': write_page('projects.html', default_page='projects'),
}
write_page('public/index.html', default_page='home', prefix='../')
write_page('services/index.html', default_page='services', prefix='../')
write_page('about/index.html', default_page='about', prefix='../')
write_page('news/index.html', default_page='news', prefix='../')
write_page('projects/index.html', default_page='projects', prefix='../')
for slug in all_dedicated_services:
    write_page(f'services/{slug}/index.html', default_page='single', prefix='../../',
               service_slug=slug, include_all_views=False)

print('Built homepage, services, About, News & Events and Projects with the shared original homepage header/footer.')
print(f'Updated {len(all_dedicated_services)} existing dedicated service pages, plus directory aliases.')
for filename, size in outputs.items():
    print(f'{filename}: {size:,} bytes')
