# 🤖 Binance Trading Bot (Python)

## 📌 Overview

This project is a **Python-based Binance trading bot** that allows interaction with Binance Futures API, including fetching account data and placing orders programmatically.

📘 **Note:** The file `manual.txt` contains a detailed step-by-step guide explaining how this project was built, including setup, structure, and implementation flow.

---

## 🛠️ Tech Stack

* **Language:** Python 🐍 (Version 3.13.12)
* **Libraries:**

  * `python-binance`
  * `python-dotenv`
* **Tools Used:**

  * Windows CMD
  * VS Code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd <repo-folder>
```

### 2️⃣ Create virtual environment

```
python -m venv primetrade
primetrade\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install python-binance python-dotenv
```

### 4️⃣ Add API keys

Create a `.env` file:

```
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

## ▶️ How to Run

### 🔹 Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### 🔹 Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
```

---

## 📌 Assumptions

* User has a Binance account with API keys enabled
* Binance Futures Testnet is being used
* Python 3.13.12 is installed

---

## ⚠️ Note

On Binance Futures Testnet, MARKET orders may sometimes return `NEW` status initially due to delayed updates. Therefore, execution is verified using `executedQty` and `avgPrice` fields.
