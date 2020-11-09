
from flask import Flask, jsonify, request
app = Flask(__name__)

#设置编码
app.config['JSON_AS_ASCII'] = False

@app.route('/getJson',methods = ['GET'])
def get_json():
    idx = request.args.get('idx')
    return jsonify({'idx': idx, 'text1': '登录成功！'})
@app.route('/predict',methods = ['POST'])
def predict():
    
    return jsonify({'true_label': '移动业务', 'predict_label': '移动业务'})
if __name__ == '__main__':
    app.run(host='0.0.0.0',  # 任何ip都可以访问
            port=7777,       # 端口
            debug=True
            )