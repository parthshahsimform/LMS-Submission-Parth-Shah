# # Ecom360 - End-to-End E-Commerce Data Engineering Pipeline

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange?logo=amazonaws)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue?logo=snowflake)
![dbt](https://img.shields.io/badge/dbt-Transformations-orange?logo=dbt)
![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-red?logo=apacheairflow)
![Snowpipe](https://img.shields.io/badge/Snowflake-Snowpipe-blue)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-blue?logo=tableau)
![Parquet](https://img.shields.io/badge/Format-Parquet-green)
![Medallion Architecture](https://img.shields.io/badge/Architecture-Bronze%20%7C%20Silver%20%7C%20Gold-gold)
![Production Ready](https://img.shields.io/badge/Production-Ready-success)

</p>

---

## Project Overview

**Ecom360** is a production-grade data engineering project that simulates a modern e-commerce platform and processes data through a fully automated analytics pipeline.

The project demonstrates how modern data engineering technologies work together to transform raw business events into trusted analytical datasets and actionable business insights.

---

##  Architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/parthshahsimform/LMS-Submission-Parth-Shah/main/Proof%20Of%20Concept/project_architecture.png" alt="Ecom360 Architecture" width="100%">
</p>

---

##  Pipeline Flow

```text
Python + Faker
       │
       ▼
    AWS S3
       │
       ▼
   Snowpipe
       │
       ▼
Snowflake Bronze
       │
       ▼
   dbt Silver
       │
       ▼
    dbt Gold
       │
       ▼
Apache Airflow
       │
       ▼
Tableau Dashboard
```

---

##  Business Problem

Modern e-commerce businesses generate large volumes of:

* Customer data
* Product data
* Order transactions
* Customer reviews

Without a centralized analytics platform:

* Revenue reporting becomes delayed.
* Customer insights become difficult.
* Product performance lacks visibility.
* Decision-making relies on manual analysis.

### Solution

Ecom360 solves these challenges using a modern ELT architecture built on AWS, Snowflake, dbt, Airflow, and Tableau.

---

#  End-to-End Data Pipeline

## 1️. Synthetic Data Generation

Generate realistic e-commerce datasets using Python and Faker.

### Generated Entities

* Customers
* Products
* Orders
* Reviews

### Output Files

```text
customers.parquet
products.parquet
orders.parquet
reviews.parquet
```

---

## 2️. Data Lake Storage (AWS S3)

Raw Parquet files are uploaded to Amazon S3.

```text
s3://ecom-raw-data/
```

### Folder Structure

```text
customers/
products/
orders/
reviews/
```

---

## 3️. Real-Time Ingestion (Snowpipe)

Snowpipe automatically ingests incoming files from S3 into Snowflake.

### Features

* Event-Driven Ingestion
* Auto-Ingest
* SQS Notifications
* Near Real-Time Processing
* No Manual COPY Commands

---

## 4️. Bronze Layer (Raw Data)

Raw immutable source tables stored in Snowflake.

### Tables

```sql
RAW_CUSTOMERS
RAW_PRODUCTS
RAW_ORDERS
RAW_REVIEWS
```

### Purpose

* Preserve source data
* Historical tracking
* Incremental processing
* Data recovery

---

## 5️. Silver Layer (Data Cleaning & Standardization)

Data is cleaned, validated, and standardized using dbt.

### Transformations

* Data Type Casting
* Null Handling
* Deduplication
* Data Validation
* Business Rule Enforcement

### Models

```sql
stg_customers
stg_products
stg_orders
stg_reviews
```

---

## 6️. Gold Layer (Business Models)

Business-ready analytical models optimized for reporting and BI.

### Fact & Dimension Models

```sql
dim_customers
dim_products
fct_orders
fct_reviews
```

### Advanced Analytics Models

```sql
customer_ltv
customer_rfm
customer_cohorts
```

### Features

* Star Schema
* Customer Lifetime Value (CLV)
* RFM Segmentation
* Cohort Analysis
* SCD Type 2 Snapshots

---

## 7️. Workflow Orchestration (Apache Airflow)

Airflow automates the complete data pipeline.

### DAG Flow

```text
Generate Data
      │
      ▼
Upload to S3
      │
      ▼
Wait for Snowpipe
      │
      ▼
Run dbt Build
      │
      ▼
Execute Tests
      │
      ▼
Send Alerts
```

---

## 8️. Analytics & Visualization

Tableau connects directly to the Snowflake Gold Layer.

### Dashboard Modules

*  Executive Dashboard
*  Customer Analytics
* Product Analytics
*  Operational Monitoring

---

#  Key Analytics

## Revenue Analytics

* Monthly Revenue Trend
* Revenue by Category
* Average Order Value (AOV)
* Revenue Growth Analysis

## Customer Analytics

* Customer Lifetime Value (CLV)
* RFM Segmentation
* Cohort Analysis
* Conversion Rate
* New vs Returning Customers

## Product Analytics

* Top Selling Products
* Category Performance
* SKU Revenue Analysis
* Product Ratings Analysis

---

#  Data Quality & Governance

Implemented using dbt.

## Data Quality Tests

* `not_null`
* `unique`
* `relationships`
* `accepted_values`

## Governance Features

* Source Freshness Monitoring
* Data Lineage
* dbt Documentation
* SCD Type 2 Tracking
* Automated Validation

---

#  Dashboard KPIs

The Tableau dashboard provides visibility into:

* Revenue
* Orders
* Average Order Value
* Conversion Rate
* Customer Lifetime Value
* Revenue by Category
* Top Products
* Returning Customer %
* Customer Segments

---

#  Future Improvements

* Kafka Streaming Integration
* Great Expectations for Data Validation
* GitHub Actions CI/CD
* Customer Churn Prediction
* Product Recommendation Engine
* Reverse ETL
* Real-Time Analytics

---

#  Author

**Parth Shah**

Built to demonstrate a production-grade Modern Data Stack implementation using:

* Snowflake
* dbt Cloud
* Apache Airflow
* AWS S3
* Snowpipe
* Tableau

---

**If you found this project useful, consider giving it a star ⭐!**
