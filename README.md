# CPG Inventory Dashboard - Canada Operations

This repository contains a fictional dataset for a Canadian Consumer Packaged Goods (CPG) company's inventory and supply chain operations.

## Company Overview

**Northern Essentials Co.** is a fictional CPG company distributing consumable products across Canada through 4 regional operations.

### Regions
- **Atlantic**: Serving NB, NS, PE, NL
- **Ontario**: Serving ON
- **Quebec**: Serving QC
- **West**: Serving BC, AB, SK, MB

### Major Customers (10 Retailers)
1. Loblaw Companies
2. Sobeys Inc.
3. Metro Inc.
4. Walmart Canada
5. Costco Canada
6. Save-On-Foods
7. Shoppers Drug Mart
8. Dollarama
9. Canadian Tire
10. Amazon Canada

### Product Categories
- Snacks & Confectionery
- Beverages (Non-Alcoholic)
- Personal Care
- Household Cleaning
- Health & Wellness

## Dataset Structure

### Files
- `data/products.csv` - Product master data (SKUs, categories, pricing)
- `data/customers.csv` - Customer/retailer information
- `data/warehouses.csv` - Distribution center locations
- `data/inventory_transactions.csv` - Daily inventory movements
- `data/current_inventory.csv` - Current stock levels by location
- `data/supply_chain_metrics.csv` - KPIs for supply chain performance

### Key Metrics
- Stock levels (units)
- Inventory value (CAD)
- Days of supply
- Fill rates
- Order fulfillment
- Lead times
- Stock-out incidents

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Data (Optional)

The dataset is already included, but you can regenerate or extend it:

```bash
python generate_data.py
```

### 3. Run Exploratory Data Analysis

**Option A: Quick Analysis (Recommended)**

Run the standalone Python script for instant insights:

```bash
python run_eda.py
```

**Option B: Interactive Notebook**

Explore the data interactively with Jupyter:

```bash
jupyter notebook exploratory_data_analysis.ipynb
```

See [EDA_GUIDE.md](EDA_GUIDE.md) for detailed instructions and insights.

## Dashboard Use Cases

This dataset supports dashboards for:
- Inventory levels by region/product/customer
- Supply chain performance metrics
- Stock rotation and aging analysis
- Demand forecasting
- Distribution center efficiency
- Customer service levels
