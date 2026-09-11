import gradio as gr
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. ENRICHED DATASET WITH MULTI-DIMENSIONAL OLFACTORY ACCORDS
perfume_data = [
    {
        "Perfume Name": "Sauvage Elixir",
        "Brand": "Dior",
        "Release Year": 2021,
        "Rating": 4.55,
        "Sillage": "Enormous",
        "Main Accords": "Fresh Spicy",
        "Age_Group_Score": 92,
        "Woody": 75, "Citrus": 40, "Sweet": 55, "Spicy": 95, "Aromatic": 85, "Smoky": 60
    },
    {
        "Perfume Name": "Bleu de Chanel Parfum",
        "Brand": "Chanel",
        "Release Year": 2018,
        "Rating": 4.60,
        "Sillage": "Strong",
        "Main Accords": "Woody",
        "Age_Group_Score": 88,
        "Woody": 90, "Citrus": 70, "Sweet": 45, "Spicy": 50, "Aromatic": 80, "Smoky": 35
    },
    {
        "Perfume Name": "Y Eau de Parfum",
        "Brand": "Yves Saint Laurent",
        "Release Year": 2018,
        "Rating": 4.48,
        "Sillage": "Strong",
        "Main Accords": "Sweet",
        "Age_Group_Score": 96,
        "Woody": 60, "Citrus": 65, "Sweet": 90, "Spicy": 55, "Aromatic": 85, "Smoky": 20
    },
    {
        "Perfume Name": "Stronger With You Intensely",
        "Brand": "Giorgio Armani",
        "Release Year": 2019,
        "Rating": 4.70,
        "Sillage": "Enormous",
        "Main Accords": "Sweet",
        "Age_Group_Score": 98,
        "Woody": 50, "Citrus": 25, "Sweet": 98, "Spicy": 80, "Aromatic": 55, "Smoky": 40
    },
    {
        "Perfume Name": "Acqua di Giò Parfum",
        "Brand": "Giorgio Armani",
        "Release Year": 2023,
        "Rating": 4.42,
        "Sillage": "Moderate",
        "Main Accords": "Citrus",
        "Age_Group_Score": 81,
        "Woody": 70, "Citrus": 90, "Sweet": 20, "Spicy": 45, "Aromatic": 90, "Smoky": 50
    },
    {
        "Perfume Name": "Explorer",
        "Brand": "Montblanc",
        "Release Year": 2019,
        "Rating": 4.25,
        "Sillage": "Moderate",
        "Main Accords": "Woody",
        "Age_Group_Score": 85,
        "Woody": 85, "Citrus": 80, "Sweet": 30, "Spicy": 50, "Aromatic": 70, "Smoky": 40
    },
    {
        "Perfume Name": "Hacivat",
        "Brand": "Nishane",
        "Release Year": 2017,
        "Rating": 4.62,
        "Sillage": "Enormous",
        "Main Accords": "Citrus",
        "Age_Group_Score": 84,
        "Woody": 90, "Citrus": 95, "Sweet": 35, "Spicy": 40, "Aromatic": 60, "Smoky": 70
    },
    {
        "Perfume Name": "Eros Flame",
        "Brand": "Versace",
        "Release Year": 2018,
        "Rating": 4.38,
        "Sillage": "Strong",
        "Main Accords": "Fresh Spicy",
        "Age_Group_Score": 94,
        "Woody": 65, "Citrus": 85, "Sweet": 80, "Spicy": 90, "Aromatic": 70, "Smoky": 25
    },
    {
        "Perfume Name": "Khamrah",
        "Brand": "Lattafa",
        "Release Year": 2022,
        "Rating": 4.51,
        "Sillage": "Enormous",
        "Main Accords": "Sweet",
        "Age_Group_Score": 95,
        "Woody": 65, "Citrus": 15, "Sweet": 95, "Spicy": 85, "Aromatic": 35, "Smoky": 55
    },
    {
        "Perfume Name": "Terre d'Hermès Eau Givrée",
        "Brand": "Hermès",
        "Release Year": 2022,
        "Rating": 4.40,
        "Sillage": "Moderate",
        "Main Accords": "Citrus",
        "Age_Group_Score": 76,
        "Woody": 80, "Citrus": 98, "Sweet": 15, "Spicy": 65, "Aromatic": 75, "Smoky": 20
    },
    {
        "Perfume Name": "Oud Wood (2020 Batch)",
        "Brand": "Tom Ford",
        "Release Year": 2020,
        "Rating": 4.35,
        "Sillage": "Moderate",
        "Main Accords": "Woody",
        "Age_Group_Score": 68,
        "Woody": 98, "Citrus": 10, "Sweet": 40, "Spicy": 75, "Aromatic": 60, "Smoky": 80
    },
    {
        "Perfume Name": "Angels' Share",
        "Brand": "Kilian",
        "Release Year": 2020,
        "Rating": 4.80,
        "Sillage": "Strong",
        "Main Accords": "Sweet",
        "Age_Group_Score": 91,
        "Woody": 75, "Citrus": 20, "Sweet": 96, "Spicy": 88, "Aromatic": 40, "Smoky": 50
    },
    {
        "Perfume Name": "Gentleman Réserve Privée",
        "Brand": "Givenchy",
        "Release Year": 2022,
        "Rating": 4.58,
        "Sillage": "Strong",
        "Main Accords": "Woody",
        "Age_Group_Score": 79,
        "Woody": 90, "Citrus": 20, "Sweet": 70, "Spicy": 60, "Aromatic": 65, "Smoky": 75
    },
    {
        "Perfume Name": "Scandal Pour Homme",
        "Brand": "Jean Paul Gaultier",
        "Release Year": 2021,
        "Rating": 4.30,
        "Sillage": "Strong",
        "Main Accords": "Sweet",
        "Age_Group_Score": 93,
        "Woody": 55, "Citrus": 45, "Sweet": 94, "Spicy": 50, "Aromatic": 75, "Smoky": 30
    },
    {
        "Perfume Name": "Le Male Elixir",
        "Brand": "Jean Paul Gaultier",
        "Release Year": 2023,
        "Rating": 4.75,
        "Sillage": "Enormous",
        "Main Accords": "Sweet",
        "Age_Group_Score": 99,
        "Woody": 60, "Citrus": 30, "Sweet": 98, "Spicy": 75, "Aromatic": 85, "Smoky": 45
    },
    {
        "Perfume Name": "Allure Homme Sport Eau Extrême",
        "Brand": "Chanel",
        "Release Year": 2016,
        "Rating": 4.45,
        "Sillage": "Moderate",
        "Main Accords": "Citrus",
        "Age_Group_Score": 90,
        "Woody": 70, "Citrus": 85, "Sweet": 60, "Spicy": 55, "Aromatic": 90, "Smoky": 20
    },
    {
        "Perfume Name": "Dior Homme 2020",
        "Brand": "Dior",
        "Release Year": 2020,
        "Rating": 4.15,
        "Sillage": "Moderate",
        "Main Accords": "Woody",
        "Age_Group_Score": 74,
        "Woody": 92, "Citrus": 60, "Sweet": 30, "Spicy": 65, "Aromatic": 60, "Smoky": 45
    },
    {
        "Perfume Name": "The Most Wanted Parfum",
        "Brand": "Azzaro",
        "Release Year": 2022,
        "Rating": 4.65,
        "Sillage": "Strong",
        "Main Accords": "Sweet",
        "Age_Group_Score": 97,
        "Woody": 70, "Citrus": 20, "Sweet": 96, "Spicy": 85, "Aromatic": 50, "Smoky": 55
    },
    {
        "Perfume Name": "Cedrat Boise Intense",
        "Brand": "Mancera",
        "Release Year": 2021,
        "Rating": 4.46,
        "Sillage": "Strong",
        "Main Accords": "Citrus",
        "Age_Group_Score": 83,
        "Woody": 80, "Citrus": 90, "Sweet": 40, "Spicy": 65, "Aromatic": 60, "Smoky": 75
    },
    {
        "Perfume Name": "Apex Extraordinaire",
        "Brand": "Roja Parfums",
        "Release Year": 2024,
        "Rating": 4.20,
        "Sillage": "Strong",
        "Main Accords": "Fresh Spicy",
        "Age_Group_Score": 65,
        "Woody": 85, "Citrus": 70, "Sweet": 25, "Spicy": 85, "Aromatic": 80, "Smoky": 85
    },
]

