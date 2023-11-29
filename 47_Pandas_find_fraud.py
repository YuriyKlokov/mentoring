import pandas as pd

data = [[3, 21000],[4, 10400]]
accounts = pd.DataFrame(data, columns=['account_id', 'max_income']).astype({'account_id':'Int64', 'max_income':'Int64'})

data = [[2, 3, 'Creditor', 107100, '2021-06-02 11:38:14'], [4, 4, 'Creditor', 10400, '2021-06-20 12:39:18'], [11, 4, 'Debtor', 58800, '2021-07-23 12:41:55'], [1, 4, 'Creditor', 49300, '2021-05-03 16:11:04'], [15, 3, 'Debtor', 75500, '2021-05-23 14:40:20'],
         [10, 3, 'Creditor', 102100, '2021-06-15 10:37:16'], [14, 4, 'Creditor', 56300, '2021-07-21 12:12:25'], [19, 4, 'Debtor', 101100, '2021-05-09 15:21:49'], [8, 3, 'Creditor', 64900, '2021-07-26 15:09:56'], [7, 3, 'Creditor', 90900, '2021-06-14 11:23:07']]   
transactions = pd.DataFrame(data, columns=['transaction_id', 'account_id', 'type', 'amount', 'day']).astype({'transaction_id':'Int64', 'account_id':'Int64', 'type':'object', 'amount':'Int64', 'day':'datetime64[ns]'})


def find_faud(accounts, transactions):
    transactions.sort_values(by = ['account_id','day', 'type'])
    transactions_only_creditor = transactions[transactions['type'] == 'Creditor']
    transactions_only_creditor['event_month'] = transactions_only_creditor['day'].values.astype('datetime64[M]')
    transactions_aggr = transactions_only_creditor.groupby(['account_id', 'event_month'])['amount'].sum().reset_index()
    transactions_aggr['event_month'].diff(periods=1)
    transactions_aggr = transactions_aggr.merge(accounts, how='inner', on ='account_id')
    transactions_aggr['bigger_then_max'] =  (transactions_aggr['amount'] > transactions_aggr['max_income']).astype(int)
    transactions_aggr['account_id'] = transactions_aggr['account_id'].astype(str)
    transactions_aggr['LAG_mark'] = transactions_aggr.groupby('account_id')['bigger_then_max'].shift(1).fillna(0)
    transactions_aggr['month_check'] = transactions_aggr['event_month'].diff(periods=1)
    transactions_final = transactions_aggr[(transactions_aggr['bigger_then_max'] == 1) & (transactions_aggr['LAG_mark'] == 1.0) & (transactions_aggr ['month_check'] < pd.Timedelta(days=32)) ]['account_id']
    transactions_final.reset_index().drop_duplicates(['account_id'])
    return transactions_final

