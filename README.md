# PUC_Rio_MVP_sprint_04

Repositório usando para a disciplina Sprint IV: Disciplina: Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes do curso de POS da PUC-RJ

Proposta do projeto :

1. Escolha um dataset que possa ser utilizado em um problema de classificação que não tenha sido utilizado na disciplina de Engenharia de Software para Sistemas Inteligentes.

   O dataset escolhido é um que contém as medidas de peso, altura e idade como classe de entrada e como saida o tamanho do cliente ( XXS, S, M, L, XL, XXl e XXXL).

   O datase pode ser localizado no endereço: https://www.kaggle.com/datasets/tourist55/clothessizeprediction.
   O dataset original possui 147.237 registros. Fiz uma separação de 80% para o dataset de teste, que ficou por volta de 117.790 registros e um dataset Golden com 29.446 registros. No Google Colab eu faço uma demostração desses valores.
   
   Como trabalho em uma empresa que desenvolve software para a aréa de confecção, achei interessante analisar esse dataset e gostaria de usá-lo futuramente na empresa.

3. Você deverá treinar um modelo de machine learning utilizando métodos clássicos para um problema de classificação

   Foi feito o treino de para os algorítmos abaixo:

   knn = ('KNN', KNeighborsClassifier())
   
   cart = ('CART', DecisionTreeClassifier())

   naive_bayes = ('NB', GaussianNB())

   lr = ('LR', LogisticRegression())

   Nos treinos, o melhor algorítmo foi KNeighbors, seguido do LogisticRegression. Com acurácia de KNN = 61,52% e LogisticRegression = 59,57%. Mas gerei o modelo para os dois, pois quero fazer o teste automatizado com o PyTest com ambos.
   
4. Produza um notebook no Google Colab
   Na produção do notebook eu criei dois, um sem o conceito de programação orientada a objetos e outra com o conceito com os seguintes nomes:

   MVP_sprint_04.ipynb
   
   MVP_sprint_04_em_POO.ipynb

   Como era de se esperar os dois apresentam os mesmos resultados e no final também faço a geração dos arquivos do modelo e do scaler para os algorítmos, para o teste automatizado com o PyTest.

6. Desenvolva uma aplicação full stack (contemplando back-end e front-end) simples, utilizando as tecnologias estudadas na sprint Desenvolvimento Full Stack Básico.
7. Implemente um teste automatizado utilizando PyTest para assegurar que o modelo atenda aos requisitos de desempenho estabelecidos (por você).
8. Reflita sobre como as boas práticas vistas na disciplina Desenvolvimento de Software Seguro (por exemplo, técnicas de anonimização de dados) poderiam ser aplicadas ao seu problema.
   No meu caso, como o me
9. Video

