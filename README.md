# NEXORA

## AI Decision Intelligence Copilot

**From Data to Decisions.**

NEXORA is an AI-powered Decision Intelligence Copilot that helps businesses understand their data, identify important trends, and turn those insights into actionable decisions.

## 🚀 Problem

Businesses often have large amounts of sales data but struggle to quickly understand:

- Why revenue is changing
- Why orders are increasing or decreasing
- What business problems need attention
- What actions should be prioritized

NEXORA addresses this by combining data analytics with AI-powered business insights.

## 💡 Solution

NEXORA analyzes business data and provides:

- Revenue and order trends
- Customer activity insights
- Key performance indicators
- Automated issue detection
- Decision-oriented recommendations
- Natural-language business questions and answers

## 🏗️ Architecture

Business Data
↓
Exasol Database
↓
Analytics Engine
↓
NEXORA AI Engine
↓
Decision Intelligence
↓
Streamlit Dashboard

## 🛠️ Technology Stack

- Python
- Streamlit
- Pandas
- Exasol Personal
- PyExasol
- SQL

## 📊 Demo

The current demonstration dataset contains monthly business data including:

- Revenue
- Orders
- Customers
- Marketing Spend

NEXORA automatically detects important changes and generates recommendations.

## 🤖 Example Questions

You can ask NEXORA:

- Why is revenue declining?
- What happened to orders?
- What should we do?

NEXORA analyzes the available business data and returns a decision-oriented response.

## 📁 Project Structure

```text
NEXORA/
├── app.py
├── ai_engine.py
├── analytics.py
├── database.py
├── config.py
├── requirements.txt
├── .env.example
├── data/
│   └── sample_sales.csv
└── sql/
    └── setup.sql

