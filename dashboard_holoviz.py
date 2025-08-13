#!/usr/bin/env python3
"""
Dashboard ONS - Operador Nacional do Sistema Elétrico
Desenvolvido para a Copel (Companhia Paranaense de Energia)

Este arquivo é o ponto de entrada principal para executar o dashboard.
"""

import os
import sys
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dashboard.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Função principal para executar o dashboard."""
    try:
        logger.info("Iniciando Dashboard ONS...")
        
        # Verificar se o notebook existe
        notebook_path = Path("dashboard_holoviz.ipynb")
        if not notebook_path.exists():
            logger.error("Notebook dashboard_holoviz.ipynb não encontrado!")
            return 1
        
        # Verificar se o arquivo HTML existe
        html_path = Path("dashboard_holoviz.html")
        if not html_path.exists():
            logger.warning("Arquivo HTML não encontrado. Execute o notebook primeiro.")
            return 1
        
        logger.info("Dashboard ONS iniciado com sucesso!")
        logger.info(f"Arquivo HTML disponível em: {html_path.absolute()}")
        logger.info("Abra o arquivo HTML em seu navegador para visualizar o dashboard.")
        
        return 0
        
    except Exception as e:
        logger.error(f"Erro ao iniciar o dashboard: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
