# Operadores de Identidade em Python

Este repositório contém o arquivo `operadores_identidade.py`, que demonstra o uso de operadores de identidade em Python. Os operadores de identidade são usados para verificar se dois objetos ocupam o mesmo espaço na memória.

## Operadores de Identidade

Os principais operadores de identidade abordados no arquivo são:

- **`is`**: Retorna `True` se dois objetos ocuparem o mesmo espaço na memória.
- **`is not`**: Retorna `True` se dois objetos não ocuparem o mesmo espaço na memória.

## Exemplos no Código

1. **Comparação de Objetos**:
   - Verifica se duas variáveis apontam para o mesmo objeto na memória.
   - Exemplo:

     ```python
     a = [1, 2, 3]
     b = a
     c = [1, 2, 3]
     print(a is b)  # True
     print(a is c)  # False
     ```

2. **Verificação com `None`**:
   - Verifica se uma variável é ou não `None`.
   - Exemplo:

     ```python
     print(a is not None)  # True
     print(a is None)      # False
     ```

3. **Caixa Eletrônico**:
   - Demonstra o uso de operadores de identidade em um contexto prático, como verificar se o saldo e o limite são o mesmo objeto na memória.

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `operadores_identidade.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_07\operadores de identidade"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados dos operadores de identidade:

   ```bash
   python operadores_identidade.py
   ```

4. O terminal exibirá os resultados das comparações realizadas no arquivo.

## Exemplo de Saída

Ao executar o arquivo, você verá uma saída semelhante a esta:

```plaintext
True
False
False
True
True
False
Realizando saque
Novo saldo: 8000
Saldo igual ao limite
False
True
True
False
True
False
False
True
True
True
False
False
True
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
