import pickle
import numpy as np

def model(data):
    data = np.array(list(data.values()))
    data = data.astype(float)
    print(data)
    LR_model = pickle.load(open('pickel_files/LR.pkl','rb'))
    data = [data]
    result = LR_model.predict(data)
    return result
