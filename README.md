# PUC_Rio_MVP_sprint_04

Repositório usando para a disciplina Sprint IV: Disciplina: Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes do curso de POS da PUC-RJ

Proposta do projeto :

## 1. Escolha um dataset que possa ser utilizado em um problema de classificação que não tenha sido utilizado na disciplina de Engenharia de Software para Sistemas Inteligentes.

   O dataset escolhido é um que contém as medidas de peso, altura e idade como classe de entrada e como saida o tamanho do cliente ( XXS, S, M, L, XL, XXl e XXXL).

   O datase pode ser localizado no endereço: https://www.kaggle.com/datasets/tourist55/clothessizeprediction.
   O dataset original possui 147.237 registros. Fiz uma separação de 80% para o dataset de teste, que ficou por volta de 117.790 registros e um dataset Golden com 29.446 registros. No Google Colab eu faço uma demostração desses valores.
   
   Como trabalho em uma empresa que desenvolve software para a aréa de confecção, achei interessante analisar esse dataset e gostaria de usá-lo futuramente na empresa.

## 2. Você deverá treinar um modelo de machine learning utilizando métodos clássicos para um problema de classificação

   Foi feito o treino de para os algorítmos abaixo:

   knn = ('KNN', KNeighborsClassifier())
   
   cart = ('CART', DecisionTreeClassifier())

   naive_bayes = ('NB', GaussianNB())

   lr = ('LR', LogisticRegression())

   Nos treinos, o melhor algorítmo foi KNeighbors, seguido do LogisticRegression. Com acurácia de KNN = 61,52% e LogisticRegression = 59,57%. Acabei gerando um modelo para os dois, pois vou utilizá-los para fazer o teste automatizado com o PyTest com ambos.
   
## 3. Produza um notebook no Google Colab

   Na produção do notebook eu criei dois, um sem o conceito de programação orientada a objetos POO e outra com o conceito, com os seguintes nomes:

   MVP_sprint_04.ipynb
   
   MVP_sprint_04_em_POO.ipynb

   Como era de se esperar os dois apresentam os mesmos resultados. No final faço a geração dos arquivos do modelo e do scaler para os dois algorítmos para o teste automatizado com o PyTest.

## 4. Desenvolva uma aplicação full stack (contemplando back-end e front-end) simples, utilizando as tecnologias estudadas na sprint Desenvolvimento Full Stack Básico.

   No GitHub coloquei os fontes na pasta aplicação/api e aplicação/front o back-end e front-end, respectivamente.
   Para a aplicação foi usando o mesmo modelo passado nas aulas de Orientação do MVP. No back-end, foi usada uma base de dados SQLite que guarda as medidas e nomes dos usuários. No front-end o usuário informa a altura, peso e idade e a aplicação retorna a medida do seu tamanho.

## 5. Implemente um teste automatizado utilizando PyTest para assegurar que o modelo atenda aos requisitos de desempenho estabelecidos (por você).
   
   Na implementação do teste automatizado foram criados dois testes. Um para o algorítmo LR e outro para o KNN. Como na avalição do dataset o algorítmo KNN foi o melhor, os requisitos de desempenho estabelecidos foram os dele. Desta forma podemos avaliar se o teste passa para um e não para o outro.

## 6. Reflita sobre como as boas práticas vistas na disciplina Desenvolvimento de Software Seguro (por exemplo, técnicas de anonimização de dados) poderiam ser aplicadas ao seu problema.

   Cono o dataset escolhido não possui dados sensíveis, não houve a necessidade da aplicação das técnicas de anonimização de dados. Caso houvesse, seria necessária a aplicação, pois poderia trazer vários prejuízos para quem tivesse seus dados mostrados no dataset. Por exemplo se o nome, endereço e CPF estivessem na relação, esses dados poderiam ser usados para emitir documentos falsos.  

## 7. Video

   No mesmo diretório no GitHub foi colocado o arquivo MVP_4.mp4 com o vídeo de apresentação do trabalho

