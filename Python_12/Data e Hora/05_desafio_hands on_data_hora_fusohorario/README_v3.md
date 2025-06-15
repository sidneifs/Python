# Desafio Data e Hora - Sistema Bancário (v3)

## O que foi feito nas versões anteriores

- **v1:** Estrutura básica de um sistema bancário com orientação a objetos, manipulação de contas, clientes e transações, e uso de datas/hora para registro das operações.
- **v2:** Adicionadas regras de negócio, como limite de transações diárias, mensagens de aviso e código mais modular, preparando para futuras expansões.

## Aprimoramentos da versão 3 (v3)

- Todas as operações principais (depósito, saque, extrato, criação de cliente e conta) foram refatoradas em funções separadas e reutilizáveis.
- Adicionadas funções auxiliares para validação de dados de entrada (CPF, valores numéricos, etc).
- Estrutura do código mais limpa, modular e fácil de manter.
- Pronto para expansão futura, como autenticação, tipos de conta, integração com banco de dados e interface gráfica/web.
- **Novo:** Autenticação real por senha para clientes e ADMIN, múltiplas contas por cliente, tipos de conta, menu ADMIN separado e acesso restrito.

---

## Instruções para Usuário Comum

1. **Criar novo usuário**
   - Escolha a opção `[nu]` no menu.
   - Informe CPF (11 dígitos), nome, data de nascimento, endereço e defina uma senha.

2. **Criar nova conta**
   - Escolha `[nc]`.
   - Informe o CPF do cliente já cadastrado.
   - Escolha o tipo de conta (corrente ou simples).

3. **Depositar, Sacar, Ver Extrato**
   - Escolha `[d]`, `[s]` ou `[e]`.
   - Informe o CPF e a senha cadastrada.
   - Se houver mais de uma conta, selecione a desejada.

4. **Listar contas do usuário**
   - Escolha `[lc]` e informe o CPF.

5. **Recuperar senha**
   - Escolha `[rs]` e siga as instruções para redefinir a senha do seu CPF.

6. **Sair**
   - Escolha `[q]`.

---

## Instruções para ADMINISTRADOR

1. **Acessar modo ADMIN**
   - No menu principal, escolha `[a]`.
   - Informe o CPF do ADMIN: `00000000000`
   - Informe a senha do ADMIN: `admin123`

2. **Menu ADMIN**
   - Após autenticação, o menu ADMIN será exibido:
     - `[1]` Listar todos os clientes cadastrados
     - `[2]` Listar todas as contas do sistema
     - `[q]` Sair do modo ADMIN

3. **Funções restritas**
   - Apenas o ADMIN pode acessar as listagens completas de clientes e contas.
   - O acesso é protegido por senha e não aparece para usuários comuns.

---

## Observações de Segurança

- Nunca compartilhe sua senha.
- O ADMIN deve alterar a senha padrão após o primeiro acesso (recomendado para produção).
- O sistema pode ser expandido para logs, bloqueio após tentativas incorretas, autenticação multifator, etc.

---

## Execução

Execute o arquivo `desafio_data_e_hora_v3.py` em um terminal Python 3. Exemplo:

```bash
python desafio_data_e_hora_v3.py
```

---

Sidnei Silva (sidneifs)
