import pandas as pd

data = pd.read_csv("./horario_12_02_2020.csv", sep=';')

data = data[data.MAGNITUD == 8]

data = data.drop(['V01', 'V02', 'V03', 'V04', 'V05', 'V06', 'V07', 'V08', 'V09', 'V10', 'V11', 'V12',
                  'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24'], axis=1)

data.insert(5, "DATE", data.ANO)
data['DATE'] = data['ANO'].astype(
    str) + '-' + data['MES'].astype(str) + '-' + data['DIA'].astype(str)

data = data.drop(['ANO', 'MES', 'DIA', 'PROVINCIA', 'MUNICIPIO',
                  'ESTACION', 'MAGNITUD', 'PUNTO_MUESTREO'], axis=1)

date = data['DATE'].values[0]
data = data.drop(['DATE'], axis=1)

data = data.add_prefix(date + "-")
data = data.T

data.index.name = 'idx'
data.reset_index(inplace=True)
data.columns = ['date', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']

data.to_csv('processed.csv', index=False)
