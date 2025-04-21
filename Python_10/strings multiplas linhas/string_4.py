# Dados do pedido e do cliente
empresa = "Titanium SiD"
cliente = "Sidnei Silva"
pedido = 12345
data = "21/04/2025"
total = 2599.90
email = "sidnei.silva@example.com"
telefone = "+55 11 91234-5678"
site = "www.titaniumsid.com"
gift_qr_code = "https://www.titaniumsid.com/gift/12345"

# Mensagem de confirmação do pedido
mensagem_pedido = f"""
==========================================
          CONFIRMAÇÃO DE PEDIDO
==========================================

Empresa: {empresa}
Cliente: {cliente}
E-mail: {email}
Telefone: {telefone}
Site: {site}
Numero do Pedido: {pedido}
Data: {data}

Itens do Pedido:
1x Notebook Gamer - R$ 2.000,00
1x Mouse Sem Fio - R$ 199,90
1x Teclado Mecanico - R$ 400,00

Total: R$ {total:.2f}

Obrigado por comprar na {empresa}!
==========================================

Aproveite um presente especial para sua proxima compra!
Use o QR Code abaixo para acessar seu gift exclusivo:
QR Code: {gift_qr_code}
"""

print(mensagem_pedido)

# Gerar QR Code para o gift exclusivo
import qrcode

# Configuração do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(gift_qr_code)
qr.make(fit=True)

# Salvar QR Code como imagem
img = qr.make_image(fill_color="black", back_color="white")
img.save("gift_qr_code.png")

print("QR Code gerado e salvo como 'gift_qr_code.png'.")