df_perfumes = pd.DataFrame(perfume_data)
accord_dimensions = ["Woody", "Citrus", "Sweet", "Spicy", "Aromatic", "Smoky"]
all_perfume_names = sorted(df_perfumes["Perfume Name"].tolist())
accord_options = ["All"] + sorted(df_perfumes["Main Accords"].unique().tolist())
sillage_size_map = {"Moderate": 12, "Strong": 20, "Enormous": 30}
df_perfumes["Bubble_Size"] = df_perfumes["Sillage"].map(sillage_size_map)


# 2. NUMPY-POWERED 2D PCA ENGINE
def compute_pca_space():
    X = df_perfumes[accord_dimensions].values.astype(float)
    # Mean-center the data matrix
    X_centered = X - np.mean(X, axis=0)

    # Perform Singular Value Decomposition: X = U * S * Vt
    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

    # Project onto first two principal components
    coords_2d = np.dot(X_centered, Vt.T[:, :2])

    # Calculate variance explained ratios
    variances = (S ** 2) / (X.shape[0] - 1)
    total_var = np.sum(variances)
    var_pc1 = round((variances[0] / total_var) * 100, 1)
    var_pc2 = round((variances[1] / total_var) * 100, 1)

    df_pca = df_perfumes.copy()
    df_pca["PC1"] = coords_2d[:, 0]
    df_pca["PC2"] = coords_2d[:, 1]

    # Loading vectors (how each accord projects onto PC1 & PC2)
    loadings = Vt[:2, :].T  # shape (6, 2)
    return df_pca, loadings, var_pc1, var_pc2


