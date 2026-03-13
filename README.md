# E-commerce Log Analytics with ELK Stack - MLOps LAB4

## Project Description
A log analytics system using ELK Stack (Elasticsearch, Logstash, Kibana) to monitor and analyze e-commerce transactions in real-time. The system processes 1,000+ transaction logs and provides interactive dashboards for business insights.

## My Modifications
Instead of basic log monitoring, I created:
- **E-commerce transaction analytics** with real customer behavior data
- **1,000 transaction logs** across 15 products and 5 categories
- **Real-time dashboards** showing sales, revenue, and product trends
- **Automated log processing** with Logstash filtering and enrichment
- **Interactive Kibana visualizations** for business intelligence

## Technologies Used
- **Elasticsearch 8.11.0** - Search and analytics engine
- **Logstash 8.11.0** - Log processing pipeline
- **Kibana 8.11.0** - Data visualization
- **Docker & Docker Compose** - Containerization
- **Python** - Log generation script

## Dataset Features
- **Products**: 15 items across Electronics, Furniture, Appliances, Sports, Accessories
- **Events**: page_view, add_to_cart, purchase, remove_from_cart, checkout
- **Locations**: 8 countries, 30+ cities
- **Metrics**: price, quantity, revenue, payment method, device type

## Visualizations Created
1. **Sales by Category** - Bar chart showing product category distribution
2. **Top Products** - Horizontal bar chart of most purchased products  
3. **Transactions Over Time** - Area chart showing transaction trends

All dashboards provide real-time filtering by event type, country, product, and price range with automated revenue calculation.

## How to Run

### Prerequisites
- Docker Desktop installed and running
- At least 4GB RAM allocated to Docker

### Steps
```bash
# 1. Clone repository
git clone https://github.com/afrah123456/mlops-elk-ecommerce-analytics.git
cd mlops-elk-ecommerce-analytics

# 2. Generate logs
cd scripts
python generate_ecommerce_logs.py
cd ..

# 3. Start ELK Stack
docker compose up -d
```

Wait 2-3 minutes, then access Kibana at `http://localhost:5601`

### Stop the system
```bash
docker compose down
```

## Screenshots
Dashboard visualizations and analytics are available in the `output/` folder.

## Author
Afrah Fathima

## Course
MLOps (IE-7374) - LAB4