# Strings de Múltiplas Linhas em Python

Este repositório contém o arquivo `string_4.py`, que demonstra como utilizar **strings de múltiplas linhas** em Python. Strings de múltiplas linhas são úteis para formatar textos longos, como mensagens, recibos, e-mails ou qualquer outro conteúdo que precise ser exibido de forma estruturada.

---

## O que são Strings de Múltiplas Linhas?

Strings de múltiplas linhas em Python são definidas usando aspas triplas (`"""` ou `'''`). Elas permitem criar textos que ocupam várias linhas, mantendo a formatação original.

### Sintaxe

```python
texto = """
Linha 1
Linha 2
Linha 3
"""
```

---

## Exemplo no Código

O arquivo `string_4.py` utiliza strings de múltiplas linhas para criar uma mensagem de confirmação de pedido em um ambiente de e-commerce. Veja o exemplo abaixo:

```python
empresa = "Titanium SiD"
cliente = "Sidnei Silva"
pedido = 12345
data = "21/04/2025"
total = 2599.90

mensagem_pedido = f"""
==========================================
          CONFIRMAÇÃO DE PEDIDO
==========================================

Empresa: {empresa}
Cliente: {cliente}
Número do Pedido: {pedido}
Data: {data}

Itens do Pedido:
1x Notebook Gamer - R$ 2.000,00
1x Mouse Sem Fio - R$ 199,90
1x Teclado Mecânico - R$ 400,00

Total: R$ {total:.2f}

Obrigado por comprar na {empresa}!
==========================================
"""
print(mensagem_pedido)
```

**Saída no Terminal:**

```plaintext
==========================================
          CONFIRMAÇÃO DE PEDIDO
==========================================

Empresa: Titanium SiD
Cliente: Sidnei Silva
Número do Pedido: 12345
Data: 21/04/2025

Itens do Pedido:
1x Notebook Gamer - R$ 2.000,00
1x Mouse Sem Fio - R$ 199,90
1x Teclado Mecânico - R$ 400,00

Total: R$ 2599,90

Obrigado por comprar na Titanium SiD!
==========================================
```

---

## Gerando um QR Code com Link

O arquivo também gera um QR Code para um **gift exclusivo**. O link do QR Code pode ser acessado diretamente no navegador:

[https://www.titaniumsid.com/gift/12345](https://github.com/sidneifs/Python/blob/main/Python_10/strings%20multiplas%20linhas/gift_qr_code.png?raw=true)

### Código para Gerar o QR Code

```python
import qrcode

gift_qr_code = "https://www.titaniumsid.com/gift/12345"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(gift_qr_code)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("gift_qr_code.png")
```

O QR Code será salvo como `gift_qr_code.png` no diretório atual. Você pode escaneá-lo para acessar o link do gift.

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `qrcode` caso ainda não tenha:

   ```bash
   pip install qrcode[pil]
   ```

3. Navegue até o diretório onde o arquivo `string_4.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_10\strings multiplas linhas"
   ```

4. Execute o arquivo diretamente no terminal:

   ```bash
   python string_4.py
   ```

5. O terminal exibirá a mensagem de confirmação do pedido, e o QR Code será salvo como `gift_qr_code.png`.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar strings de múltiplas linhas e gerar QR Codes em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
