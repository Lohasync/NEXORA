import pandas as pd


def calculate_kpis(df):
    revenue = df["revenue"].sum()
    orders = df["orders"].sum()
    customers = df["customers"].sum()

    avg_order_value = revenue / orders if orders else 0

    return {
        "revenue": revenue,
        "orders": orders,
        "customers": customers,
        "avg_order_value": avg_order_value,
    }


def detect_trends(df):
    if len(df) < 2:
        return {}

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    revenue_change = (
        (latest["revenue"] - previous["revenue"])
        / previous["revenue"]
        * 100
    )

    orders_change = (
        (latest["orders"] - previous["orders"])
        / previous["orders"]
        * 100
    )

    return {
        "revenue_change": revenue_change,
        "orders_change": orders_change,
    }


def generate_insights(df):
    trends = detect_trends(df)

    insights = []

    if trends["revenue_change"] < -5:
        insights.append(
            f"Revenue declined {abs(trends['revenue_change']):.1f}% "
            "in the latest period."
        )

    if trends["orders_change"] < -5:
        insights.append(
            f"Orders declined {abs(trends['orders_change']):.1f}% "
            "in the latest period."
        )

    if not insights:
        insights.append("Business performance is relatively stable.")

    return insights