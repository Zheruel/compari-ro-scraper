from models.vendor import Vendor
from csv import writer as csv_writer
from pathlib import Path


def save_scraped_vendor(vendor: Vendor) -> None:
    my_file = Path("output/scraped_vendors.csv")
    write_header = False

    if not my_file.exists():
        write_header = True

    with open("output/scraped_vendors.csv", "a", encoding="UTF8", newline="") as csv_file:
        writer = csv_writer(csv_file)

        if write_header:
            table_header = ["Vendor Name", "Vendor Page", "Email", "Phone Number", "Personal Web Page"]
            writer.writerow(table_header)

        vendor_info = [
            vendor.name,
            vendor.page_link,
            vendor.email,
            vendor.phone_number,
            vendor.web_page
        ]
        writer.writerow(vendor_info)
