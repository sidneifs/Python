# Gestão e Controle de Transações Bancárias

## Descrição do Desafio

Imagine que você trabalha no setor de TI de um banco e precisa criar um programa que registre as transações de uma conta bancária. Cada transação pode ser um depósito ou um saque, e todas elas serão armazenadas em uma lista. Seu programa deve calcular o saldo final da conta com base nas transações realizadas. Depósitos são representados como valores positivos e saques como valores negativos.

### Entrada

- Uma lista contendo valores inteiros ou decimais representando as transações realizadas (exemplo: `[100, -50, 200]`).
- Valores positivos representam depósitos.
- Valores negativos representam saques.

### Saída

- O saldo final da conta no formato: `Saldo: R$ X.XX`

#### Exemplos

| Entrada                | Saída                |
|------------------------|----------------------|
| [100, -50, 200]        | Saldo: R$ 250.00     |
| [500, -200, -100]      | Saldo: R$ 200.00     |
| [250, -150, -50]       | Saldo: R$ 50.00      |

> **Atenção:** As entradas e saídas devem ser exatamente iguais às descritas acima para aprovação nos testes automáticos da plataforma DIO.

---

## O que foi realizado

- O programa lê a lista de transações via entrada padrão (stdin), conforme exigido pela plataforma DIO.
- Aceita tanto valores inteiros quanto decimais.
- Calcula corretamente o saldo final, somando depósitos e subtraindo saques.
- A saída é impressa exatamente no formato solicitado: `Saldo: R$ X.XX`.
- O código trata entradas vazias e possíveis erros de conversão, garantindo robustez.

---

## Como executar localmente

1. Clone este repositório ou copie o arquivo `gestao_transacoes_bancarias1.py`.
2. Execute o script em um terminal Python 3:

    ```bash
    python gestao_transacoes_bancarias1.py
    ```

3. Digite a lista de transações quando solicitado, por exemplo:

    ```text
    [100, -50, 200]
    ```

---

## Observações

- Para submissão na DIO, utilize a versão que lê diretamente do stdin.
- Para testes locais, o código permite digitar a lista manualmente caso não haja entrada padrão.

---

Desenvolvido por Sidnei Silva (sidneifs)