def generate_pca_cluster_map(show_vectors):
    df_pca, loadings, var_pc1, var_pc2 = compute_pca_space()

    fig = px.scatter(
        df_pca,
        x="PC1",
        y="PC2",
        color="Main Accords",
        size="Bubble_Size",
        hover_name="Perfume Name",
        hover_data=["Brand", "Rating", "Sillage", "Release Year", "Age_Group_Score"],
        template="plotly_dark",
        title=f"2D PCA Fragrance Landscape (Variance Explained: PC1={var_pc1}%, PC2={var_pc2}%)"
    )

    # Clean styling and marker outlines
    fig.update_traces(
        marker=dict(line=dict(width=1.5, color="rgba(255, 255, 255, 0.4)")),
        textposition="top center"
    )

    # Optional Biplot vector arrows demonstrating accord orientation
    if show_vectors:
        # Scale loading vectors to make them visible on the scatter scale
        scale_factor = max(df_pca["PC1"].abs().max(), df_pca["PC2"].abs().max()) * 0.8
        for i, accord in enumerate(accord_dimensions):
            vec_x = loadings[i, 0] * scale_factor
            vec_y = loadings[i, 1] * scale_factor

            fig.add_shape(
                type="line",
                x0=0, y0=0, x1=vec_x, y1=vec_y,
                line=dict(color="rgba(255, 215, 0, 0.6)", width=2, dash="dash")
            )
            fig.add_annotation(
                x=vec_x, y=vec_y,
                text=accord,
                showarrow=False,
                font=dict(color="#ffd700", size=11, family="monospace"),
                xanchor="center", yanchor="bottom"
            )

    fig.add_hline(y=0, line_dash="dot", line_color="rgba(128, 128, 128, 0.3)")
    fig.add_vline(x=0, line_dash="dot", line_color="rgba(128, 128, 128, 0.3)")

    fig.update_layout(
        xaxis_title=f"Principal Component 1 ({var_pc1}% variance)",
        yaxis_title=f"Principal Component 2 ({var_pc2}% variance)",
        height=520,
        margin=dict(l=60, r=40, t=60, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=-0.22, xanchor="center", x=0.5)
    )

    summary_md = f"""
    ### 🧭 Interpreting the PCA Scent Space
    * **PC1 ({var_pc1}% variance):** Separates **Citrus & Fresh** scents on one side from **Gourmand & Sweet** scents on the opposite side.
    * **PC2 ({var_pc2}% variance):** Differentiates **Aromatic / Fresh Spicy** profiles from deep **Woody & Smoky** signatures.
    * **Cluster Proximity:** Fragrances that sit near each other in this 2D plane share similar chemical accord ratios regardless of marketing terms.
    """

    out_cols = ["Perfume Name", "Brand", "Main Accords", "Rating", "Sillage", "PC1", "PC2"]
    return fig, summary_md, df_pca[out_cols].round(2)


