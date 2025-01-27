import pandas as pd
import json

with open('t20_json_files/t20_wc_match_results.json') as f:
    data = json.load(f)
 

df_match = pd.DataFrame(data[0]['matchSummary'])
df_match.head()

df_match.rename({'scorecard': 'match_id'}, axis=1, inplace=True)
df_match.head()

# betting summary
with open('t20_json_files/t20_wc_batting_summary.json') as f:
    data = json.load(f)
    all_records = []

    for rec in data:
        all_records.extend(rec['battingSummary'])
# print(all_records)


df_batting = pd.DataFrame(all_records)

# print(df_batting.head(11))

df_batting["out/not_out"] = df_batting.dismissal.apply(lambda x: "out" if len(x) >0 else "not out")

df_batting.drop(columns=['dismissal'], inplace=True)

# df_batting.head(10)

df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace('\xa0',''))
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace('â€',''))
# print(df_batting.head(11))

match_ids_dist ={}
for index, row in df_match.iterrows():
    key1 = row['team1'] + 'Vs' + row['team2']
    key2 = row['team2'] + 'Vs' + row['team1']

    match_ids_dist[key1] = row['match_id']
    match_ids_dist[key2] = row['match_id']
# print(match_ids_dist)
    