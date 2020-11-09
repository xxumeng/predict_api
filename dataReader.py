import json
from tqdm import tqdm

class dataReader():
    def __init__(self, path:str) -> None:
        with open('./data/month1-6-v8-label-greater200/month6-test-half.json', 'r', encoding='UTF-8') as in_data:
            self.list_dict_data = json.load(in_data)
        print('----------build index-----------')

        self.dict_id_index = {}
    
        index = 0
        for dict_data in tqdm(self.list_dict_data):
            self.dict_id_index[dict_data['idx']] = index
            index += 1

    def getDataByID(self, ID:str) -> dict:

        index = self.dict_id_index[ID]
    
        return self.list_dict_data[index]



if __name__ == "__main__":
    
    data = dataReader('./data/month1-6-v8-label-greater200/month6-test-half.json')
    print(data.getDataByID('3-980062817582610'))
    
    


    
