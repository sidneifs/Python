# Transações Acima de um Limite

## Descrição do Desafio

Você foi solicitado a criar um programa que analise uma lista de transações bancárias e filtre apenas aquelas que ultrapassam um valor limite. O programa deve retornar uma nova lista contendo somente as transações cujo valor absoluto (ignorando o sinal) seja maior que o limite informado.

### Entrada

- Uma linha contendo a lista de valores representando as transações bancárias e o limite, separados por vírgula, por exemplo: `[100, -50, 300, -150], 100`
- Valores positivos representam depósitos e negativos representam saques.
- O valor limite pode ser inteiro ou decimal.

### Saída

- Uma nova lista com as transações que ultrapassam o limite, no formato: `Transações: [X, Y, Z]`

#### Exemplos

| Entrada                        | Saída                      |
|--------------------------------|----------------------------|
| [100, -50, 300, -150], 100     | Transações: [300, -150]    |
| [200, -50, 400], 150           | Transações: [200, 400]     |
| [1000, -75, 800], 500          | Transações: [1000, 800]    |

> **Atenção:** As entradas e saídas devem ser exatamente iguais às descritas acima para aprovação nos testes automáticos da plataforma DIO.

---

## O que foi realizado

- O programa lê a lista de transações e o limite em uma única linha via entrada padrão (stdin), conforme exigido pela plataforma DIO.
- Separa corretamente a lista de transações do valor limite, mesmo quando estão juntos na mesma linha.
- Filtra corretamente as transações cujo valor absoluto é maior que o limite informado.
- Mantém inteiros como inteiros e decimais como decimais na saída, igual aos exemplos da DIO.
- A saída é impressa exatamente no formato solicitado: `Transações: [X, Y, Z]`.
- O código trata entradas vazias e possíveis erros de conversão, garantindo robustez.

---

## Como executar localmente

1. Clone este repositório ou copie o arquivo `transacoes_acima_do_limite.py`.
2. Execute o script em um terminal Python 3:

```bash
python transacoes_acima_do_limite.py
```

3.Digite a linha de entrada no formato:

```text
[100, -50, 300, -150], 100
```

---

## Observações

- Para submissão na DIO, utilize a versão que lê diretamente do stdin e espera a entrada em uma única linha.
- Para testes locais, o código permite digitar a linha manualmente caso não haja entrada padrão.

---

Desenvolvido por Sidnei Silva (sidneifs)
