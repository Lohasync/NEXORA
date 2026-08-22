import streamlit as st
import plotly.express as px

from database import load_data
from analytics import calculate_kpis, detect_trends, generate_insights
from ai_engine import answer_question

st.set_page_config(
    page_title="NEXORA",
    page_icon="🧠",
    layout="wide",
)


# ---------- LOAD DATA ----------

df = load_data()
kpis = calculate_kpis(df)
trends = detect_trends(df)
insights = generate_insights(df)


# ---------- HEADER ----------

st.title("🧠 NEXORA")
st.caption("AI Decision Intelligence Copilot — From Data to Decisions.")

st.divider()


# ---------- KPI CARDS ----------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Revenue",
        f"₹{kpis['revenue']:,.0f}",
    )

with col2:
    st.metric(
        "Total Orders",
        f"{kpis['orders']:,}",
    )

with col3:
    st.metric(
        "Customers",
        f"{kpis['customers']:,}",
    )

with col4:
    st.metric(
        "Avg. Order Value",
        f"₹{kpis['avg_order_value']:,.2f}",
    )


st.divider()


# ---------- BUSINESS OVERVIEW ----------

left, right = st.columns(2)

with left:
    st.subheader("📈 Revenue Trend")

    fig = px.line(
        df,
        x="month",
        y="revenue",
        markers=True,
        title="Monthly Revenue",
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


with right:
    st.subheader("📦 Orders Trend")

    fig = px.bar(
        df,
        x="month",
        y="orders",
        title="Monthly Orders",
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Orders",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# ---------- AI INSIGHTS ----------

st.divider()

st.header("🤖 NEXORA Intelligence")

st.write(
    "NEXORA analyzes the latest business data and identifies "
    "important changes that may require attention."
)

for insight in insights:
    st.warning("⚠️ " + insight)


# ---------- DECISION RECOMMENDATION ----------

st.subheader("💡 Recommended Action")

if trends["revenue_change"] < -5:

    st.info(
        """
        **Priority: Investigate the revenue decline**

        NEXORA recommends:
        - Analyze the products/categories driving the decline.
        - Review customer order frequency.
        - Compare marketing performance with previous months.
        - Identify whether the decline is temporary or structural.
        """
    )

else:

    st.success(
        """
        **Performance is stable**

        Continue monitoring revenue, orders and customer activity.
        """
    )

# ---------- AI COPILOT ----------

st.divider()

st.header("💬 Ask NEXORA")

st.write(
    "Ask a business question and NEXORA will analyze the available data "
    "and provide a decision-oriented answer."
)

question = st.text_input(
    "Your question",
    placeholder="Why is revenue declining?"
)

if st.button("🔍 Analyze", use_container_width=True):

    if question.strip():
        with st.spinner("NEXORA is analyzing the data..."):
            answer = answer_question(question, df)

        st.success(answer)

    else:
        st.warning("Please enter a question.")
# ---------- DATA EXPLORER ----------

st.divider()

st.subheader("🔎 Data Explorer")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
)   