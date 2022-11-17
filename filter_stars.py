import plotly.express as px
import pandas as pd
import matplotlib

#info = pd.read_csv('./Nuevo.csv')
info = pd.read_csv('./star_with_gravity.csv')
stars = pd.DataFrame(info)
stars.info()

bools =[]
for d in stars.Distance:
    if d<=100:
        bools.append(True)
    else:
        bools.append(False)

is_dist = pd.Series(bools)

star_dist=stars[is_dist]
star_dist.reset_index(inplace=True,drop=True)
star_dist.shape

gravity_bool = []
for g in star_dist.Gravity:
    if g<=350 and g>=150:
        gravity_bool.append(True)
    else :
        gravity_bool.append(False)

is_gravity = pd.Series(gravity_bool)

final_stars = star_dist[is_gravity]
final_stars.shape
final_stars.reset_index(inplace=True,drop=True)

print(final_stars)
final_stars.to_csv("filtered_stars.csv")