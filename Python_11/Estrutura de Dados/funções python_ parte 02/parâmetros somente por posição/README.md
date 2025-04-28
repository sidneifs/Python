# Funções em Python: Parâmetros Somente por Posição

Este repositório contém o arquivo `parametros_somente_por_posicao.py`, que demonstra o uso de **parâmetros somente por posição** em funções Python. Esse recurso é útil para garantir que certos argumentos sejam passados exclusivamente por posição, evitando ambiguidades ou erros ao chamar a função.

---

## O que são Parâmetros Somente por Posição?

Parâmetros somente por posição são aqueles que **não podem ser passados como argumentos nomeados**. Eles devem ser fornecidos na ordem em que foram definidos na função.

### Como Definir Parâmetros Somente por Posição?

Para definir parâmetros como somente por posição, utiliza-se o operador `/` na definição da função. Todos os parâmetros à esquerda da barra `/` devem ser passados exclusivamente por posição.

### Estrutura Básica

```python
def funcao_exemplo(parametro1, parametro2, /, parametro3, parametro4):
    print(parametro1, parametro2, parametro3, parametro4)
```

- **Antes do `/`**: Os parâmetros devem ser passados somente por posição.
- **Depois do `/`**: Os parâmetros podem ser passados por posição ou nomeados.

---

## Exemplo no Código

### Função `criar_carro`

A função `criar_carro` utiliza o operador `/` para definir que os parâmetros `modelo`, `ano` e `placa` devem ser passados somente por posição, enquanto os parâmetros `marca`, `motor` e `combustivel` podem ser passados por posição ou nomeados.

#### Código

```python
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    """
    Função para criar um carro com os dados fornecidos.

    Parâmetros:
    - modelo (str): Modelo do carro (somente por posição).
    - ano (int): Ano de fabricação do carro (somente por posição).
    - placa (str): Placa do carro (somente por posição).
    - marca (str): Marca do carro (por posição ou nomeado).
    - motor (str): Tipo de motor do carro (por posição ou nomeado).
    - combustivel (str): Tipo de combustível do carro (por posição ou nomeado).

    Retorno:
    - None. Apenas exibe os dados do carro.
    """
    print(modelo, ano, placa, marca, motor, combustivel)
```

---

### Exemplos de Uso

#### Exemplo Válido

Os parâmetros `modelo`, `ano` e `placa` são passados somente por posição, enquanto `marca`, `motor` e `combustivel` podem ser passados por posição ou nomeados.

```python
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")  # Válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Válido
```

**Saída:**

```plaintext
Palio 1999 ABC-1234 Fiat 1.0 Gasolina
Palio 1999 ABC-1234 Fiat 1.0 Gasolina
```

---

#### Exemplo Inválido

Os parâmetros `modelo`, `ano` e `placa` não podem ser passados como argumentos nomeados.

```python
# Inválido: 'modelo', 'ano' e 'placa' devem ser passados por posição.
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
```

**Erro:**

```plaintext
TypeError: criar_carro() got some positional-only arguments passed as keyword arguments: 'modelo', 'ano', 'placa'
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `parametros_somente_por_posicao.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 02\parâmetros somente por posição"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python parametros_somente_por_posicao.py
   ```

4. O terminal exibirá os resultados das chamadas válidas da função `criar_carro`.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar parâmetros somente por posição em funções Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
