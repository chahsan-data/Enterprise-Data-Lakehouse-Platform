# Making an unified Lakehouse Data Platform for Post-Acquisition Analytics (Databricks + AWS S3)


## Project Overview
Atliqon, a well-established parent company, recently acquired SportsBar. While Atliqon’s data systems were mature and well-managed, SportsBar’s data existed in unstructured CSV files with no proper data pipelines.

This project focuses on building a **scalable, unified data platform** using **Databricks and Amazon S3**, enabling Atliqon to efficiently manage, analyze, and generate insights across both companies using a **Lakehouse + Medallion Architecture**.

---

## Architecture Overview
The solution follows the **Medallion Architecture**:

- **Bronze Layer** – Raw data ingestion from Amazon S3
- **Silver Layer** – Data cleaning, validation, and standardization
- **Gold Layer** – Business-ready datasets and denormalized views for analytics

Delta Lake is used across Silver and Gold layers to enable **ACID transactions**, **schema enforcement**, and **incremental processing**.

---

## Tech Stack
- **Databricks**
- **Apache Spark (PySpark & Spark SQL)**
- **Amazon S3**
- **Delta Lake**
- **SQL**
- **Databricks Jobs (Automation)**
- **Databricks Dashboards**

---

## Data Pipeline Flow

1. SportsBar data ingested as CSV files into **Amazon S3**
2. Data loaded into Databricks Bronze tables
3. Historical data processed via **manual backfill**
4. Incremental batch updates handled via **automated Databricks Jobs**
5. Data transformed and cleaned in Silver layer
6. Business aggregations and denormalized views created in Gold layer
7. Unified dashboards built for business analysis

---

## Data Processing Strategy

### Historical Backfill
- Initial full load of historical SportsBar data
- Manually triggered notebooks
- Stored as Delta tables

### Incremental Batch Processing
- Automated Databricks Jobs
- Processes only new or updated records
- Ensures efficient and scalable updates

---

## Analytics & Business Insights
A **denormalized Gold view** was created to unify Atliqon and SportsBar data, enabling:

- Cross-company performance analysis
- Unified sales and operational insights
- Simplified reporting for stakeholders

Interactive dashboards were built in Databricks to visualize key business KPIs and trends.

## ⚠️ Disclaimer
This project is a **fictional case study** created for learning and portfolio purposes.
Any company names, datasets, or scenarios mentioned (including *Atliqon* and *SportsBar*)
are **not real** and do not represent any actual organization.
