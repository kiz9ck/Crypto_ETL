# 🚀 Fault-Tolerant Crypto ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-elephant?logo=postgresql&logoColor=white)
![Build Status](https://github.com/kiz9ck/Crypto_ETL/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-green)

A professional, containerized **ETL (Extract, Transform, Load) Pipeline** designed to track cryptocurrency prices, analyze market fluctuations, and send real-time alerts.

Built with **Python**, **PostgreSQL**, and **Docker**. Features a robust architecture with automated scheduling and CI/CD integration.

---

## 🏗 Architecture

The system operates as a set of Docker containers orchestrated by Docker Compose:

1.  **Extraction Service (Worker):**
    * Fetches real-time data from **CoinGecko API**.
    * Supports monitoring multiple assets simultaneously (Bitcoin, Ethereum, Solana, etc.).
2.  **Transformation & Analysis:**
    * Cleans and normalizes JSON data using `Pandas`.
    * Compares current prices with historical data to detect volatility.
    * **Logic:** Triggers an alert if the price changes by more than **5%** (configurable) since the last check.
3.  **Loading (Storage):**
    * Persists historical data into a **PostgreSQL 15** database.
4.  **Notification System:**
    * Sends email alerts via SMTP (Gmail) when volatility thresholds are breached.

---

## 🛠 Tech Stack

* **Language:** Python 3.10
* **Libraries:** Pandas, SQLAlchemy, Requests, Schedule, Psycopg2
* **Database:** PostgreSQL 15
* **Infrastructure:** Docker & Docker Compose
* **CI/CD:** GitHub Actions (Automated Linting & Build Tests)
* **Tools:** Git, python-dotenv

---

## 📂 Project Structure

```text
crypto_etl/
├── .github/workflows/   # CI/CD Pipeline configuration
├── src/                 # Source code
│   ├── api.py           # API Client (CoinGecko)
│   ├── db.py            # Database Handler (SQLAlchemy)
│   ├── notifications.py # Email Alerting System
│   ├── config.py        # Configuration Management
│   └── main.py          # Application Entrypoint (Worker)
├── .dockerignore        # Security exclusions for Docker
├── .env.example         # Template for environment variables
├── docker-compose.yml   # Container orchestration
├── Dockerfile           # Python worker image definition
└── requirements.txt     # Python dependencies

## 🏃‍♂️ How to Run

Follow these steps to get the pipeline running in minutes.

### 1. Clone the repository
```bash
git clone [https://github.com/kiz9ck/Crypto_ETL.git](https://github.com/kiz9ck/Crypto_ETL.git)
cd Crypto_ETL
```

### 2. Configure Environment
```bash
cp .env.example .env
```
Open .env and fill in your credentials (database user, password, and email settings).

### 3. Launch with Docker 🐳
```bash
docker-compose up --build -d
```

### 4. Verify Status
```bash 
docker ps
```
To see the real-time logs of the Python worker:
```bash
docker logs -f crypto_worker
```

