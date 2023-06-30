import pickle
import numpy as np
LR_model = pickle.load(open('pickel_files/LR.pkl', 'rb'))


def model(data):
    data = np.array(list(data.values()))
    data = data.astype(float)
    print(data)
    data = [data]
    result = LR_model.predict(data)
    return result

    
# Accuracy(RF): 0.88375
# Accuracy(LR): 0.8853125
# Accuracy(DT): 0.815625
# Accuracy(SVM): 0.8296875
# Accuracy(KNN): 0.8071875
# Accuracy(NN): 0.8296875