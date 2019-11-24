import pandas as pd
data = pd.read_csv('grades.csv')
data["Total"]= (0.25*data["Final"]+0.75*data["MidTerm"])
print(data)
data.to_csv("new-grades.csv")
