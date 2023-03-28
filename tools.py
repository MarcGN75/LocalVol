import csv

fav_path = 'C:/Users/MarcNogueira/Documents/test_csv/'
def create_new_csv(csv_file, path=fav_path):
    with open(path + csv_file, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        csvfile.close()

    return path + csv_file

def find_rate(yield_curve, ttm):
    diff = 100000
    for i in range(len(yield_curve[0])):
        temp_diff = yield_curve[0, i] - ttm
