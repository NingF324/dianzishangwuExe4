import requests

seedword_list = ["华为","小米","佳能","索尼","惠普","松下","华星光电","京东方","黑人牙膏"]


for seedword in seedword_list:
    # 发送 GET 请求
    response_get = requests.get('http://127.0.0.1:5000/compkey/lists?seedword=' + seedword)
    print('GET Response:', response_get.text)

