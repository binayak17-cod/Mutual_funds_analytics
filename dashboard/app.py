import os
import glob
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Mutual Funds Analytics & Insights",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Custom CSS for modern design and glassmorphism styling
st.markdown("""
<style>
    /* Main body background & font family */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Metrics block styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(255, 255, 255, 0.2);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.25);
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #88888b;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff;
        margin-top: 5px;
    }
    
    .metric-delta {
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 5px;
    }
    
    .metric-delta.positive {
        color: #00fa9a;
    }
    
    .metric-delta.negative {
        color: #ff4d4d;
    }
    
    /* Header decoration */
    .header-container {
        padding: 30px;
        background: linear-gradient(135deg, #1f1f2e 0%, #111119 100%);
        border-radius: 16px;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)


def calculate_metrics(df: pd.DataFrame) -> dict:
    """Calculate key financial metrics for a given scheme dataframe."""
    metrics = {}
    if df.empty:
        return metrics
    
    # Sort chronologically just in case
    df = df.sort_values("Date").reset_index(drop=True)
    
    # General values
    initial_nav = df["NAV"].iloc[0]
    latest_nav = df["NAV"].iloc[-1]
    metrics["latest_nav"] = latest_nav
    metrics["latest_date"] = df["Date"].iloc[-1].strftime("%Y-%m-%d")
    
    # Simple Total Return
    total_return = (latest_nav - initial_nav) / initial_nav
    metrics["total_return"] = total_return
    
    # CAGR
    days = (df["Date"].iloc[-1] - df["Date"].iloc[0]).days
    if days > 365:
        years = days / 365.25
        cagr = (latest_nav / initial_nav) ** (1 / years) - 1
    else:
        # Annualized simple return if less than a year
        cagr = total_return * (365.25 / max(days, 1))
    metrics["cagr"] = cagr
    
    # Standard deviation of daily returns (annualized)
    daily_returns = df["Daily_Return"].dropna()
    ann_vol = daily_returns.std() * np.sqrt(252) if len(daily_returns) > 1 else 0.0
    metrics["annualized_volatility"] = ann_vol
    
    # Sharpe Ratio (assuming risk free rate of 6% or 0.06 annualized)
    rf_daily = (1 + 0.06) ** (1 / 252) - 1
    excess_returns = daily_returns - rf_daily
    if len(daily_returns) > 1 and excess_returns.std() > 0:
        sharpe = (excess_returns.mean() / excess_returns.std()) * np.sqrt(252)
    else:
        sharpe = 0.0
    metrics["sharpe_ratio"] = sharpe
    
    # Max Drawdown
    peak = df["NAV"].cummax()
    drawdown = (df["NAV"] - peak) / peak
    metrics["max_drawdown"] = drawdown.min()
    
    return metrics


# Sidebar and Ingestion instructions
st.sidebar.title("📊 Control Panel")
st.sidebar.markdown("Configure and analyze mutual fund performances.")

# Load processed data
processed_files = glob.glob(os.path.join("data", "processed", "scheme_*_processed.csv"))
scheme_dict = {}

for fp in processed_files:
    try:
        temp_df = pd.read_csv(fp)
        if not temp_df.empty:
            temp_df["Date"] = pd.to_datetime(temp_df["Date"])
            scheme_code = temp_df["Scheme_Code"].iloc[0]
            scheme_name = temp_df["Scheme_Name"].iloc[0]
            scheme_dict[f"{scheme_name} ({scheme_code})"] = temp_df
    except Exception as e:
        pass

# Header Section
st.markdown("""
    <div class="header-container">
        <h1 style="margin:0; font-weight:800; background: linear-gradient(90deg, #a8ff78, #78ffd6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Mutual Funds Analytics Dashboard
        </h1>
        <p style="color:#88888b; font-size:1.1rem; margin:10px 0 0 0;">
            Explore live Net Asset Value (NAV) trends, performance metrics, and volatility analysis.
        </p>
    </div>
""", unsafe_allow_html=True)

if not scheme_dict:
    st.warning("⚠️ No processed mutual fund data found in **data/processed/**.")
    
    st.markdown("""
    ### Get Started & Ingest Data
    To fetch live data, run the following commands in your terminal:
    
    ```bash
    # 1. Install dependencies
    pip install -r requirements.txt
    
    # 2. Search for a fund to get its code
    python live_nav_fetch.py --search "Parag Parikh Flexi Cap"
    
    # 3. Fetch and save raw data (e.g. scheme code 122639)
    python live_nav_fetch.py --code 122639 --save
    
    # 4. Ingest and process raw data
    python data_ingestion.py
    ```
    """)
    
    # Add dummy/preview database display if empty
    st.info("💡 A demo view will appear here once data has been ingested.")
else:
    selected_scheme_name = st.sidebar.selectbox("Select Mutual Fund Scheme", list(scheme_dict.keys()))
    df = scheme_dict[selected_scheme_name]
    
    # Calculate performance metrics
    metrics = calculate_metrics(df)
    
    # Display KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Latest NAV ({metrics.get('latest_date')})</div>
                <div class="metric-value">₹ {metrics.get('latest_nav'):,.2f}</div>
                <div class="metric-delta positive">Live Fetch Active</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        cagr_val = metrics.get('cagr', 0) * 100
        delta_class = "positive" if cagr_val >= 0 else "negative"
        sign = "+" if cagr_val >= 0 else ""
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">CAGR / Annualized Return</div>
                <div class="metric-value">{sign}{cagr_val:.2f}%</div>
                <div class="metric-delta {delta_class}">Annualized</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        vol_val = metrics.get('annualized_volatility', 0) * 100
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Annual Volatility (30d)</div>
                <div class="metric-value">{vol_val:.2f}%</div>
                <div class="metric-delta">Risk Metric</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col4:
        dd_val = metrics.get('max_drawdown', 0) * 100
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Max Drawdown</div>
                <div class="metric-value">{dd_val:.2f}%</div>
                <div class="metric-delta negative">Peak-to-Trough Decline</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main Tabs
    tab1, tab2, tab3 = st.tabs(["📈 NAV & MA Trends", "📊 Returns & Volatility Analysis", "📁 Processed Dataset View"])
    
    with tab1:
        st.subheader("NAV Performance & Simple Moving Averages")
        # Line chart of NAV, 30d, and 90d MAs
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Date"], y=df["NAV"], name="NAV", line=dict(color="#00fa9a", width=2)))
        fig.add_trace(go.Scatter(x=df["Date"], y=df["Rolling_30_NAV"], name="30d Moving Avg", line=dict(color="#ff9900", width=1.5, dash="dash")))
        fig.add_trace(go.Scatter(x=df["Date"], y=df["Rolling_90_NAV"], name="90d Moving Avg", line=dict(color="#00bfff", width=1.5, dash="dot")))
        
        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Date",
            yaxis_title="NAV (INR)",
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
            margin=dict(l=20, r=20, t=30, b=20),
            height=500,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with tab2:
        st.subheader("Risk & Returns Analysis")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.markdown("**Daily Returns Distribution**")
            fig_hist = px.histogram(
                df, x="Daily_Return", nbins=100, 
                color_discrete_sequence=["#78ffd6"]
            )
            fig_hist.update_layout(
                template="plotly_dark",
                xaxis_title="Daily Return",
                yaxis_title="Frequency",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_hist, use_container_width=True)
            
        with col_chart2:
            st.markdown("**Annualized Rolling 30-Day Volatility Timeline**")
            fig_vol = px.line(
                df, x="Date", y="Rolling_Volatility_30d",
                color_discrete_sequence=["#ff4d4d"]
            )
            fig_vol.update_layout(
                template="plotly_dark",
                xaxis_title="Date",
                yaxis_title="Annualized Volatility",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_vol, use_container_width=True)
            
    with tab3:
        st.subheader("Data Inspector")
        st.dataframe(df, use_container_width=True)
        
# Add Footer branding
st.markdown("""
<div style="text-align:center; padding:20px; color:#55555c; font-size:0.85rem; border-top:1px solid rgba(255,255,255,0.05); margin-top:50px;">
    Mutual Funds Analytics Pipeline • Built with Streamlit, Pandas & Plotly
</div>
""", unsafe_allow_html=True)
