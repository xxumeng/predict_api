import requests
import json

url = "http://10.109.246.247"
# 获得id号的数据
def getJson(idx:str):
    response = requests.get(url+":5555/getJson?idx="+idx)
    print(response.json())
    return response.json()

# 预测
def predict(data):
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url+":5555/predict", headers = headers, data=json.dumps(data))
    print(response.json())


data = getJson('3-650062220093510')
#可对data进行修改后输入模型

predict(data)