"""
Run Exploratory Data Analysis on Northern Essentials Co. inventory dataset
Outputs all key insights and statistics to console
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("NORTHERN ESSENTIALS CO. - EXPLORATORY DATA ANALYSIS")
print("=" * 80)
print()

# Load all datasets
print("Loading datasets...")
products = pd.read_csv('data/products.csv')
customers = pd.read_csv('data/customers.csv')
warehouses = pd.read_csv('data/warehouses.csv')
current_inventory = pd.read_csv('data/current_inventory.csv')
transactions = pd.read_csv('data/inventory_transactions.csv')
metrics = pd.read_csv('data/supply_chain_metrics.csv')

# Convert date columns
current_inventory['last_updated'] = pd.to_datetime(current_inventory['last_updated'])
transactions['date'] = pd.to_datetime(transactions['date'])
metrics['week_ending'] = pd.to_datetime(metrics['week_ending'])

print("✓ Data loaded successfully!\n")
print(f"Dataset Sizes:")
print(f"  • Products: {len(products):,} SKUs")
print(f"  • Customers: {len(customers):,} retailers")
print(f"  • Warehouses: {len(warehouses):,} distribution centers")
print(f"  • Current Inventory: {len(current_inventory):,} records")
print(f"  • Transactions (90 days): {len(transactions):,} records")
print(f"  • Supply Chain Metrics: {len(metrics):,} weekly records")
print()

# ============================================================================
# 1. PRODUCT CATALOG ANALYSIS
# ============================================================================
print("=" * 80)
print("1. PRODUCT CATALOG ANALYSIS")
print("=" * 80)
print()

print("Products by Category:")
category_dist = products.groupby('category').size().sort_values(ascending=False)
for cat, count in category_dist.items():
    print(f"  • {cat}: {count} SKUs")
print()

# Calculate margins
products['margin_pct'] = ((products['retail_price_cad'] - products['unit_cost_cad']) /
                          products['retail_price_cad'] * 100).round(1)

print("Pricing Analysis by Category:")
pricing_stats = products.groupby('category').agg({
    'unit_cost_cad': ['mean', 'min', 'max'],
    'retail_price_cad': ['mean', 'min', 'max'],
    'margin_pct': 'mean'
}).round(2)

for cat in pricing_stats.index:
    print(f"\n  {cat}:")
    print(f"    Cost:   ${pricing_stats.loc[cat, ('unit_cost_cad', 'mean')]:.2f} avg (${pricing_stats.loc[cat, ('unit_cost_cad', 'min')]:.2f} - ${pricing_stats.loc[cat, ('unit_cost_cad', 'max')]:.2f})")
    print(f"    Retail: ${pricing_stats.loc[cat, ('retail_price_cad', 'mean')]:.2f} avg (${pricing_stats.loc[cat, ('retail_price_cad', 'min')]:.2f} - ${pricing_stats.loc[cat, ('retail_price_cad', 'max')]:.2f})")
    print(f"    Margin: {pricing_stats.loc[cat, ('margin_pct', 'mean')]:.1f}%")
print()

# ============================================================================
# 2. CUSTOMER & WAREHOUSE ANALYSIS
# ============================================================================
print("=" * 80)
print("2. CUSTOMER & WAREHOUSE ANALYSIS")
print("=" * 80)
print()

print("Customer Distribution:")
print(f"  By Type:")
for ctype, count in customers['customer_type'].value_counts().items():
    print(f"    • {ctype}: {count}")
print(f"\n  By Tier:")
for tier, count in customers['tier'].value_counts().items():
    print(f"    • {tier}: {count}")
print()

print("Warehouse Summary by Region:")
wh_summary = warehouses.groupby('region').agg({
    'warehouse_id': 'count',
    'capacity_pallets': 'sum',
    'current_utilization_pct': 'mean',
    'operating_cost_monthly_cad': 'sum',
    'staff_count': 'sum'
}).round(1)

for region in wh_summary.index:
    print(f"\n  {region}:")
    print(f"    Warehouses: {int(wh_summary.loc[region, 'warehouse_id'])}")
    print(f"    Total Capacity: {int(wh_summary.loc[region, 'capacity_pallets']):,} pallets")
    print(f"    Avg Utilization: {wh_summary.loc[region, 'current_utilization_pct']:.1f}%")
    print(f"    Monthly Costs: ${int(wh_summary.loc[region, 'operating_cost_monthly_cad']):,}")
    print(f"    Staff: {int(wh_summary.loc[region, 'staff_count'])}")
print()

high_util = warehouses[warehouses['current_utilization_pct'] > 80]
if len(high_util) > 0:
    print(f"⚠️  High Utilization Warehouses (>80%):")
    for _, wh in high_util.iterrows():
        print(f"  • {wh['warehouse_id']} ({wh['city']}): {wh['current_utilization_pct']:.1f}%")
    print()

# ============================================================================
# 3. CURRENT INVENTORY ANALYSIS
# ============================================================================
print("=" * 80)
print("3. CURRENT INVENTORY ANALYSIS")
print("=" * 80)
print()

# Convert inventory value to numeric
current_inventory['inventory_value_cad'] = current_inventory['inventory_value_cad'].astype(float)

print("Inventory Status Distribution:")
status_dist = current_inventory['status'].value_counts()
for status, count in status_dist.items():
    pct = count / len(current_inventory) * 100
    emoji = "🟢" if status == "Normal" else "🟡" if status == "Low" else "🔴" if status == "Critical" else "🔵"
    print(f"  {emoji} {status}: {count} ({pct:.1f}%)")
print()

total_inv_value = current_inventory['inventory_value_cad'].sum()
print(f"Total Inventory Value: ${total_inv_value:,.2f}")
print()

print("Inventory Value by Region:")
inv_by_region = current_inventory.groupby('region')['inventory_value_cad'].sum().sort_values(ascending=False)
for region, value in inv_by_region.items():
    pct = value / total_inv_value * 100
    print(f"  • {region}: ${value:,.2f} ({pct:.1f}%)")
print()

print("Inventory Value by Category:")
inv_by_cat = current_inventory.groupby('category')['inventory_value_cad'].sum().sort_values(ascending=False)
for cat, value in inv_by_cat.items():
    pct = value / total_inv_value * 100
    print(f"  • {cat}: ${value:,.2f} ({pct:.1f}%)")
print()

print("Days of Supply Statistics:")
print(f"  • Mean: {current_inventory['days_of_supply'].mean():.1f} days")
print(f"  • Median: {current_inventory['days_of_supply'].median():.1f} days")
print(f"  • Min: {current_inventory['days_of_supply'].min():.1f} days")
print(f"  • Max: {current_inventory['days_of_supply'].max():.1f} days")
print()

# Items with low days of supply
low_supply = current_inventory[current_inventory['days_of_supply'] < 7].sort_values('days_of_supply')
if len(low_supply) > 0:
    print(f"⚠️  Items with < 7 Days of Supply: {len(low_supply)}")
    print("\n  Top 5 Most Urgent:")
    for _, item in low_supply.head(5).iterrows():
        print(f"    • {item['warehouse_id']} - {item['product_name']}: {item['days_of_supply']:.1f} days ({item['status']})")
    print()

# ============================================================================
# 4. TRANSACTION ANALYSIS
# ============================================================================
print("=" * 80)
print("4. TRANSACTION ANALYSIS (90 Days)")
print("=" * 80)
print()

# Convert total value to numeric
transactions['total_value_cad'] = transactions['total_value_cad'].astype(float)

print("Transaction Type Distribution:")
txn_types = transactions['transaction_type'].value_counts()
for txn_type, count in txn_types.items():
    pct = count / len(transactions) * 100
    print(f"  • {txn_type}: {count:,} ({pct:.1f}%)")
print()

print("Transaction Volume by Region:")
txn_by_region = transactions['region'].value_counts().sort_values(ascending=False)
for region, count in txn_by_region.items():
    pct = count / len(transactions) * 100
    print(f"  • {region}: {count:,} ({pct:.1f}%)")
print()

print("Total Transaction Value by Type:")
txn_value_type = transactions.groupby('transaction_type')['total_value_cad'].sum().sort_values(ascending=False)
for txn_type, value in txn_value_type.items():
    print(f"  • {txn_type}: ${value:,.2f}")
print()

# Daily stats
daily_txn = transactions.groupby('date').agg({
    'transaction_id': 'count',
    'total_value_cad': 'sum'
})

print("Daily Transaction Statistics:")
print(f"  • Avg transactions/day: {daily_txn['transaction_id'].mean():.0f}")
print(f"  • Min transactions/day: {daily_txn['transaction_id'].min():.0f}")
print(f"  • Max transactions/day: {daily_txn['transaction_id'].max():.0f}")
print(f"  • Avg value/day: ${daily_txn['total_value_cad'].mean():,.2f}")
print(f"  • Total value (90 days): ${daily_txn['total_value_cad'].sum():,.2f}")
print()

# Customer shipments
outbound = transactions[transactions['transaction_type'] == 'Outbound']
outbound_with_customer = outbound[outbound['customer_id'] != '']

if len(outbound_with_customer) > 0:
    print("Top 5 Customers by Shipment Value:")
    customer_shipments = outbound_with_customer.groupby('customer_id').agg({
        'transaction_id': 'count',
        'total_value_cad': 'sum'
    }).sort_values('total_value_cad', ascending=False).head(5)

    for cust_id, row in customer_shipments.iterrows():
        print(f"  • {cust_id}: {int(row['transaction_id'])} shipments, ${row['total_value_cad']:,.2f}")
    print()

# ============================================================================
# 5. SUPPLY CHAIN KPI ANALYSIS
# ============================================================================
print("=" * 80)
print("5. SUPPLY CHAIN PERFORMANCE METRICS")
print("=" * 80)
print()

print("Overall KPIs (90-day average):")
print(f"  • Order Fill Rate: {metrics['order_fill_rate_pct'].mean():.2f}%")
print(f"  • On-Time Delivery: {metrics['on_time_delivery_pct'].mean():.2f}%")
print(f"  • Average Lead Time: {metrics['avg_lead_time_days'].mean():.2f} days")
print(f"  • Inventory Accuracy: {metrics['inventory_accuracy_pct'].mean():.2f}%")
print(f"  • Picking Accuracy: {metrics['picking_accuracy_pct'].mean():.2f}%")
print(f"  • Total Stockout Incidents: {int(metrics['stockout_incidents'].sum())}")
print()

print("KPIs by Region:")
kpi_by_region = metrics.groupby('region').agg({
    'order_fill_rate_pct': 'mean',
    'on_time_delivery_pct': 'mean',
    'avg_lead_time_days': 'mean',
    'stockout_incidents': 'sum',
    'inventory_accuracy_pct': 'mean'
}).round(2)

for region in kpi_by_region.index:
    print(f"\n  {region}:")
    print(f"    Fill Rate: {kpi_by_region.loc[region, 'order_fill_rate_pct']:.2f}%")
    print(f"    On-Time: {kpi_by_region.loc[region, 'on_time_delivery_pct']:.2f}%")
    print(f"    Lead Time: {kpi_by_region.loc[region, 'avg_lead_time_days']:.2f} days")
    print(f"    Stockouts: {int(kpi_by_region.loc[region, 'stockout_incidents'])}")
    print(f"    Inv Accuracy: {kpi_by_region.loc[region, 'inventory_accuracy_pct']:.2f}%")
print()

# Identify low performers
low_fill_rate = kpi_by_region[kpi_by_region['order_fill_rate_pct'] < 95]
if len(low_fill_rate) > 0:
    print(f"⚠️  Regions Below 95% Fill Rate Target:")
    for region in low_fill_rate.index:
        print(f"  • {region}: {low_fill_rate.loc[region, 'order_fill_rate_pct']:.2f}%")
    print()

# ============================================================================
# 6. REGIONAL COMPARISON
# ============================================================================
print("=" * 80)
print("6. COMPREHENSIVE REGIONAL COMPARISON")
print("=" * 80)
print()

# Build comprehensive regional summary
regional_summary = pd.DataFrame()
regional_summary['Warehouses'] = warehouses.groupby('region')['warehouse_id'].count()
regional_summary['Capacity'] = warehouses.groupby('region')['capacity_pallets'].sum()
regional_summary['Util %'] = warehouses.groupby('region')['current_utilization_pct'].mean().round(1)
regional_summary['SKUs'] = current_inventory.groupby('region')['sku'].nunique()
regional_summary['Inv Value (CAD)'] = current_inventory.groupby('region')['inventory_value_cad'].sum().round(2)
regional_summary['Avg Days'] = current_inventory.groupby('region')['days_of_supply'].mean().round(1)
regional_summary['Txns'] = transactions.groupby('region')['transaction_id'].count()
regional_summary['Fill %'] = metrics.groupby('region')['order_fill_rate_pct'].mean().round(2)
regional_summary['OnTime %'] = metrics.groupby('region')['on_time_delivery_pct'].mean().round(2)
regional_summary['Stockouts'] = metrics.groupby('region')['stockout_incidents'].sum()

# Sort by inventory value
regional_summary = regional_summary.sort_values('Inv Value (CAD)', ascending=False)

print(regional_summary.to_string())
print()

# ============================================================================
# 7. KEY INSIGHTS & RECOMMENDATIONS
# ============================================================================
print("=" * 80)
print("7. KEY INSIGHTS & RECOMMENDATIONS")
print("=" * 80)
print()

critical_low_items = current_inventory[current_inventory['status'].isin(['Critical', 'Low'])]
overstock_items = current_inventory[current_inventory['status'] == 'Overstock']
high_util_warehouses = warehouses[warehouses['current_utilization_pct'] > 80]

print("📊 INVENTORY INSIGHTS:")
print(f"  • Total inventory value: ${total_inv_value:,.2f}")
print(f"  • Critical/Low stock items: {len(critical_low_items)} ({len(critical_low_items)/len(current_inventory)*100:.1f}%)")
print(f"  • Overstock items: {len(overstock_items)} ({len(overstock_items)/len(current_inventory)*100:.1f}%)")
print(f"  • Average days of supply: {current_inventory['days_of_supply'].mean():.1f} days")
print()

print("🏭 WAREHOUSE CAPACITY:")
print(f"  • Average utilization: {warehouses['current_utilization_pct'].mean():.1f}%")
print(f"  • High utilization (>80%) warehouses: {len(high_util_warehouses)}/{len(warehouses)}")
if len(high_util_warehouses) > 0:
    print(f"  • Warehouses needing attention: {', '.join(high_util_warehouses['warehouse_id'].tolist())}")
print()

print("📦 SUPPLY CHAIN PERFORMANCE:")
print(f"  • Average fill rate: {metrics['order_fill_rate_pct'].mean():.2f}%")
print(f"  • Average on-time delivery: {metrics['on_time_delivery_pct'].mean():.2f}%")
print(f"  • Average lead time: {metrics['avg_lead_time_days'].mean():.2f} days")
print(f"  • Total stockout incidents: {int(metrics['stockout_incidents'].sum())}")
print()

print("💡 TOP RECOMMENDATIONS:")
print()
print("1. INVENTORY OPTIMIZATION:")
if len(critical_low_items) > 0:
    print(f"   ✓ Prioritize replenishment for {len(critical_low_items)} critical/low items")
    top_critical = critical_low_items.nsmallest(3, 'days_of_supply')
    urgent_products = top_critical['product_name'].unique()
    print(f"   ✓ Most urgent products: {', '.join(urgent_products[:3])}")
if len(overstock_items) > 0:
    print(f"   ✓ Review and potentially discount {len(overstock_items)} overstocked items")
print()

print("2. WAREHOUSE MANAGEMENT:")
if len(high_util_warehouses) > 0:
    print(f"   ✓ Consider capacity expansion for high-utilization warehouses")
    print(f"   ✓ Focus on: {', '.join(high_util_warehouses['warehouse_id'].tolist())}")
print()

print("3. SUPPLY CHAIN IMPROVEMENTS:")
low_fill_regions = kpi_by_region[kpi_by_region['order_fill_rate_pct'] < 95].index.tolist()
if len(low_fill_regions) > 0:
    print(f"   ✓ Investigate fill rate issues in: {', '.join(low_fill_regions)}")
high_stockout_regions = metrics.groupby('region')['stockout_incidents'].sum().nlargest(2).index.tolist()
if len(high_stockout_regions) > 0:
    print(f"   ✓ Address stockout patterns in: {', '.join(high_stockout_regions)}")
print(f"   ✓ Target lead time reduction from {metrics['avg_lead_time_days'].mean():.1f} to <3 days")
print()

print("4. REGIONAL FOCUS:")
best_region = kpi_by_region['order_fill_rate_pct'].idxmax()
print(f"   ✓ Share best practices from {best_region} (highest fill rate)")
print(f"   ✓ Maintain {current_inventory['days_of_supply'].mean():.0f}+ days supply across all regions")
print()

print("=" * 80)
print("EDA COMPLETE - Ready for Dashboard Development!")
print("=" * 80)
