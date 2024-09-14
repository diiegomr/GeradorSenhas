import random
import string

# Closure: Função para criar uma função de geração de senha personalizada
def geradorSenha(conjCaract):
    def gerarSenha(comprimento):
        # List Comprehension: Gera a lista de caracteres aleatórios
        digitos = ''.join([random.choice(conjCaract) for _ in range(comprimento)])
        listaTemporaria = list(digitos)
        listaEmbaralhada = random.sample(listaTemporaria, len(listaTemporaria))
        return ''.join(listaEmbaralhada)
    return gerarSenha

# Função de Alta Ordem: Aplica uma transformação à senha gerada
def transformar(transformacao):
    def transformarSenha(comprimento):
        senha = criarSenhaPers(comprimento)
        return transformacao(senha)
    return transformarSenha

# Funções de transformação exemplo: Adiciona um prefixo ou sufixo
def addPrefixo(prefixo):
    return lambda senha: prefixo + ": " + senha

# Conjunto de caracteres para a senha: dígitos, letras minúsculas e maiúsculas
conjCaract = string.digits + string.ascii_letters + string.punctuation + string.hexdigits

# Cria uma função de geração de senha usando o conjunto de caracteres especificado
criarSenhaPers = geradorSenha(conjCaract)

# Função para salvar a senha em um arquivo
def criarArquivo(senha, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(senha + '\n')

# Programa principal
if __name__ == "__main__":

    # Especificar a plataforma
    plataforma = str(input("Para qual plataforma a senha será criada? "))

    # Cria funções de transformação que adicionam prefixo
    addPrefixo = transformar(addPrefixo(plataforma))

    # Função Lambda: Valida o comprimento da senha
    testeComprimento = lambda x: 6 <= x <= 20
    
    comprimento = int(input("Qual o comprimento da senha (entre 6 e 20)? "))
    
    # Validar comprimento usando a função lambda
    while not testeComprimento(comprimento):
        print("Comprimento inválido. Por favor, insira um valor entre 6 e 20.")
        comprimento = int(input("Digite o comprimento da senha (entre 6 e 20): "))
    
    # Usa as funções de transformação para gerar senhas com prefixo e sufixo
    senhaFinal = addPrefixo(comprimento)
    
    print("Senha para ", senhaFinal)
    
    criarArquivo(senhaFinal, 'minhasSenhas.txt')

