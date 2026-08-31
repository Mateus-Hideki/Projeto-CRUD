import './App.css'

const products = [
  {
    name: 'Corte estruturado',
    category: 'Camisetas',
    price: 'R$ 249',
    tone: 'Monochrome',
  },
  {
    name: 'Jaqueta urbana',
    category: 'Outerwear',
    price: 'R$ 489',
    tone: 'Soft black',
  },
  {
    name: 'Calça relax',
    category: 'Essentials',
    price: 'R$ 329',
    tone: 'Stone grey',
  },
]

const categories = [
  'Casual',
  'Esporte',
  'Formal',
  'Linha premium',
  'Accessories',
]

function App() {
  return (
    <div className="page-shell">
      <header className="topbar">
        <div className="brand-lockup">
          <span className="brand-mark">LOJA</span>
          <span className="brand-name">PROJETO CRUD</span>
        </div>

        <nav className="main-nav" aria-label="Menu principal">
          <a href="#colecao">Coleção</a>
          <a href="#categorias">Categorias</a>
          <a href="#sobre">Sobre</a>
          <a href="#contato">Contato</a>
        </nav>

        <button type="button" className="shop-button">
          Ver catálogo
        </button>
      </header>

      <main className="content">
        <section className="hero-section" id="colecao">
          <div className="hero-copy">
            <p className="eyebrow">Novidade / Primavera</p>
            <h1>Essencial, preciso e sofisticado.</h1>
            <p className="hero-text">
              Peças marcadas por linhas limpas, acabamentos refinados e a
              liberdade do visual em preto, branco e cinza.
            </p>

            <div className="hero-actions">
              <button type="button" className="primary-btn">
                Explorar coleção
              </button>
              <button type="button" className="secondary-btn">
                Ver lookbook
              </button>
            </div>

            <div className="stats-row">
              <div>
                <strong>14k</strong>
                <span>Clientes</span>
              </div>
              <div>
                <strong>48h</strong>
                <span>Entrega</span>
              </div>
              <div>
                <strong>4.9</strong>
                <span>Avaliação</span>
              </div>
            </div>
          </div>

          <div className="hero-visual" aria-label="Visual editorial da coleção">
            <div className="image-card image-large" />
            <div className="image-card image-small" />
            <div className="floating-note">
              <span>Nova coleção</span>
              <strong>Monolith</strong>
            </div>
          </div>
        </section>

        <section className="feature-strip" aria-label="Destaques">
          <div>
            <span>01</span>
            <p>Texturas premium</p>
          </div>
          <div>
            <span>02</span>
            <p>Montagens minimalistas</p>
          </div>
          <div>
            <span>03</span>
            <p>Entrega rápida</p>
          </div>
        </section>

        <section className="catalog-section">
          <div className="section-heading">
            <p className="eyebrow">Coleção selecionada</p>
            <h2>Itens em destaque</h2>
          </div>

          <div className="product-grid">
            {products.map((product) => (
              <article key={product.name} className="product-card">
                <div className="product-image product-one" aria-hidden="true" />
                <div className="product-body">
                  <div className="product-header">
                    <span>{product.category}</span>
                    <span>{product.tone}</span>
                  </div>
                  <h3>{product.name}</h3>
                  <div className="product-footer">
                    <strong>{product.price}</strong>
                    <button type="button">Comprar</button>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="category-showcase" id="categorias">
          <div className="category-copy">
            <p className="eyebrow">Categorias</p>
            <h2>Versatilidade em cada look.</h2>
            <p>
              Uma seleção pensada para o dia a dia urbano, do trabalho ao fim de
              semana, mantendo a estética limpa e autoral.
            </p>
          </div>

          <div className="category-list">
            {categories.map((category) => (
              <div key={category} className="category-item">
                <span>{category}</span>
                <strong>01</strong>
              </div>
            ))}
          </div>
        </section>

        <section className="editorial-banner" id="sobre">
          <div className="banner-text">
            <p className="eyebrow">Estilo contemporâneo</p>
            <h2>Construído para quem valoriza simplicidade com presença.</h2>
          </div>
          <button type="button" className="primary-btn">Fazer pedido</button>
        </section>
      </main>
    </div>
  )
}

export default App
