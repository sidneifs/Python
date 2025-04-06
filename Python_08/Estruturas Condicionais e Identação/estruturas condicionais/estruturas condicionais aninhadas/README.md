# Estruturas Condicionais, Identação e Blocos, Estruturas de Repetição e Estruturas Condicionais Aninhadas em Python

Este repositório contém o arquivo `estruturas_condicionais_aninhadas.py`, que demonstra o uso de **estruturas condicionais**, **identação e blocos**, **estruturas de repetição** e **estruturas condicionais aninhadas** em Python.

---

## Estruturas Condicionais

As estruturas condicionais permitem que o programa tome decisões com base em condições específicas. Os principais comandos são:

- **`if`**: Executa um bloco de código se a condição for verdadeira.
- **`elif`**: (opcional) Verifica outra condição se a anterior for falsa.
- **`else`**: (opcional) Executa um bloco de código se todas as condições anteriores forem falsas.

### Exemplo de Estruturas Condicionais

```python
idade = 18
if idade >= 18:
    print("Maior de idade.")
elif idade == 17:
    print("Quase maior de idade.")
else:
    print("Menor de idade.")
```

---

## Identação e Blocos

A **identação** é o espaço em branco no início de uma linha de código. Em Python, a identação é obrigatória e usada para definir blocos de código.

- O padrão recomendado é usar **4 espaços** para cada nível de identação.
- A identação ajuda a organizar o código e torna mais fácil entender a lógica.

### Exemplo de Estruturas Condicionais Aninhadas

```python
if True:
    print("Bloco if")
    if False:
        print("Bloco aninhado")
```

---

## Estruturas de Repetição

As estruturas de repetição permitem executar um bloco de código várias vezes. Os principais comandos são:

- **`for`**: Itera sobre uma sequência (como listas, strings ou intervalos).
- **`while`**: Executa um bloco de código enquanto uma condição for verdadeira.

### Exemplo com `for`

```python
for i in range(3):
    print(f"Iteração {i}")
```

### Exemplo com `while`

```python
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
```

---

## Estruturas Condicionais Aninhadas

As **estruturas condicionais aninhadas** são estruturas condicionais dentro de outras estruturas condicionais. Elas são usadas para verificar múltiplas condições de forma hierárquica.

### Exemplo

```python
saldo = 2000
saque = 1500
cheque_especial = 450

if saldo >= saque:
    print("Saque realizado com sucesso!")
elif saque <= (saldo + cheque_especial):
    print("Saque realizado com uso do cheque especial!")
else:
    print("Saldo insuficiente para realizar o saque.")
```

---

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `estruturas_condicionais_aninhadas.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_08\Estruturas Condicionais e Identação\estruturas condicionais\estruturas condicionais aninhadas"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python estruturas_condicionais_aninhadas.py
   ```

4. O terminal exibirá as mensagens de saída baseadas nas condições e operações realizadas no código.

---

## Exemplo de Saída

Dependendo do tipo de conta e saldo, você verá uma saída semelhante a esta:

```plaintext
Conta especial selecionada!
Saque realizado com sucesso!
```

---

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

---

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
