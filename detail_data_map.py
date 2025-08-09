from camoufox.sync_api import Camoufox
from bs4 import BeautifulSoup
import time
import json
import os

# ------------------ مرحله اول: استخراج لینک‌ها ------------------ #
def extract_links_from_google_maps(search_url):
    results = []

    with Camoufox(headless=False) as browser:
        page = browser.new_page()
        page.goto(search_url, wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(5000)

        scroll_box = page.query_selector('div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd')

        seen_titles = set()
        counter = 1

        if scroll_box:
            box_bounds = scroll_box.bounding_box()
            if box_bounds:
                page.mouse.move(
                    box_bounds['x'] + box_bounds['width'] / 2,
                    box_bounds['y'] + box_bounds['height'] / 2
                )
                time.sleep(1)

                while True:
                    page.mouse.wheel(0, 800)
                    time.sleep(1.5)

                    titles = page.query_selector_all('span[dir="rtl"]')
                    links = page.query_selector_all('a.hfpxzc')

                    for t, l in zip(titles, links):
                        title = t.inner_text().strip()
                        href = l.get_attribute("href")
                        if title and title not in seen_titles:
                            seen_titles.add(title)
                            results.append({
                                "index": counter,
                                "title": title,
                                "link": href
                            })
                            counter += 1

                    # می‌توان اینجا محدودیت تعداد قرار داد
                    if counter > 10:  # مثلا فقط 10 مکان اول
                        break

    return results

# ------------------ مرحله دوم: استخراج اطلاعات هر لینک ------------------ #
def extract_place_data_from_html(html_content, place_url=None):
    soup = BeautifulSoup(html_content, "html.parser")

    def get_text_or_none(selector):
        element = soup.select_one(selector)
        return element.get_text(strip=True) if element else None

    def get_attr_or_none(selector, attr):
        element = soup.select_one(selector)
        return element[attr] if element and element.has_attr(attr) else None

    data = {
        "title": get_text_or_none("h1.DUwDvf"),
        "subtitle": get_text_or_none("h2.bwoZTb"),
        "rating": get_text_or_none("span[aria-hidden='true']"),
        "reviews_count": get_text_or_none("button.GQjSyb span"),
        "category": get_text_or_none("button.DkEaL"),
        "address": get_text_or_none("button[data-item-id='address'] div.Io6YTe"),
        "phone": get_text_or_none("button[data-item-id^='phone:'] div.Io6YTe"),
        "opening_hours": [li.get_text(strip=True) for li in soup.select("table.eK4R0e li")] or None,
        "main_image": get_attr_or_none("div.RZ66Rb img", "src"),
        "location_coordinates": None
    }

    # اگر مختصات در لینک باشد
    if place_url and "@" in place_url:
        try:
            coords_part = place_url.split("@")[1].split(",")[:2]
            data["location_coordinates"] = {
                "lat": coords_part[0],
                "lng": coords_part[1]
            }
        except:
            pass

    return data

# ------------------ اجرای کامل برنامه ------------------ #
def main():
    search_url = "https://www.google.com/maps/search/قزوین+،+سوپرمارکت‬‬/@36.2898665,49.9831087,13z"
    output_file = "places_info.txt"

    # حذف فایل قبلی اگر وجود دارد
    if os.path.exists(output_file):
        os.remove(output_file)

    print("🔍 در حال استخراج لینک‌ها از نقشه گوگل...")
    places = extract_links_from_google_maps(search_url)

    print(f"✅ {len(places)} مکان پیدا شد. در حال استخراج اطلاعات جزئی...")

    with Camoufox(headless=True) as browser:
        for place in places:
            try:
                page = browser.new_page()
                page.goto(place["link"], wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(4000)

                html = page.content()
                details = extract_place_data_from_html(html, place["link"])

                # ذخیره در فایل متنی
                with open(output_file, "a", encoding="utf-8") as f:
                    f.write(f"{place['index']}. عنوان: {place['title']}\nلینک: {place['link']}\n")
                    for k, v in details.items():
                        f.write(f"{k}: {v}\n")
                    f.write("-" * 60 + "\n")

                print(f"✅ {place['index']}. {place['title']} ذخیره شد.")

            except Exception as e:
                print(f"❌ خطا در مکان {place['index']}: {e}")

    print(f"\n📁 تمام اطلاعات در فایل `{output_file}` ذخیره شد.")

# ------------------ اجرا ------------------ #
if __name__ == "__main__":
    main()
