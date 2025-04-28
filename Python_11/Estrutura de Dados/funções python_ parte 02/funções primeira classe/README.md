# Funções em Python: Objetos de Primeira Classe

Este repositório contém o arquivo `05_objetos_primeira_classe.py`, que demonstra como as funções em Python são tratadas como **objetos de primeira classe**. Isso significa que as funções podem ser passadas como argumentos para outras funções, retornadas de outras funções e atribuídas a variáveis.

---

## O que são Objetos de Primeira Classe?

Em Python, funções são consideradas **objetos de primeira classe**, o que significa que elas podem:

- Ser atribuídas a variáveis.
- Ser passadas como argumentos para outras funções.
- Ser retornadas de outras funções.
- Ser armazenadas em estruturas de dados como listas, dicionários, etc.

Essa característica permite a criação de **funções de ordem superior**, que são funções que operam em outras funções.

---

## Exemplo no Código

### Função `somar`

A função `somar` recebe dois números como argumentos e retorna a soma deles.

```python
def somar(a, b):
    """Função que soma dois números."""
    return a + b
```

---

### Função `subtrair`

A função `subtrair` recebe dois números como argumentos e retorna a subtração deles.

```python
def subtrair(a, b):
    """Função que subtrai dois números."""
    return a - b
```

---

### Função `exibir_resultado`

A função `exibir_resultado` recebe dois números e uma função como argumentos. Ela executa a função passada como argumento com os dois números e exibe o resultado.

```python
def exibir_resultado(a, b, funcao):
    """Função que exibe o resultado da operação."""
    resultado = funcao(a, b)  # Chama a função passada como argumento
    print(f"O resultado da operação é = {resultado}")
```

---

### Exemplos de Uso

#### Passando a Função `subtrair` como Argumento

```python
exibir_resultado(20, 10, subtrair)
```

**Saída:**

```plaintext
O resultado da operação é = 10
```

---

#### Passando a Função `somar` como Argumento

```python
exibir_resultado(50, 1500, somar)
```

**Saída:**

```plaintext
O resultado da operação é = 1550
```

---

#### Outro Exemplo com a Função `subtrair`

```python
exibir_resultado(10, 5, subtrair)
```

**Saída:**

```plaintext
O resultado da operação é = 5
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `05_objetos_primeira_classe.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 02\funções primeira classe"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 05_objetos_primeira_classe.py
   ```

4. O terminal exibirá os resultados das operações realizadas pelas funções.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar funções como objetos de primeira classe em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
