from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Avaliador:

    def avaliar(self, modelo,scaler,X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """

        # Estimativa da acurácia no conjunto de teste
        X_input_scaler= scaler.transform(X_test)
        predicoes = modelo.predict(X_input_scaler)
         
        return (accuracy_score(Y_test, predicoes),
                recall_score(Y_test, predicoes,average='weighted'),
                precision_score(Y_test, predicoes,average='weighted'),
                f1_score(Y_test, predicoes,average='weighted'))
    
    