# Exemplo de Uso no Site do Portfólio

## HTML para o Site

```html
<section class="project-dashboard-ons">
    <div class="container">
        <h2>Dashboard ONS - Copel</h2>
        
        <div class="project-description">
            <p>
                Dashboard interativo desenvolvido para a <strong>Copel</strong> 
                utilizando dados do <strong>ONS</strong> (Operador Nacional do Sistema Elétrico).
                O projeto oferece uma interface moderna para análise de dados energéticos
                com visualizações interativas e em tempo real.
            </p>
        </div>

        <div class="dashboard-screenshots">
            <div class="screenshot-item">
                <img src="assets/screenshots/dashboard_full.png" 
                     alt="Dashboard ONS - Visão Geral"
                     loading="lazy">
                <p>Visão Geral do Dashboard</p>
            </div>
            
            <div class="screenshot-item">
                <img src="assets/screenshots/dashboard_charts.png" 
                     alt="Dashboard ONS - Gráficos Interativos"
                     loading="lazy">
                <p>Gráficos Interativos</p>
            </div>
            
            <div class="screenshot-item">
                <img src="assets/screenshots/dashboard_responsive.png" 
                     alt="Dashboard ONS - Interface Responsiva"
                     loading="lazy">
                <p>Interface Responsiva</p>
            </div>
        </div>

        <div class="project-features">
            <h3>Funcionalidades Principais</h3>
            <ul>
                <li>📊 Gráficos interativos em tempo real</li>
                <li>🔄 Atualizações automáticas de dados</li>
                <li>📱 Interface responsiva para todos os dispositivos</li>
                <li>🔍 Filtros avançados para análise</li>
                <li>📤 Exportação de dados em múltiplos formatos</li>
                <li>🎨 Design personalizado com tema da Copel</li>
            </ul>
        </div>

        <div class="project-tech">
            <h3>Tecnologias Utilizadas</h3>
            <div class="tech-stack">
                <span class="tech-tag">Python</span>
                <span class="tech-tag">Panel</span>
                <span class="tech-tag">Holoviz</span>
                <span class="tech-tag">Bokeh</span>
                <span class="tech-tag">Pandas</span>
                <span class="tech-tag">MongoDB</span>
            </div>
        </div>

        <div class="project-links">
            <a href="dashboard_holoviz.html" class="btn btn-primary" target="_blank">
                🚀 Ver Dashboard
            </a>
            <a href="https://github.com/seu-usuario/dashboard_holoviz" class="btn btn-secondary" target="_blank">
                📁 Ver Código
            </a>
        </div>
    </div>
</section>
```

## CSS para Estilização

```css
.project-dashboard-ons {
    padding: 4rem 0;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.project-dashboard-ons .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.project-dashboard-ons h2 {
    font-size: 2.5rem;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 2rem;
}

.project-description {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 3rem;
    font-size: 1.1rem;
    line-height: 1.6;
    color: #34495e;
}

.dashboard-screenshots {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.screenshot-item {
    text-align: center;
    background: white;
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.screenshot-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.15);
}

.screenshot-item img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    margin-bottom: 1rem;
}

.screenshot-item p {
    font-weight: 600;
    color: #2c3e50;
    margin: 0;
}

.project-features {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    margin: 3rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.project-features h3 {
    color: #2c3e50;
    margin-bottom: 1.5rem;
    font-size: 1.5rem;
}

.project-features ul {
    list-style: none;
    padding: 0;
}

.project-features li {
    padding: 0.5rem 0;
    color: #34495e;
    font-size: 1.1rem;
}

.project-tech {
    text-align: center;
    margin: 3rem 0;
}

.project-tech h3 {
    color: #2c3e50;
    margin-bottom: 1.5rem;
    font-size: 1.5rem;
}

.tech-stack {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
}

.tech-tag {
    background: #3498db;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    font-size: 0.9rem;
    font-weight: 500;
}

.project-links {
    text-align: center;
    margin: 3rem 0;
}

.btn {
    display: inline-block;
    padding: 1rem 2rem;
    margin: 0 1rem;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary {
    background: #e74c3c;
    color: white;
}

.btn-primary:hover {
    background: #c0392b;
    transform: translateY(-2px);
}

.btn-secondary {
    background: #34495e;
    color: white;
}

.btn-secondary:hover {
    background: #2c3e50;
    transform: translateY(-2px);
}

/* Responsividade */
@media (max-width: 768px) {
    .dashboard-screenshots {
        grid-template-columns: 1fr;
    }
    
    .project-links .btn {
        display: block;
        margin: 1rem auto;
        max-width: 250px;
    }
}
```

## Texto Explicativo para o Portfólio

### Descrição do Projeto
"Desenvolvi um dashboard interativo para a Copel (Companhia Paranaense de Energia) que consome dados do ONS (Operador Nacional do Sistema Elétrico) em tempo real. O projeto utiliza tecnologias modernas de visualização de dados para criar uma interface intuitiva e responsiva que permite aos analistas e gestores monitorar e analisar informações energéticas de forma eficiente."

### Desafios Superados
- **Integração com APIs**: Implementei conexão segura com as APIs do ONS e sistemas da Copel
- **Performance**: Otimizei o dashboard para lidar com grandes volumes de dados em tempo real
- **UX/UI**: Criei uma interface intuitiva que facilita a análise de dados complexos
- **Responsividade**: Garantir que o dashboard funcione perfeitamente em todos os dispositivos

### Resultados Alcançados
- Dashboard funcional com atualizações em tempo real
- Interface responsiva e acessível
- Redução no tempo de análise de dados energéticos
- Melhoria na tomada de decisões baseada em dados

### Tecnologias e Habilidades Demonstradas
- **Backend**: Python, MongoDB, APIs REST
- **Frontend**: Panel, Holoviz, Bokeh
- **Análise de Dados**: Pandas, NumPy
- **DevOps**: Versionamento Git, Documentação
- **Soft Skills**: Trabalho com cliente, Análise de requisitos, Comunicação técnica
