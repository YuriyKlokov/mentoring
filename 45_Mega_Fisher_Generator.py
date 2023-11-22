import random
from collections import defaultdict
import seaborn as sns
import pandas as pd

def generator(array):

    n = len(array)
    for i in range(n, 0, -1):
        j = random.randint(0, i - 1)
        array[i - 1], array[j] = array[j], array[i - 1]
        yield array[i - 1]

q = generator([0, 1, 2, 3])

def generator(array):
    #random.seed(42)
    n = len(array)
    for i in range(n, 0, -1):
        j = random.randint(0, i - 1)
        array[i - 1], array[j] = array[j], array[i - 1]
        yield array[i - 1]

q = generator([0, 1, 2, 3])

print(list(q))

random.seed(41)
def randomize(arr):

    n = len(arr)
    for i in range(n):
        j = random.randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [0, 1, 2, 3]
print(randomize(arr))

dct = defaultdict(int)

for i in range(1000000):
    q = generator([0, 1, 2, 3])
    str_from = ''.join(map(str, q)) 
    dct[str_from] += 1
    
df = pd.DataFrame(dct.items(), columns=['combo', 'amount'])
sns.barplot(x='combo', y='amount', data=df)
