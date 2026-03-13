"""
E-commerce Log Generator
Generates realistic e-commerce transaction logs
"""
import json
import random
from datetime import datetime, timedelta

# Product catalog
PRODUCTS = [
    {"id": "P001", "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": "P002", "name": "Wireless Mouse", "category": "Electronics", "price": 29.99},
    {"id": "P003", "name": "Keyboard", "category": "Electronics", "price": 79.99},
    {"id": "P004", "name": "Monitor", "category": "Electronics", "price": 299.99},
    {"id": "P005", "name": "Headphones", "category": "Electronics", "price": 149.99},
    {"id": "P006", "name": "Office Chair", "category": "Furniture", "price": 249.99},
    {"id": "P007", "name": "Desk", "category": "Furniture", "price": 399.99},
    {"id": "P008", "name": "Bookshelf", "category": "Furniture", "price": 179.99},
    {"id": "P009", "name": "Coffee Maker", "category": "Appliances", "price": 89.99},
    {"id": "P010", "name": "Blender", "category": "Appliances", "price": 59.99},
    {"id": "P011", "name": "Running Shoes", "category": "Sports", "price": 89.99},
    {"id": "P012", "name": "Yoga Mat", "category": "Sports", "price": 29.99},
    {"id": "P013", "name": "Water Bottle", "category": "Sports", "price": 19.99},
    {"id": "P014", "name": "Backpack", "category": "Accessories", "price": 49.99},
    {"id": "P015", "name": "Sunglasses", "category": "Accessories", "price": 79.99},
]

COUNTRIES = ["USA", "UK", "Canada", "Germany", "France", "Australia", "Japan", "India"]
CITIES = {
    "USA": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "UK": ["London", "Manchester", "Birmingham"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"],
    "India": ["Mumbai", "Delhi", "Bangalore"]
}

EVENTS = ["page_view", "add_to_cart", "purchase", "remove_from_cart", "checkout"]
PAYMENT_METHODS = ["credit_card", "debit_card", "paypal", "apple_pay", "google_pay"]


def generate_user_id():
    """Generate random user ID"""
    return f"U{random.randint(1000, 9999)}"


def generate_session_id():
    """Generate random session ID"""
    return f"S{random.randint(100000, 999999)}"


def generate_log_entry(timestamp):
    """Generate a single log entry"""
    product = random.choice(PRODUCTS)
    country = random.choice(COUNTRIES)
    city = random.choice(CITIES[country])
    event = random.choice(EVENTS)

    log_entry = {
        "timestamp": timestamp.isoformat(),
        "user_id": generate_user_id(),
        "session_id": generate_session_id(),
        "event": event,
        "product_id": product["id"],
        "product_name": product["name"],
        "category": product["category"],
        "price": product["price"],
        "quantity": random.randint(1, 5) if event == "purchase" else 1,
        "country": country,
        "city": city,
        "device": random.choice(["desktop", "mobile", "tablet"]),
        "browser": random.choice(["Chrome", "Firefox", "Safari", "Edge"]),
    }

    # Add payment method for purchases
    if event == "purchase":
        log_entry["payment_method"] = random.choice(PAYMENT_METHODS)
        log_entry["status"] = random.choice(["success", "success", "success", "failed"])

    return log_entry


def generate_logs(num_logs=1000, output_file="../logs/ecommerce.log"):
    """Generate multiple log entries"""
    print(f"Generating {num_logs} e-commerce log entries...")

    # Generate logs over the past 7 days
    end_time = datetime.now()
    start_time = end_time - timedelta(days=7)

    logs = []
    for i in range(num_logs):
        # Random timestamp within the time range
        time_delta = (end_time - start_time) * random.random()
        timestamp = start_time + time_delta

        log_entry = generate_log_entry(timestamp)
        logs.append(log_entry)

    # Sort by timestamp
    logs.sort(key=lambda x: x["timestamp"])

    # Write to file
    with open(output_file, 'w') as f:
        for log in logs:
            f.write(json.dumps(log) + '\n')

    print(f"Successfully generated {num_logs} logs!")
    print(f"Output file: {output_file}")

    # Print statistics
    events_count = {}
    for log in logs:
        event = log["event"]
        events_count[event] = events_count.get(event, 0) + 1

    print("\n=== Log Statistics ===")
    for event, count in events_count.items():
        print(f"{event}: {count}")

    # Calculate total revenue
    total_revenue = sum(
        log["price"] * log["quantity"]
        for log in logs
        if log["event"] == "purchase" and log.get("status") == "success"
    )
    print(f"\nTotal Revenue: ${total_revenue:,.2f}")


if __name__ == "__main__":
    generate_logs(num_logs=1000)