
# 📈 Stock Portfolio Performance Tracker

## 📌 About the Project

The Stock Portfolio Performance Tracker is a Python-based web application developed to track stock investments and analyze portfolio performance.

It helps users calculate their total investment, current market value, profit or loss, and profit/loss percentage.

The application uses the S&P 500 company dataset and retrieves the latest available stock prices using Yahoo Finance.

## 🎯 Project Objective

The main objective of this project is to develop an application that helps users monitor their stock investments and understand their portfolio performance.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- yfinance
- CSV
- Jupyter Notebook

## ✨ Features

- S&P 500 stock selection
- Stock price retrieval
- Buy price and quantity input
- Investment amount calculation
- Current market value calculation
- Profit and loss calculation
- Total portfolio performance
- Portfolio performance chart
- CSV report download

## 📂 Project Structure

```text
Stock_Portfolio_Tracker/
│
├── app.py
├── constituents.csv
├── requirements.txt
├── Stock_Portfolio_Tracker.ipynb
└── README.md
```

## 📊 Calculations

**Investment Amount**

Buy Price × Quantity

**Market Value**

Current Price × Quantity

**Profit or Loss**

Market Value − Investment Amount

**Profit or Loss Percentage**

(Profit or Loss / Investment Amount) × 100

## 🚀 Installation and Execution

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd stock-portfolio-performance-tracker
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
streamlit run app.py
```

## 📁 Dataset

The project uses the S&P 500 company constituents dataset (`constituents.csv`) to identify company names and ticker symbols.

## 📌 Output

The application displays individual stock performance, total portfolio investment, current market value, and profit or loss.

Users can also download their portfolio report in CSV format.

## 👩‍💻 Author

BTech Computer Science Engineering Student

## ⚠️ Disclaimer

This project is developed for educational and internship purposes. Stock prices are based on available market data and should not be treated as financial advice.
