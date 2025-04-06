# Estruturas Condicionais, Identação e Estruturas de Repetição em Python

Este repositório contém o arquivo `identacao_e_blocos.py`, que demonstra o uso de **estruturas condicionais**, **identação** e **estruturas de repetição** em Python. Esses conceitos são fundamentais para organizar e controlar o fluxo de execução de um programa.

## Identação em Python

A **identação** é o espaço em branco no início de uma linha de código. Em Python, a identação é obrigatória e usada para definir blocos de código que pertencem a estruturas como `if`, `for`, `while`, funções, entre outros.

- O padrão recomendado é usar **4 espaços** para cada nível de identação.
- A identação ajuda a organizar o código e torna mais fácil entender a lógica.

### Exemplo de Identação

```python
if True:  # Bloco if
    print("Bloco if")  # Este código pertence ao bloco if
```

## Estruturas Condicionais

As estruturas condicionais permitem executar diferentes blocos de código com base em condições. Os principais comandos são:

- **`if`**: Executa um bloco de código se a condição for verdadeira.
- **`elif`**: (opcional) Executa um bloco de código se a condição anterior for falsa e a condição atual for verdadeira.
- **`else`**: (opcional) Executa um bloco de código se todas as condições anteriores forem falsas.

### Exemplo de Estrutura Condicional

```python
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")
        saldo -= valor
    elif saldo == 0:
        print("Saldo zerado!")
    else:
        print("Saldo insuficiente!")
    return saldo
```

## Estruturas de Repetição

As estruturas de repetição permitem executar um bloco de código várias vezes. Os principais comandos são:

- **`for`**: Itera sobre uma sequência (como listas, strings ou intervalos).
- **`while`**: Executa um bloco de código enquanto uma condição for verdadeira.

### Exemplo de Estrutura de Repetição com `for`

```python
def listar_saldos():
    saldos = [500, 1000, 1500, 2000]
    for saldo in saldos:
        print(f"Saldo: {saldo}")
```

### Exemplo de Estrutura de Repetição com `while`

```python
def simular_saque():
    saldo = 500
    while saldo > 0:
        print(f"Saldo atual: {saldo}")
        saque = int(input("Digite o valor do saque: "))
        if saque <= saldo:
            saldo -= saque
            print(f"Saque realizado! Novo saldo: {saldo}")
        else:
            print("Saldo insuficiente!")
    print("Saldo zerado.")
```

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `identacao_e_blocos.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python_08\Estruturas Condicionais e Identação\identacao e blocos"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python identacao_e_blocos.py
   ```

4. O terminal exibirá as mensagens de saída baseadas nas condições e operações realizadas no código.

## Exemplo de Saída

Ao executar o arquivo, você verá uma saída semelhante a esta:

```plaintext
valor sacado!
Novo saldo: 400
Valor depositado!
Novo saldo: 500
Saldo: 500
Saldo: 1000
Saldo: 1500
Saldo: 2000
Saldo atual: 500
Digite o valor do saque: 100
Saque realizado! Novo saldo: 400
...
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