# 3. CUSTOM SYNTHESIZER MATCHING ENGINE
def synthesize_custom_scent(woody, citrus, sweet, spicy, aromatic, smoky, top_k):
    custom_vec = np.array([woody, citrus, sweet, spicy, aromatic, smoky], dtype=float)
    custom_norm = np.linalg.norm(custom_vec)

    if custom_norm == 0:
        empty_fig = px.bar(title="Adjust at least one accord slider above zero.")
        empty_fig.update_layout(template="plotly_dark")
        return empty_fig, "### ⚠️ Please increase at least one slider to create a scent profile.", pd.DataFrame()

    candidate_matrix = df_perfumes[accord_dimensions].values.astype(float)
    candidate_norms = np.linalg.norm(candidate_matrix, axis=1)

    dot_products = np.dot(candidate_matrix, custom_vec)
    cosine_sims = dot_products / (candidate_norms * custom_norm)

    matched_df = df_perfumes.copy()
    matched_df["Match Score (%)"] = (cosine_sims * 100).round(1)
    results = matched_df.sort_values(by="Match Score (%)", ascending=False).head(int(top_k))

    top_match = results.iloc[0]
    top_name = top_match["Perfume Name"]

    radar_cats = accord_dimensions + [accord_dimensions[0]]
    custom_closed = custom_vec.tolist() + [custom_vec[0]]
    match_closed = [top_match[acc] for acc in accord_dimensions] + [top_match[accord_dimensions[0]]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=custom_closed,
        theta=radar_cats,
        fill="toself",
        name="Your Custom Formula",
        line=dict(color="#f72585", width=2.5),
        fillcolor="rgba(247, 37, 133, 0.25)"
    ))
    fig.add_trace(go.Scatterpolar(
        r=match_closed,
        theta=radar_cats,
        fill="toself",
        name=f"Closest: {top_name} ({top_match['Match Score (%)']}%)",
        line=dict(color="#4cc9f0", width=2.5),
        fillcolor="rgba(76, 201, 240, 0.25)"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#777"),
            bgcolor="rgba(0,0,0,0)"
        ),
        template="plotly_dark",
        margin=dict(l=60, r=60, t=50, b=40),
        height=380,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )

    summary_md = f"""
    ### 🏆 Closest Market Alternative: **{top_name}** by {top_match['Brand']}
    * **Accord Match:** `{top_match['Match Score (%)']}%` vector alignment
    * **Community Rating:** ⭐ {top_match['Rating']} / 5.0
    * **Projection Class:** 💨 {top_match['Sillage']}
    * **Primary Market Classification:** {top_match['Main Accords']}
    """

    display_cols = ["Perfume Name", "Brand", "Match Score (%)", "Rating", "Sillage", "Main Accords", "Age_Group_Score"]
    return fig, summary_md, results[display_cols]


