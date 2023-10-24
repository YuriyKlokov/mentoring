import pandas as pd


data = [[1, 'Nadal'], [2, 'Federer'], [3, 'Novak']]
players = pd.DataFrame(data, columns=['player_id', 'player_name']).astype({'player_id':'Int64', 'player_name':'object'})
data = [[2018, 1, 1, 1, 1], [2019, 1, 1, 2, 2], [2020, 2, 1, 2, 2]]
championships = pd.DataFrame(data, columns=['year', 'Wimbledon', 'Fr_open', 'US_open', 'Au_open']).astype({'year':'Int64', 'Wimbledon':'Int64', 'Fr_open':'Int64', 'US_open':'Int64', 'Au_open':'Int64'})


for column in championships.columns:
    counts_df = championships[column].value_counts().reset_index()
    counts_df.columns = ['player_id', f'{column}_counts']
    players = players.merge(counts_df, on='player_id', how='left')  
    
players = players.fillna(0)
players['total'] = players['Wimbledon_counts'] + players['Fr_open_counts'] + players['US_open_counts'] +  players['Au_open_counts']
players['total'] = players['total'].astype(int) 
players = players.query('total > 0')
players  = players.loc[:, ['player_name', 'total']]
print(players)




