import numpy as np
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model

    def preditor_cliente(model, scaler, form):
        """Realiza a predição de um cliebnte com base no modelo treinado
        """

        print("type(model)")
        print(type(model))

        print("type(scaler)")
        print(type(scaler))
       
        X_input = np.array([form.weight, 
                            form.age, 
                            form.height
                        ])
        data = [form.weight, 
                            form.height, 
                            form.age
                        ]
        
        X_input_scaler= scaler.transform(X_input.reshape(1, -1))
        
        print("X_input")
        print(X_input)

        print("X_input.reshape(1, -1)")
        print(X_input.reshape(1, -1))
   
   

        # Faremos o reshape para que o mod= scaler.transform(elo entenda que estamos passando
        diagnosis = model.predict(X_input_scaler)
        #diagnosis = model.predict(X_input_scaler)
        return diagnosis[0]