from sqlalchemy import create_engine
from sqlalchemy import text


# connecting to database
def connect_to_db():
    server = "GOVARDHAN\\SQLEXPRESS"
    database = "shark_data"

    engine = create_engine(
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&Encrypt=yes"
    "&TrustServerCertificate=yes"
    )


    return engine
connection =connect_to_db().connect()
#------------calling stored procedure add shark data----------------------

def add_attack(connection,
               Date, Type, Country, Area, Location, Activity,
               Name, Sex, Age, Injury, FatalYN, Time, Species):

    AddAttack_call = text("""
        EXEC AddAttack
        :Date, :Type, :Country, :Area, :Location, :Activity,
        :Name, :Sex, :Age, :Injury, :FatalYN, :Time, :Species
    """)

    params = {
        "Date": Date,
        "Type": Type,
        "Country": Country,
        "Area": Area,
        "Location": Location,
        "Activity": Activity,
        "Name": Name,
        "Sex": Sex,
        "Age": Age,
        "Injury": Injury,
        "FatalYN": FatalYN,
        "Time": Time,
        "Species": Species
    }

    connection.execute(AddAttack_call, params)
    connection.commit()

# creating function for seeing history
# getting unique years
def dist_attack_year(connection):
    query = text("""
        SELECT DISTINCT YEAR([Date]) AS Year
        FROM dbo.[attacks$]
        WHERE [Date] IS NOT NULL
        ORDER BY Year
    """)
    result = connection.execute(query)
    return result.fetchall()
def attack_history(connection, Year):
    query = text("""
        SELECT *
        FROM dbo.[attacks$]
        WHERE YEAR([Date]) = :Year
        ORDER BY [Date]
    """)
    result = connection.execute(query, {"Year": Year})
    return result.fetchall()

