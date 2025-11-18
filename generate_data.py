"""
Generate realistic inventory and supply chain data for Northern Essentials Co.
A fictional CPG company operating in Canada across 4 regions.
"""

import csv
import random
from datetime import datetime, timedelta
from typing import List, Dict
import os

# Set seed for reproducibility
random.seed(42)

# Configuration
REGIONS = {
    'Atlantic': ['Halifax, NS', 'Moncton, NB', "St. John's, NL"],
    'Ontario': ['Toronto, ON', 'Ottawa, ON', 'Mississauga, ON'],
    'Quebec': ['Montreal, QC', 'Quebec City, QC', 'Laval, QC'],
    'West': ['Vancouver, BC', 'Calgary, AB', 'Edmonton, AB', 'Winnipeg, MB']
}

CUSTOMERS = [
    {'id': 'C001', 'name': 'Loblaw Companies', 'type': 'Grocery', 'tier': 'National'},
    {'id': 'C002', 'name': 'Sobeys Inc.', 'type': 'Grocery', 'tier': 'National'},
    {'id': 'C003', 'name': 'Metro Inc.', 'type': 'Grocery', 'tier': 'National'},
    {'id': 'C004', 'name': 'Walmart Canada', 'type': 'Big Box', 'tier': 'National'},
    {'id': 'C005', 'name': 'Costco Canada', 'type': 'Warehouse Club', 'tier': 'National'},
    {'id': 'C006', 'name': 'Save-On-Foods', 'type': 'Grocery', 'tier': 'Regional'},
    {'id': 'C007', 'name': 'Shoppers Drug Mart', 'type': 'Pharmacy', 'tier': 'National'},
    {'id': 'C008', 'name': 'Dollarama', 'type': 'Discount', 'tier': 'National'},
    {'id': 'C009', 'name': 'Canadian Tire', 'type': 'General Merchandise', 'tier': 'National'},
    {'id': 'C010', 'name': 'Amazon Canada', 'type': 'E-Commerce', 'tier': 'National'}
]

PRODUCT_CATEGORIES = {
    'Snacks & Confectionery': [
        {'name': 'Maple Crunch Granola Bars', 'pack_size': 12, 'unit_cost': 4.50, 'retail_price': 8.99},
        {'name': 'Trail Mix - Canadian Blend', 'pack_size': 10, 'unit_cost': 5.25, 'retail_price': 10.49},
        {'name': 'Potato Chips - Sea Salt', 'pack_size': 24, 'unit_cost': 3.75, 'retail_price': 7.49},
        {'name': 'Chocolate Wafer Cookies', 'pack_size': 18, 'unit_cost': 4.20, 'retail_price': 8.49},
        {'name': 'Mixed Nuts Premium', 'pack_size': 8, 'unit_cost': 6.80, 'retail_price': 13.99}
    ],
    'Beverages': [
        {'name': 'Sparkling Water - Lemon', 'pack_size': 24, 'unit_cost': 5.50, 'retail_price': 10.99},
        {'name': 'Iced Tea - Peach', 'pack_size': 12, 'unit_cost': 4.25, 'retail_price': 8.49},
        {'name': 'Energy Drink - Arctic Blast', 'pack_size': 12, 'unit_cost': 8.75, 'retail_price': 17.99},
        {'name': 'Coconut Water Organic', 'pack_size': 12, 'unit_cost': 9.25, 'retail_price': 18.99},
        {'name': 'Cold Brew Coffee RTD', 'pack_size': 12, 'unit_cost': 7.50, 'retail_price': 14.99}
    ],
    'Personal Care': [
        {'name': 'Hand Soap - Lavender', 'pack_size': 6, 'unit_cost': 8.25, 'retail_price': 15.99},
        {'name': 'Body Lotion - Unscented', 'pack_size': 4, 'unit_cost': 12.50, 'retail_price': 24.99},
        {'name': 'Shampoo - Moisturizing', 'pack_size': 6, 'unit_cost': 15.75, 'retail_price': 29.99},
        {'name': 'Toothpaste - Whitening', 'pack_size': 12, 'unit_cost': 6.50, 'retail_price': 12.99},
        {'name': 'Deodorant - Fresh Scent', 'pack_size': 8, 'unit_cost': 10.25, 'retail_price': 19.99}
    ],
    'Household Cleaning': [
        {'name': 'Multi-Surface Cleaner', 'pack_size': 6, 'unit_cost': 9.75, 'retail_price': 18.99},
        {'name': 'Dish Soap - Citrus', 'pack_size': 8, 'unit_cost': 6.25, 'retail_price': 11.99},
        {'name': 'Laundry Detergent Pods', 'pack_size': 4, 'unit_cost': 18.50, 'retail_price': 34.99},
        {'name': 'Glass Cleaner', 'pack_size': 6, 'unit_cost': 7.80, 'retail_price': 14.99},
        {'name': 'Disinfecting Wipes', 'pack_size': 6, 'unit_cost': 11.25, 'retail_price': 21.99}
    ],
    'Health & Wellness': [
        {'name': 'Vitamin C Gummies', 'pack_size': 12, 'unit_cost': 8.75, 'retail_price': 16.99},
        {'name': 'Protein Bars - Chocolate', 'pack_size': 12, 'unit_cost': 12.50, 'retail_price': 24.99},
        {'name': 'Probiotics Daily', 'pack_size': 6, 'unit_cost': 22.50, 'retail_price': 44.99},
        {'name': 'Fiber Supplement Powder', 'pack_size': 4, 'unit_cost': 16.75, 'retail_price': 32.99},
        {'name': 'Multivitamin Adult', 'pack_size': 6, 'unit_cost': 14.25, 'retail_price': 27.99}
    ]
}


