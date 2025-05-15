"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB
import os
import time


with SB(uc=True, test=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.uc_open_with_disconnect(url, 4)
    sb.uc_gui_press_keys("\t ")
    sb.reconnect(3)
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    url = os.getenv("url")
    sb.open(url)
    time.sleep(5)
    print(sb.get_page_title())