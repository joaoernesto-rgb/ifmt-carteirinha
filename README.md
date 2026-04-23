# 🎓 Sistema de Carteirinha Estudantil — IFMT

Sistema web completo para emissão de carteirinhas estudantis do IFMT com validação por QR Code.

## 🚀 Como Rodar

```bash
# 1. Entre na pasta
cd ifmt_carteirinha

# 2. Instale as dependências
pip install --user -r requirements.txt

# 3. Inicie o servidor
python3 app.py
```

Acesse: **http://localhost:5000**

---

## 🔐 Credenciais Padrão do Administrador

| Campo | Valor |
|-------|-------|
| E-mail | `admin@ifmt.edu.br` |
| Senha  | `Admin@2025` |

> ⚠️ **Altere a senha do admin após o primeiro acesso!**

---

## 📋 Funcionalidades

### Para Estudantes
- ✅ Cadastro com nome, e-mail, CPF e senha
- ✅ Upload de foto (JPG/PNG, recortada automaticamente em 3×4)
- ✅ Formulário com: matrícula, curso, campus, semestre, data de nascimento
- ✅ Acompanhar status da solicitação (pendente / aprovada / rejeitada)
- ✅ Download da carteirinha em PDF após aprovação

### Para Administradores
- ✅ Painel com contadores de pendentes, aprovadas e rejeitadas
- ✅ Visualização dos dados completos do estudante
- ✅ Pré-visualização da carteirinha antes de aprovar
- ✅ Aprovação com escolha do ano de validade
- ✅ Rejeição com motivo (feedback para o estudante)
- ✅ Download do PDF da carteirinha aprovada

### Segurança
- ✅ QR Code único por carteirinha (gerado no momento da aprovação)
- ✅ Página pública de verificação: `/verify/<token>`
- ✅ Senhas criptografadas com Werkzeug (PBKDF2+SHA256)
- ✅ Tokens únicos gerados com `secrets.token_urlsafe(32)`

---

## 📄 Layout da Carteirinha (PDF)

A carteirinha é gerada no padrão **CR80** (85,6mm × 54mm) — mesmo tamanho de cartão de crédito — centralizada em folha A4 com linha de corte tracejada.

Contém:
- Cabeçalho verde IFMT com nome da instituição
- Foto do estudante (3×4)
- Nome, matrícula e curso
- QR Code de segurança (verde #006633)
- Rodapé com campus e validade

---

## 📁 Estrutura de Arquivos

```
ifmt_carteirinha/
├── app.py                     # Aplicação Flask principal
├── requirements.txt           # Dependências Python
├── run.sh                     # Script de inicialização
├── templates/
│   ├── base.html              # Layout base (navbar + footer)
│   ├── index.html             # Página inicial
│   ├── login.html             # Login
│   ├── register.html          # Cadastro de estudante
│   ├── verify.html            # Verificação pública de QR Code
│   ├── student/
│   │   ├── dashboard.html     # Painel do estudante
│   │   └── form.html          # Formulário de solicitação
│   ├── admin/
│   │   ├── dashboard.html     # Painel do administrador
│   │   └── review.html        # Análise de solicitação
│   └── errors/
│       ├── 403.html
│       └── 404.html
└── static/
    ├── css/style.css          # Estilos (identidade IFMT)
    └── uploads/               # Fotos dos estudantes + QR codes
        └── qrcodes/
```

---

## ⚙️ Variáveis de Ambiente (Produção)

| Variável | Descrição |
|----------|-----------|
| `SECRET_KEY` | Chave secreta Flask (gere com `python3 -c "import secrets; print(secrets.token_hex(32))"`) |
| `DATABASE_URL` | URL do banco (padrão: SQLite em /tmp — use PostgreSQL em produção) |

---

## 🌐 Implantação em Produção

Para colocar em produção (ex: VPS com Ubuntu):

```bash
# Instalar Gunicorn
pip install gunicorn

# Rodar com Gunicorn (4 workers)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Usar Nginx como reverse proxy na porta 80
```

Configure uma URL real para os QR Codes editando a função `generate_qr()` em `app.py`:
```python
url = f"https://SEU-DOMINIO.com.br/verify/{token}"
```
