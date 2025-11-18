# Data Dictionary

## products.csv
Product master data containing all SKUs offered by Northern Essentials Co.

| Field | Type | Description |
|-------|------|-------------|
| sku | String | Unique product identifier (format: SKU-XXXX) |
| product_name | String | Product display name |
| category | String | Product category (Snacks & Confectionery, Beverages, Personal Care, Household Cleaning, Health & Wellness) |
| pack_size | Integer | Number of units per case |
| unit_cost_cad | Decimal | Cost per case in Canadian dollars |
| retail_price_cad | Decimal | Suggested retail price per case in CAD |
| weight_kg | Decimal | Weight per case in kilograms |
| cubic_meters | Decimal | Volume per case in cubic meters |
| shelf_life_days | Integer | Product shelf life in days |

## customers.csv
Major retail customers/distribution partners across Canada.

| Field | Type | Description |
|-------|------|-------------|
| customer_id | String | Unique customer identifier (format: C0XX) |
| customer_name | String | Customer/retailer name |
| customer_type | String | Type of retail operation (Grocery, Big Box, Warehouse Club, etc.) |
| tier | String | National or Regional presence |
| regions | String | Regions where customer operates (semicolon-separated) |
| payment_terms_days | Integer | Standard payment terms in days |
| credit_limit_cad | Integer | Credit limit in Canadian dollars |

## warehouses.csv
Distribution centers and warehouse facilities across 4 regions.

| Field | Type | Description |
|-------|------|-------------|
| warehouse_id | String | Unique warehouse identifier (format: WH-XXX) |
| warehouse_name | String | Warehouse display name |
| region | String | Region (Atlantic, Ontario, Quebec, West) |
| city | String | City location with province |
| capacity_pallets | Integer | Maximum storage capacity in pallets |
| current_utilization_pct | Decimal | Current capacity utilization percentage |
| operating_cost_monthly_cad | Integer | Monthly operating costs in CAD |
| staff_count | Integer | Number of warehouse employees |

## current_inventory.csv
Current stock levels across all warehouse locations (snapshot).

| Field | Type | Description |
|-------|------|-------------|
| warehouse_id | String | Warehouse identifier |
| region | String | Region name |
| sku | String | Product SKU |
| product_name | String | Product name |
| category | String | Product category |
| current_stock_units | Integer | Current inventory on hand (cases) |
| safety_stock_units | Integer | Minimum safety stock level |
| reorder_point_units | Integer | Reorder trigger point |
| max_stock_units | Integer | Maximum stock level |
| inventory_value_cad | Decimal | Total inventory value in CAD |
| days_of_supply | Decimal | Estimated days until stockout at current demand |
| status | String | Inventory status (Normal, Low, Critical, Overstock) |
| last_updated | Date | Last inventory count date |

## inventory_transactions.csv
Historical inventory movements (90 days of transactions).

| Field | Type | Description |
|-------|------|-------------|
| transaction_id | String | Unique transaction identifier (format: TXN-XXXXXXX) |
| date | Date | Transaction date |
| warehouse_id | String | Warehouse identifier |
| region | String | Region name |
| sku | String | Product SKU |
| product_name | String | Product name |
| category | String | Product category |
| transaction_type | String | Type (Inbound, Outbound, Transfer, Adjustment) |
| quantity | Integer | Quantity moved (negative for outbound) |
| customer_id | String | Customer ID (for outbound transactions) |
| reference | String | Reference number (PO, SO, TR, ADJ) |
| unit_cost_cad | Decimal | Unit cost at time of transaction |
| total_value_cad | Decimal | Total transaction value in CAD |

## supply_chain_metrics.csv
Weekly supply chain performance KPIs by warehouse (90 days).

| Field | Type | Description |
|-------|------|-------------|
| week_ending | Date | End date of the week |
| warehouse_id | String | Warehouse identifier |
| region | String | Region name |
| orders_received | Integer | Total orders received during week |
| orders_fulfilled | Integer | Orders successfully fulfilled |
| order_fill_rate_pct | Decimal | Percentage of orders filled completely |
| on_time_delivery_pct | Decimal | Percentage delivered on time |
| avg_lead_time_days | Decimal | Average lead time in days |
| stockout_incidents | Integer | Number of stockout events |
| inventory_accuracy_pct | Decimal | Physical vs system inventory accuracy |
| putaway_time_hours | Decimal | Average time to putaway received goods |
| picking_accuracy_pct | Decimal | Percentage of orders picked correctly |
| dock_to_stock_hours | Decimal | Average hours from dock to stock location |

## Key Metrics Explained

**Days of Supply**: Current stock divided by average daily demand. Indicates how many days of inventory coverage exists.

**Order Fill Rate**: Percentage of customer orders filled completely from available stock.

**Inventory Status**:
- **Normal**: Stock between reorder point and max level
- **Low**: Stock below reorder point but above safety stock
- **Critical**: Stock below safety stock level
- **Overstock**: Stock exceeds 150% of target maximum

**Transaction Types**:
- **Inbound**: Receipts from suppliers/manufacturing
- **Outbound**: Shipments to customers
- **Transfer**: Inter-warehouse movements
- **Adjustment**: Inventory corrections (cycle counts, damage, etc.)
