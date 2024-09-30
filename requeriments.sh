#!/bin/bash

# Atualiza o Termux e instala Python e pip
echo "Atualizando o Termux e instalando Python..."
pkg update && pkg upgrade -y
pkg install python -y
pkg install python3-pip -y

# Verifica se o Python foi instalado com sucesso
if command -v python3 &>/dev/null; then
    echo "Python instalado com sucesso."
else
    echo "Falha na instalação do Python. Verifique a saída e tente novamente."
    exit 1
fi

# Instala o módulo HTTP se não estiver disponível
echo "Verificando se o módulo HTTP está disponível..."
pip install --upgrade pip

# Verifica se o pip foi instalado com sucesso
if command -v pip &>/dev/null; then
    echo "Pip instalado com sucesso."
else
    echo "Falha na instalação do pip. Verifique a saída e tente novamente."
    exit 1
fi

# Finaliza a instalação
echo "Todas as ferramentas necessárias foram instaladas com sucesso!"
echo " Siga @Safelockai no instagram "