# 4. SCENT-TWIN VECTOR ENGINE
def find_scent_twins(target_name, top_k):
    target_row = df_perfumes[df_perfumes["Perfume Name"] == target_name].iloc[0]
    target_vec = target_row[accord_dimensions].values.astype(float)
    target_norm = np.linalg.norm(target_vec)

    candidates = df_perfumes[df_perfumes["Perfume Name"] != target_name].copy()
    candidate_matrix = candidates[accord_dimensions].values.astype(float)
    candidate_norms = np.linalg.norm(candidate_matrix, axis=1)

    dot_products = np.dot(candidate_matrix, target_vec)
    cosine_sims = dot_products / (candidate_norms * target_norm)

    candidates["Match Score (%)"] = (cosine_sims * 100).round(1)
    results = candidates.sort_values(by="Match Score (%)", ascending=False).head(int(top_k))

    best_match_row = results.iloc[0]
    best_name = best_match_row["Perfume Name"]

    radar_cats = accord_dimensions + [accord_dimensions[0]]
    t_vals = [target_row[acc] for acc in accord_dimensions] + [target_row[accord_dimensions[0]]]
    m_vals = [best_match_row[acc] for acc in accord_dimensions] + [best_match_row[accord_dimensions[0]]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=t_vals,
        theta=radar_cats,
        fill="toself",
        name=f"Source: {target_name}",
        line=dict(color="#00f2fe", width=2.5),
        fillcolor="rgba(0, 242, 254, 0.2)"
    ))
    fig.add_trace(go.Scatterpolar(
        r=m_vals,
        theta=radar_cats,
        fill="toself",
        name=f"Top Twin: {best_name} ({best_match_row['Match Score (%)']}%)",
        line=dict(color="#39ff14", width=2.5),
        fillcolor="rgba(57, 255, 20, 0.2)"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#777"),
            bgcolor="rgba(0,0,0,0)"
        ),
        template="plotly_dark",
        margin=dict(l=60, r=60, t=50, b=40),
        height=380,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )

    summary_md = f"""
    ### 🎯 Top Olfactory Twin: **{best_name}**
    * **Olfactory Similarity:** `{best_match_row['Match Score (%)']}%` overlap
    * **Brand Comparison:** {target_row['Brand']} vs. {best_match_row['Brand']}
    * **Rating Variance:** ⭐ {target_row['Rating']} vs. ⭐ {best_match_row['Rating']}
    * **Projection Match:** {target_row['Sillage']} vs. {best_match_row['Sillage']}
    """

    out_cols = ["Perfume Name", "Brand", "Match Score (%)", "Rating", "Sillage", "Main Accords"]
    return fig, summary_md, results[out_cols]


# 5. RADAR COMPARISON DUEL
def generate_radar_duel(name_a, name_b):
    row_a = df_perfumes[df_perfumes["Perfume Name"] == name_a].iloc[0]
    row_b = df_perfumes[df_perfumes["Perfume Name"] == name_b].iloc[0]

    vals_a = [row_a[acc] for acc in accord_dimensions] + [row_a[accord_dimensions[0]]]
    vals_b = [row_b[acc] for acc in accord_dimensions] + [row_b[accord_dimensions[0]]]
    radar_categories = accord_dimensions + [accord_dimensions[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vals_a,
        theta=radar_categories,
        fill="toself",
        name=f"{name_a} ({row_a['Brand']})",
        line=dict(color="#00f2fe", width=2.5),
        fillcolor="rgba(0, 242, 254, 0.2)"
    ))
    fig.add_trace(go.Scatterpolar(
        r=vals_b,
        theta=radar_categories,
        fill="toself",
        name=f"{name_b} ({row_b['Brand']})",
        line=dict(color="#ff0844", width=2.5),
        fillcolor="rgba(255, 8, 68, 0.2)"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#777"),
            bgcolor="rgba(0,0,0,0)"
        ),
        template="plotly_dark",
        margin=dict(l=60, r=60, t=50, b=40),
        height=380,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )

    stats_md = f"""
    | Spec Metric | **{name_a}** | **{name_b}** |
    | :--- | :---: | :---: |
    | **Brand** | {row_a['Brand']} | {row_b['Brand']} |
    | **Release Year** | {row_a['Release Year']} | {row_b['Release Year']} |
    | **Community Rating** | ⭐ {row_a['Rating']} | ⭐ {row_b['Rating']} |
    | **Sillage Projection** | 💨 {row_a['Sillage']} | 💨 {row_b['Sillage']} |
    | **Youth Appeal (18–24)** | 🔥 {row_a['Age_Group_Score']}/100 | 🔥 {row_b['Age_Group_Score']}/100 |
    """

    return fig, stats_md


