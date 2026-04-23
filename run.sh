#!/bin/bash
echo "📦 Instalando dependências..."
pip install -q -r requirements.txt

echo "🚀 Iniciando sistema IFMT Carteirinha..."
echo ""
echo "  Acesse: http://localhost:5000"
echo "  Admin:  admin@ifmt.edu.br / Admin@2025"
echo ""
python app.py
