import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import webbrowser
from urllib.parse import quote
import pyperclip
import os, json, re
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ─── RENK PALETİ ──────────────────────────────────────────────────────────────
C = {
    "bg":        "#080c14",
    "bg2":       "#0c1220",
    "surface":   "#101828",
    "surface2":  "#151f30",
    "card":      "#1a2540",
    "border":    "#1e2d47",
    "border2":   "#253356",
    "accent":    "#38bdf8",
    "accent2":   "#6366f1",
    "accent3":   "#f472b6",
    "text":      "#e2e8f0",
    "text2":     "#94a3b8",
    "muted":     "#475569",
    "green":     "#34d399",
    "red":       "#f87171",
    "amber":     "#fbbf24",
    "orange":    "#fb923c",
    "purple":    "#a78bfa",
    "teal":      "#2dd4bf",
}

FONT_MONO  = ("Consolas", 11)
FONT_BOLD  = ("Consolas", 11, "bold")
FONT_TITLE = ("Consolas", 13, "bold")
FONT_SMALL = ("Consolas", 10)

# ─── DİL PAKETLERİ ────────────────────────────────────────────────────────────
LANG = {
    "TR": {
        "app_title":    "OSINT INTELLİGENCE ENGINE  v4.0",
        "search_engine":"ARAMA MOTORU",
        "lang_label":   "DİL",
        "tabs": ["👤  Kişi", "🏢  Şirket", "🌐  Domain / IP", "💥  Sızıntı", "🛠️  Araçlar", "📋  Geçmiş"],
        "generate":     "▶  DORK ÜRET",
        "copy_all":     "Tümünü Kopyala",
        "open_all":     "Tümünü Aç",
        "export_html":  "HTML Rapor",
        "export_txt":   "TXT İndir",
        "export_json":  "JSON İndir",
        "clear":        "Temizle",
        "clear_hist":   "Geçmişi Temizle",
        "dl_hist":      "TXT İndir",
        "dl_hist_json": "JSON İndir",
        "no_query":     "Henüz sorgu üretilmedi.",
        "ready":        "Hazır.",
        "copied":       "Kopyalandı!",
        "copy_btn":     "KOPYALA",
        "open_btn":     "AÇ",
        "total":        "Toplam:",
        "dorks":        "sorgu",
        "quick_svc":    "🔗  HIZLI SERVİSLER",
        "dorksgen":     "dork üretildi ✓",
        "err_name":     "Ad Soyad zorunlu!",
        "err_company":  "Şirket adı zorunlu!",
        "err_domain":   "Domain veya IP zorunlu!",
        "err_breach":   "En az bir alan doldurulmalı!",
        "err_tools":    "En az bir alan girin!",
        "saved":        "Kaydedildi:",
        "err_save":     "Hata:",
        "open_confirm": "sekme açılacak. Devam edilsin mi?",
        "open_sure":    "Emin misin?",
        "hist_empty":   "Geçmiş boş!",
        "copy_hist":    "Kopyala",
        "open_hist":    "Aç",
        # Field labels – Kişi
        "k_name":    "Ad Soyad *",       "k_name_ph":    "Ahmet Yılmaz...",
        "k_city":    "Şehir",             "k_city_ph":    "İstanbul...",
        "k_job":     "Meslek",            "k_job_ph":     "Yazılım Mühendisi...",
        "k_company": "Şirket",            "k_company_ph": "Acme A.Ş....",
        "k_phone":   "Telefon",           "k_phone_ph":   "+90 5xx xxx xx xx",
        "k_email":   "E-posta domain",   "k_email_ph":   "sirket.com",
        "k_social":  "Sosyal Medya Adı", "k_social_ph":  "@kullanici",
        "k_age":     "Doğum Yılı",       "k_age_ph":     "1990",
        "k_exclude": "Hariç tut",        "k_exclude_ph": "futbol, haber...",
        # Field labels – Şirket
        "s_company":  "Şirket Adı *",    "s_company_ph": "Acme A.Ş....",
        "s_domain":   "Domain",          "s_domain_ph":  "acme.com",
        "s_city":     "Şehir",           "s_city_ph":    "İstanbul",
        "s_sector":   "Sektör",          "s_sector_ph":  "Teknoloji",
        "s_founder":  "Kurucu",          "s_founder_ph": "Ahmet Bey",
        "s_exclude":  "Hariç tut",       "s_exclude_ph": "reklam, tanıtım",
        # Field labels – Domain/IP
        "d_domain":  "Domain",           "d_domain_ph":  "example.com",
        "d_ip":      "IP Adresi",        "d_ip_ph":      "192.168.1.1",
        "d_org":     "Organizasyon/ASN", "d_org_ph":     "Türk Telekom",
        "d_tech":    "Teknoloji",        "d_tech_ph":    "WordPress, nginx...",
        "d_exclude": "Hariç tut",        "d_exclude_ph": "",
        # Field labels – Sızıntı
        "b_email":    "E-posta",         "b_email_ph":   "user@example.com",
        "b_username": "Kullanıcı Adı",   "b_username_ph":"username123",
        "b_name":     "Ad Soyad",        "b_name_ph":    "Kenan Yıldız",
        "b_phone":    "Telefon",         "b_phone_ph":   "+90 5xx...",
        "b_hash":     "Hash / Şifre",    "b_hash_ph":    "md5/sha1...",
        "b_exclude":  "Hariç tut",       "b_exclude_ph": "",
        # Gruplar
        "group_social":   "🌐  Sosyal Medya",
        "group_profile":  "👤  Profil & CV",
        "group_contact":  "📧  İletişim & E-posta",
        "group_loc":      "📍  Konum & Coğrafya",
        "group_news":     "📰  Haber & Medya",
        "group_docs":     "📄  Belgeler & Dosyalar",
        "group_adv":      "🔍  İleri Sorgular",
        "group_company":  "🏢  Genel Şirket",
        "group_finance":  "💰  Finansal & Yasal",
        "group_staff":    "👥  Çalışanlar & Yönetim",
        "group_digital":  "🌐  Dijital Varlık",
        "group_rep":      "📰  Haberler & İtibar",
        "group_domain":   "🌐  Domain Keşfi",
        "group_subdom":   "🔧  Alt Domain & Teknoloji",
        "group_email2":   "📧  E-posta Keşfi",
        "group_sec":      "🔒  Güvenlik & Açık",
        "group_ip":       "🖥️  IP Keşfi",
        "group_org":      "🏛️  Organizasyon",
        "group_emailleak":"📬  E-posta Sızıntı",
        "group_userleak": "👤  Kullanıcı Adı İzi",
        "group_nameleak": "🔎  İsim Sızıntı",
        "group_phoneleak":"📱  Telefon Sızıntı",
        "group_external": "🔗  Harici Servisler",
        # Araçlar
        "tool_hash_lbl":    "Hash Değeri",
        "tool_hash_ph":     "5f4dcc3b5aa765d61d8327deb882cf99",
        "tool_hash_btn":    "Hash Tanımla",
        "tool_email_lbl":   "E-posta Adresi",
        "tool_email_ph":    "user@example.com",
        "tool_email_btn":   "Doğrula",
        "tool_phone_lbl":   "Telefon",
        "tool_phone_ph":    "+90 532 000 0000",
        "tool_phone_btn":   "Analiz Et",
        "tool_uname_lbl":   "Kullanıcı Adı",
        "tool_uname_ph":    "username123",
        "tool_uname_btn":   "Tarama Yap",
        "tool_kw_lbl":      "Anahtar Kelime",
        "tool_kw_ph":       "hedef şirket",
        "tool_copy_result": "Kopyala",
        "tool_dork_done":   "Dork oluşturuldu.",
        "sec_hash":         "🔑  Hash Tanımlama",
        "sec_email_val":    "📧  E-posta Doğrulama",
        "sec_phone_val":    "📱  Telefon Analiz",
        "sec_uname":        "👤  Kullanıcı Adı Ara",
        "sec_custom":       "🔧  Özel Dork Oluşturucu",
        "td_site_lbl":      "site:",
        "td_site_ph":       "example.com",
        "td_ft_lbl":        "filetype:",
        "td_ft_ph":         "pdf",
        "td_inurl_lbl":     "inurl:",
        "td_inurl_ph":      "admin",
        "td_intext_lbl":    "intext:",
        "td_intext_ph":     "password",
        "td_intitle_lbl":   "intitle:",
        "td_intitle_ph":    "dashboard",
        "td_excl_lbl":      "Hariç (-)",
        "td_excl_ph":       "reklam, haber",
        "td_btn":           "▶  Dork Oluştur",
    },
    "EN": {
        "app_title":    "OSINT INTELLIGENCE ENGINE  v4.0",
        "search_engine":"SEARCH ENGINE",
        "lang_label":   "LANG",
        "tabs": ["👤  Person", "🏢  Company", "🌐  Domain / IP", "💥  Breach", "🛠️  Tools", "📋  History"],
        "generate":     "▶  GENERATE",
        "copy_all":     "Copy All",
        "open_all":     "Open All",
        "export_html":  "HTML Report",
        "export_txt":   "Download TXT",
        "export_json":  "Download JSON",
        "clear":        "Clear",
        "clear_hist":   "Clear History",
        "dl_hist":      "Download TXT",
        "dl_hist_json": "Download JSON",
        "no_query":     "No queries generated yet.",
        "ready":        "Ready.",
        "copied":       "Copied!",
        "copy_btn":     "COPY",
        "open_btn":     "OPEN",
        "total":        "Total:",
        "dorks":        "dorks",
        "quick_svc":    "🔗  QUICK SERVICES",
        "dorksgen":     "dorks generated ✓",
        "err_name":     "Full name is required!",
        "err_company":  "Company name is required!",
        "err_domain":   "Domain or IP is required!",
        "err_breach":   "At least one field is required!",
        "err_tools":    "Enter at least one field!",
        "saved":        "Saved:",
        "err_save":     "Error:",
        "open_confirm": "tabs will open. Continue?",
        "open_sure":    "Are you sure?",
        "hist_empty":   "History is empty!",
        "copy_hist":    "Copy",
        "open_hist":    "Open",
        # Field labels – Person
        "k_name":    "Full Name *",      "k_name_ph":    "John Doe...",
        "k_city":    "City",             "k_city_ph":    "New York...",
        "k_job":     "Job Title",        "k_job_ph":     "Software Engineer...",
        "k_company": "Company",          "k_company_ph": "Acme Inc....",
        "k_phone":   "Phone",            "k_phone_ph":   "+1 xxx xxx xxxx",
        "k_email":   "Email domain",     "k_email_ph":   "company.com",
        "k_social":  "Social Handle",   "k_social_ph":  "@username",
        "k_age":     "Birth Year",       "k_age_ph":     "1990",
        "k_exclude": "Exclude",         "k_exclude_ph": "news, football...",
        # Field labels – Company
        "s_company":  "Company Name *", "s_company_ph": "Acme Inc....",
        "s_domain":   "Domain",         "s_domain_ph":  "acme.com",
        "s_city":     "City",           "s_city_ph":    "New York",
        "s_sector":   "Sector",         "s_sector_ph":  "Technology",
        "s_founder":  "Founder",        "s_founder_ph": "John Smith",
        "s_exclude":  "Exclude",        "s_exclude_ph": "ads, promo",
        # Field labels – Domain/IP
        "d_domain":  "Domain",          "d_domain_ph":  "example.com",
        "d_ip":      "IP Address",      "d_ip_ph":      "192.168.1.1",
        "d_org":     "Org / ASN",       "d_org_ph":     "ISP name",
        "d_tech":    "Technology",      "d_tech_ph":    "WordPress, nginx...",
        "d_exclude": "Exclude",         "d_exclude_ph": "",
        # Field labels – Breach
        "b_email":    "Email",          "b_email_ph":   "user@example.com",
        "b_username": "Username",       "b_username_ph":"username123",
        "b_name":     "Full Name",      "b_name_ph":    "John Doe",
        "b_phone":    "Phone",          "b_phone_ph":   "+1 xxx...",
        "b_hash":     "Hash / Password","b_hash_ph":    "md5/sha1...",
        "b_exclude":  "Exclude",        "b_exclude_ph": "",
        # Groups
        "group_social":   "🌐  Social Media",
        "group_profile":  "👤  Profile & CV",
        "group_contact":  "📧  Contact & Email",
        "group_loc":      "📍  Location",
        "group_news":     "📰  News & Media",
        "group_docs":     "📄  Documents & Files",
        "group_adv":      "🔍  Advanced Queries",
        "group_company":  "🏢  General Company",
        "group_finance":  "💰  Financial & Legal",
        "group_staff":    "👥  Staff & Management",
        "group_digital":  "🌐  Digital Presence",
        "group_rep":      "📰  News & Reputation",
        "group_domain":   "🌐  Domain Discovery",
        "group_subdom":   "🔧  Subdomains & Tech",
        "group_email2":   "📧  Email Discovery",
        "group_sec":      "🔒  Security & Exploits",
        "group_ip":       "🖥️  IP Discovery",
        "group_org":      "🏛️  Organization",
        "group_emailleak":"📬  Email Leak",
        "group_userleak": "👤  Username Trace",
        "group_nameleak": "🔎  Name-Based Leak",
        "group_phoneleak":"📱  Phone Leak",
        "group_external": "🔗  External Services",
        # Tools
        "tool_hash_lbl":    "Hash Value",
        "tool_hash_ph":     "5f4dcc3b5aa765d61d8327deb882cf99",
        "tool_hash_btn":    "Identify Hash",
        "tool_email_lbl":   "Email Address",
        "tool_email_ph":    "user@example.com",
        "tool_email_btn":   "Validate",
        "tool_phone_lbl":   "Phone Number",
        "tool_phone_ph":    "+1 555 000 0000",
        "tool_phone_btn":   "Analyze",
        "tool_uname_lbl":   "Username",
        "tool_uname_ph":    "username123",
        "tool_uname_btn":   "Search",
        "tool_kw_lbl":      "Keyword",
        "tool_kw_ph":       "target company",
        "tool_copy_result": "Copy",
        "tool_dork_done":   "Dork generated.",
        "sec_hash":         "🔑  Hash Identifier",
        "sec_email_val":    "📧  Email Validator",
        "sec_phone_val":    "📱  Phone Analyzer",
        "sec_uname":        "👤  Username Search",
        "sec_custom":       "🔧  Custom Dork Builder",
        "td_site_lbl":      "site:",
        "td_site_ph":       "example.com",
        "td_ft_lbl":        "filetype:",
        "td_ft_ph":         "pdf",
        "td_inurl_lbl":     "inurl:",
        "td_inurl_ph":      "admin",
        "td_intext_lbl":    "intext:",
        "td_intext_ph":     "password",
        "td_intitle_lbl":   "intitle:",
        "td_intitle_ph":    "dashboard",
        "td_excl_lbl":      "Exclude (-)",
        "td_excl_ph":       "ads, news",
        "td_btn":           "▶  Build Dork",
    }
}

