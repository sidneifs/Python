# Funções em Python: Uso de `*args` e `**kwargs`

Este repositório contém o arquivo `03_args_kwargs.py`, que demonstra como utilizar os parâmetros especiais `*args` e `**kwargs` em funções Python. Esses parâmetros são amplamente usados para criar funções flexíveis que podem aceitar um número variável de argumentos posicionais e nomeados.

---

## O que são `*args` e `**kwargs`?

- **`*args`**: Permite que uma função receba um número variável de argumentos posicionais. Os valores são armazenados como uma tupla.
- **`**kwargs`**: Permite que uma função receba um número variável de argumentos nomeados. Os valores são armazenados como um dicionário.

### Estrutura Básica

```python
def funcao_exemplo(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)
```

---

## Exemplo no Código

### Função `exibir_poema`

A função `exibir_poema` utiliza `*args` para receber os versos de um poema e `**kwargs` para receber metadados adicionais, como autor, ano, tema, etc.

#### Código

```python
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)  # Junta os versos do poema em uma string separada por nova linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])  # Formata os metadados
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"  # Combina data, poema e metadados
    print(mensagem)
```

---

### Exemplo de Uso

#### Chamando a Função

```python
exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    autor="Tim Peters",
    ano=1999,
    tema="Python",
    estilo="Programação",
)
```

#### Saída

```plaintext
Zen of Python

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Autor: Tim Peters
Ano: 1999
Tema: Python
Estilo: Programação
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `03_args_kwargs.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 01\args e kwargs"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 03_args_kwargs.py
   ```

4. O terminal exibirá o poema formatado com os metadados fornecidos.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar `*args` e `**kwargs` em funções Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
