from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///project.db")
connection = engine.connect()

starting_path = "../raw_data"

car_details_df = pd.read_csv(f"../raw_data/CarDetails.csv")

car_details_df.to_sql("Car Details", con=connection, if_exists="replace", index=False)

connection.close()