# ─── ARAMA MOTORLARİ ──────────────────────────────────────────────────────────
SEARCH_ENGINES = {
    "Google":     lambda q: f"https://www.google.com/search?q={quote(q)}",
    "Bing":       lambda q: f"https://www.bing.com/search?q={quote(q)}",
    "DuckDuckGo": lambda q: f"https://duckduckgo.com/?q={quote(q)}",
    "Yandex":     lambda q: f"https://yandex.com/search/?text={quote(q)}",
    "Brave":      lambda q: f"https://search.brave.com/search?q={quote(q)}",
    "Startpage":  lambda q: f"https://www.startpage.com/search?query={quote(q)}",
}

# ─── DIŞ SERVİSLER ────────────────────────────────────────────────────────────
EXTERNAL_SERVICES = {
    "person": [
        ("LinkedIn",      "https://www.linkedin.com/search/results/people/?keywords="),
        ("Twitter/X",     "https://twitter.com/search?q="),
        ("Pipl",          "https://pipl.com/search/?q="),
        ("Spokeo",        "https://www.spokeo.com/"),
        ("TrueCaller",    "https://www.truecaller.com/search/tr/"),
        ("Namechk",       "https://namechk.com/"),
        ("Sherlock (GH)", "https://github.com/sherlock-project/sherlock"),
        ("WhatsMyName",   "https://whatsmyname.app/"),
    ],
    "company": [
        ("LinkedIn Şirket","https://www.linkedin.com/company/"),
        ("Crunchbase",     "https://www.crunchbase.com/textsearch?q="),
        ("Bloomberg",      "https://www.bloomberg.com/search?query="),
        ("Glassdoor",      "https://www.glassdoor.com/Search/results.htm?keyword="),
        ("OpenCorporates", "https://opencorporates.com/companies?q="),
    ],
    "domain": [
        ("Shodan",         "https://www.shodan.io/search?query="),
        ("Censys",         "https://search.censys.io/search?resource=hosts&q="),
        ("VirusTotal",     "https://www.virustotal.com/gui/domain/"),
        ("DNSDumpster",    "https://dnsdumpster.com/"),
        ("SecurityTrails", "https://securitytrails.com/domain/"),
        ("AbuseIPDB",      "https://www.abuseipdb.com/check/"),
        ("WhoIs",          "https://www.whois.com/whois/"),
        ("Wayback Machine","https://web.archive.org/web/*/"),
        ("URLScan.io",     "https://urlscan.io/search/#"),
        ("crt.sh",         "https://crt.sh/?q="),
    ],
    "breach": [
        ("HaveIBeenPwned", "https://haveibeenpwned.com/"),
        ("DeHashed",       "https://dehashed.com/search?query="),
        ("IntelX",         "https://intelx.io/?s="),
        ("LeakCheck",      "https://leakcheck.io/"),
        ("BreachDirectory","https://breachdirectory.org/"),
        ("Snusbase",       "https://snusbase.com/"),
    ],
}

# ─── DORK ÜRETİCİLERİ ────────────────────────────────────────────────────────
def _excl(exclude):
    parts = [f"-{x.strip()}" for x in exclude.split(",") if x.strip()]
    return (" " + " ".join(parts)) if parts else ""

