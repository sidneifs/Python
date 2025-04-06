# Estruturas de Repetição: Loop WHILE em Python

Este repositório contém o arquivo `estrutura_de_repeticao_while.py`, que demonstra o uso do loop `while` em Python. O loop `while` é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.

---

## O que é o Loop WHILE?

O loop `while` é usado para executar repetidamente um bloco de código enquanto uma condição especificada for avaliada como `True`. Ele é útil quando não sabemos previamente o número de iterações necessárias.

### Sintaxe

```python
while condicao:
    # bloco de código a ser executado enquanto a condição for verdadeira
```

---

## Exemplos no Código

### Exemplo 1: Jogo de Adivinhação com WHILE

Neste exemplo, o programa solicita ao usuário que adivinhe um número sorteado. O loop `while` continua até que o número correto seja informado.

```python
numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou, tente novamente...")
    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

print("Parabéns! Você acertou!")
```

### Exemplo 2: Menu Interativo de Opções

Neste exemplo, o programa exibe um menu de opções para o usuário. O loop `while` continua até que o usuário escolha a opção de sair (`0`).

```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
```

---

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `estrutura_de_repeticao_while.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_09\estruturas de repetição WHILE"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python estrutura_de_repeticao_while.py
   ```

4. Siga as instruções exibidas no terminal para interagir com o programa.

---

## Exemplo de Saída

### Exemplo 1: Jogo de Adivinhação

```plaintext
Informe um número entre 1 e 20: 10
Você errou, tente novamente...
Informe um número entre 1 e 20: 15
Parabéns! Você acertou!
```

### Exemplo 2: Menu de Opções

```plaintext
[1] Sacar 
[2] Extrato 
[0] Sair 
: 1
Sacando...
[1] Sacar 
[2] Extrato 
[0] Sair 
: 2
Exibindo o extrato...
[1] Sacar 
[2] Extrato 
[0] Sair 
: 0
Obrigado por usar nosso sistema bancário, até logo!
```

---

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

---

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
