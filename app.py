from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import re  # Importação para sanitizar o nome

app = Flask(__name__)

# Registro da fonte Alex Brush
pdfmetrics.registerFont(TTFont('Alex Brush', 'static/fonts/AlexBrush-Regular.ttf'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_certificate():
    name = request.form['name']
    description = request.form['description'][:250]  # Limitar a 250 caracteres
    responsavel = request.form['responsavel']
    estado = request.form['estado']
    cidade = request.form['cidade']
    data_emissao = request.form['data_emissao']  # A data já chega no formato YYYY-MM-DD

    try:
        ano, mes, dia = data_emissao.split('-')
        meses = {
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
            '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
            '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
        }
        data_emissao_formatada = f"{dia} de {meses[mes]} de {ano}"
    except (ValueError, IndexError, KeyError):
        data_emissao_formatada = "Data inválida"

    # Criação do PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=landscape(letter))
    width, height = landscape(letter)

    # Adicionando a imagem de fundo
    p.drawImage('static/images/certificado_bg.png', 0, 0, width=width, height=height)

    # Centralizar "CERTIFICADO"
    p.setFont("Helvetica-Bold", 65)
    certificado_texto = "CERTIFICADO"
    p.drawString((width - p.stringWidth(certificado_texto, "Helvetica-Bold", 65)) / 2, height - 150, certificado_texto.upper())

    # Centralizar "Este certificado comprova que"
    p.setFont("Helvetica", 19)
    descricao_texto = "ESTE CERTIFICADO COMPROVA QUE"
    p.drawString((width - p.stringWidth(descricao_texto, "Helvetica", 19)) / 2, height - 200, descricao_texto.upper())

    # Centralizar nome da pessoa
    p.setFont("Alex Brush", 58)
    p.drawString((width - p.stringWidth(name, "Alex Brush", 58)) / 2, height - 280, name)

    # Ajustar posição e largura do texto da descrição
    p.setFont("Helvetica", 16)
    max_width = width - 300  # Reduzir ainda mais a largura máxima para mover mais para a esquerda

    # Dividindo a descrição em palavras para ajuste de linha
    palavras = description.split(' ')
    linhas_descricao = []
    linha_atual = ""

    for palavra in palavras:
        if len(palavra) > 50:
            for i in range(0, len(palavra), 50):
                linha_forcada = palavra[i:i + 50]
                linhas_descricao.append(linha_forcada)
        else:
            if p.stringWidth(linha_atual + palavra + " ", "Helvetica", 16) < max_width:
                linha_atual += palavra + " "
            else:
                linhas_descricao.append(linha_atual)
                linha_atual = palavra + " "

    linhas_descricao.append(linha_atual)  # Adicionar a última linha

    altura_descricao = height - 350
    for linha in linhas_descricao:
        if altura_descricao > 150:
            p.drawString((width - p.stringWidth(linha, "Helvetica", 16)) / 2 - 60, altura_descricao, linha.upper())
            altura_descricao -= 25  # Espaçamento entre as linhas

    # Adicionar nome do responsável, cidade, estado e data
    p.setFont("Helvetica", 14)
    p.drawString((width - p.stringWidth(responsavel, "Helvetica", 14)) / 2, 90, responsavel)
    rodape_text = f"{cidade} - {estado}, {data_emissao_formatada}"
    p.drawString((width - p.stringWidth(rodape_text, "Helvetica", 14)) / 2, 60, rodape_text)

    p.showPage()
    p.save()

    buffer.seek(0)

    # Sanitizar o nome para ser usado como parte do nome do arquivo
    nome_sanitizado = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')

    # Gerar o nome do arquivo como "Certificado - NOME_DO_DESTINATÁRIO.pdf"
    return send_file(buffer, as_attachment=True, download_name=f'Certificado_{nome_sanitizado}.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
