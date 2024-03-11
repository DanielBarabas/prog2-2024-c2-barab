import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv("input.csv")
    query_df = pd.read_csv("query.csv")

    damage_types = df["dmg_type"].unique()
    out = []
    for idx, row in query_df.iterrows():
        out_row = {}
        for dt in damage_types:
            sub_df = df.loc[
                (df["dmg_type"] == dt)
                & (df["dmg"] >= row["dmg_min"])
                & (df["dmg"] <= row["dmg_max"]),
                ["x", "y", "dmg"],
            ]
            if sub_df.empty:
                out_row[dt] = 0
            else:
                diffs = ((sub_df[["x", "y"]] - row) ** 2).sum(axis=1)
                out_row[dt] = sub_df.iloc[diffs.argmin(), 2]
            #print(out_row)

        out.append(out_row)

    pd.DataFrame(out).to_csv("out.csv", index=False)
