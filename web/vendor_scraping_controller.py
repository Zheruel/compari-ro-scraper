from requests import Session
from models.vendor import Vendor
from bs4 import BeautifulSoup
from io_utils.csv_exporter import save_scraped_vendor


def grab_vendor_information(vendor_page_url: str, ses: Session) -> Vendor:
    res = ses.get(vendor_page_url)

    soup = BeautifulSoup(res.content, 'html.parser')
    store_info_div = soup.find("div", {"class": "store-header-info"})

    vendor_name = soup.find("h1", {"class": "shop-title"}).text.strip()

    try:
        vendor_email = store_info_div.find("div", {"itemprop": "email"}).text.strip()
    except AttributeError:
        vendor_email = "Not found"
    try:
        vendor_phone_number = store_info_div.find("div", {"itemprop": "telephone"}).text.strip()
    except AttributeError:
        vendor_phone_number = "Not found"

    vendor_web_page = "Not found"
    vendor_div_list = store_info_div.find_all("div", {"class": "col-xs-8"})

    for vendor_div in vendor_div_list:
        if "https" in vendor_div.text:
            vendor_web_page = vendor_div.text.strip()

    return Vendor(vendor_name, vendor_page_url, vendor_email, vendor_phone_number, vendor_web_page)


def scrape_vendors():
    ses = Session()
    res = ses.get("https://www.compari.ro/stores/")

    soup = BeautifulSoup(res.content, 'html.parser')
    shop_div_list = soup.find_all("div", {"class": "shop-box"})

    for shop_div in shop_div_list:
        shop_url = shop_div.find("a").get("href")

        vendor = grab_vendor_information(shop_url, ses)
        save_scraped_vendor(vendor)
        print("Vendor {0} scraped and saved".format(vendor.name))
