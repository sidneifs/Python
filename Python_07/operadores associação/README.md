# Operadores de Associação em Python

Este repositório contém o arquivo `operadores_associacao.py`, que demonstra o uso de operadores de associação em Python. Os operadores de associação são usados para verificar se um valor ou variável está presente em uma sequência, como listas, strings, conjuntos ou dicionários.

## Operadores de Associação

Os principais operadores de associação abordados no arquivo são:

- **`in`**: Retorna `True` se o elemento estiver presente na sequência.
- **`not in`**: Retorna `True` se o elemento **não** estiver presente na sequência.

## Exemplos no Código

1. **Listas e Strings**:
   - Verifica se um elemento está presente em uma lista ou string.
   - Exemplo:

     ```python
     frutas = ["limao", "uva", "laranja"]
     curso = "Curso de Python"
     print("uva" in frutas)  # True
     print("Python" in curso)  # True
     ```

2. **Conjuntos**:
   - Verifica se um elemento está presente em um conjunto.
   - Exemplo:

     ```python
     saques = {1500, 100, 500, 2000}
     print(1500 in saques)  # True
     print(3000 not in saques)  # True
     ```

3. **Dicionários**:
   - Verifica se uma chave ou valor está presente em um dicionário.
   - Exemplo:

     ```python
     dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
     print("nome" in dados)  # True
     print("João" in dados.values())  # True
     ```

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `operadores_associacao.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_07\operadores associação"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados dos operadores de associação:

   ```bash
   python operadores_associacao.py
   ```

4. O terminal exibirá os resultados das verificações realizadas no arquivo.

## Exemplo de Saída

Ao executar o arquivo, você verá uma saída semelhante a esta:

```plaintext
True
True
True
True
True
True
True
True
False
True
True
True
True
True
True
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
