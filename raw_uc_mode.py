"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB
import os
import time

with SB(uc=True, test=True) as sb:
    url = os.getenv("url")
    sb.open(url)
    time.sleep(5)
    print(sb.get_page_title())
    