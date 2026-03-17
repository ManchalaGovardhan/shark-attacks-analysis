🦈 Shark Attack Data Analysis
📌 What is Shark Attack Data?
        
        Shark attack data contains records of incidents involving sharks across the world.
        It helps analyze patterns, risks, and trends related to human-shark interactions.
        
        Covers multiple years of incidents
        
        Includes location, activity, injury type
        
        Helps identify high-risk areas
        
        Useful for safety awareness and research

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
