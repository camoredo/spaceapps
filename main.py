# pip install pandas

import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

names = os.listdir(os.path.join(dir_path, 'inputs'))

scatter_dfs = []
heatmap_dfs = []

count = [0, 0]

for name in names:
    if not name.endswith('.txt'):
        continue
    inp_path = os.path.join(dir_path, 'inputs', name)

    df = pd.read_csv(inp_path, delim_whitespace=True)
    df = df[['Longitude', 'Latitude']]
    df.columns = ['lng', 'lat']

    print(name, df.shape)

    scatter_dfs.append(df)
    heatmap_dfs.append(df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'}))

scatter_df = pd.concat(scatter_dfs)
heatmap_df = pd.concat(heatmap_dfs)

json_scatter_data = scatter_df.to_json(orient="records")
with open(os.path.join(dir_path, 'scatter_data.json'), 'w') as f:
    f.write(json_scatter_data)

json_heatmap_data = heatmap_df.to_json(orient="records")
with open(os.path.join(dir_path, 'heatmap_data.json'), 'w') as f:
    f.write(json_heatmap_data)

print(scatter_df.shape)
print(heatmap_df.shape)
