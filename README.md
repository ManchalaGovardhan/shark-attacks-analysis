🦈 Shark Attack Data Analysis
📌 What is Shark Attack Data?
        
        Shark attack data contains records of incidents involving sharks across the world.
        It helps analyze patterns, risks, and trends related to human-shark interactions.
        
        Covers multiple years of incidents
        
        Includes location, activity, injury type
        
        Helps identify high-risk areas
        
        Useful for safety awareness and research
        🦈 Shark Attack Data Analysis
📌 Overview

Shark attack data consists of recorded incidents involving human-shark interactions across the globe. This project analyzes historical data to identify patterns, trends, and high-risk factors such as location, activity, and injury type. It helps improve awareness and supports data-driven safety insights.

❗ Problem Statement

Analyzing shark attack data is challenging due to inconsistent records, missing values, and scattered data sources. This project aims to build a structured system that collects, cleans, and visualizes shark attack data to uncover meaningful insights and trends for better understanding and decision-making.

⚙️ Project Workflow (End-to-End System)

This project is designed as a data entry + cleaning + visualization pipeline:

User interacts via Streamlit App
Data is stored in a database (raw layer)
Data is cleaned and transformed using Excel Power Query
Cleaned data is visualized in an interactive Excel dashboard
Insights are updated dynamically

⚙️ How the Project Works (End-to-End Flow)

This project is designed as a data entry + cleaning + visualization system.

                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit App      │
                    │──────────────────────│
                    │ • Add New Data       │
                    │ • View Insights      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Database        │
                    │  (Stores Raw Data)   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Excel (Power Query)│
                    │──────────────────────│
                    │ • Data Cleaning      │
                    │ • Transformation     │
                    │ • Auto Refresh       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Excel Dashboard    │
                    │──────────────────────│
                    │ • Visual Insights    │
                    │ • Trends Analysis    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Real-Time Insights │
                    └──────────────────────┘
🔹 1. User Interaction (Streamlit App)
        
        Users interact through a Streamlit application:
        
        Features:
        
        Add new shark attack records
        
        View key insights
        
        Simple and user-friendly interface

🔹 2. Database Layer

        Stores raw shark attack data
        
        Data inserted via Streamlit
        
        Acts as the central data source

🔹 3. Data Cleaning (Excel Power Query)

        Cleaning handled in Excel using Power Query
        
        Automatically processes:
        
        Missing values
        
        Incorrect data
        
        Duplicate records

👉 Data updates automatically when refreshed

🔹 4. Data Visualization (Excel Dashboard)
      
      Interactive dashboard built in Excel
      
      Provides:
      
      Attack trends over time
      
      Location-based analysis
      
      Injury severity insights

🔹 5. Real-Time Updates

      When new data is added:
      
      Data is inserted into database
      
      Excel fetches updated data
      
      Power Query cleans data
      
      Dashboard updates on refresh
      🛠️ Tech Stack
Programming: Python
Framework: Streamlit
Database: SQL (or relational database)
Data Processing: Excel (Power Query)
Visualization: Excel Dashboard
📈 Results & Insights
Built an automated data pipeline for continuous updates
Identified high-risk locations and common activities during attacks
Improved data quality using Power Query transformations
Delivered interactive dashboards for easy analysis
🔮 Future Improvements
Integrate Power BI for advanced dashboards
Add predictive analytics for risk estimation
Deploy Streamlit app on cloud
Include real-time API-based data sources
👤 Author

Manchala Govardhan

ph:7671939221
mail:manchalagovardhan91@gmail.com