# 6. FILTERING & LEADERBOARD LOGIC
def filter_and_plot(min_year, max_year, selected_accord, min_rating):
    low_year = min(min_year, max_year)
    high_year = max(min_year, max_year)

    filtered = df_perfumes[
        (df_perfumes["Release Year"] >= low_year)
        & (df_perfumes["Release Year"] <= high_year)
        & (df_perfumes["Rating"] >= min_rating)
    ]

    if selected_accord != "All":
        filtered = filtered[filtered["Main Accords"] == selected_accord]

    filtered = filtered.sort_values(by="Age_Group_Score", ascending=False).head(20)

    if not filtered.empty:
        fig = px.bar(
            filtered,
            x="Age_Group_Score",
            y="Perfume Name",
            color="Brand",
            orientation="h",
            hover_data=["Rating", "Sillage", "Release Year", "Main Accords"],
            template="plotly_dark",
        )

        fig.update_layout(
            yaxis={"categoryorder": "total ascending", "tickfont": {"size": 11}},
            xaxis_title="Age Group Score (18–24)",
            yaxis_title="",
            margin=dict(l=170, r=160, t=30, b=40),
            height=max(400, len(filtered) * 28 + 80),
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.02,
                title={"text": "Brand"},
            ),
        )
    else:
        fig = px.bar(title="No perfumes match the selected criteria.")
        fig.update_layout(
            template="plotly_dark",
            xaxis={"visible": False},
            yaxis={"visible": False},
            annotations=[{
                "text": "No matching records found. Adjust your filters.",
                "xref": "paper", "yref": "paper", "showarrow": False,
                "font": {"size": 14, "color": "gray"},
            }],
        )

    table_columns = ["Perfume Name", "Brand", "Release Year", "Rating", "Sillage", "Main Accords", "Age_Group_Score"]
    return fig, filtered[table_columns]


