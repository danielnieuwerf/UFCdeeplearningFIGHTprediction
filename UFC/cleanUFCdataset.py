# Load csv file into pandas dataframe
import pandas as pd

# Column names we wish to use in our NN:
column_names = ["Winner", "B_current_lose_streak", "B_current_win_streak", "B_longest_win_streak", "B_losses", "B_wins", "B_Height_cms", "B_Reach_cms",	"B_Weight_lbs", "R_current_lose_streak", "R_current_win_streak", "R_longest_win_streak", "R_losses", "R_wins", "R_Height_cms", "R_Reach_cms", "R_Weight_lbs", "B_age", "R_age"]

# load dataframe from UFCdata.csv only using columns specified in column_names
df = pd.read_csv("UFC/UFCdata.csv", delimiter = ",", usecols= column_names)
# print(df)   # Print dataframe

