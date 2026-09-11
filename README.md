# 🧴 ScentMetrics: Fragrance Market Intelligence & Olfactory Analysis Platform

ScentMetrics is an interactive data analytics dashboard and recommendation engine for modern fragrance market research. Built with **Gradio**, **Plotly**, and **NumPy**, it provides multidimensional exploratory tools for community fragrance reviews, demographic preferences, and chemical accord footprints.

---

## 🚀 Core Features

### 1. 📊 Market Leaderboard & Dynamic Filtering
* Real-time slicing by **Release Year**, **Main Accords**, and **Community Rating Thresholds**.
* Horizontal bar rankings tracking demographic resonance among young adult consumers (18–24 cohort).
* Synchronized interactive records data table.

### 2. 🗺️ 2D PCA Olfactory Space (Dimensionality Reduction)
* Custom Singular Value Decomposition (SVD) projection mapping 6D accord spaces (`Woody`, `Citrus`, `Sweet`, `Spicy`, `Aromatic`, `Smoky`) onto a 2D plane.
* Marker sizing by Sillage projection class (`Moderate`, `Strong`, `Enormous`).
* Toggleable Biplot loading vectors showing the directional pull of each olfactory note.

### 3. 🧪 Custom Scent Synthesizer
* Interactive formula mixer allowing users to design an olfactory footprint from scratch.
* Cosine similarity scoring matching custom formulations to the closest commercially available bottles.
* Dual-trace radar chart overlaying custom formulas against top market twins.

### 4. 🧬 Scent-Twin Vector Engine
* Nearest-neighbor retrieval based on vector cosine similarity:
  $$\text{Similarity}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\Vert{}\mathbf{u}\Vert{}_2 \Vert{}\mathbf{v}\Vert{}_2}$$
* Identifies direct market substitutes and clones with match percentage scoring and delta breakdowns.

### 5. ⚔️ Olfactory Duel (Head-to-Head Radar Comparison)
* Direct side-by-side radar overlay for any two catalog fragrances.
* Comparative technical specification matrix (longevity class, sillage, rating, and launch year).

---

## 🛠️ Tech Stack

* **UI & Reactive Layout:** Gradio (`gr.Blocks`)
* **Visualizations:** Plotly Express (`px.bar`, `px.scatter`), Plotly Graph Objects (`go.Scatterpolar`)
* **Vector Math & Analytics:** NumPy (SVD, Vector Norms, Cosine Similarity)
* **Data Ingestion & Slicing:** Pandas

---

## 📦 Installation & Setup

### Prerequisites
* Python 3.9+
* Recommended: Virtual environment (`venv` or `conda`)

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/perfume-market-insights.git](https://github.com/your-username/perfume-market-insights.git)
cd perfume-market-insights