import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv("spotify/data/1uvVSTlB0AytVbrPmpWwfw.csv"))
df.to_json("spotify/data/1uvVSTlB0AytVbrPmpWwfw.json")
print(df)