import pandas as pd


def answer_question(question: str, df: pd.DataFrame) -> str:
    q = question.lower().strip()

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

    if "revenue" in q or "sales" in q:
        return (
            f"Revenue in {latest['month']} was ₹{latest['revenue']:,.0f}, "
            f"down {abs(revenue_change):.1f}% from {previous['month']}. "
            "This indicates a recent deterioration in business performance. "
            "NEXORA recommends investigating product performance, "
            "customer activity and marketing effectiveness."
        )

    if "order" in q:
        return (
            f"Orders fell from {previous['orders']:,} in {previous['month']} "
            f"to {latest['orders']:,} in {latest['month']}, "
            f"a decline of {abs(orders_change):.1f}%. "
            "The decline in orders is a major contributor to the revenue drop."
        )

    if "customer" in q:
        return (
            f"Customer count decreased from {previous['customers']:,} "
            f"to {latest['customers']:,}. "
            "This suggests reduced customer activity and should be investigated "
            "alongside order frequency and retention."
        )

    if "why" in q or "problem" in q or "issue" in q:
        return (
            f"The most significant recent issue is declining demand. "
            f"Revenue decreased {abs(revenue_change):.1f}% and orders decreased "
            f"{abs(orders_change):.1f}% in the latest period. "
            "NEXORA recommends investigating customer behavior, "
            "product performance and marketing effectiveness."
        )

    if "recommend" in q or "should" in q or "action" in q:
        return (
            "NEXORA recommends prioritizing root-cause analysis of the revenue "
            "decline. Compare product-level sales, customer activity and "
            "marketing performance before making major business decisions."
        )

    return (
        "Based on the latest data, NEXORA detected declining revenue and orders. "
        "Try asking: 'Why is revenue declining?', "
        "'What happened to orders?', or 'What should we do?'"
    )