def generate_products() -> List[Dict]:
    """Generate product master data"""
    products = []
    sku_counter = 1000

    for category, items in PRODUCT_CATEGORIES.items():
        for item in items:
            sku = f'SKU-{sku_counter}'
            products.append({
                'sku': sku,
                'product_name': item['name'],
                'category': category,
                'pack_size': item['pack_size'],
                'unit_cost_cad': f"{item['unit_cost']:.2f}",
                'retail_price_cad': f"{item['retail_price']:.2f}",
                'weight_kg': round(random.uniform(0.5, 5.0), 2),
                'cubic_meters': round(random.uniform(0.01, 0.05), 3),
                'shelf_life_days': random.choice([180, 365, 540, 730])
            })
            sku_counter += 1

    return products


def generate_customers() -> List[Dict]:
    """Generate customer master data with regional presence"""
    customers_data = []

    for customer in CUSTOMERS:
        # Determine which regions this customer operates in
        if customer['tier'] == 'National':
            regions = list(REGIONS.keys())
        else:  # Regional
            regions = random.sample(list(REGIONS.keys()), k=random.randint(1, 2))

        customers_data.append({
            'customer_id': customer['id'],
            'customer_name': customer['name'],
            'customer_type': customer['type'],
            'tier': customer['tier'],
            'regions': ';'.join(regions),
            'payment_terms_days': random.choice([30, 45, 60]),
            'credit_limit_cad': random.randint(500000, 5000000)
        })

    return customers_data


def generate_warehouses() -> List[Dict]:
    """Generate warehouse/distribution center data"""
    warehouses = []
    wh_counter = 1

    for region, cities in REGIONS.items():
        for city in cities:
            warehouses.append({
                'warehouse_id': f'WH-{wh_counter:03d}',
                'warehouse_name': f'{city} Distribution Center',
                'region': region,
                'city': city,
                'capacity_pallets': random.randint(5000, 20000),
                'current_utilization_pct': round(random.uniform(60, 85), 1),
                'operating_cost_monthly_cad': random.randint(50000, 200000),
                'staff_count': random.randint(20, 100)
            })
            wh_counter += 1

    return warehouses


def generate_current_inventory(products: List[Dict], warehouses: List[Dict]) -> List[Dict]:
    """Generate current inventory snapshot"""
    inventory = []

    for warehouse in warehouses:
        # Each warehouse stocks 60-80% of all products
        stocked_products = random.sample(products, k=int(len(products) * random.uniform(0.6, 0.8)))

        for product in stocked_products:
            # Calculate realistic stock levels
            base_stock = random.randint(100, 5000)
            safety_stock = int(base_stock * 0.2)
            reorder_point = int(base_stock * 0.3)

            current_stock = random.randint(safety_stock, base_stock * 2)

            # Calculate metrics
            unit_cost = float(product['unit_cost_cad'])
            inventory_value = current_stock * unit_cost

            # Days of supply based on typical daily movement
            avg_daily_demand = random.randint(10, 100)
            days_of_supply = round(current_stock / avg_daily_demand, 1) if avg_daily_demand > 0 else 0

            # Determine status
            if current_stock < safety_stock:
                status = 'Critical'
            elif current_stock < reorder_point:
                status = 'Low'
            elif current_stock > base_stock * 1.5:
                status = 'Overstock'
            else:
                status = 'Normal'

            inventory.append({
                'warehouse_id': warehouse['warehouse_id'],
                'region': warehouse['region'],
                'sku': product['sku'],
                'product_name': product['product_name'],
                'category': product['category'],
                'current_stock_units': current_stock,
                'safety_stock_units': safety_stock,
                'reorder_point_units': reorder_point,
                'max_stock_units': base_stock * 2,
                'inventory_value_cad': f"{inventory_value:.2f}",
                'days_of_supply': days_of_supply,
                'status': status,
                'last_updated': datetime.now().strftime('%Y-%m-%d')
            })

    return inventory


