# Estruturas Condicionais, Identação e Estruturas de Repetição em Python

Este repositório contém o arquivo `estruturas_condicionais.py`, que demonstra o uso de **estruturas condicionais**, **identação** e **estruturas de repetição** em Python. Esses conceitos são fundamentais para controlar o fluxo de execução de um programa.

## Estruturas Condicionais

As estruturas condicionais permitem que o programa tome decisões com base em condições específicas. Os principais comandos são:

- **`if`**: Executa um bloco de código se a condição for verdadeira.
- **`elif`**: (opcional) Verifica outra condição se a anterior for falsa.
- **`else`**: (opcional) Executa um bloco de código se todas as condições anteriores forem falsas.

### Exemplo de Estrutura Condicional

```python
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")
```

## Identação em Python

A **identação** é o espaço em branco no início de uma linha de código. Em Python, a identação é obrigatória e usada para definir blocos de código que pertencem a estruturas como `if`, `for`, `while`, funções, entre outros.

- O padrão recomendado é usar **4 espaços** para cada nível de identação.
- A identação ajuda a organizar o código e torna mais fácil entender a lógica.

### Exemplo de Identação

```python
if True:  # Bloco if
    print("Bloco if")  # Este código pertence ao bloco if
```

## Estruturas de Repetição

As estruturas de repetição permitem executar um bloco de código várias vezes. Os principais comandos são:

- **`for`**: Itera sobre uma sequência (como listas, strings ou intervalos).
- **`while`**: Executa um bloco de código enquanto uma condição for verdadeira.

### Exemplo de Estrutura de Repetição com `for`

```python
for i in range(5):
    print(f"Iteração {i}")
```

### Exemplo de Estrutura de Repetição com `while`

```python
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
```

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `estruturas_condicionais.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python_08\Estruturas Condicionais e Identação\estruturas condicionais"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python estruturas_condicionais.py
   ```

4. O terminal exibirá as mensagens de saída baseadas nas condições e operações realizadas no código.

## Exemplo de Saída

Ao executar o arquivo, você verá uma saída semelhante a esta (dependendo da idade informada):

```plaintext
Informe sua idade: 18
Maior de idade, pode tirar a CNH.
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
