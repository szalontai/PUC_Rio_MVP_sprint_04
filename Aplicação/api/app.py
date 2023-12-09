from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

# from sqlalchemy.exc import IntegrityError

from model import Session, Model, Cliente
from logger import logger
from schemas import *
from flask_cors import CORS

# Instanciação das Classes
modelo = Model()

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização, remoção e predição do tamanho clientes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


###############################################################################################################################################################
#   CLIENTES
################################################################################################################################################################

# Rota de listagem de clientes
@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_clientes():
    """Lista todos os clientes cadastrados na base
    Retorna uma lista de clientes cadastrados na base.
    
    Args:
        nome (str): nome do cliente
        
    Returns:
        list: lista de clientes cadastrados na base
    """
    session = Session()
    
    # Buscando todos os clientes
    clientes = session.query(Cliente).all()
    
    if not clientes:
        logger.warning("Não há clientes cadastrados na base :/")
        return {"message": "Não há clientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d clientes econtrados" % len(clientes))
        return apresenta_clientes(clientes), 200


# Rota de adição de cliente
@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict_cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados
    Retorna uma representação dos clientes e tamanhos associados.
    
    Args:
        name (str): nome do cliente
        weight (float):peso (kgs): Weight
        height (float): altura (cms): Height
        age (int): idade (anos): Age
        
    Returns:
        dict: representação do cliente e tamanho associado
    """
    
    # Carregando modelo
    modelo_path = 'ml_model/grade_knn.pkl'
    modelo = Model.carrega_modelo(modelo_path)
    
    # Carregando scaler
    scaler_path = 'ml_model/scaler.pkl'
    scaler = Model.carrega_modelo(scaler_path)
    

    cliente = Cliente(
        name=form.name.strip(),
        weight=form.weight,
        height=form.height,
        age=form.age,
        outcome=Model.preditor_cliente(modelo, scaler, form)
    )
    logger.debug(f"Adicionando cliente de nome: '{cliente.name}'")
    logger.debug(f"Adicionando cliente de tamanho: '{cliente.outcome}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se cliente já existe na base
        if session.query(Cliente).filter(Cliente.name == form.name).first():
            error_msg = "Cliente já existente na base :/"
            logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando cliente
        session.add(cliente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado cliente de nome: '{cliente.name}'")
        return apresenta_cliente(cliente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de cliente por nome
@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):    
    """Faz a busca por um cliente cadastrado na base a partir do nome

    Args:
        nome (str): nome do cliente
        
    Returns:
        dict: representação do cliente e diagnóstico associado
    """
    
    cliente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{cliente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.name == cliente_nome).first()
    
    if not cliente:
        # se o cliente não foi encontrado
        error_msg = f"Cliente {cliente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Cliente econtrado: '{cliente.name}'")
        # retorna a representação do cliente
        return apresenta_cliente(cliente), 200
   
    
# Rota de remoção de cliente por nome
@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteViewSchema, "404": ErrorSchema})
def delete_cliente(query: ClienteBuscaSchema):
    """Remove um cliente cadastrado na base a partir do nome
    Args:
        nome (str): nome do cliente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
        
    cliente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre cliente #{cliente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando cliente
    cliente = session.query(Cliente).filter(Cliente.name == cliente_nome).first()
    
    if not cliente:
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente '{cliente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(cliente)
        session.commit()
        logger.debug(f"Deletado cliente #{cliente_nome}")
        return {"message": f"Cliente {cliente_nome} removido com sucesso!"}, 200
    
# Rota de testes
@app.post('/teste', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict_teste(form: ClienteSchema):
    """Rota teste de predição de grade.
    
    Args:
        name (str): nome do cliente
        weight (float):peso (kgs): Weight
        height (float): altura (cms): Height
        age (int): idade (anos): Age
        
    Returns:
        dict: representação do cliente e grade associada
    """
    
    # Carregando modelo
    modelo_path = 'ml_model/grade_knn.pkl'
    modelo = Model.carrega_modelo(modelo_path)
    
    # Carregando modelo
    scaler_path = 'ml_model/scaler.pkl'
    scaler = Model.carrega_modelo(scaler_path)
    

    cliente = Cliente(
        name=form.name.strip(),
        weight=form.weight,
        height=form.height,
        age=form.age,
        outcome=Model.preditor_cliente(modelo, scaler, form)
    )
    logger.debug(f"Adicionando cliente de nome: '{cliente.name}'")
    logger.debug(f"Adicionando cliente de tamanho: '{cliente.outcome}'")
    
    try:
        # Criando conexão com a base
     
        logger.debug(f"Adicionado cliente de nome: '{cliente.name}'")
        return apresenta_cliente(cliente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"message": error_msg}, 400
   