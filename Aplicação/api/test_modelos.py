from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/grade_golden.csv"

# Carga dos dados
dataset = carregador.carregar_dados(url_dados)
ds = dataset[["weight","age","height","size"]]

# Retirando os campos em branco
df = ds.dropna(how='any')
dados = df.values

# Separando em dados de entrada e saída
X = dados[:, 0:3]
Y = dados[:, 3]

# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
def test_modelo_lr():  

    # Importando o modelo de Regressão Logística
    lr_path = 'ml_model/grade_lr.pkl'
    modelo_lr = Model.carrega_modelo(lr_path)

    # Carregando scaler
    scaler_path = 'ml_model/scaler.pkl'
    scaler = Model.carrega_modelo(scaler_path)
    
    # Obtendo as métricas da Regressão Logística
    acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(modelo_lr,scaler, X, Y)
    
    #Mostraando o valor da acuracia_lr
    print("acuracia_lr:", acuracia_lr)
 
    #Mostraando o valor da recall_lr
    print("recall_lr:", recall_lr)
 
    #Mostraando o valor da precisao_lr
    print("precisao_lr:", precisao_lr)

    #Mostraando o valor da f1_lr
    print("f1_lr:", f1_lr)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.53
    assert recall_lr >= 0.53
    assert precisao_lr >= 0.52
    assert f1_lr >= 0.52
 
# Método para testar o modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/grade_knn.pkl'
    modelo_knn = Model.carrega_modelo(knn_path)

    # Carregando scaler
    scaler_path = 'ml_model/scaler.pkl'
    scaler = Model.carrega_modelo(scaler_path)
    
    # Obtendo as métricas do KNN
    acuracia_knn,recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn,scaler, X, Y)
    
    #Mostraando o valor da acuracia_lr
    print("acuracia_knn:", acuracia_knn)
 
    #Mostraando o valor da recall_knn
    print("recall_knn:", recall_knn)
 
    #Mostraando o valor da precisao_knn
    print("precisao_knn:", precisao_knn)

    #Mostraando o valor da f1_knn
    print("f1_knn:", f1_knn)
    
    # Testando as métricas da KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.53
    assert recall_knn >= 0.53
    assert precisao_knn >= 0.52
    assert f1_knn >= 0.52

