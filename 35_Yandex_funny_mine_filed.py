import pprint
from IPython.display import display

def yandex_funny_mines(mnk, k):
    filed = []
    for i in range(mnk[0]):
        filed.append([0 for j in range(mnk[1])])
    for x, y in k:
        filed[x - 1][y - 1] = '*'
    for i in range(len(filed)):
        for j in range(len(filed[i])):
            if filed[i][j] != '*':
                if i == 0 and j == 0:
                    if filed[i + 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j + 1] == '*':
                        filed[i][j] += 1
                elif i == 0 and j == len(filed[i]) - 1:
                    if filed[i + 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j - 1] == '*':
                        filed[i][j] += 1
                elif i == len(filed) - 1 and j == 0:
                    if filed[i - 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                elif i == len(filed) - 1 and j == len(filed[i]) - 1:
                    if filed[i - 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j - 1] == '*':
                        filed[i][j] += 1
                elif i == 0:
                    if filed[i][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j + 1] == '*':
                        filed[i][j] += 1
                elif i == len(filed) - 1:
                    if filed[i][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j + 1] == '*':
                        filed[i][j] += 1
                elif j == 0:
                    if filed[i - 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j] == '*':
                        filed[i][j] += 1
                elif j == len(filed[i]) - 1:
                    if filed[i - 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j] == '*':
                        filed[i][j] += 1
                else:
                    if filed[i - 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i - 1][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j + 1] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j] == '*':
                        filed[i][j] += 1
                    if filed[i + 1][j - 1] == '*':
                        filed[i][j] += 1
                    if filed[i - 11][j] == '*':
                        filed[i][j] += 1
    pprint.pprint(filed, width=20)

yandex_funny_mines((3,2,2), ((3, 1), (1 , 2)))