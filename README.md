# 🎓 Gerador de Certificados - Versão 1.0

Este é um projeto simples e funcional que permite a geração de certificados personalizados com dados como nome do participante, data, e descrição do curso/evento. O objetivo é facilitar a criação de certificados diretamente de uma aplicação web sem a necessidade de ferramentas externas. 💡

## 🎯 Funcionalidades
- 🎨 Interface web intuitiva e fácil de usar.
- 🖋️ Geração de certificados personalizados com diferentes nomes, datas e descrições.
- 📄 Utilização de modelos predefinidos, podendo ser substituídos por personalizados.
- ✍️ Uso de fontes estilizadas para um design elegante e profissional.
- 🌗 Alternância entre modo claro e escuro para melhor experiência do usuário.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework para criar a interface web.
- **PIL (Pillow)**: Biblioteca para manipulação de imagens e renderização do texto nos certificados.
- **HTML/CSS**: Para a criação da interface amigável do usuário.

## 📋 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o Python 3.x instalado. Você pode verificar se o Python está instalado executando:

```bash
python --version
```

## 🚀 Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerador-certificados.git
cd gerador-certificados
```

### 2. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Ou, se você preferir instalar manualmente:

```bash
pip install Flask Pillow
```

## 🏃‍♂️ Como Usar

### 1. Execute o arquivo principal:

```bash
python app.py
```

### 2. Geração de Certificado:

- Insira os dados necessários como nome do participante, nome do responsável, data, e descrição.
- Clique em Gerar Certificado para criar o certificado personalizado.
- Visualize e baixe o certificado gerado.

## 🔧 Personalização

- Modelo de Certificado: Para utilizar um modelo próprio, substitua o arquivo **static/certificado_template.png** pelo seu próprio modelo.
- Fontes: Adicione novas fontes na pasta fonts/ e modifique o código para utilizá-las nos certificados.
- 
## 🌟 Funcionalidades Futuras

- 📤 Envio automático de certificados gerados para os e-mails dos participantes.
- 📅 Agendamento para geração em massa de certificados.
- 🔗 Integração com sistemas de inscrição para gerar certificados automaticamente.

# 🛡️ Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