def build_kisi_dorks(L, name, city, job, company, phone, email_hint, social, birth_year, exclude):
    ex = _excl(exclude)
    g  = {}

    g[L["group_social"]] = [
        f'"{name}" site:linkedin.com{ex}',
        f'"{name}" site:twitter.com OR site:x.com{ex}',
        f'"{name}" site:instagram.com{ex}',
        f'"{name}" site:facebook.com{ex}',
        f'"{name}" site:youtube.com{ex}',
        f'"{name}" site:tiktok.com{ex}',
        f'"{name}" site:reddit.com{ex}',
        f'"{name}" site:threads.net{ex}',
        f'"{name}" site:mastodon.social{ex}',
        f'"{name}" site:tumblr.com{ex}',
        f'"{name}" site:pinterest.com{ex}',
    ]
    if social:
        g[L["group_social"]].insert(0, f'"{social}"{ex}')
        g[L["group_social"]].insert(1, f'site:twitter.com "{social}"{ex}')

    g[L["group_profile"]] = [
        f'"{name}" site:github.com{ex}',
        f'"{name}" site:gitlab.com{ex}',
        f'"{name}" inurl:profile OR inurl:about{ex}',
        f'"{name}" inurl:cv OR inurl:resume{ex}',
        f'"{name}" site:xing.com{ex}',
        f'"{name}" site:researchgate.net{ex}',
        f'"{name}" site:academia.edu{ex}',
        f'"{name}" filetype:pdf inurl:cv OR inurl:resume{ex}',
        f'"{name}" site:about.me{ex}',
        f'"{name}" site:slideshare.net{ex}',
    ]
    if company:
        g[L["group_profile"]].append(f'"{name}" "{company}" site:linkedin.com{ex}')
    if job:
        g[L["group_profile"]].append(f'"{name}" "{job}" filetype:pdf{ex}')
        g[L["group_profile"]].append(f'"{name}" "{job}" site:linkedin.com{ex}')

    g[L["group_contact"]] = [
        f'"{name}" intext:"@gmail.com" OR intext:"@hotmail.com" OR intext:"@yahoo.com"{ex}',
        f'"{name}" intext:"@" filetype:pdf OR filetype:doc{ex}',
        f'"{name}" "e-posta" OR "email" OR "mail"{ex}',
        f'"{name}" "telefon" OR "phone" OR "gsm" OR "cep"{ex}',
        f'"{name}" intext:"0(5" OR intext:"+90"{ex}',
        f'"{name}" "contact" OR "iletişim" filetype:html{ex}',
    ]
    if email_hint:
        g[L["group_contact"]].append(f'"{name}" "@{email_hint}"{ex}')
    if phone:
        g[L["group_contact"]].append(f'"{phone}"{ex}')
        g[L["group_contact"]].append(f'"{phone}" site:truecaller.com{ex}')

    g[L["group_loc"]] = [
        f'"{name}" "Türkiye" OR "Turkey"{ex}',
        f'"{name}" "adres" OR "address" OR "ikamet"{ex}',
    ]
    if city:
        g[L["group_loc"]].insert(0, f'"{name}" "{city}"{ex}')
        g[L["group_loc"]].append(f'"{name}" "{city}" site:linkedin.com{ex}')
        if job:
            g[L["group_loc"]].append(f'"{name}" "{city}" "{job}"{ex}')
    if birth_year:
        g[L["group_loc"]].append(f'"{name}" "{birth_year}"{ex}')
        g[L["group_loc"]].append(f'"{name}" "doğum" "{birth_year}"{ex}')

    g[L["group_news"]] = [
        f'"{name}" site:hurriyet.com.tr OR site:sabah.com.tr OR site:milliyet.com.tr{ex}',
        f'"{name}" site:bbc.com OR site:reuters.com OR site:apnews.com{ex}',
        f'"{name}" "röportaj" OR "interview" OR "haber"{ex}',
        f'"{name}" "açıklama" OR "statement" OR "basın"{ex}',
        f'"{name}" site:wikipedia.org{ex}',
        f'"{name}" site:ntv.com.tr OR site:cnnturk.com{ex}',
        f'"{name}" "mahkeme" OR "dava" OR "suçlama"{ex}',
    ]

    g[L["group_docs"]] = [
        f'"{name}" filetype:pdf{ex}',
        f'"{name}" filetype:doc OR filetype:docx{ex}',
        f'"{name}" filetype:xls OR filetype:xlsx{ex}',
        f'"{name}" filetype:ppt OR filetype:pptx{ex}',
        f'"{name}" site:slideshare.net{ex}',
        f'"{name}" site:scribd.com{ex}',
        f'"{name}" site:issuu.com{ex}',
        f'"{name}" filetype:txt{ex}',
    ]

    g[L["group_adv"]] = [
        f'"{name}" intext:"doğum" OR intext:"born" OR intext:"d."{ex}',
        f'"{name}" "yazarı" OR "author" OR "tarafından"{ex}',
        f'"{name}" related:linkedin.com{ex}',
        f'intitle:"{name}"{ex}',
        f'allintext:"{name}"{ex}',
        f'"{name}" -site:linkedin.com -site:facebook.com{ex}',
        f'"{name}" site:pastebin.com{ex}',
        f'"{name}" inurl:user OR inurl:profile OR inurl:member{ex}',
    ]

    return g


def build_sirket_dorks(L, company, domain, city, sector, founder, exclude):
    ex = _excl(exclude)
    g  = {}

    g[L["group_company"]] = [
        f'"{company}" site:linkedin.com/company{ex}',
        f'"{company}" "hakkında" OR "about" OR "kurumsal"{ex}',
        f'"{company}" site:crunchbase.com{ex}',
        f'"{company}" site:bloomberg.com{ex}',
        f'"{company}" "çalışan sayısı" OR "employee count"{ex}',
        f'"{company}" site:glassdoor.com{ex}',
        f'"{company}" site:indeed.com{ex}',
        f'"{company}" site:builtwith.com{ex}',
    ]
    if sector:
        g[L["group_company"]].append(f'"{company}" "{sector}"{ex}')
    if founder:
        g[L["group_company"]].append(f'"{company}" "{founder}"{ex}')

    g[L["group_finance"]] = [
        f'"{company}" site:kap.org.tr{ex}',
        f'"{company}" "faaliyet raporu" OR "annual report"{ex}',
        f'"{company}" "vergi no" OR "tax id" OR "ticaret sicil"{ex}',
        f'"{company}" filetype:pdf "bilanço" OR "balance sheet"{ex}',
        f'"{company}" site:ticaretsicil.gov.tr{ex}',
        f'"{company}" "iflas" OR "konkordato" OR "bankruptcy"{ex}',
        f'"{company}" "ortaklık" OR "shareholder" OR "hissedar"{ex}',
        f'"{company}" "sermaye" OR "capital" filetype:pdf{ex}',
        f'"{company}" site:opencorporates.com{ex}',
    ]

    g[L["group_staff"]] = [
        f'site:linkedin.com "{company}" "CEO" OR "Genel Müdür" OR "Yönetim Kurulu"{ex}',
        f'site:linkedin.com "{company}" "çalışıyor" OR "works at"{ex}',
        f'"{company}" "yönetim kurulu" OR "board of directors"{ex}',
        f'"{company}" "genel müdür" OR "CEO" OR "CTO" OR "CFO"{ex}',
        f'site:linkedin.com "{company}" "mühendis" OR "engineer"{ex}',
        f'site:linkedin.com "{company}" "müdür" OR "manager"{ex}',
        f'"{company}" "eski çalışan" OR "former employee"{ex}',
    ]

    g[L["group_digital"]] = [
        f'"{company}" site:twitter.com OR site:x.com{ex}',
        f'"{company}" site:instagram.com{ex}',
        f'"{company}" site:youtube.com{ex}',
        f'"{company}" site:tiktok.com{ex}',
    ]
    if domain:
        g[L["group_digital"]] += [
            f'site:{domain}{ex}',
            f'site:{domain} filetype:pdf{ex}',
            f'site:{domain} inurl:admin OR inurl:login OR inurl:panel{ex}',
            f'site:{domain} "index of"',
        ]

    g[L["group_rep"]] = [
        f'"{company}" "dava" OR "lawsuit" OR "mahkeme"{ex}',
        f'"{company}" "soruşturma" OR "investigation"{ex}',
        f'"{company}" "skandal" OR "yolsuzluk" OR "dolandırıcılık"{ex}',
        f'"{company}" site:eksisozluk.com{ex}',
        f'"{company}" site:sikayetvar.com{ex}',
        f'"{company}" "müşteri şikayeti" OR "complaint"{ex}',
        f'"{company}" site:trustpilot.com{ex}',
    ]
    if city:
        g[L["group_rep"]].append(f'"{company}" "{city}"{ex}')

    return g


def build_domain_dorks(L, domain, ip, org, tech, exclude):
    ex = _excl(exclude)
    g  = {}

    if domain:
        g[L["group_domain"]] = [
            f'site:{domain}{ex}',
            f'site:{domain} inurl:admin OR inurl:login OR inurl:panel OR inurl:dashboard',
            f'site:{domain} inurl:config OR inurl:backup OR inurl:db',
            f'site:{domain} filetype:pdf OR filetype:doc OR filetype:xls',
            f'site:{domain} "index of /"',
            f'site:{domain} intext:"password" OR intext:"şifre"',
            f'site:{domain} intext:"error" OR intext:"exception"',
            f'"{domain}" -site:{domain}',
            f'link:{domain}',
            f'related:{domain}',
            f'cache:{domain}',
        ]

        g[L["group_subdom"]] = [
            f'site:*.{domain}',
            f'site:{domain} inurl:api OR inurl:v1 OR inurl:v2',
            f'site:{domain} inurl:swagger OR inurl:api-docs',
            f'site:{domain} "powered by" OR "built with"',
            f'"{domain}" site:dnsdumpster.com',
            f'"{domain}" site:shodan.io',
            f'"{domain}" site:censys.io',
            f'"{domain}" site:securitytrails.com',
            f'"{domain}" site:crt.sh',
            f'"{domain}" site:urlscan.io',
        ]
        if tech:
            g[L["group_subdom"]].append(f'site:{domain} intext:"{tech}"{ex}')

        g[L["group_email2"]] = [
            f'"@{domain}" filetype:pdf OR filetype:xls OR filetype:xlsx',
            f'"@{domain}" site:pastebin.com',
            f'"@{domain}" site:github.com',
            f'intext:"@{domain}" "password" OR "credentials"',
            f'"@{domain}" -site:{domain}',
        ]

        g[L["group_sec"]] = [
            f'site:{domain} inurl:".env" OR inurl:".git" OR inurl:".svn"',
            f'site:{domain} ext:sql OR ext:db OR ext:bak',
            f'site:{domain} intext:"sql syntax" OR intext:"mysql_fetch"',
            f'site:{domain} intext:"Warning: include" OR intext:"Fatal error"',
            f'site:{domain} inurl:phpinfo.php',
            f'site:{domain} inurl:wp-admin OR inurl:wp-login',
            f'site:{domain} inurl:".htpasswd" OR inurl:".htaccess"',
            f'site:{domain} ext:log OR ext:conf',
            f'site:{domain} inurl:shell OR inurl:cmd OR inurl:exec',
        ]

    if ip:
        g[L["group_ip"]] = [
            f'"{ip}"{ex}',
            f'"{ip}" site:shodan.io',
            f'"{ip}" site:censys.io',
            f'"{ip}" site:abuseipdb.com',
            f'"{ip}" site:virustotal.com',
            f'"{ip}" "open port" OR "açık port"',
            f'"{ip}" site:ipinfo.io',
        ]

    if org:
        g[L["group_org"]] = [
            f'"{org}" site:shodan.io',
            f'"{org}" "ASN" OR "autonomous system"',
            f'"{org}" site:arin.net OR site:ripe.net',
        ]

    return g


