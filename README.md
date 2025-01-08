# Gerenciamento de produtos Loja AgilStore
Gerenciamento de produtos para a Loja AgilStore (Inventário).

## Situação:

**A AgilStore é uma pequena loja de eletrônicos que recentemente expandiu seu catálogo de produtos para incluir uma variedade maior de itens, desde smartphones e laptops até acessórios como cabos, carregadores e fones de ouvido. Com o aumento do número de produtos e a diversidade das categorias, a equipe de gerenciamento percebeu a necessidade de otimizar o controle do inventário para garantir que os produtos estejam sempre disponíveis para os clientes e que os níveis de estoque sejam mantidos de forma eficiente.
Atualmente, o controle de inventário está sendo feito manualmente em planilhas, o que tem se mostrado ineficiente e propenso a erros, especialmente quando se trata de atualizações rápidas ou buscas específicas. Para resolver esse problema, a loja decidiu desenvolver uma aplicação que permita a gestão automatizada do inventário de produtos, facilitando operações como adicionar novos produtos, listar produtos existentes, atualizar informações e remover itens obsoletos.**

# Sistema de Inventário em Python

Este é um sistema simples de gerenciamento de inventário, onde você pode adicionar, listar, atualizar, excluir e buscar produtos. Os dados dos produtos são armazenados em um arquivo JSON, o que permite a persistência entre as execuções do programa.

## Funcionalidades
- **Adicionar Produto**: Permite que o usuário adicione um novo produto ao inventário, informando nome, categoria, quantidade e preço.
- **Listar Produtos**: Exibe todos os produtos cadastrados no inventário.
- **Atualizar Produto**: Permite atualizar as informações de um produto já cadastrado.
- **Excluir Produto**: Permite excluir um produto do inventário.
- **Buscar Produto**: Permite buscar produtos por nome ou ID.

## Tecnologias Utilizadas
- **Python 3**: A aplicação foi desenvolvida usando Python 3
- **JSON**: Os dados do inventário são salvos em um arquivo JSON para persistência entre as execuções.
- **UUID**: Usado para gerar IDs únicos para cada produto no inventário.

## Pré-requisitos
Antes de rodar a aplicação, você precisa ter o Python instalado em sua máquina. Se ainda não tem o Python instalado, você pode baixá-lo em: [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Como Rodar a Aplicação

1. **Clone o repositório ou faça o download do arquivo**:
   - Se você tiver o repositório, faça o clone utilizando o comando:
     
     git clone https://seu-repositorio.git
     
   - Se você não tiver o repositório, pode simplesmente baixar o arquivo `main.py` e movê-lo para um diretório de sua escolha.

2. **Instale o Python 3**:
   Caso não tenha o Python 3 instalado, siga o [link oficial de download](https://www.python.org/downloads/) para instalar.

3. **Execute o código**:
   Após garantir que o Python 3 está instalado, abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo `main.py` está localizado. Em seguida, execute o seguinte comando:
   
   python main.py
