import pandas as pd
import numpy as np
import time
import random

print("Generating dummy dataset for metric calculation...")
start_time = time.time()

# 1. Generate Customers
num_customers = 100_000
print(f"Generating {num_customers} customers...")
cities = ["Bengaluru", "Hyderabad", "New Delhi", "Pune", None, "Bengaluruu", "NewDelhi"]

# Generate base customers
np.random.seed(42)
customer_ids = np.arange(num_customers)
names = [f"Customer_{i}" + (" " if np.random.random() > 0.9 else "") for i in range(num_customers)]
cust_cities = np.random.choice(cities, num_customers)

df_customers = pd.DataFrame({
    'customer_id': customer_ids,
    'customer_name': names,
    'city': cust_cities
})

# Add duplicates
duplicates = df_customers.sample(n=5000, random_state=42)
df_customers = pd.concat([df_customers, duplicates], ignore_index=True)
initial_customer_count = len(df_customers)

# Simulate processing
print(f"Processing {initial_customer_count} customer records...")

# Drop duplicates
df_customers = df_customers.drop_duplicates(subset=['customer_id'])
after_dedup_count = len(df_customers)

# Trim names
df_customers['customer_name'] = df_customers['customer_name'].str.strip()

# City mapping
city_mapping = {
    'Bengaluruu': 'Bengaluru',
    'Bengalore': 'Bengaluru',
    'Hyderabadd': 'Hyderabad',
    'Hyderbad': 'Hyderabad',
    'NewDelhi': 'New Delhi',
    'NewDheli': 'New Delhi',
    'NewDelhee': 'New Delhi'
}
allowed = ["Bengaluru", "Hyderabad", "New Delhi", "Pune"]

df_customers['city'] = df_customers['city'].replace(city_mapping)
df_customers.loc[~df_customers['city'].isin(allowed), 'city'] = None
null_cities = df_customers['city'].isna().sum()

# 2. Generate Orders
num_orders = 1_000_000
print(f"Generating {num_orders} orders...")

df_orders = pd.DataFrame({
    'order_id': np.arange(num_orders),
    'order_placement_date': [f"2025/0{random.randint(1, 9)}/{random.randint(10, 28)}" for _ in range(num_orders)],
    'customer_id': np.random.randint(0, num_customers, num_orders),
    'product_id': np.random.randint(1, 1000, num_orders),
    'order_qty': np.random.randint(1, 10, num_orders)
})

# Add bad data to orders
df_orders.loc[np.random.choice(df_orders.index, 10000), 'customer_id'] = "abc"

initial_order_count = len(df_orders)
print(f"Processing {initial_order_count} order records...")

# Clean customer_id
df_orders['customer_id'] = pd.to_numeric(df_orders['customer_id'], errors='coerce').fillna(999999).astype(int)

# Drop duplicates
df_orders = df_orders.drop_duplicates(subset=["order_id", "order_placement_date", "customer_id", "product_id", "order_qty"])
final_order_count = len(df_orders)

end_time = time.time()
processing_time = end_time - start_time

print("\n" + "="*50)
print("RESUME METRICS GENERATED")
print("="*50)
print(f"Total Rows Processed: {initial_customer_count + initial_order_count:,}")
print(f"Processing Time: {processing_time:.2f} seconds")
print(f"Data Quality Improvements: Removed {initial_customer_count - after_dedup_count:,} duplicate customers, normalized {null_cities:,} missing/invalid location identifiers")
print(f"Fact Table Final Row Count: {final_order_count:,}")
print(f"Data Processing Throughput: {((initial_customer_count + initial_order_count) / processing_time):,.0f} rows/second")
print("="*50)
