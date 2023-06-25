import pickle
import numpy as np
LR_model = pickle.load(open('pickel_files/LR.pkl', 'rb'))
DT_model = pickle.load(open('pickel_files/DT.pkl', 'rb'))
KNN_model = pickle.load(open('pickel_files/KNN.pkl', 'rb'))
MLPC_model = pickle.load(open('pickel_files/MLPC.pkl', 'rb'))
RF_model = pickle.load(open('pickel_files/RF.pkl', 'rb'))
SVM_model = pickle.load(open('pickel_files/DT.pkl', 'rb'))


def model(data, method):

    data = np.array(list(data.values()))
    data = data.astype(float)
    print(data)
    data = [data]
    if method == "LR":
        result = LR_model.predict(data)
        return result
    if method == "DT":
        result = DT_model.predict(data)
        return result
    if method == "KNN":
        result = KNN_model.predict(data)
        return result
    if method == "MLPC":
        result = MLPC_model.predict(data)
        return result
    if method == "RF":
        result = RF_model.predict(data)
        return result
    if method == "SVM":
        result = SVM_model.predict(data)
        return result
    
# Accuracy(RF): 0.88375
# Accuracy(LR): 0.8853125
# Accuracy(DT): 0.815625
# Accuracy(SVM): 0.8296875
# Accuracy(KNN): 0.8071875
# Accuracy(NN): 0.8296875
