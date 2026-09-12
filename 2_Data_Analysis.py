import streamlit as st
import pandas as pd

st.title("IPL Data Analysis")

# Load dataset
df = pd.read_csv("IPL_2008_2026_Merged.csv")

# Create calculations
df["total_runs"] = df["team1_runs"] + df["team2_runs"]
df["total_wickets"] = df["team1_wickets"] + df["team2_wickets"]

# KPI Section
st.subheader("Key Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Matches", len(df))

with col2:
    st.metric("Total Seasons", df["season"].nunique())

with col3:
    st.metric("Total Venues", df["venue"].nunique())

with col4:
    st.metric("Average Runs", round(df["total_runs"].mean(), 2))

# Calculations
st.subheader("Match Calculations")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Match Runs", int(df["total_runs"].sum()))

with col2:
    st.metric("Total Wickets", int(df["total_wickets"].sum()))

with col3:
    st.metric("Highest Combined Score", int(df["total_runs"].max()))

# Filters
st.subheader("Filters")

seasons = sorted(df["season"].dropna().unique())

selected_season = st.selectbox(
    "Select Season",
    seasons
)

teams = sorted(
    pd.concat([
        df["team1"],
        df["team2"]
    ]).dropna().unique()
)

selected_team = st.selectbox(
    "Select Team",
    teams
)

# Apply filters
filtered_df = df[
    (df["season"] == selected_season) &
    (
        (df["team1"] == selected_team) |
        (df["team2"] == selected_team)
    )
]

# Display filtered data
st.subheader(
    f"Matches for {selected_team} - Season {selected_season}"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Missing values
st.subheader("Missing Values")

missing_values = df.isnull().sum()

st.dataframe(missing_values)

# Complete dataset
with st.expander("View Complete Dataset"):
    st.dataframe(
        df,
        use_container_width=True
    )