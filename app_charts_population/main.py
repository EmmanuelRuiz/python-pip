import utils
import read_csv
import charts

def run():
    #Leer csv
    data = read_csv.read_csv('./app/data.csv')
    #filtramos por columna donde el continente será south america
    data = list(filter(lambda item : item['Continent'] == 'South America', data))
