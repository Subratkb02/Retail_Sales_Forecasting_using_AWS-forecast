# Retail Sales Forecasting

This project forecasts future retail store sales using historical transactional data and Amazon Web Services (AWS) Forecast, a fully managed service that uses machine learning to deliver highly accurate time-series forecasts. It involves a full data pipeline starting from data preprocessing, exploratory data analysis (EDA), feature engineering, and model training using AWS Forecast. The primary goal is to    help retail businesses make informed decisions in areas like inventory management, supply chain optimization, seasonal promotions, and budget planning by anticipating customer demand trends. The implementation ensures scalability, cloud integration, and automation potential for real-world retail forecasting systems.

---

## Table of Contents

1. [Project Overview](#1-project-overview)  
2. [Setup](#2-setup)  
3. [Data Preparation](#3-data-preparation)  
4. [Exploratory Data Analysis](#4-exploratory-data-analysis)  
5. [AWS Forecast Integration](#5-aws-forecast-integration)  
6. [File Structure](#6-file-structure)  
7. [Usage](#7-usage)  
8. [Contributing](#8-contributing)  
9. [License](#9-license)  
10. [Acknowledgements](#10-acknowledgements)

---

## 1. Project Overview

The **Retail Sales Forecasting** project leverages historical sales data to predict future trends, aiding in better inventory planning, staffing, and promotions.  
Tech stack: `Python`, `Pandas`, `Matplotlib`, `Seaborn`, `Boto3`, and `AWS Forecast`.

---

## 2. Setup

### 2.1 Clone the Repository

```bash
git clone https://github.com/yourusername/Retail_Sales_Forecasting.git
cd Retail_Sales_Forecasting
````

### 2.2 Set Up Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate     
```

### 2.3 Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn boto3 awscli
```

### 2.4 Configure AWS CLI

```bash
aws configure
```

Make sure your IAM role has access to S3, Forecast, and Forecast permissions.

---

## 3. Data Preparation

### 3.1 Place Raw Data

Place your CSV file in the `data/` directory with the name:

```
data/Sales_data.csv
```

### 3.2 Run Preprocessing Script

```bash
cd scripts
python data_preprocessing.py
```

This will create:

```
data/processed_sales_data.csv
```

> Sample content: `timestamp, item_id, target_value`

---

## 4. Exploratory Data Analysis

### 4.1 Launch Jupyter Notebook

```bash
cd ../notebook
jupyter notebook eda.ipynb
```

### 4.2 Open and Run the Notebook

Run all cells in `eda.ipynb` to visualize sales patterns and trends.

---

## 5. AWS Forecast Integration

### 5.1 Schema File (`schema.json`)

Create a file named `schema.json`:

```json
{
  "Attributes": [
    {"AttributeName": "item_id", "AttributeType": "string"},
    {"AttributeName": "timestamp", "AttributeType": "timestamp"},
    {"AttributeName": "target_value", "AttributeType": "float"}
  ]
}
```

### 5.2 Create Dataset

```bash
aws forecast create-dataset \
  --dataset-name retail_sales \
  --domain RETAIL \
  --dataset-type TARGET_TIME_SERIES \
  --data-frequency "D" \
  --schema file://schema.json \
  --region your-region
```

### 5.3 Create Dataset Import Job

```bash
aws forecast create-dataset-import-job \
  --dataset-import-job-name retail_sales_import \
  --dataset-arn your-dataset-arn \
  --data-source '{"S3Config":{"Path":"s3://your-bucket-name/processed_sales_data.csv","RoleArn":"your-iam-role-arn"}}' \
  --timestamp-format "yyyy-MM-dd" \
  --region your-region
```

Replace:

* `your-dataset-arn`
* `your-bucket-name`
* `your-iam-role-arn`
* `your-region`

---

## 6. 🗂️ File Structure

```
Retail_Sales_Forecasting/
├── data/
│   ├── Sales_data.csv
│   └── processed_sales_data.csv
├── myenv/
├── notebook/
│   └── eda.ipynb
├── scripts/
│   ├── data_preprocessing.py
│   └── forecast_integration.py
├── schema.json
└── README.md
```

---

## 7. 🚀 Usage Summary

1. Clone repository and set up environment
2. Add raw CSV data to `data/`
3. Run preprocessing script
4. Explore data with Jupyter notebook
5. Upload to AWS Forecast and generate predictions

---

## 8. 🤝 Contributing

### 8.1 Fork & Clone

```bash
git fork https://github.com/Subratkb02/Retail_Sales_Forecasting_using_AWS-forecast.git
git clone https://github.com/Subratkb02/Retail_Sales_Forecasting_using_AWS-forecast.git
```

### 8.2 Create Feature Branch

```bash
git checkout -b feature/YourFeature
```

### 8.3 Commit & Push

```bash
git commit -m "Add new feature"
git push origin feature/YourFeature
```

### 8.4 Submit Pull Request

Open a PR from your fork to the main repository.

---

## 9. 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 10. 🙏 Acknowledgements

* [AWS Forecast Documentation](https://docs.aws.amazon.com/forecast/)
* [Pandas](https://pandas.pydata.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Boto3 (AWS SDK for Python)](https://boto3.amazonaws.com/)

