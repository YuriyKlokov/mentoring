def find_avg_of_spam(actions, removals):
    spam_actions = actions[actions['extra'] == 'spam']
    spam_actions['post_id'] = spam_actions['post_id'].astype(int)
    removals['post_id'] = removals['post_id'].astype(int)
    removals['remove_date'] = pd.to_datetime(removals['remove_date'].str.strip(), format='%Y-%m-%d')
    spam_actions['action_date'] = pd.to_datetime(spam_actions['action_date'].str.strip(), format='%Y-%m-%d')
    spam_actions = spam_actions.merge(removals, on ='post_id', how = 'left' )
    spam_actions = spam_actions.drop(['user_id'], axis=1).drop_duplicates()
    spam_actions_agg = spam_actions.groupby('action_date').agg(count_action_date=('action_date', 'count'), count_remove_date=('remove_date', 'count')).reset_index()
    spam_actions_agg['daily_pecent'] = spam_actions_agg['count_remove_date'] / spam_actions_agg['count_action_date']
    return pd.DataFrame([[spam_actions_agg.daily_pecent.mean().round(2)]], columns = ['average_daily_percent '])