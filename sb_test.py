from seleniumbase import Driver

def intercept_response(request, response):
    print("-----response.url------")
    print(request.headers)
    print("--------request.headers-------")
    try:
        print(response.body.decode('utf-8'))
    except UnicodeDecodeError:
        pass

driver = Driver(wire=True)
driver.response_interceptor = intercept_response
driver.get("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&is_targeted_country=false&media_type=all&q=3D%20printer&search_type=keyword_unordered&source=nav-header")
# driver.get("https://www.baidu.com")
driver.quit()