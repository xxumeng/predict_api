# coding: UTF-8
from dataReader import dataReader
from flask import Flask, jsonify, request
import json
from collections import defaultdict
import pandas as pd
import requests
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def read_label_noName(file):
    """
    读入csv格式的标签数据，转为dict
    :param file:标签数据
    :return:label2idx
    """
    # 最后一个是无法预测
    label_name = defaultdict(str)
    # label_idx = defaultdict(lambda : -1)
    df = pd.read_csv(file)
    df = df.where(df.notnull(), 'null')
    for i,label in enumerate(df['0']):
        label_name[i] = label
    return label_name

data = dataReader('./data/month1-6-v8-label-greater200/month6-test-half.json')
label_name = read_label_noName("./data/month1-6-v8-label-greater200/label/label1.csv")


@app.route('/getJson',methods = ['GET'])
def get_json():
    idx = request.args.get('idx')
    return jsonify(data.getDataByID(idx))
@app.route('/predict',methods = ['GET','POST'])
def predict():
    #接收json文件
    sample = json.loads(request.get_data(as_text=True))
    print(type(sample))
    # 调用函数，处理传入的数据json，进行预测，返回处理结果和预测结果
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://127.0.0.1:7777/predict", headers=headers, data=json.dumps(sample))
    print(response.json())
    token_input = response.json()['input']
    predict_id =response.json()['labels'][:3]
    predict_name = [label_name[id] for id in predict_id]
    probs = response.json()['probs'][:3]
    true_id = sample['label1_id']
    return jsonify({'input': token_input,'true_label': label_name[true_id], 'predict_label': predict_name,'probs':probs})
if __name__ == '__main__':
    app.run(host='0.0.0.0',  # 任何ip都可以访问
            port=5555,       # 端口
            debug=True
            )