def build_breach_dorks(L, email, username, name, phone, hash_val, exclude):
    ex = _excl(exclude)
    g  = {}

    pastes = ["pastebin.com", "ghostbin.co", "paste.ee", "hastebin.com",
              "rentry.co", "paste2.org", "pastecode.io"]

    if email:
        g[L["group_emailleak"]] = [f'"{email}" site:{s}' for s in pastes] + [
            f'"{email}" "password" OR "passwd" OR "hash"',
            f'"{email}" site:github.com',
            f'"{email}" filetype:sql OR filetype:txt',
        ]

    if username:
        g[L["group_userleak"]] = [
            f'"{username}" site:pastebin.com',
            f'"{username}" site:github.com',
            f'"{username}" site:twitter.com OR site:x.com',
            f'"{username}" site:reddit.com',
            f'"{username}" site:instagram.com',
            f'inurl:"{username}" -site:google.com',
            f'"{username}" "uid" OR "user_id" OR "account"',
        ]

    if name:
        g[L["group_nameleak"]] = [
            f'"{name}" site:pastebin.com{ex}',
            f'"{name}" "leaked" OR "breach" OR "dump"{ex}',
            f'"{name}" "database" OR "veritabanı" filetype:sql{ex}',
            f'"{name}" site:dehashed.com{ex}',
            f'"{name}" site:intelx.io{ex}',
        ]

    if phone:
        g[L["group_phoneleak"]] = [
            f'"{phone}" site:pastebin.com',
            f'"{phone}" "leaked" OR "breach"',
            f'"{phone}" site:github.com',
            f'"{phone}" -site:google.com',
        ]

    if hash_val:
        g["🔑  Hash"] = [
            f'"{hash_val}" site:pastebin.com',
            f'"{hash_val}" site:github.com',
            f'"{hash_val}" "cracked" OR "plain" OR "plaintext"',
        ]

    g[L["group_external"]] = [
        "haveibeenpwned.com — Email breach check",
        "dehashed.com — Leaked database search",
        "intelx.io — Dark web & paste search",
        "leakcheck.io — Credential lookup",
        "breachdirectory.org — Free breach search",
        "snusbase.com — Advanced leak search",
    ]

    return g


# ─── ARAÇ FONKSİYONLARI ───────────────────────────────────────────────────────
def identify_hash(h):
    h = h.strip()
    hlen = len(h)
    patterns = {32:"MD5", 40:"SHA-1", 56:"SHA-224", 64:"SHA-256", 96:"SHA-384", 128:"SHA-512"}
    if re.match(r'^[a-fA-F0-9]+$', h):
        return patterns.get(hlen, f"Unknown hex hash ({hlen} chars)")
    if h.startswith("$2"):    return "bcrypt"
    if h.startswith("$1$"):   return "MD5-crypt"
    if h.startswith("$5$"):   return "SHA-256-crypt"
    if h.startswith("$6$"):   return "SHA-512-crypt"
    if h.startswith("{SHA}"): return "SSHA (LDAP)"
    return "Unknown"

def analyze_phone(phone):
    phone = re.sub(r'[\s\-\(\)]', '', phone)
    result = []
    if phone.startswith("+90") or phone.startswith("0090"):
        result.append("Ülke: Türkiye (+90)")
        num = phone.lstrip("+").lstrip("90").lstrip("0090")
        prefixes = {
            "530":"Turkcell","531":"Turkcell","532":"Turkcell","533":"Turkcell",
            "534":"Turkcell","535":"Turkcell","536":"Turkcell","537":"Turkcell",
            "538":"Turkcell","539":"Turkcell",
            "540":"Vodafone","541":"Vodafone","542":"Vodafone","543":"Vodafone",
            "544":"Vodafone","545":"Vodafone","546":"Vodafone","547":"Vodafone",
            "548":"Vodafone","549":"Vodafone",
            "550":"Türk Telekom","551":"Türk Telekom","552":"Türk Telekom",
            "553":"Türk Telekom","554":"Türk Telekom","555":"Türk Telekom",
            "556":"Türk Telekom","557":"Türk Telekom","558":"Türk Telekom",
            "559":"Türk Telekom",
        }
        p3 = num[:3]
        op = prefixes.get(p3, "Bilinmeyen operatör")
        result.append(f"Operatör: {op}")
        if len(num) >= 10:
            result.append(f"Format: +90 {num[:3]} {num[3:6]} {num[6:8]} {num[8:10]}")
    elif phone.startswith("+1"):
        result.append("Country: USA / Canada (+1)")
    elif phone.startswith("+44"):
        result.append("Country: United Kingdom (+44)")
    elif phone.startswith("+49"):
        result.append("Country: Germany (+49)")
    else:
        result.append("Country code not identified")
    result.append(f"Length: {len(phone.lstrip('+'))} digits")
    return "\n".join(result)

def validate_email(email):
    email = email.strip()
    results = []
    pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        results.append("✓  Syntax valid")
    else:
        results.append("✗  Syntax invalid")
    domain = email.split("@")[-1] if "@" in email else ""
    disposable = ["tempmail","mailinator","guerrillamail","10minutemail","yopmail",
                  "throwam","fakeinbox","trashmail","dispostable","maildrop"]
    if any(d in domain.lower() for d in disposable):
        results.append("⚠  Disposable / temp domain!")
    else:
        results.append(f"Domain: {domain}")
    known = {
        "gmail.com":"Google Mail","yahoo.com":"Yahoo","hotmail.com":"Microsoft",
        "outlook.com":"Microsoft","icloud.com":"Apple","protonmail.com":"ProtonMail",
        "yandex.com":"Yandex","yandex.ru":"Yandex",
    }
    if domain in known:
        results.append(f"Provider: {known[domain]}")
    return "\n".join(results)

def build_custom_dork(site, filetype, inurl, intext, intitle, keyword, exclude):
    parts = []
    if keyword:  parts.append(f'"{keyword}"')
    if site:     parts.append(f'site:{site}')
    if filetype: parts.append(f'filetype:{filetype}')
    if inurl:    parts.append(f'inurl:{inurl}')
    if intext:   parts.append(f'intext:"{intext}"')
    if intitle:  parts.append(f'intitle:"{intitle}"')
    if exclude:
        for e in exclude.split(","):
            e = e.strip()
            if e: parts.append(f'-{e}')
    return " ".join(parts)


