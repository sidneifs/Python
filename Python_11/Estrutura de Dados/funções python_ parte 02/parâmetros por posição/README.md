# Funções em Python: Parâmetros por Posição

Este repositório contém o arquivo `04_parametros_por_posicao.py`, que demonstra o uso de **parâmetros por posição** em funções Python. Parâmetros por posição são úteis para garantir que certos argumentos sejam passados na ordem correta, enquanto outros podem ser nomeados para maior clareza.

---

## O que são Parâmetros por Posição?

Parâmetros por posição são aqueles que devem ser passados na ordem em que foram definidos na função. Em Python, o operador `/` pode ser usado para indicar que os parâmetros anteriores a ele devem ser obrigatoriamente passados por posição.

### Estrutura Básica

```python
def funcao_exemplo(parametro1, parametro2, /, parametro3, parametro4):
    print(parametro1, parametro2, parametro3, parametro4)
```

- **Antes do `/`**: Os parâmetros devem ser passados por posição.
- **Depois do `/`**: Os parâmetros podem ser passados por nome (nomeados).

---

## Exemplo no Código

### Função `criar_carro`

A função `criar_carro` utiliza o operador `/` para definir que os parâmetros `modelo`, `ano` e `placa` devem ser passados por posição, enquanto os parâmetros `marca`, `motor` e `combustivel` devem ser nomeados.

#### Código

```python
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    """
    Função para criar um carro com os dados fornecidos.

    Parâmetros:
    - modelo (str): Modelo do carro (obrigatório por posição).
    - ano (int): Ano de fabricação do carro (obrigatório por posição).
    - placa (str): Placa do carro (obrigatório por posição).
    - marca (str): Marca do carro (obrigatório por nome).
    - motor (str): Tipo de motor do carro (obrigatório por nome).
    - combustivel (str): Tipo de combustível do carro (obrigatório por nome).

    Retorno:
    - None. Apenas exibe os dados do carro.
    """
    print(f"Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Marca: {marca}, Motor: {motor}, Combustível: {combustivel}")
```

---

### Exemplos de Uso

#### Exemplo Válido

Os parâmetros `modelo`, `ano` e `placa` são passados por posição, enquanto `marca`, `motor` e `combustivel` são nomeados.

```python
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
```

**Saída:**

```plaintext
Modelo: Palio, Ano: 1999, Placa: ABC-1234, Marca: Fiat, Motor: 1.0, Combustível: Gasolina
```

---

#### Exemplos Inválidos

Os exemplos abaixo são inválidos e geram erros porque não seguem as regras de parâmetros por posição e nomeados.

```python
# Inválido: 'marca', 'motor' e 'combustivel' devem ser nomeados.
# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")

# Inválido: 'motor' deve ser nomeado.
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", "1.0", combustivel="Gasolina")

# Inválido: 'combustivel' deve ser nomeado.
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", "Gasolina")
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `04_parametros_por_posicao.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 02\parâmetros por posição"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 04_parametros_por_posicao.py
   ```

4. O terminal exibirá os resultados das chamadas válidas da função `criar_carro`.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar parâmetros por posição em funções Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