def generate_inventory_transactions(products: List[Dict], warehouses: List[Dict],
                                   customers_data: List[Dict], days: int = 90) -> List[Dict]:
    """Generate inventory transaction history"""
    transactions = []
    transaction_id = 1

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    # Generate daily transactions
    current_date = start_date
    while current_date <= end_date:
        # Each day has multiple transactions
        daily_transactions = random.randint(50, 150)

        for _ in range(daily_transactions):
            warehouse = random.choice(warehouses)
            product = random.choice(products)

            # Transaction types with weights
            transaction_type = random.choices(
                ['Inbound', 'Outbound', 'Transfer', 'Adjustment'],
                weights=[0.3, 0.5, 0.15, 0.05]
            )[0]

            # Generate quantities based on transaction type
            if transaction_type == 'Inbound':
                quantity = random.randint(500, 3000)
                customer_id = None
                reference = f'PO-{random.randint(10000, 99999)}'
            elif transaction_type == 'Outbound':
                quantity = -random.randint(100, 1500)
                customer = random.choice(customers_data)
                # Check if customer operates in this region
                if warehouse['region'] in customer['regions'].split(';'):
                    customer_id = customer['customer_id']
                else:
                    customer_id = None
                reference = f'SO-{random.randint(10000, 99999)}'
            elif transaction_type == 'Transfer':
                quantity = random.choice([random.randint(-500, -100), random.randint(100, 500)])
                customer_id = None
                reference = f'TR-{random.randint(10000, 99999)}'
            else:  # Adjustment
                quantity = random.randint(-50, 50)
                customer_id = None
                reference = f'ADJ-{random.randint(10000, 99999)}'

            transactions.append({
                'transaction_id': f'TXN-{transaction_id:07d}',
                'date': current_date.strftime('%Y-%m-%d'),
                'warehouse_id': warehouse['warehouse_id'],
                'region': warehouse['region'],
                'sku': product['sku'],
                'product_name': product['product_name'],
                'category': product['category'],
                'transaction_type': transaction_type,
                'quantity': quantity,
                'customer_id': customer_id if customer_id else '',
                'reference': reference,
                'unit_cost_cad': product['unit_cost_cad'],
                'total_value_cad': f"{abs(quantity) * float(product['unit_cost_cad']):.2f}"
            })

            transaction_id += 1

        current_date += timedelta(days=1)

    return transactions


def generate_supply_chain_metrics(warehouses: List[Dict], days: int = 90) -> List[Dict]:
    """Generate supply chain performance metrics"""
    metrics = []

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    # Generate weekly metrics
    current_date = start_date
    while current_date <= end_date:
        for warehouse in warehouses:
            # Generate realistic KPIs
            order_fill_rate = round(random.uniform(92, 99.5), 2)
            on_time_delivery = round(random.uniform(88, 97), 2)

            metrics.append({
                'week_ending': current_date.strftime('%Y-%m-%d'),
                'warehouse_id': warehouse['warehouse_id'],
                'region': warehouse['region'],
                'orders_received': random.randint(200, 800),
                'orders_fulfilled': int(random.randint(200, 800) * order_fill_rate / 100),
                'order_fill_rate_pct': order_fill_rate,
                'on_time_delivery_pct': on_time_delivery,
                'avg_lead_time_days': round(random.uniform(1.5, 5.0), 1),
                'stockout_incidents': random.randint(0, 5),
                'inventory_accuracy_pct': round(random.uniform(96, 99.9), 2),
                'putaway_time_hours': round(random.uniform(2, 8), 1),
                'picking_accuracy_pct': round(random.uniform(97, 99.9), 2),
                'dock_to_stock_hours': round(random.uniform(4, 24), 1)
            })

        current_date += timedelta(days=7)

    return metrics


def save_to_csv(data: List[Dict], filename: str):
    """Save data to CSV file"""
    if not data:
        print(f"No data to save for {filename}")
        return

    filepath = os.path.join('data', filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Generated {filename} with {len(data)} records")


def main():
    """Generate all datasets"""
    print("Generating CPG Inventory Data for Northern Essentials Co.")
    print("=" * 60)

    # Generate master data
    products = generate_products()
    save_to_csv(products, 'products.csv')

    customers_data = generate_customers()
    save_to_csv(customers_data, 'customers.csv')

    warehouses = generate_warehouses()
    save_to_csv(warehouses, 'warehouses.csv')

    # Generate operational data
    current_inventory = generate_current_inventory(products, warehouses)
    save_to_csv(current_inventory, 'current_inventory.csv')

    transactions = generate_inventory_transactions(products, warehouses, customers_data, days=90)
    save_to_csv(transactions, 'inventory_transactions.csv')

    metrics = generate_supply_chain_metrics(warehouses, days=90)
    save_to_csv(metrics, 'supply_chain_metrics.csv')

    print("=" * 60)
    print("Data generation complete!")
    print("\nDataset Summary:")
    print(f"  - Products: {len(products)} SKUs across 5 categories")
    print(f"  - Customers: {len(customers_data)} major retailers")
    print(f"  - Warehouses: {len(warehouses)} distribution centers")
    print(f"  - Current Inventory: {len(current_inventory)} records")
    print(f"  - Transactions (90 days): {len(transactions)} records")
    print(f"  - Supply Chain Metrics (90 days): {len(metrics)} records")


if __name__ == '__main__':
    main()
