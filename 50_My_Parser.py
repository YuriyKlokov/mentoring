
def my_parser(d_str):
    d_str = d_str[2:-1]
    data_string = d_str.split(' | | ')
    data_body = list(map(lambda x: x.split('|'), data_string[2:]))
    data_columns =  data_string[0].split(' | ')
    print(data_string[2:])
    return pd.DataFrame(data_body, columns=data_columns)

w = '| transaction_id | account_id | type | amount | day || -------------- | ---------- | -------- | ------ | ------------------- || 58             | 9          | Debtor   | 34500  | 2021-06-18 17:52:31 || 66             | 2          | Creditor | 12100  | 2021-05-07 17:14:09 || 43             | 15         | Debtor   | 79600  | 2021-06-19 13:09:17 || 9              | 3          | Creditor | 28600  | 2021-05-30 11:33:10 || 29             | 9          | Debtor   | 2700   | 2021-07-08 15:25:40 || 70             | 2          | Creditor | 104200 | 2021-06-07 17:40:02 || 32             | 3          | Debtor   | 3400   | 2021-06-07 14:42:57 || 33             | 3          | Creditor | 32700  | 2021-05-08 10:16:16 || 25             | 3          | Debtor   | 37700  | 2021-07-19 17:15:39 || 1              | 2          | Debtor   | 108600 | 2021-06-24 09:50:52 || 65             | 9          | Debtor   | 107000 | 2021-05-03 15:37:21 || 38             | 15         | Debtor   | 2000   | 2021-05-17 15:41:58 || 27             | 9          | Creditor | 61300  | 2021-07-28 13:00:36 || 60             | 9          | Debtor   | 31800  | 2021-06-13 09:33:50 || 40             | 10         | Creditor | 81700  | 2021-06-18 17:54:06 || 26             | 3          | Debtor   | 65900  | 2021-05-11 17:53:27 || 3              | 10         | Creditor | 50400  | 2021-06-29 16:12:53 || 42             | 16         | Creditor | 94800  | 2021-05-27 17:16:32 || 55             | 2          | Creditor | 77900  | 2021-05-13 13:06:54 || 73             | 3          | Debtor   | 13000  | 2021-06-17 11:18:41 || 54             | 15         | Creditor | 24300  | 2021-07-29 10:36:49 || 5              | 4          | Debtor   | 100900 | 2021-07-29 13:37:09 || 44             | 16         | Creditor | 23100  | 2021-07-28 12:54:50 || 15             | 10         | Creditor | 29600  | 2021-06-18 10:02:07 || 74             | 4          | Debtor   | 78500  | 2021-06-21 09:31:52 || 78             | 2          | Creditor | 30300  | 2021-07-22 09:49:31 || 64             | 16         | Creditor | 90300  | 2021-07-26 12:36:27 || 57             | 9          | Debtor   | 8600   | 2021-05-13 12:19:53 || 53             | 15         | Creditor | 13300  | 2021-06-15 14:26:01 || 79             | 16         | Debtor   | 74000  | 2021-05-29 09:16:28 || 46             | 2          | Creditor | 96000  | 2021-07-02 14:44:38 || 52             | 3          | Creditor | 39800  | 2021-07-23 15:31:01 || 51             | 3          | Creditor | 55500  | 2021-07-10 14:34:32 || 49             | 15         | Debtor   | 85200  | 2021-06-18 12:52:55 || 12             | 14         | Creditor | 106100 | 2021-05-03 13:25:18 || 16             | 9          | Debtor   | 106000 | 2021-05-21 09:39:47 || 56             | 4          | Debtor   | 96900  | 2021-06-07 16:37:55 || 37             | 9          | Creditor | 63300  | 2021-06-19 17:04:54 || 45             | 4          | Creditor | 77000  | 2021-05-28 14:00:42 || 48             | 2          | Creditor | 3900   | 2021-07-01 16:15:16 |'
w = w.replace('||', '| |')

transactions = my_parser(w)