# 7. GRADIO APPLICATION LAYOUT
with gr.Blocks(title="Fragrance Analytics Intelligence") as demo:
    gr.Markdown("# 🧴 Fragrance Intelligence & Olfactory Analysis Platform")

    with gr.Tabs():
        # TAB 1: MARKET EXPLORER
        with gr.TabItem("📊 Market Leaderboard & Filters"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Filter Controls")
                    with gr.Row():
                        min_year_slider = gr.Slider(2016, 2026, value=2016, step=1, label="From Year")
                        max_year_slider = gr.Slider(2016, 2026, value=2026, step=1, label="To Year")

                    accord_dropdown = gr.Dropdown(choices=accord_options, value="All", label="Main Accords")
                    rating_slider = gr.Slider(1.0, 5.0, value=3.8, step=0.1, label="Minimum Rating")

                with gr.Column(scale=2):
                    gr.Markdown("### Demographic Leaderboard")
                    chart_output = gr.Plot(show_label=False)
                    table_output = gr.DataFrame(interactive=False, wrap=True)

        # TAB 2: 2D PCA OLFACTORY CLUSTER MAP
        with gr.TabItem("🗺️ 2D PCA Olfactory Space"):
            gr.Markdown("Dimensionality reduction projecting 6-dimensional olfactory accord vectors onto a 2D plane to uncover macro scent families and clusters.")
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### ⚙️ Projection Settings")
                    vector_toggle = gr.Checkbox(value=True, label="Show Accord Vector Axes (Biplot)")
                    pca_summary_md = gr.Markdown()

                with gr.Column(scale=2):
                    pca_scatter_plot = gr.Plot(show_label=False)
                    pca_table_output = gr.DataFrame(interactive=False, wrap=True)

        # TAB 3: CUSTOM SCENT SYNTHESIZER
        with gr.TabItem("🧪 Custom Scent Synthesizer"):
            gr.Markdown("Mix your ideal olfactory formula by adjusting accord intensities to find commercial perfumes matching your custom profile.")
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### 🎛️ Accord Formula Blender")
                    synth_woody = gr.Slider(0, 100, value=85, step=5, label="Woody")
                    synth_citrus = gr.Slider(0, 100, value=20, step=5, label="Citrus")
                    synth_sweet = gr.Slider(0, 100, value=40, step=5, label="Sweet / Gourmand")
                    synth_spicy = gr.Slider(0, 100, value=75, step=5, label="Spicy")
                    synth_aromatic = gr.Slider(0, 100, value=60, step=5, label="Aromatic / Herbal")
                    synth_smoky = gr.Slider(0, 100, value=70, step=5, label="Smoky / Leather")
                    synth_top_k = gr.Slider(1, 5, value=3, step=1, label="Max Results Returned")

                with gr.Column(scale=2):
                    gr.Markdown("### 📡 Olfactory Footprint Match")
                    synth_summary_md = gr.Markdown()
                    synth_radar_plot = gr.Plot(show_label=False)
                    synth_table_output = gr.DataFrame(interactive=False, wrap=True)

        # TAB 4: SCENT-TWIN VECTOR ENGINE
        with gr.TabItem("🧬 Scent-Twin Vector Engine"):
            gr.Markdown("Identify direct market alternatives using cosine similarity across normalized 6D olfactory accord coordinates.")
            with gr.Row():
                with gr.Column(scale=1):
                    target_fragrance = gr.Dropdown(
                        choices=all_perfume_names,
                        value="Sauvage Elixir",
                        label="Select Anchor Fragrance"
                    )
                    top_k_slider = gr.Slider(1, 5, value=3, step=1, label="Number of Scent Twins")
                    twin_summary_md = gr.Markdown()

                with gr.Column(scale=2):
                    twin_radar_plot = gr.Plot(show_label=False)
                    twin_table_output = gr.DataFrame(interactive=False, wrap=True)

        # TAB 5: OLFACTORY RADAR DUEL
        with gr.TabItem("⚔️ Olfactory Duel & Radar Analysis"):
            gr.Markdown("Compare the 6-axis accord footprint and metrics of any two fragrances side-by-side.")
            with gr.Row():
                with gr.Column():
                    fragrance_a = gr.Dropdown(choices=all_perfume_names, value="Sauvage Elixir", label="Challenger A")
                with gr.Column():
                    fragrance_b = gr.Dropdown(choices=all_perfume_names, value="Bleu de Chanel Parfum", label="Challenger B")

            with gr.Row():
                with gr.Column(scale=3):
                    radar_chart = gr.Plot(show_label=False)
                with gr.Column(scale=2):
                    duel_stats = gr.Markdown()

    # Event Bindings for Tab 1 (Leaderboard)
    filter_inputs = [min_year_slider, max_year_slider, accord_dropdown, rating_slider]
    filter_outputs = [chart_output, table_output]
    for ctrl in filter_inputs:
        ctrl.change(fn=filter_and_plot, inputs=filter_inputs, outputs=filter_outputs)

    # Event Bindings for Tab 2 (PCA Cluster Map)
    vector_toggle.change(
        fn=generate_pca_cluster_map,
        inputs=[vector_toggle],
        outputs=[pca_scatter_plot, pca_summary_md, pca_table_output]
    )

    # Event Bindings for Tab 3 (Synthesizer)
    synth_inputs = [
        synth_woody, synth_citrus, synth_sweet,
        synth_spicy, synth_aromatic, synth_smoky,
        synth_top_k
    ]
    synth_outputs = [synth_radar_plot, synth_summary_md, synth_table_output]
    for slider in synth_inputs:
        slider.change(fn=synthesize_custom_scent, inputs=synth_inputs, outputs=synth_outputs)

    # Event Bindings for Tab 4 (Scent-Twin Engine)
    twin_inputs = [target_fragrance, top_k_slider]
    twin_outputs = [twin_radar_plot, twin_summary_md, twin_table_output]
    target_fragrance.change(fn=find_scent_twins, inputs=twin_inputs, outputs=twin_outputs)
    top_k_slider.change(fn=find_scent_twins, inputs=twin_inputs, outputs=twin_outputs)

    # Event Bindings for Tab 5 (Duel)
    duel_inputs = [fragrance_a, fragrance_b]
    duel_outputs = [radar_chart, duel_stats]
    fragrance_a.change(fn=generate_radar_duel, inputs=duel_inputs, outputs=duel_outputs)
    fragrance_b.change(fn=generate_radar_duel, inputs=duel_inputs, outputs=duel_outputs)

    # Global Startup Loaders
    demo.load(fn=filter_and_plot, inputs=filter_inputs, outputs=filter_outputs)
    demo.load(fn=generate_pca_cluster_map, inputs=[vector_toggle], outputs=[pca_scatter_plot, pca_summary_md, pca_table_output])
    demo.load(fn=synthesize_custom_scent, inputs=synth_inputs, outputs=synth_outputs)
    demo.load(fn=find_scent_twins, inputs=twin_inputs, outputs=twin_outputs)
    demo.load(fn=generate_radar_duel, inputs=duel_inputs, outputs=duel_outputs)

if __name__ == "__main__":
    demo.launch()