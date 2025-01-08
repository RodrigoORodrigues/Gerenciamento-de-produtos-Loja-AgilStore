import uuid
import json
import os

# Caminho do arquivo onde os dados serão armazenados
ARQUIVO_INVENTARIO = "inventario.json"

# Classe Produto
class Produto:
    def __init__(self, nome, categoria, quantidade, preco, id=None):
        self.id = id or str(uuid.uuid4().hex[:5])  # Gera um id 
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.id} | {self.nome} | {self.categoria} | {self.quantidade} | R${self.preco:.2f}"

    def to_dict(self):
        # Converte para poder salvar em JSON
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "preco": self.preco
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nome'], data['categoria'], data['quantidade'], data['preco'], data['id'])

# Funções do Sistema

# Banco de dados: Lista de produtos
inventario = []

def carregar_dados():
    """Carrega os dados do inventário do arquivo JSON"""
    if os.path.exists(ARQUIVO_INVENTARIO):
        with open(ARQUIVO_INVENTARIO, 'r', encoding='utf-8') as file:
            dados = json.load(file)
            return [Produto.from_dict(p) for p in dados]
    return []

def salvar_dados():
    """Salva os dados do inventário no arquivo JSON"""
    with open(ARQUIVO_INVENTARIO, 'w', encoding='utf-8') as file:
        json.dump([produto.to_dict() for produto in inventario], file, indent=4)

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço do produto: R$"))
    produto = Produto(nome, categoria, quantidade, preco)
    inventario.append(produto)
    salvar_dados()
    print(f"Produto {nome} adicionado com sucesso!")

def listar_produtos():
    if not inventario:
        print("Nenhum produto cadastrado.")
        return
    print("\nLista de Produtos:")
    print(f"{'ID':<36} {'Nome':<20} {'Categoria':<15} {'Quantidade':<10} {'Preço'}")
    for produto in inventario:
        print(f"{produto.id:<36} {produto.nome:<20} {produto.categoria:<15} {produto.quantidade:<10} R${produto.preco:.2f}")

def atualizar_produto():
    id_produto = input("Digite o ID do produto a ser atualizado: ")
    produto = next((p for p in inventario if p.id == id_produto), None)

    if produto:
        print("Produto encontrado:")
        print(produto)

        nome = input("Novo nome (deixe em branco para manter): ")
        categoria = input("Nova categoria (deixe em branco para manter): ")
        quantidade = input("Nova quantidade (deixe em branco para manter): ")
        preco = input("Novo preço (deixe em branco para manter): ")

        if nome:
            produto.nome = nome
        if categoria:
            produto.categoria = categoria
        if quantidade:
            produto.quantidade = int(quantidade)
        if preco:
            produto.preco = float(preco)

        salvar_dados()
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def excluir_produto():
    id_produto = input("Digite o ID do produto a ser excluído: ")
    produto = next((p for p in inventario if p.id == id_produto), None)

    if produto:
        confirmacao = input(f"Tem certeza que deseja excluir o produto {produto.nome}? (s/n): ").lower()
        if confirmacao == 's':
            inventario.remove(produto)
            salvar_dados()
            print(f"Produto {produto.nome} excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("Produto não encontrado.")

def buscar_produto():
    criterio = input("Digite o ID ou nome do produto a buscar: ")
    resultados = [p for p in inventario if criterio.lower() in p.id.lower() or criterio.lower() in p.nome.lower()]

    if resultados:
        print("\nProdutos encontrados:")
        for produto in resultados:
            print(produto)
    else:
        print("Nenhum produto encontrado.")

# (Menu de interação)
def menu():
    while True:
        print("\n=== Sistema de Inventário ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            excluir_produto()
        elif opcao == '5':
            buscar_produto()
        elif opcao == '6':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Execução
if __name__ == "__main__":
    inventario = carregar_dados()
    menu()
