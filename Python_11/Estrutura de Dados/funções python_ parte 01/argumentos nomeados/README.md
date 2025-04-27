# Funções em Python: Argumentos Nomeados

Este repositório contém o arquivo `02_argumentos_nomeados.py`, que demonstra como utilizar **argumentos nomeados** em funções Python. Argumentos nomeados tornam o código mais legível e flexível, permitindo que os parâmetros sejam passados explicitamente pelo nome.

---

## O que são Argumentos Nomeados?

Argumentos nomeados permitem que você especifique os valores dos parâmetros de uma função utilizando seus nomes. Isso melhora a clareza do código, especialmente quando a função possui muitos parâmetros ou quando alguns deles têm valores padrão.

### Vantagens

- Torna o código mais legível.
- Permite alterar a ordem dos argumentos.
- Facilita o uso de dicionários para passar argumentos.

---

## Exemplos no Código

### 1. Função `salvar_carro`

A função `salvar_carro` recebe os seguintes parâmetros:

- **`marca`**: Marca do carro (ex.: "Fiat").
- **`modelo`**: Modelo do carro (ex.: "Palio").
- **`ano`**: Ano de fabricação do carro (ex.: 1999).
- **`placa`**: Placa do carro (ex.: "ABC-1234").

#### Código

```python
def salvar_carro(marca, modelo, ano, placa):
    # Salva o carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    return True
```

---

### 2. Chamadas da Função

#### a) Passando Argumentos Posicionais

Os valores são passados na ordem em que os parâmetros foram definidos.

```python
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
```

**Saída:**

```plaintext
Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
```

---

#### b) Passando Argumentos Nomeados

Os valores são passados explicitamente pelo nome dos parâmetros, permitindo alterar a ordem.

```python
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
```

**Saída:**

```plaintext
Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
```

---

#### c) Usando um Dicionário com `**`

Os valores são passados como um dicionário, utilizando o operador `**` para desempacotar os argumentos.

```python
dados_carro = {"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}
salvar_carro(**dados_carro)
```

**Saída:**

```plaintext
Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `02_argumentos_nomeados.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 01\argumentos nomeados"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 02_argumentos_nomeados.py
   ```

4. O terminal exibirá as mensagens geradas pelas chamadas da função `salvar_carro`.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar argumentos nomeados em funções Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
