import gradio as gr
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


# 2. RADAR COMPARISON GENERATOR
def generate_radar_duel(name_a, name_b):
    row_a = df_perfumes[df_perfumes["Perfume Name"] == name_a].iloc[0]
    row_b = df_perfumes[df_perfumes["Perfume Name"] == name_b].iloc[0]

    vals_a = [row_a[acc] for acc in accord_dimensions]
    vals_b = [row_b[acc] for acc in accord_dimensions]

    # Close the radar loop
    radar_categories = accord_dimensions + [accord_dimensions[0]]
    vals_a_closed = vals_a + [vals_a[0]]
    vals_b_closed = vals_b + [vals_b[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=vals_a_closed,
        theta=radar_categories,
        fill="toself",
        name=f"{name_a} ({row_a['Brand']})",
        line=dict(color="#00f2fe", width=2.5),
        fillcolor="rgba(0, 242, 254, 0.2)"
    ))

    fig.add_trace(go.Scatterpolar(
        r=vals_b_closed,
        theta=radar_categories,
        fill="toself",
        name=f"{name_b} ({row_b['Brand']})",
        line=dict(color="#ff0844", width=2.5),
        fillcolor="rgba(255, 8, 68, 0.2)"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#888"),
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


# 3. FILTERING & LEADERBOARD LOGIC
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

    # Return filtered table columns (omitting individual accord scores for clean display)
    table_columns = ["Perfume Name", "Brand", "Release Year", "Rating", "Sillage", "Main Accords", "Age_Group_Score"]
    return fig, filtered[table_columns]


# 4. GRADIO INTERFACE (Tabbed Architecture)
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

        # TAB 2: SIDE-BY-SIDE OLFACTORY RADAR DUEL
        with gr.TabItem("⚔️ Olfactory Duel & Radar Analysis"):
            gr.Markdown("Select two fragrances to compare their 6-axis olfactory accord footprint, demographic appeal, and projection side-by-side.")
            with gr.Row():
                with gr.Column():
                    fragrance_a = gr.Dropdown(choices=all_perfume_names, value="Sauvage Elixir", label="Fragrance Challenger A")
                with gr.Column():
                    fragrance_b = gr.Dropdown(choices=all_perfume_names, value="Bleu de Chanel Parfum", label="Fragrance Challenger B")

            with gr.Row():
                with gr.Column(scale=3):
                    radar_chart = gr.Plot(show_label=False)
                with gr.Column(scale=2):
                    duel_stats = gr.Markdown()

    # Event Bindings for Tab 1
    filter_inputs = [min_year_slider, max_year_slider, accord_dropdown, rating_slider]
    filter_outputs = [chart_output, table_output]

    for ctrl in filter_inputs:
        ctrl.change(fn=filter_and_plot, inputs=filter_inputs, outputs=filter_outputs)

    # Event Bindings for Tab 2
    duel_inputs = [fragrance_a, fragrance_b]
    duel_outputs = [radar_chart, duel_stats]

    fragrance_a.change(fn=generate_radar_duel, inputs=duel_inputs, outputs=duel_outputs)
    fragrance_b.change(fn=generate_radar_duel, inputs=duel_inputs, outputs=duel_outputs)

    # Global Load Initializer
    demo.load(fn=filter_and_plot, inputs=filter_inputs, outputs=filter_outputs)
    demo.load(fn=generate_radar_duel, inputs=duel_inputs, outputs=duel_outputs)

if __name__ == "__main__":
    demo.launch()