# Funções em Python: Escopo Local e Global

Este repositório contém o arquivo `05_escopo_local_e_global.py`, que demonstra o conceito de **escopo local** e **escopo global** em Python. O escopo de uma variável define onde ela pode ser acessada ou modificada no programa.

---

## O que é Escopo?

- **Escopo Global**: Variáveis definidas fora de qualquer função ou bloco. Elas podem ser acessadas em qualquer parte do programa, incluindo dentro de funções (se declaradas como `global`).
- **Escopo Local**: Variáveis definidas dentro de uma função. Elas só podem ser acessadas dentro da função onde foram criadas.

---

## Exemplo no Código

### Variável Global

A variável `salario` é definida no escopo global e pode ser acessada ou modificada em qualquer parte do programa.

```python
salario = 2000  # Variável global
```

---

### Função `salario_bonus`

A função `salario_bonus` utiliza a palavra-chave `global` para indicar que a variável `salario` do escopo global será modificada.

```python
def salario_bonus(bonus):
    global salario  # Declara que a variável salario é global
    salario += bonus  # Adiciona o bônus ao salário global
    return salario  # Retorna o salário atualizado
```

#### Exemplo de Uso

```python
salario_bonus(500)  # Atualiza o salário global adicionando o bônus
print(salario)  # Saída: 2500
```

---

### Função `salario_bonus_local`

A função `salario_bonus_local` utiliza uma variável local chamada `salario`, que é independente da variável global.

```python
def salario_bonus_local(bonus):
    salario = 2000  # Variável local
    salario += bonus  # Adiciona o bônus ao salário local
    return salario  # Retorna o salário atualizado
```

#### Exemplo de Uso

```python
print(salario_bonus_local(500))  # Saída: 2500 (variável local)
print(salario)  # Saída: 2000 (variável global permanece inalterada)
```

---

## Diferença entre Escopo Local e Global

| **Aspecto**         | **Escopo Global**                     | **Escopo Local**                     |
|----------------------|---------------------------------------|---------------------------------------|
| **Definição**        | Fora de qualquer função ou bloco      | Dentro de uma função ou bloco         |
| **Acessibilidade**   | Acessível em todo o programa          | Acessível apenas dentro da função     |
| **Modificação**      | Pode ser modificada com `global`      | Não afeta variáveis fora da função    |

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `05_escopo_local_e_global.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 02"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 05_escopo_local_e_global.py
   ```

4. O terminal exibirá os resultados das funções que utilizam variáveis de escopo local e global.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar escopos local e global em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
