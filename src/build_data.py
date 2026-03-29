import pandas as pd
import numpy as np
from functools import reduce

barttorvik_away_neutral = pd.read_csv('../data/2026/Raw/Barttorvik Away-Neutral.csv')
barttorvik_home = pd.read_csv('../data/2026/Raw/Barttorvik Home.csv')
evanMiya = pd.read_csv('../data/2026/Raw/EvanMiya.csv')
heat_check = pd.read_csv('../data/2026/Raw/Heat Check Tournament Index.csv')
kenPom = pd.read_csv('../data/2026/Raw/KenPom Barttorvik.csv')
rppf = pd.read_csv('../data/2026/Raw/RPPF Ratings.csv')
resumes = pd.read_csv('../data/2026/Raw/Resumes.csv')
shooting_splits = pd.read_csv('../data/2026/Raw/Shooting Splits.csv')
teamsheets_ranks = pd.read_csv('../data/2026/Raw/Teamsheet Ranks.csv')
z_rating = pd.read_csv('../data/2026/Raw/Z Rating Teams.csv')


JOIN_KEYS = ['TEAM NO']   # <-- adjust if your column names differ

dfs = [
    barttorvik_away_neutral,
    barttorvik_home,
    evanMiya,
    heat_check,
    kenPom,
    rppf,
    resumes,
    shooting_splits,
    teamsheets_ranks,
    z_rating
]

combined = reduce(lambda left, right: pd.merge(left, right, on=JOIN_KEYS, how='outer'), dfs)

print(f"Combined shape: {combined.shape}")
print(combined.columns.tolist())




