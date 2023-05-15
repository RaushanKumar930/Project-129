import pandas as pd
import numpy as np

bright_stars_df = pd.read_csv("./scraped_data.csv")
brown_dwarf_df = pd.read_csv("./new_scraped_data.csv")

brown_dwarf_df = brown_dwarf_df.fillna(0.0)
#brown_dwarf_df["Mass"] = brown_dwarf_df["Mass"].apply(lambda num : num * 0.000954588)
def cvt(df, col, num):
    brown_dwarf = []
    for i in (df[col]):
        try: 
            brown_dwarf.append(float(i) * num)
            #print(i)
        except:
            brown_dwarf.append(0)
            #print(i)
    #print(brown_dwarf)
    return brown_dwarf

brown_dwarf_df["Radius"] = cvt(brown_dwarf_df, "Radius", 0.102763)
brown_dwarf_df["Mass"] = cvt(brown_dwarf_df, "Mass", 0.00095488)
print(brown_dwarf_df)
print(bright_stars_df)

merge_df = pd.DataFrame(pd.concat([bright_stars_df, brown_dwarf_df], axis=0))
merge_df.to_csv("merged_data.csv")
print(merge_df)
