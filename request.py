import requests
import json


# 获得id号的数据
def getJson(idx):
    response = requests.get("http://127.0.0.1:7777/getJson?idx=3-1")
    print(response.text)

# 预测
def predict(data):
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://127.0.0.1:7777/predict", headers = headers, data=json.dumps(data))
    print(response.text)


getJson('3-1')

data = {'idx':'3-1','text1':'test'}
predict(data)