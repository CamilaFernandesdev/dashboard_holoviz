# 📊 Dashboard ONS - Operador Nacional do Sistema Elétrico

## 🎯 Sobre o Projeto

Este projeto consiste em um dashboard interativo desenvolvido para a **Copel** (Companhia Paranaense de Energia) utilizando dados do **ONS** (Operador Nacional do Sistema Elétrico). O dashboard foi construído com tecnologias modernas de visualização de dados e oferece uma interface intuitiva para análise de informações energéticas.

## 🏢 O que é o ONS?

O **ONS** (Operador Nacional do Sistema Elétrico) é uma entidade privada, sem fins lucrativos, responsável pela coordenação e controle da operação das instalações de geração e transmissão de energia elétrica no Sistema Interligado Nacional (SIN) do Brasil.

### Principais responsabilidades:
- **Coordenação da operação** do sistema elétrico brasileiro
- **Monitoramento em tempo real** da geração e transmissão de energia
- **Gestão da rede** de transmissão nacional
- **Fornecimento de dados** sobre o sistema elétrico
- **Planejamento** da operação energética

## 🚀 Funcionalidades do Dashboard

### 📈 Visualizações Principais
- **Gráficos interativos** de dados energéticos
- **Dashboards em tempo real** com atualizações automáticas
- **Múltiplas abas** para diferentes tipos de análise
- **Filtros dinâmicos** para segmentação de dados
- **Exportação de dados** em diferentes formatos

### 🎨 Interface do Usuário
- **Design responsivo** adaptável a diferentes dispositivos
- **Tema personalizado** com cores da Copel
- **Navegação intuitiva** entre diferentes seções
- **Indicadores visuais** para melhor compreensão dos dados

### 🔧 Tecnologias Utilizadas
- **Python** como linguagem principal
- **Panel** para interface web interativa
- **Holoviz** para visualizações avançadas
- **Bokeh** para gráficos interativos
- **Pandas** para manipulação de dados
- **MongoDB** para armazenamento de dados

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- MongoDB instalado e configurado
- Acesso aos dados do ONS

### Instalação das Dependências
```bash
pip install -r requirements.txt
```

### Configuração do Ambiente
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/dashboard_holoviz.git
cd dashboard_holoviz
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. Execute o dashboard:
```bash
python dashboard_holoviz.py
```

## 📁 Estrutura do Projeto

```
dashboard_holoviz/
├── dashboard_holoviz.ipynb    # Notebook principal com o código
├── dashboard_holoviz.html     # Versão HTML renderizada
├── infra_copel/              # Módulo de infraestrutura da Copel
├── assets/                    # Imagens e recursos visuais
├── requirements.txt           # Dependências do projeto
├── README.md                 # Este arquivo
└── LICENSE                   # Licença do projeto
```

## 🎮 Como Usar

### 1. Acesso ao Dashboard
- Abra o arquivo `dashboard_holoviz.html` em qualquer navegador moderno
- Ou execute o notebook Jupyter para desenvolvimento

### 2. Navegação
- Use as abas para alternar entre diferentes visualizações
- Utilize os filtros para refinar os dados exibidos
- Interaja com os gráficos para obter mais detalhes

### 3. Exportação
- Clique nos botões de exportação para baixar dados
- Use as opções de captura de tela para relatórios

## 🔍 Casos de Uso

### Para Analistas de Energia
- Monitoramento de tendências energéticas
- Análise de padrões de consumo
- Relatórios para stakeholders

### Para Gestores
- Visão geral do sistema energético
- Tomada de decisões baseada em dados
- Planejamento estratégico

### Para Operadores
- Monitoramento em tempo real
- Alertas e notificações
- Controle operacional

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

- **Seu Nome** - *Desenvolvimento inicial* - [SeuGitHub](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- **Copel** pela oportunidade de desenvolvimento
- **ONS** pelo fornecimento dos dados
- **Comunidade Python** pelas bibliotecas utilizadas

## 📞 Contato

- **Email**: seu-email@exemplo.com
- **LinkedIn**: [Seu Perfil](https://linkedin.com/in/seu-perfil)
- **GitHub**: [@seu-usuario](https://github.com/seu-usuario)

## 🔄 Status do Projeto

- ✅ Dashboard funcional
- ✅ Interface responsiva
- ✅ Integração com MongoDB
- 🔄 Documentação em andamento
- 🔄 Testes automatizados
- 🔄 Deploy em produção

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!**