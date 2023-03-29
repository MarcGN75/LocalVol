import csv

fav_path = 'C:/Users/MarcNogueira/Documents/test_csv/'
def create_new_csv(csv_file, path=fav_path):
    with open(path + csv_file, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        csvfile.close()

    return path + csv_file

def find_rate(yield_curve, ttm):
    diff = 100000
    for i in range(len(yield_curve)):
        temp_diff = ttm - yield_curve['TimeToMaturity'].loc[i]
        if abs(temp_diff) < diff:
            diff = abs(temp_diff)
            tenor_ind = i
        elif abs(temp_diff) > diff:
            break
    return tenor_ind
