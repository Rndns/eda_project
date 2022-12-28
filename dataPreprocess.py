import csv
import pandas as pd

data01 = pd.read_csv('./csvFile/movieInfo01.csv')
data02 = pd.read_csv('./csvFile/movieInfo02.csv')
data03 = pd.read_csv('./csvFile/movieInfo03.csv')
data04 = pd.read_csv('./csvFile/movieInfo04.csv')
data05 = pd.read_csv('./csvFile/movieInfo05.csv')

data01.drop([data01.columns[0]], axis=1, inplace=True)
data02.drop([data02.columns[0]], axis=1, inplace=True)
data03.drop([data03.columns[0], data03.columns[1]], axis=1, inplace=True)
data04.drop([data04.columns[0]], axis=1, inplace=True)

data05['Actors'] = data05[['Actor00','Actor01','Actor02','Actor03','Actor04','Actor05','Actor06','Actor07','Actor08']].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)

data06 = data05[['Actors']]

data07 = pd.concat([data01,data02,data03,data04,data06], axis=1)

data07.drop([data07.columns[2]], axis=1, inplace=True)
print(data02)

data07.to_csv('./csvFile/movieInfo.csv')

data08 = pd.read_csv('./csvFile/wachaPediaComment.csv')
data09 = pd.read_csv('./csvFile/wachaPediaStar.csv')

data01.drop([data01.columns[0]], axis=1, inplace=True)
data10 = pd.concat([data08, data09], axis=1)