# ─── ANA UYGULAMA ─────────────────────────────────────────────────────────────
class OSINTApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OSINT Intelligence Engine v4.0")
        self.geometry("1380x860")
        self.minsize(1100, 700)
        self.configure(fg_color=C["bg"])

        self.all_dorks   = []
        self.session_log = []
        self.engine_var  = ctk.StringVar(value="Google")
        self.lang_var    = ctk.StringVar(value="TR")
        self.theme_var   = ctk.StringVar(value="Dark")
        self._L          = LANG["TR"]

        # Entry widget references (dil güncellemesi için)
        self._field_widgets = {}   # attr -> (lbl_widget, entry_widget)
        self._toolbar_btn_refs = {}  # "gen","copy","open","html","txt","json" -> list of buttons
        self._service_frames = {}    # category key -> frame holding service buttons

        self._build_ui()

    # ── TOPBAR ────────────────────────────────────────────────────────────────
    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=C["surface"], corner_radius=0, height=54)
        bar.grid(row=0, column=0, sticky="ew")
        bar.grid_columnconfigure(1, weight=1)
        bar.grid_propagate(False)

        logo_f = ctk.CTkFrame(bar, fg_color="transparent")
        logo_f.grid(row=0, column=0, padx=18, pady=0, sticky="w")

        self.lbl_title = ctk.CTkLabel(
            logo_f, text=f"⬡  {self._L['app_title']}",
            font=ctk.CTkFont("Consolas", 15, "bold"),
            text_color=C["accent"]
        )
        self.lbl_title.grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(
            logo_f, text="Advanced Open Source Intelligence Toolkit",
            font=ctk.CTkFont("Consolas", 9),
            text_color=C["muted"]
        ).grid(row=1, column=0, sticky="w")

        right_f = ctk.CTkFrame(bar, fg_color="transparent")
        right_f.grid(row=0, column=2, padx=18, pady=0, sticky="e")

        # Tema
        ctk.CTkLabel(right_f, text="TEMA", font=ctk.CTkFont("Consolas",9),
                     text_color=C["muted"]).grid(row=0, column=0, padx=(0,4))
        ctk.CTkSegmentedButton(
            right_f, values=["Dark","Light"],
            variable=self.theme_var,
            command=self._toggle_theme,
            font=ctk.CTkFont("Consolas",10),
            height=26, width=100,
        ).grid(row=0, column=1, padx=(0,14))

        # Dil
        self.lbl_lang_top = ctk.CTkLabel(right_f, text=self._L["lang_label"],
                                          font=ctk.CTkFont("Consolas",9), text_color=C["muted"])
        self.lbl_lang_top.grid(row=0, column=2, padx=(0,4))
        ctk.CTkSegmentedButton(
            right_f, values=["TR","EN"],
            variable=self.lang_var,
            command=self._apply_lang,
            font=ctk.CTkFont("Consolas",11,"bold"),
            height=26, width=90,
        ).grid(row=0, column=3, padx=(0,14))

        # Motor
        self.lbl_engine_top = ctk.CTkLabel(right_f, text=self._L["search_engine"],
                                            font=ctk.CTkFont("Consolas",9), text_color=C["muted"])
        self.lbl_engine_top.grid(row=0, column=4, padx=(0,4))
        ctk.CTkOptionMenu(
            right_f,
            values=list(SEARCH_ENGINES.keys()),
            variable=self.engine_var,
            fg_color=C["surface2"],
            button_color=C["accent2"],
            button_hover_color=C["accent"],
            text_color=C["text"],
            font=ctk.CTkFont("Consolas", 11),
            height=28, width=130,
        ).grid(row=0, column=5)

    # ── STATUSBAR ─────────────────────────────────────────────────────────────
    def _build_statusbar(self):
        bar = ctk.CTkFrame(self, fg_color=C["surface"], corner_radius=0, height=30)
        bar.grid(row=2, column=0, sticky="ew")
        bar.grid_columnconfigure(1, weight=1)
        bar.grid_propagate(False)

        self.lbl_status = ctk.CTkLabel(bar, text=self._L["ready"],
                                        font=ctk.CTkFont("Consolas",11), text_color=C["green"])
        self.lbl_status.grid(row=0, column=0, padx=16, pady=4, sticky="w")

        ctk.CTkLabel(bar, text=datetime.now().strftime("%d.%m.%Y"),
                     font=ctk.CTkFont("Consolas",10), text_color=C["muted"]
                     ).grid(row=0, column=1, pady=4)

        self.lbl_count = ctk.CTkLabel(bar, text="",
                                       font=ctk.CTkFont("Consolas",11), text_color=C["muted"])
        self.lbl_count.grid(row=0, column=2, padx=16, pady=4, sticky="e")

    # ── TAB WIDGET ────────────────────────────────────────────────────────────
    def _build_tabview(self):
        """Tab widget'ı sıfırdan oluşturur"""
        L = self._L
        tv = ctk.CTkTabview(
            self._tab_container,
            fg_color=C["bg"],
            segmented_button_fg_color=C["surface"],
            segmented_button_selected_color=C["accent2"],
            segmented_button_selected_hover_color=C["accent"],
            segmented_button_unselected_color=C["surface"],
            segmented_button_unselected_hover_color=C["border2"],
            text_color=C["text"],
        )
        tv.pack(fill="both", expand=True)

        self._tab_names = list(L["tabs"])
        for tn in self._tab_names:
            tv.add(tn)
            tv.tab(tn).grid_columnconfigure(0, weight=1)
            tv.tab(tn).grid_rowconfigure(0, weight=1)

        return tv

    # ── ANA BUILD ─────────────────────────────────────────────────────────────
    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_topbar()

        # Tab container frame (dil değişiminde içini destroy edebiliriz)
        self._tab_container = ctk.CTkFrame(self, fg_color=C["bg"], corner_radius=0)
        self._tab_container.grid(row=1, column=0, sticky="nsew", padx=6, pady=(0,6))
        self._tab_container.pack_propagate(False)

        self.tab_view = self._build_tabview()

        # Entry widget sözlüğünü sıfırla
        self._field_widgets = {}
        self._toolbar_btn_refs = {"gen": [], "copy": [], "open": [], "html": [], "txt": [], "json": []}
        self._service_frames = {}

        self._build_kisi_tab()
        self._build_sirket_tab()
        self._build_domain_tab()
        self._build_breach_tab()
        self._build_tools_tab()
        self._build_history_tab()

        self._build_statusbar()

    # ── DİL UYGULAMA ──────────────────────────────────────────────────────────
    def _apply_lang(self, lang=None):
        if lang is None:
            lang = self.lang_var.get()
        self._L = LANG[lang]
        L = self._L

        # Topbar
        self.lbl_title.configure(text=f"⬡  {L['app_title']}")
        self.lbl_lang_top.configure(text=L["lang_label"])
        self.lbl_engine_top.configure(text=L["search_engine"])
        self.lbl_status.configure(text=L["ready"])

        # Tab view'ı yeniden oluştur (rename güvenilmez)
        self._rebuild_tabs()

    def _rebuild_tabs(self):
        """Tüm tab içeriğini dil değişiminde yeniden oluşturur"""
        L = self._L

        # Eski tab view'ı kaldır
        for w in self._tab_container.winfo_children():
            w.destroy()

        # Entry değerlerini sakla
        saved = {}
        for attr, (lbl, entry) in self._field_widgets.items():
            try:
                saved[attr] = entry.get()
            except Exception:
                saved[attr] = ""

        # Sıfırla
        self._field_widgets = {}
        self._toolbar_btn_refs = {"gen": [], "copy": [], "open": [], "html": [], "txt": [], "json": []}
        self._service_frames = {}

        # Yeni tab view
        self.tab_view = self._build_tabview()

        # Sekmeleri yeniden kur
        self._build_kisi_tab()
        self._build_sirket_tab()
        self._build_domain_tab()
        self._build_breach_tab()
        self._build_tools_tab()
        self._build_history_tab()

        # Kaydedilen değerleri geri yaz
        for attr, val in saved.items():
            if attr in self._field_widgets and val:
                try:
                    _, entry = self._field_widgets[attr]
                    entry.insert(0, val)
                except Exception:
                    pass

        # Geçmişi yenile
        self._refresh_history()

        # Status
        self.lbl_status.configure(text=L["ready"], text_color=C["green"])

    # ── YARDIMCILAR ───────────────────────────────────────────────────────────
    def _make_split(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        left = ctk.CTkScrollableFrame(parent, fg_color=C["surface"], width=285,
                                      scrollbar_button_color=C["border"])
        left.grid(row=0, column=0, sticky="nsew", padx=(0,3), pady=0)
        left.grid_columnconfigure(0, weight=1)
        right = ctk.CTkFrame(parent, fg_color=C["bg"])
        right.grid(row=0, column=1, sticky="nsew")
        right.grid_rowconfigure(1, weight=1)
        right.grid_columnconfigure(0, weight=1)
        return left, right

    def _make_toolbar(self, parent, gen_cmd):
        L = self._L
        tb = ctk.CTkFrame(parent, fg_color=C["surface2"], corner_radius=6, height=44)
        tb.grid(row=0, column=0, sticky="ew", padx=4, pady=(4,2))
        tb.grid_columnconfigure(6, weight=1)
        tb.grid_propagate(False)

        bs = dict(fg_color=C["surface"], hover_color=C["card"],
                  text_color=C["text"], font=ctk.CTkFont("Consolas",10), height=28, corner_radius=5)

        gen_btn = ctk.CTkButton(tb, text=L["generate"], command=gen_cmd,
                                 fg_color=C["accent2"], hover_color=C["accent"],
                                 text_color="#fff", font=ctk.CTkFont("Consolas",11,"bold"),
                                 height=28, corner_radius=5)
        gen_btn.grid(row=0, column=0, padx=(8,4), pady=8)
        self._toolbar_btn_refs["gen"].append(gen_btn)

        spec = [
            ("copy", L["copy_all"],    self.copy_all,    1),
            ("open", L["open_all"],    self.open_all,    2),
            ("html", L["export_html"], self.export_html, 3),
            ("txt",  L["export_txt"],  self.export_txt,  4),
            ("json", L["export_json"], self.export_json, 5),
        ]
        for key, label, cmd, col in spec:
            b = ctk.CTkButton(tb, text=label, command=cmd, **bs)
            b.grid(row=0, column=col, padx=3, pady=8)
            self._toolbar_btn_refs[key].append(b)

    def _make_scroll(self, parent):
        sf = ctk.CTkScrollableFrame(parent, fg_color=C["bg"],
                                    scrollbar_button_color=C["border"],
                                    scrollbar_button_hover_color=C["muted"])
        sf.grid(row=1, column=0, sticky="nsew", padx=4, pady=(2,4))
        sf.grid_columnconfigure(0, weight=1)
        return sf

    def _field(self, parent, row, label_text, placeholder_text, attr):
        """Creates label+entry pair, stores in _field_widgets[attr]"""
        lbl = ctk.CTkLabel(parent, text=label_text,
                           font=ctk.CTkFont("Consolas",9), text_color=C["text2"])
        lbl.grid(row=row*2, column=0, padx=14, pady=(7,0), sticky="w")
        e = ctk.CTkEntry(parent, placeholder_text=placeholder_text,
                         fg_color=C["bg2"], border_color=C["border"],
                         text_color=C["text"], placeholder_text_color=C["muted"],
                         font=ctk.CTkFont("Consolas",12), height=32)
        e.grid(row=row*2+1, column=0, padx=14, pady=(2,0), sticky="ew")
        self._field_widgets[attr] = (lbl, e)
        return lbl, e

    def _get(self, attr):
        if attr in self._field_widgets:
            return self._field_widgets[attr][1].get().strip()
        return ""

    def _section_sep(self, parent, row, text):
        ctk.CTkFrame(parent, height=1, fg_color=C["border"]).grid(
            row=row, column=0, padx=12, sticky="ew", pady=(10,0))
        ctk.CTkLabel(parent, text=text,
                     font=ctk.CTkFont("Consolas",9,"bold"), text_color=C["accent2"]
                     ).grid(row=row+1, column=0, padx=14, pady=(2,0), sticky="w")

    def _gen_btn_side(self, parent, row, cmd):
        L = self._L
        b = ctk.CTkButton(parent, text=L["generate"],
                          command=cmd, fg_color=C["accent2"], hover_color=C["accent"],
                          text_color="#fff", font=ctk.CTkFont("Consolas",11,"bold"),
                          height=36, corner_radius=8)
        b.grid(row=row, column=0, padx=14, pady=(12,8), sticky="ew")
        self._toolbar_btn_refs["gen"].append(b)

    def _ext_services(self, parent, row_start, svc_key):
        L = self._L
        self._section_sep(parent, row_start, L["quick_svc"])
        svc_list = EXTERNAL_SERVICES.get(svc_key, [])
        for i, (name, url) in enumerate(svc_list):
            ctk.CTkButton(
                parent, text=f"↗  {name}",
                command=lambda u=url: webbrowser.open(u),
                fg_color=C["bg2"], hover_color=C["card"],
                text_color=C["teal"], border_color=C["border"], border_width=1,
                font=ctk.CTkFont("Consolas",10), height=26, corner_radius=5, anchor="w",
            ).grid(row=row_start+2+i, column=0, padx=14, pady=1, sticky="ew")

    # ── SEKME KURUCULAR ───────────────────────────────────────────────────────
    def _build_kisi_tab(self):
        tab = self.tab_view.tab(self._tab_names[0])
        left, right = self._make_split(tab)
        L = self._L
        fields = [
            (L["k_name"],    L["k_name_ph"],    "k_name"),
            (L["k_city"],    L["k_city_ph"],    "k_city"),
            (L["k_job"],     L["k_job_ph"],     "k_job"),
            (L["k_company"], L["k_company_ph"], "k_company"),
            (L["k_phone"],   L["k_phone_ph"],   "k_phone"),
            (L["k_email"],   L["k_email_ph"],   "k_email"),
            (L["k_social"],  L["k_social_ph"],  "k_social"),
            (L["k_age"],     L["k_age_ph"],     "k_age"),
            (L["k_exclude"], L["k_exclude_ph"], "k_exclude"),
        ]
        for i, (lbl, ph, attr) in enumerate(fields):
            self._field(left, i, lbl, ph, attr)
        r = len(fields)*2
        self._gen_btn_side(left, r+1, self._gen_kisi)
        self._ext_services(left, r+2, "person")
        self._make_toolbar(right, self._gen_kisi)
        self.kisi_scroll = self._make_scroll(right)

    def _build_sirket_tab(self):
        tab = self.tab_view.tab(self._tab_names[1])
        left, right = self._make_split(tab)
        L = self._L
        fields = [
            (L["s_company"], L["s_company_ph"], "s_company"),
            (L["s_domain"],  L["s_domain_ph"],  "s_domain"),
            (L["s_city"],    L["s_city_ph"],    "s_city"),
            (L["s_sector"],  L["s_sector_ph"],  "s_sector"),
            (L["s_founder"], L["s_founder_ph"], "s_founder"),
            (L["s_exclude"], L["s_exclude_ph"], "s_exclude"),
        ]
        for i, (lbl, ph, attr) in enumerate(fields):
            self._field(left, i, lbl, ph, attr)
        r = len(fields)*2
        self._gen_btn_side(left, r+1, self._gen_sirket)
        self._ext_services(left, r+2, "company")
        self._make_toolbar(right, self._gen_sirket)
        self.sirket_scroll = self._make_scroll(right)

    def _build_domain_tab(self):
        tab = self.tab_view.tab(self._tab_names[2])
        left, right = self._make_split(tab)
        L = self._L
        fields = [
            (L["d_domain"],  L["d_domain_ph"],  "d_domain"),
            (L["d_ip"],      L["d_ip_ph"],      "d_ip"),
            (L["d_org"],     L["d_org_ph"],     "d_org"),
            (L["d_tech"],    L["d_tech_ph"],    "d_tech"),
            (L["d_exclude"], L["d_exclude_ph"], "d_exclude"),
        ]
        for i, (lbl, ph, attr) in enumerate(fields):
            self._field(left, i, lbl, ph, attr)
        r = len(fields)*2
        self._gen_btn_side(left, r+1, self._gen_domain)
        self._ext_services(left, r+2, "domain")
        self._make_toolbar(right, self._gen_domain)
        self.domain_scroll = self._make_scroll(right)

    def _build_breach_tab(self):
        tab = self.tab_view.tab(self._tab_names[3])
        left, right = self._make_split(tab)
        L = self._L
        fields = [
            (L["b_email"],    L["b_email_ph"],    "b_email"),
            (L["b_username"], L["b_username_ph"], "b_username"),
            (L["b_name"],     L["b_name_ph"],     "b_name"),
            (L["b_phone"],    L["b_phone_ph"],    "b_phone"),
            (L["b_hash"],     L["b_hash_ph"],     "b_hash"),
            (L["b_exclude"],  L["b_exclude_ph"],  "b_exclude"),
        ]
        for i, (lbl, ph, attr) in enumerate(fields):
            self._field(left, i, lbl, ph, attr)
        r = len(fields)*2
        self._gen_btn_side(left, r+1, self._gen_breach)
        self._ext_services(left, r+2, "breach")
        self._make_toolbar(right, self._gen_breach)
        self.breach_scroll = self._make_scroll(right)

    # ── ARAÇLAR ───────────────────────────────────────────────────────────────
    def _build_tools_tab(self):
        tab = self.tab_view.tab(self._tab_names[4])
        tab.grid_columnconfigure((0,1), weight=1)
        tab.grid_rowconfigure(0, weight=1)

        left_col = ctk.CTkScrollableFrame(tab, fg_color=C["surface"],
                                           scrollbar_button_color=C["border"])
        left_col.grid(row=0, column=0, sticky="nsew", padx=(0,2))
        left_col.grid_columnconfigure(0, weight=1)

        right_col = ctk.CTkFrame(tab, fg_color=C["bg"])
        right_col.grid(row=0, column=1, sticky="nsew", padx=(2,0))
        right_col.grid_columnconfigure(0, weight=1)
        right_col.grid_rowconfigure(0, weight=1)

        L = self._L

        def tsec(text, r):
            ctk.CTkFrame(left_col, height=1, fg_color=C["border"]).grid(
                row=r, column=0, padx=12, sticky="ew", pady=(10,0))
            ctk.CTkLabel(left_col, text=text, font=ctk.CTkFont("Consolas",9,"bold"),
                         text_color=C["accent3"]).grid(row=r+1, column=0, padx=14, pady=(2,0), sticky="w")

        def tent(r, lbl, ph, attr):
            ctk.CTkLabel(left_col, text=lbl, font=ctk.CTkFont("Consolas",9),
                         text_color=C["text2"]).grid(row=r, column=0, padx=14, pady=(7,0), sticky="w")
            e = ctk.CTkEntry(left_col, placeholder_text=ph,
                             fg_color=C["bg2"], border_color=C["border"],
                             text_color=C["text"], placeholder_text_color=C["muted"],
                             font=ctk.CTkFont("Consolas",11), height=30)
            e.grid(row=r+1, column=0, padx=14, pady=(2,0), sticky="ew")
            setattr(self, attr, e)

        def tbtn(r, lbl, cmd, color=None):
            ctk.CTkButton(left_col, text=lbl, command=cmd,
                          fg_color=color or C["accent2"], hover_color=C["accent"],
                          text_color="#fff", font=ctk.CTkFont("Consolas",10,"bold"),
                          height=30, corner_radius=6
                          ).grid(row=r, column=0, padx=14, pady=(6,2), sticky="ew")

        tsec(L["sec_hash"], 0)
        tent(2, L["tool_hash_lbl"],  L["tool_hash_ph"],  "tool_hash")
        tbtn(4, L["tool_hash_btn"],  self._run_hash_id)

        tsec(L["sec_email_val"], 5)
        tent(7, L["tool_email_lbl"], L["tool_email_ph"], "tool_email")
        tbtn(9, L["tool_email_btn"], self._run_email_val)

        tsec(L["sec_phone_val"], 10)
        tent(12, L["tool_phone_lbl"], L["tool_phone_ph"], "tool_phone_val")
        tbtn(14, L["tool_phone_btn"], self._run_phone_anal)

        tsec(L["sec_uname"], 15)
        tent(17, L["tool_uname_lbl"], L["tool_uname_ph"], "tool_uname")
        tbtn(19, L["tool_uname_btn"], self._run_uname_search)

        tsec(L["sec_custom"], 20)
        tent(22, L["tool_kw_lbl"],     L["tool_kw_ph"],     "td_keyword")
        tent(24, L["td_site_lbl"],     L["td_site_ph"],     "td_site")
        tent(26, L["td_ft_lbl"],       L["td_ft_ph"],       "td_filetype")
        tent(28, L["td_inurl_lbl"],    L["td_inurl_ph"],    "td_inurl")
        tent(30, L["td_intext_lbl"],   L["td_intext_ph"],   "td_intext")
        tent(32, L["td_intitle_lbl"],  L["td_intitle_ph"],  "td_intitle")
        tent(34, L["td_excl_lbl"],     L["td_excl_ph"],     "td_excl")
        tbtn(36, L["td_btn"], self._run_custom_dork, C["teal"])

        # Sağ panel
        self.tool_result = ctk.CTkTextbox(
            right_col, font=ctk.CTkFont("Consolas",12),
            fg_color=C["surface"], text_color=C["text"],
            border_color=C["border"], border_width=1,
            wrap="word",
        )
        self.tool_result.grid(row=0, column=0, sticky="nsew", padx=8, pady=(8,2))

        ctk.CTkButton(right_col, text=L["tool_copy_result"],
                      command=self._copy_tool_result,
                      fg_color=C["surface2"], hover_color=C["card"],
                      text_color=C["green"], font=ctk.CTkFont("Consolas",10),
                      height=26, width=90, corner_radius=5
                      ).grid(row=1, column=0, padx=8, pady=(2,8), sticky="e")

    def _tool_output(self, text):
        self.tool_result.configure(state="normal")
        self.tool_result.delete("1.0", "end")
        self.tool_result.insert("end", text)
        self.tool_result.configure(state="disabled")

    def _copy_tool_result(self):
        content = self.tool_result.get("1.0", "end").strip()
        if content:
            pyperclip.copy(content)
            self._status(self._L["copied"])

    def _run_hash_id(self):
        h = self.tool_hash.get().strip()
        if not h: self._status(self._L["err_tools"], True); return
        result = identify_hash(h)
        links = ("\n\nHashCat: https://hashcat.net/wiki/\n"
                 "CrackStation: https://crackstation.net/\n"
                 "MD5Decrypt: https://md5decrypt.net/")
        self._tool_output(f"Hash: {h}\nType: {result}{links}")
        self._status("Hash analysis done.")

    def _run_email_val(self):
        em = self.tool_email.get().strip()
        if not em: self._status(self._L["err_tools"], True); return
        result = validate_email(em)
        breach = f"\n\nHaveIBeenPwned: https://haveibeenpwned.com/account/{quote(em)}"
        self._tool_output(f"Email: {em}\n\n{result}{breach}")
        self._status("Email validated.")

    def _run_phone_anal(self):
        ph = self.tool_phone_val.get().strip()
        if not ph: self._status(self._L["err_tools"], True); return
        result = analyze_phone(ph)
        tc = f"\n\nTrueCaller: https://www.truecaller.com/search/tr/{quote(ph)}"
        self._tool_output(f"Phone: {ph}\n\n{result}{tc}")
        self._status("Phone analyzed.")

    def _run_uname_search(self):
        un = self.tool_uname.get().strip()
        if not un: self._status(self._L["err_tools"], True); return
        platforms = [
            f"https://twitter.com/{un}",
            f"https://instagram.com/{un}",
            f"https://github.com/{un}",
            f"https://reddit.com/user/{un}",
            f"https://tiktok.com/@{un}",
            f"https://facebook.com/{un}",
            f"https://linkedin.com/in/{un}",
            f"https://youtube.com/@{un}",
            f"https://t.me/{un}",
            f"https://pinterest.com/{un}",
            f"https://medium.com/@{un}",
            f"https://dev.to/{un}",
        ]
        out = f"Username: @{un}\n\nPlatforms to check:\n" + "\n".join(platforms)
        out += f"\n\nNamechk: https://namechk.com/\nWhatsMyName: https://whatsmyname.app/"
        self._tool_output(out)
        self._status(f"@{un} — {len(platforms)} platforms listed.")

    def _run_custom_dork(self):
        dork = build_custom_dork(
            self.td_site.get().strip(), self.td_filetype.get().strip(),
            self.td_inurl.get().strip(), self.td_intext.get().strip(),
            self.td_intitle.get().strip(), self.td_keyword.get().strip(),
            self.td_excl.get().strip()
        )
        if not dork.strip(): self._status(self._L["err_tools"], True); return
        eng = self.engine_var.get()
        url = SEARCH_ENGINES[eng](dork)
        out = f"Dork:\n{dork}\n\nURL ({eng}):\n{url}"
        self._tool_output(out)
        self.all_dorks = [dork]
        self.lbl_count.configure(text=f"{self._L['total']} 1 {self._L['dorks']}")
        self._status(self._L["tool_dork_done"])

    # ── GEÇMİŞ ────────────────────────────────────────────────────────────────
    def _build_history_tab(self):
        tab = self.tab_view.tab(self._tab_names[5])
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(1, weight=1)

        L = self._L
        tb = ctk.CTkFrame(tab, fg_color=C["surface2"], corner_radius=6, height=42)
        tb.grid(row=0, column=0, sticky="ew", padx=4, pady=(4,2))
        tb.grid_propagate(False)

        bs = dict(fg_color=C["surface"], hover_color=C["card"],
                  text_color=C["text"], font=ctk.CTkFont("Consolas",10),
                  height=26, corner_radius=5)

        ctk.CTkButton(tb, text=L["clear_hist"], command=self._clear_history, **bs
                      ).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(tb, text=L["dl_hist"],    command=self._export_history, **bs
                      ).grid(row=0, column=1, padx=4, pady=8)
        ctk.CTkButton(tb, text=L["dl_hist_json"], command=self._export_history_json, **bs
                      ).grid(row=0, column=2, padx=4, pady=8)

        self.history_scroll = ctk.CTkScrollableFrame(
            tab, fg_color=C["bg"], scrollbar_button_color=C["border"])
        self.history_scroll.grid(row=1, column=0, sticky="nsew", padx=4, pady=(2,4))
        self.history_scroll.grid_columnconfigure(0, weight=1)

        self._refresh_history()

    def _add_history(self, label, dorks):
        ts = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.session_log.append({"ts": ts, "label": label, "dorks": list(dorks)})
        self._refresh_history()

    def _refresh_history(self):
        if not hasattr(self, "history_scroll") or not self.history_scroll.winfo_exists():
            return
        for w in self.history_scroll.winfo_children():
            w.destroy()

        L = self._L
        if not self.session_log:
            ctk.CTkLabel(self.history_scroll, text=L["no_query"],
                         font=ctk.CTkFont("Consolas",13), text_color=C["muted"]
                         ).grid(row=0, column=0, pady=60)
            return

        for i, entry in enumerate(reversed(self.session_log)):
            f = ctk.CTkFrame(self.history_scroll, fg_color=C["surface"], corner_radius=8)
            f.grid(row=i, column=0, sticky="ew", padx=8, pady=4)
            f.grid_columnconfigure(0, weight=1)

            hdr = ctk.CTkFrame(f, fg_color=C["card"], corner_radius=6)
            hdr.grid(row=0, column=0, columnspan=3, sticky="ew", padx=8, pady=(8,2))
            hdr.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(hdr, text=f"  [{entry['ts']}]  {entry['label']}",
                         font=ctk.CTkFont("Consolas",11), text_color=C["text"]
                         ).grid(row=0, column=0, padx=4, pady=6, sticky="w")
            ctk.CTkLabel(hdr, text=f"{len(entry['dorks'])} dork",
                         font=ctk.CTkFont("Consolas",10), text_color=C["accent"]
                         ).grid(row=0, column=1, padx=8, pady=6, sticky="e")

            dork_list = entry["dorks"]

            ctk.CTkButton(f, text=L["copy_hist"],
                          command=lambda d=dork_list: (pyperclip.copy("\n".join(d)),
                                                        self._status(self._L["copied"])),
                          fg_color=C["surface2"], hover_color=C["card"],
                          text_color=C["green"], font=ctk.CTkFont("Consolas",10),
                          height=24, width=70, corner_radius=4
                          ).grid(row=1, column=0, padx=(14,4), pady=(6,8), sticky="w")

            ctk.CTkButton(f, text=L["open_hist"],
                          command=lambda d=dork_list: self._open_list(d),
                          fg_color=C["surface2"], hover_color=C["card"],
                          text_color=C["accent"], font=ctk.CTkFont("Consolas",10),
                          height=24, width=50, corner_radius=4
                          ).grid(row=1, column=1, padx=4, pady=(6,8), sticky="w")

    def _clear_history(self):
        self.session_log.clear()
        self._refresh_history()
        self._status("History cleared." if self.lang_var.get() == "EN" else "Geçmiş temizlendi.")

    def _export_history(self):
        if not self.session_log:
            self._status(self._L["hist_empty"], True); return
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        dl   = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(dl, exist_ok=True)
        path = os.path.join(dl, f"osint_history_{ts}.txt")
        try:
            with open(path, "w", encoding="utf-8") as f:
                for e in self.session_log:
                    f.write(f"# {e['ts']} — {e['label']}\n")
                    f.write("\n".join(e["dorks"]) + "\n\n")
            self._status(f"{self._L['saved']} osint_history_{ts}.txt")
        except Exception as ex:
            self._status(f"{self._L['err_save']} {ex}", True)

    def _export_history_json(self):
        if not self.session_log:
            self._status(self._L["hist_empty"], True); return
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        dl   = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(dl, exist_ok=True)
        path = os.path.join(dl, f"osint_history_{ts}.json")
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.session_log, f, ensure_ascii=False, indent=2)
            self._status(f"{self._L['saved']} osint_history_{ts}.json")
        except Exception as ex:
            self._status(f"{self._L['err_save']} {ex}", True)

    # ── DORK ÜRETİCİLERİ ─────────────────────────────────────────────────────
    def _gen_kisi(self):
        name = self._get("k_name")
        if not name: self._status(self._L["err_name"], True); return
        groups = build_kisi_dorks(
            self._L, name,
            self._get("k_city"), self._get("k_job"), self._get("k_company"),
            self._get("k_phone"), self._get("k_email"), self._get("k_social"),
            self._get("k_age"), self._get("k_exclude")
        )
        self._render(self.kisi_scroll, groups, f"{'Kişi' if self.lang_var.get()=='TR' else 'Person'}: {name}")

    def _gen_sirket(self):
        company = self._get("s_company")
        if not company: self._status(self._L["err_company"], True); return
        groups = build_sirket_dorks(
            self._L, company,
            self._get("s_domain"), self._get("s_city"),
            self._get("s_sector"), self._get("s_founder"), self._get("s_exclude")
        )
        self._render(self.sirket_scroll, groups, f"{'Şirket' if self.lang_var.get()=='TR' else 'Company'}: {company}")

    def _gen_domain(self):
        domain = self._get("d_domain")
        ip     = self._get("d_ip")
        if not domain and not ip:
            self._status(self._L["err_domain"], True); return
        groups = build_domain_dorks(
            self._L, domain, ip, self._get("d_org"), self._get("d_tech"), self._get("d_exclude")
        )
        self._render(self.domain_scroll, groups, f"Domain: {domain or ip}")

    def _gen_breach(self):
        em  = self._get("b_email")
        un  = self._get("b_username")
        nm  = self._get("b_name")
        ph  = self._get("b_phone")
        hsh = self._get("b_hash")
        if not any([em, un, nm, ph, hsh]):
            self._status(self._L["err_breach"], True); return
        groups = build_breach_dorks(
            self._L, em, un, nm, ph, hsh, self._get("b_exclude")
        )
        self._render(self.breach_scroll, groups,
                     f"{'Sızıntı' if self.lang_var.get()=='TR' else 'Breach'}: {em or un or nm}")

    # ── RENDER ────────────────────────────────────────────────────────────────
    def _render(self, scroll_frame, groups, log_label):
        for w in scroll_frame.winfo_children():
            w.destroy()
        dorks = []
        row_idx = 0

        for cat, items in groups.items():
            # Kategori başlığı
            cat_hdr = ctk.CTkFrame(scroll_frame, fg_color=C["card"], corner_radius=6)
            cat_hdr.grid(row=row_idx, column=0, sticky="ew", padx=8, pady=(10,2))
            cat_hdr.grid_columnconfigure(0, weight=1)
            ctk.CTkLabel(cat_hdr, text=f"  {cat}",
                         font=ctk.CTkFont("Consolas",11,"bold"), text_color=C["accent"]
                         ).grid(row=0, column=0, padx=8, pady=6, sticky="w")
            real_count = sum(1 for x in items if not ("—" in x and not x.startswith('"') and not x.startswith("site:")))
            ctk.CTkLabel(cat_hdr, text=f"{real_count} dork",
                         font=ctk.CTkFont("Consolas",9), text_color=C["muted"]
                         ).grid(row=0, column=1, padx=8, pady=6, sticky="e")
            row_idx += 1

            for item in items:
                is_info = ("—" in item and not item.startswith('"') and not item.startswith("site:"))
                if is_info:
                    self._add_info_row(scroll_frame, item, row_idx)
                else:
                    self._add_dork_row(scroll_frame, item, row_idx)
                    dorks.append(item)
                row_idx += 1

        self.all_dorks = dorks
        self.lbl_count.configure(text=f"{self._L['total']} {len(dorks)} {self._L['dorks']}")
        self._status(f"{len(dorks)} {self._L['dorksgen']}")
        self._add_history(log_label, dorks)

    def _add_dork_row(self, parent, dork, row_idx):
        frame = ctk.CTkFrame(parent, fg_color=C["surface"], corner_radius=5)
        frame.grid(row=row_idx, column=0, sticky="ew", padx=8, pady=1)
        frame.grid_columnconfigure(1, weight=1)

        num = ctk.CTkLabel(frame, text=f"{row_idx}", width=28,
                           font=ctk.CTkFont("Consolas",9), text_color=C["muted"],
                           fg_color=C["bg2"], corner_radius=3)
        num.grid(row=0, column=0, padx=(6,4), pady=6, sticky="w")

        lbl = ctk.CTkLabel(frame, text=dork,
                           font=ctk.CTkFont("Consolas",11), text_color=C["text"],
                           anchor="w", wraplength=640, justify="left")
        lbl.grid(row=0, column=1, padx=4, pady=5, sticky="ew")

        bf = ctk.CTkFrame(frame, fg_color="transparent")
        bf.grid(row=0, column=2, padx=(2,6), pady=4)

        mini = dict(height=22, corner_radius=4, font=ctk.CTkFont("Consolas",9), width=52)
        ctk.CTkButton(bf, text=self._L["copy_btn"],
                      fg_color=C["surface2"], hover_color=C["card"], text_color=C["green"],
                      command=lambda d=dork: self._copy_one(d), **mini
                      ).grid(row=0, column=0, padx=2)
        ctk.CTkButton(bf, text=self._L["open_btn"],
                      fg_color=C["surface2"], hover_color=C["card"], text_color=C["accent"],
                      command=lambda d=dork: self._open_one(d), **mini
                      ).grid(row=0, column=1, padx=2)

        def on_enter(e, f=frame): f.configure(fg_color=C["card"])
        def on_leave(e, f=frame): f.configure(fg_color=C["surface"])
        for w in [frame, lbl, num]:
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)

    def _add_info_row(self, parent, text, row_idx):
        parts = text.split(" — ", 1)
        name  = parts[0].strip()
        desc  = parts[1].strip() if len(parts) > 1 else ""

        # URL bul
        url = None
        for svc_list in EXTERNAL_SERVICES.values():
            for k, v in svc_list:
                if k == name:
                    url = v; break
            if url: break

        frame = ctk.CTkFrame(parent, fg_color=C["bg2"], corner_radius=5)
        frame.grid(row=row_idx, column=0, sticky="ew", padx=8, pady=1)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text=f"  ↗  {name}   {desc}",
                     font=ctk.CTkFont("Consolas",10), text_color=C["amber"], anchor="w"
                     ).grid(row=0, column=0, padx=6, pady=4, sticky="w")
        if url:
            ctk.CTkButton(frame, text="OPEN", height=20, width=48, corner_radius=4,
                          fg_color=C["border"], hover_color=C["muted"], text_color=C["text"],
                          font=ctk.CTkFont("Consolas",9), command=lambda u=url: webbrowser.open(u)
                          ).grid(row=0, column=1, padx=6, pady=3)

    # ── EYLEMLER ──────────────────────────────────────────────────────────────
    def _open_one(self, dork):
        webbrowser.open(SEARCH_ENGINES[self.engine_var.get()](dork))

    def _copy_one(self, dork):
        pyperclip.copy(dork)
        self._status(self._L["copied"])

    def _open_list(self, dork_list):
        for d in dork_list:
            webbrowser.open(SEARCH_ENGINES[self.engine_var.get()](d))

    def copy_all(self):
        if not self.all_dorks: return
        pyperclip.copy("\n".join(self.all_dorks))
        self._status(f"{len(self.all_dorks)} {self._L['copied']}")

    def open_all(self):
        if not self.all_dorks: return
        if len(self.all_dorks) > 10:
            if not messagebox.askyesno(self._L["open_sure"],
                    f"{len(self.all_dorks)} {self._L['open_confirm']}"):
                return
        for d in self.all_dorks:
            webbrowser.open(SEARCH_ENGINES[self.engine_var.get()](d))

    def export_txt(self):
        if not self.all_dorks: return
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        dl = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(dl, exist_ok=True)
        path = os.path.join(dl, f"dorks_{ts}.txt")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("# OSINT Intelligence Engine v4.0\n")
                f.write(f"# {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n")
                f.write("\n".join(self.all_dorks))
            self._status(f"{self._L['saved']} dorks_{ts}.txt")
        except Exception as e:
            self._status(f"{self._L['err_save']} {e}", True)

    def export_json(self):
        if not self.all_dorks: return
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        dl = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(dl, exist_ok=True)
        path = os.path.join(dl, f"dorks_{ts}.json")
        data = {
            "generated": datetime.now().isoformat(),
            "engine":    self.engine_var.get(),
            "count":     len(self.all_dorks),
            "dorks":     self.all_dorks
        }
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self._status(f"{self._L['saved']} dorks_{ts}.json")
        except Exception as e:
            self._status(f"{self._L['err_save']} {e}", True)

    def export_html(self):
        if not self.all_dorks: return
        ts     = datetime.now().strftime("%Y%m%d_%H%M%S")
        dl     = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(dl, exist_ok=True)
        path   = os.path.join(dl, f"osint_report_{ts}.html")
        engine = self.engine_var.get()
        rows   = ""
        for i, d in enumerate(self.all_dorks, 1):
            url = SEARCH_ENGINES[engine](d)
            safe_d = d.replace("'", "\\'").replace('"', '&quot;')
            rows += (f'<tr>'
                     f'<td style="color:#64748b;width:40px">{i}</td>'
                     f'<td><code>{d}</code></td>'
                     f'<td style="white-space:nowrap">'
                     f'<a href="{url}" target="_blank" style="color:#34d399">Open ↗</a>'
                     f'  <button onclick="navigator.clipboard.writeText(\'{safe_d}\');this.textContent=\'✓\'"'
                     f' style="background:#1a2540;border:1px solid #1e2d47;color:#94a3b8;'
                     f'padding:2px 8px;border-radius:4px;cursor:pointer;font-size:11px">Copy</button>'
                     f'</td>'
                     f'</tr>\n')
        html = f"""<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<title>OSINT Report — {datetime.now().strftime('%d.%m.%Y %H:%M')}</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#080c14;color:#e2e8f0;font-family:Consolas,monospace;padding:32px;line-height:1.6}}
.header{{background:#101828;border:1px solid #1e2d47;border-radius:10px;padding:20px 24px;margin-bottom:24px;display:flex;justify-content:space-between;align-items:center}}
h1{{color:#38bdf8;font-size:18px;letter-spacing:1px}}
.meta{{color:#64748b;font-size:12px}}
.badge{{background:#1a2540;border:1px solid #1e2d47;border-radius:6px;padding:4px 12px;color:#38bdf8;font-size:12px}}
table{{width:100%;border-collapse:collapse;background:#101828;border-radius:10px;overflow:hidden;border:1px solid #1e2d47}}
th{{background:#1a2540;color:#38bdf8;padding:10px 14px;text-align:left;font-size:12px;letter-spacing:1px}}
td{{padding:8px 14px;border-bottom:1px solid #1a2540;font-size:12px;vertical-align:middle}}
tr:hover td{{background:#151f30}}
a{{text-decoration:none}}
code{{color:#fbbf24;font-size:11px}}
</style></head><body>
<div class="header">
  <div>
    <h1>⬡ OSINT Intelligence Engine v4.0</h1>
    <div class="meta">{datetime.now().strftime('%d.%m.%Y %H:%M')} · Engine: {engine}</div>
  </div>
  <div class="badge">{len(self.all_dorks)} Queries</div>
</div>
<table>
<thead><tr><th>#</th><th>DORK</th><th>ACTION</th></tr></thead>
<tbody>{rows}</tbody>
</table>
</body></html>"""
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            webbrowser.open(f"file:///{path.replace(os.sep, '/')}")
            self._status(f"HTML report: osint_report_{ts}.html")
        except Exception as e:
            self._status(f"{self._L['err_save']} {e}", True)

    # ── TEMA ──────────────────────────────────────────────────────────────────
    def _toggle_theme(self, mode):
        if mode == "Light":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

    # ── STATUS ────────────────────────────────────────────────────────────────
    def _status(self, msg, error=False):
        self.lbl_status.configure(
            text=msg,
            text_color=C["red"] if error else C["green"]
        )
        self.after(3000, lambda: self.lbl_status.configure(
            text=self._L["ready"],
            text_color=C["green"]
        ))


if __name__ == "__main__":
    app = OSINTApp()
    app.mainloop()