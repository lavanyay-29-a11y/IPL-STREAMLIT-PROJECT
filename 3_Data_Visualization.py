import streamlit as st
import pandas as pd
import plotly.express as px

st.title("IPL Data Visualization")

# Load dataset
df = pd.read_csv("IPL_2008_2026_Merged.csv")

# Calculate total runs
df["total_runs"] = df["team1_runs"] + df["team2_runs"]

# Sidebar filter
st.sidebar.title("Filters")

selected_season = st.sidebar.selectbox(
    "Select Season",
    sorted(df["season"].dropna().unique())
)

# Filter data
filtered_df = df[
    df["season"] == selected_season
]

st.subheader(
    f"Analysis for Season: {selected_season}"
)

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Matches", len(filtered_df))

with col2:
    st.metric(
        "Average Runs",
        round(filtered_df["total_runs"].mean(), 2)
    )

with col3:
    st.metric(
        "Highest Score",
        int(filtered_df["total_runs"].max())
    )

# Winning Teams
team_wins = (
    filtered_df["winner"]
    .value_counts()
    .reset_index()
)

team_wins.columns = ["Team", "Wins"]

fig1 = px.bar(
    team_wins.head(10),
    x="Team",
    y="Wins",
    title="Winning Teams"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Match Run Distribution
fig2 = px.histogram(
    filtered_df,
    x="total_runs",
    nbins=20,
    title="Match Run Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Toss Decision Pie Chart
toss_decision = (
    filtered_df["toss_decision"]
    .value_counts()
    .reset_index()
)

toss_decision.columns = ["Decision", "Count"]

fig3 = px.pie(
    toss_decision,
    names="Decision",
    values="Count",
    title="Toss Decision Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Scatter Plot
fig4 = px.scatter(
    filtered_df,
    x="team1_runs",
    y="team2_runs",
    title="Team 1 Runs vs Team 2 Runs"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# Detailed Data
with st.expander("View Detailed Match Data"):
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# Season-wise Total Runs

season_runs = (
    df.groupby("season")["total_runs"]
    .sum()
    .reset_index()
)

fig_line = px.line(
    season_runs,
    x="season",
    y="total_runs",
    markers=True,
    title="Season-wise Total Runs"
)

st.plotly_chart(
    fig_line,
    use_container_width=True
)