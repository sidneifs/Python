# Manipulação de Strings em Python

Este repositório contém o arquivo `string_1.py`, que demonstra diversas operações e métodos para manipulação de strings em Python. Strings são uma das classes mais utilizadas em Python e oferecem uma ampla gama de métodos para análise, transformação e manipulação de texto.

---

## O que são Strings?

Strings são sequências de caracteres usadas para armazenar e manipular texto. Em Python, as strings são imutáveis, o que significa que não podem ser alteradas diretamente após serem criadas. No entanto, podemos criar novas strings com base em operações realizadas nas existentes.

---

## Exemplos de Operações com Strings

### 1. **Indexação e Fatiamento**

Você pode acessar caracteres individuais ou partes de uma string usando índices.

```python
nome = "Sidnei Silva"
print(nome[0])  # Primeiro caractere: 'S'
print(nome[-1]) # Último caractere: 'a'
print(nome[0:6]) # Fatiamento: 'Sidnei'
print(nome[::-1]) # String ao contrário: 'avliS iendiS'
```

### 2. **Métodos de Análise**

Os métodos abaixo ajudam a analisar o conteúdo de uma string.

```python
nome = "Sidnei Silva"
print(len(nome))  # Tamanho da string: 12
print(nome.count("i"))  # Contagem de 'i': 3
print(nome.find("i"))  # Índice da primeira ocorrência de 'i': 1
print(nome.isalpha())  # Verifica se todos os caracteres são letras: False
print(nome.isdigit())  # Verifica se todos os caracteres são dígitos: False
print(nome.isspace())  # Verifica se todos os caracteres são espaços: False
```

### 3. **Transformação de Strings**

Os métodos abaixo permitem transformar o texto.

```python
nome = "sIdnEi sILVa"
print(nome.upper())  # Tudo em maiúsculas: 'SIDNEI SILVA'
print(nome.lower())  # Tudo em minúsculas: 'sidnei silva'
print(nome.capitalize())  # Primeira letra maiúscula: 'Sidnei silva'
print(nome.title())  # Primeira letra de cada palavra maiúscula: 'Sidnei Silva'
print(nome.swapcase())  # Troca maiúsculas por minúsculas e vice-versa: 'SiDnEi SilvA'
```

### 4. **Substituição e Divisão**

Você pode substituir partes de uma string ou dividi-la em partes.

```python
nome = "Sidnei Silva"
print(nome.replace("i", "o"))  # Substitui 'i' por 'o': 'Sodneo Solva'
print(nome.split())  # Divide a string em palavras: ['Sidnei', 'Silva']
```

### 5. **Remoção de Espaços**

Os métodos abaixo ajudam a remover espaços em branco.

```python
texto = "  HElLo WoRlD!   "
print(texto.strip())  # Remove espaços no início e no final: 'HElLo WoRlD!'
print(texto.lstrip())  # Remove espaços no início: 'HElLo WoRlD!   '
print(texto.rstrip())  # Remove espaços no final: '  HElLo WoRlD!'
```

### 6. **Formatação e Alinhamento**

Os métodos abaixo ajudam a formatar e alinhar strings.

```python
menu = "Sidnei Silva"
print(menu.center(20, "#"))  # Centraliza com preenchimento: '####Sidnei Silva####'
print("-".join(menu))  # Insere '-' entre os caracteres: 'S-i-d-n-e-i- -S-i-l-v-a'
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `string_1.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_10"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python string_1.py
   ```

4. O terminal exibirá os resultados das operações realizadas no código.

---

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como manipular strings em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)]
