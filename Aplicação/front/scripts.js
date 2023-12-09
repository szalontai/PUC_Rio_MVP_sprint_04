/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/clientes';
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        data.clientes.forEach(item => insertList(item.name, 
                                                  item.weight, 
                                                  item.height,
                                                  item.age,
                                                  item.outcome
                                                ))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Chamada da função para carregamento inicial dos dados
    --------------------------------------------------------------------------------------
  */
  getList()
  
  
  
  
  /*
    --------------------------------------------------------------------------------------
    Função para colocar um item na lista do servidor via requisição POST
    --------------------------------------------------------------------------------------
  */
  const postItem = async (inputClient, inputWeight, inputHeight,inputAge) => {
      
    const formData = new FormData();
    formData.append('name', inputClient);
    formData.append('weight', inputWeight);
    formData.append('height', inputHeight);
    formData.append('age', inputAge);
  
    let url = 'http://127.0.0.1:5000/cliente';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .then(async (data) => {

        // Retorno o JSON com o itens encontrados no servidor
        insertList(inputClient, inputWeight, inputHeight, inputAge,data.outcome);
        alert("Item adicionado!");

      })
      .catch((error) => {
        console.error('Error:', error);
      });
      
  }
  
  
  /*
    --------------------------------------------------------------------------------------
    Função para criar um botão close para cada item da lista
    --------------------------------------------------------------------------------------
  */
  const insertDeleteButton = (parent) => {
    let span = document.createElement("span");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    parent.appendChild(span);
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para remover um item da lista de acordo com o click no botão close
    --------------------------------------------------------------------------------------
  */
  const removeElement = () => {
    let close = document.getElementsByClassName("close");
    // var table = document.getElementById('myTable');
    let i;
    for (i = 0; i < close.length; i++) {
      close[i].onclick = function () {
        let div = this.parentElement.parentElement;
        const nomeItem = div.getElementsByTagName('td')[0].innerHTML
        if (confirm("Você tem certeza?")) {
          div.remove()
          deleteItem(nomeItem)
          alert("Removido!")
        }
      }
    }
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para deletar um item da lista do servidor via requisição DELETE
    --------------------------------------------------------------------------------------
  */
  const deleteItem = (item) => {
    console.log(item)
    let url = 'http://127.0.0.1:5000/cliente?name='+item;
    fetch(url, {
      method: 'delete'
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para adicionar um novo item com nome, quantidade e valor 
    --------------------------------------------------------------------------------------
  */
  const newItem = async () => {
    let inputClient = document.getElementById("newInput").value;
    let inputWeight = document.getElementById("newWeight").value;
    let inputHeight = document.getElementById("newHeight").value;
    let inputAge = document.getElementById("newAge").value;
  
    // Verifique se o nome do produto já existe antes de adicionar
    const checkUrl = `http://127.0.0.1:5000/clientes?nome=${inputClient}`;
    fetch(checkUrl, {
      method: 'get'
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.clientes && data.clientes.some(item => item.name === inputClient)) {
          alert("O cliente já está cadastrado.\nCadastre o cliente com um nome diferente ou atualize o existente.");
        } else if (inputClient === '') {
          alert("O nome do cliente não pode ser vazio!");
        } else if (isNaN(inputWeight) || isNaN(inputHeight) || isNaN(inputAge)) {
          alert("Esse(s) campo(s) precisam ser números!");
        } else {
          postItem(inputClient, inputWeight, inputHeight, inputAge);

        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  
  /*
    --------------------------------------------------------------------------------------
    Função para inserir items na lista apresentada
    --------------------------------------------------------------------------------------
  */
  const insertList = (nameClient, weight, height,age, outcome) => 
  {
    var item = [nameClient, weight, height,age, outcome];
    var table = document.getElementById('myTable');
    var row = table.insertRow();
  
    for (var i = 0; i < item.length; i++) {
      var cell = row.insertCell(i);
      cell.textContent = item[i];
    }
  
    var deleteCell = row.insertCell(-1);
    insertDeleteButton(deleteCell);
  
  
    document.getElementById("newInput").value = "";
    document.getElementById("newWeight").value = "";
    document.getElementById("newHeight").value = "";
    document.getElementById("newAge").value = "";
  
    removeElement();
  }