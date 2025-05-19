from seleniumbase import SB  
import json
  
with SB(wire=True, proxy="http://localhost:10808", headless=True) as sb:  
    sb.open("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&is_targeted_country=false&media_type=all&q=printer&search_type=keyword_unordered")  
    for request in sb.driver.requests:  
        if request.response:
                print(
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type']
                )

                print("request.url", request.url)

                if 'https://www.facebook.com/api/graphql/' in request.url:
                    body = request.body.decode('utf-8')
                    data = json.loads(body)
                    print(data)