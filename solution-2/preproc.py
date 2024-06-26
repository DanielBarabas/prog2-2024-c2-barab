import pandas as pd
from scipy import spatial
import pickle
import numpy as np

df = pd.read_csv("input.csv")
tree_dict = {}
tree_dict1 = {}
for dt in df["dmg_type"].unique():
    inner_dict = {}
    for dmg in df["dmg"].unique():
                            
        tree = spatial.cKDTree(df.loc[(df["dmg_type"] == dt)&
                                      (df["dmg"] == dmg),["x","y"]])
        inner_dict[dmg] = tree

    tree = spatial.cKDTree(df.loc[(df["dmg_type"] == dt),["x","y"]])
    tree_dict[dt] = inner_dict
    tree_dict1[dt] = tree

with open("smalltrees.pkl","wb") as file:
    pickle.dump(tree_dict,file)
with open("bigtrees.pkl","wb") as file:
    pickle.dump(tree_dict1,file)
with open("dtypes.npy","wb") as file:
    np.save(file,df["dmg_type"].unique(),allow_pickle=True)
df[["dmg_type","dmg"]].to_parquet("dmgs.parquet")