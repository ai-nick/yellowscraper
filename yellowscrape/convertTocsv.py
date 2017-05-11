import pandas as pd

infile = pd.read_json("archUS2.json")
infile.to_csv('archeryMail_2.csv')