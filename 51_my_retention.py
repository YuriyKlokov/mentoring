def my_retention(activity_df):
    activity_gr = activity_df.groupby(['player_id']).agg(first_date = ('event_date', 'min')).reset_index()
    activity_gr['first_date'] = activity_gr['first_date'] + pd.Timedelta(days=1)
    activity_mrg = activity.merge(activity_gr, how = 'left', left_on = 'player_id', right_on = 'player_id')
    activity_mrg['mark'] = (activity_mrg['event_date'] == activity_mrg['first_date']).astype(int)
    activity_result = round(activity_mrg['mark'].sum() / activity_mrg['player_id'].nunique(),2)
    return [[activity_result]]
