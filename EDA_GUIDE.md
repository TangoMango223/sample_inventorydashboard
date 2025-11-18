# Exploratory Data Analysis Guide

This guide explains how to run the EDA on the Northern Essentials Co. inventory dataset.

## Prerequisites

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Running the EDA

### Option 1: Jupyter Notebook (Recommended)

The interactive notebook allows you to explore the data step-by-step with visualizations.

```bash
jupyter notebook exploratory_data_analysis.ipynb
```

This will open the notebook in your browser. Run each cell sequentially to see:
- Data loading and overview
- Product catalog analysis with pricing and margins
- Customer and warehouse distribution
- Current inventory status and valuation
- Transaction trends over 90 days
- Supply chain KPI analysis
- Regional performance comparison
- Key insights and recommendations

### Option 2: View in VS Code

If you have VS Code with the Jupyter extension:

```bash
code exploratory_data_analysis.ipynb
```

## What You'll Learn

### 1. **Product Portfolio Analysis**
- SKU distribution across categories
- Pricing structure and profit margins
- Pack sizes and physical characteristics

### 2. **Inventory Health**
- Current stock levels by region and warehouse
- Inventory status (Normal, Low, Critical, Overstock)
- Days of supply analysis
- Total inventory valuation

### 3. **Transaction Patterns**
- Daily transaction volume trends
- Transaction types (Inbound, Outbound, Transfer, Adjustment)
- Customer shipment analysis
- Value flow over time

### 4. **Supply Chain Performance**
- Order fill rates by region
- On-time delivery metrics
- Lead time analysis
- Stockout incident tracking
- Inventory accuracy and picking accuracy

### 5. **Regional Comparison**
- Warehouse capacity and utilization
- Performance metrics by region
- Operational efficiency
- Areas needing improvement

## Key Insights Available

The EDA will identify:
- ✅ Products requiring immediate replenishment
- ✅ Overstocked items to address
- ✅ Warehouses at high capacity
- ✅ Regions with fill rate issues
- ✅ Best-performing operations to learn from
- ✅ Stockout patterns and root causes

## Next Steps

After reviewing the EDA:
1. Use insights to inform dashboard requirements
2. Identify which metrics to highlight in real-time
3. Determine alert thresholds for critical conditions
4. Design drill-down paths for investigation
5. Plan for predictive analytics (forecasting, optimization)

## Visualizations Included

- 📊 Bar charts for distributions and comparisons
- 📈 Line charts for trends over time
- 🥧 Pie charts for proportions
- 🗺️ Heatmaps for regional performance
- 📉 Histograms for statistical distributions

## Troubleshooting

### Missing Libraries
If you get import errors, ensure all requirements are installed:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Data Not Found
Ensure you're running from the project root directory where the `data/` folder exists.

### Large Dataset Warnings
The dataset includes 9,000+ transactions. If performance is slow, consider:
- Using a more powerful machine
- Sampling the data for initial exploration
- Upgrading to a database for larger datasets
