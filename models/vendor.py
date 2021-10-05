class Vendor:
    def __init__(
            self,
            vendor_name: str,
            vendor_page_link: str,
            vendor_email: str,
            vendor_phone_number: str,
            vendor_web_page: str
    ):
        self.name = vendor_name
        self.page_link = vendor_page_link
        self.email = vendor_email
        self.phone_number = vendor_phone_number
        self.web_page = vendor_web_page
