import datetime

# DATES INTERVAL
start = datetime.date(2023,4,24)
end = datetime.date(2023,4,27)

# Parameters for calls and puts on "Eurex Dow Jones UBS Commodity Index Option" on maturity DEC23
## MATURITY
maturity_dec23 = datetime.date(2023, 12, 22)
## CALLS
rics_dict_call_dec23 = {'FCCO1800L3.EX': [180, maturity_dec23, 'CALL'],
                        'FCCO1700L3.EX': [170, maturity_dec23, 'CALL'],
                        'FCCO1600L3.EX': [160, maturity_dec23, 'CALL'],
                        'FCCO1500L3.EX': [150, maturity_dec23, 'CALL'],
                        'FCCO1400L3.EX': [140, maturity_dec23, 'CALL'],
                        'FCCO1350L3.EX': [135, maturity_dec23, 'CALL'],
                        'FCCO1300L3.EX': [130, maturity_dec23, 'CALL'],
                        'FCCO1250L3.EX': [125, maturity_dec23, 'CALL'],
                        'FCCO1200L3.EX': [120, maturity_dec23, 'CALL'],
                        'FCCO1150L3.EX': [115, maturity_dec23, 'CALL'],
                        'FCCO1100L3.EX': [110, maturity_dec23, 'CALL'],
                        'FCCO1050L3.EX': [105, maturity_dec23, 'CALL'],
                        'FCCO1000L3.EX': [100, maturity_dec23, 'CALL'],
                        'FCCO950L3.EX': [95, maturity_dec23, 'CALL'],
                        'FCCO900L3.EX': [90, maturity_dec23, 'CALL'],
                        'FCCO850L3.EX': [85, maturity_dec23, 'CALL'],
                        'FCCO800L3.EX': [80, maturity_dec23, 'CALL'],
                        'FCCO750L3.EX': [75, maturity_dec23, 'CALL'],
                        'FCCO700L3.EX': [70, maturity_dec23, 'CALL'],
                        'FCCO650L3.EX': [65, maturity_dec23, 'CALL'],
                        'FCCO600L3.EX': [60, maturity_dec23, 'CALL'],
                        'FCCO550L3.EX': [55, maturity_dec23, 'CALL'],
                        'FCCO500L3.EX': [50, maturity_dec23, 'CALL'],
                        'FCCO480L3.EX': [48, maturity_dec23, 'CALL'],
                        'FCCO460L3.EX': [46, maturity_dec23, 'CALL']
                       }
## PUTS
rics_dict_put_dec23 = {'FCCO1800X3.EX': [180, maturity_dec23, 'PUT'],
                       'FCCO1700X3.EX': [170, maturity_dec23, 'PUT'],
                       'FCCO1600X3.EX': [160, maturity_dec23, 'PUT'],
                       'FCCO1500X3.EX': [150, maturity_dec23, 'PUT'],
                       'FCCO1400X3.EX': [140, maturity_dec23, 'PUT'],
                       'FCCO1350X3.EX': [135, maturity_dec23, 'PUT'],
                       'FCCO1300X3.EX': [130, maturity_dec23, 'PUT'],
                       'FCCO1250X3.EX': [125, maturity_dec23, 'PUT'],
                       'FCCO1200X3.EX': [120, maturity_dec23, 'PUT'],
                       'FCCO1150X3.EX': [115, maturity_dec23, 'PUT'],
                       'FCCO1100X3.EX': [110, maturity_dec23, 'PUT'],
                       'FCCO1050X3.EX': [105, maturity_dec23, 'PUT'],
                       'FCCO1000X3.EX': [100, maturity_dec23, 'PUT'],
                       'FCCO950X3.EX': [95, maturity_dec23, 'PUT'],
                       'FCCO900X3.EX': [90, maturity_dec23, 'PUT'],
                       'FCCO850X3.EX': [85, maturity_dec23, 'PUT'],
                       'FCCO800X3.EX': [80, maturity_dec23, 'PUT'],
                       'FCCO750X3.EX': [75, maturity_dec23, 'PUT'],
                       'FCCO700X3.EX': [70, maturity_dec23, 'PUT'],
                       'FCCO650X3.EX': [65, maturity_dec23, 'PUT'],
                       'FCCO600X3.EX': [60, maturity_dec23, 'PUT'],
                       'FCCO550X3.EX': [55, maturity_dec23, 'PUT'],
                       'FCCO500X3.EX': [50, maturity_dec23, 'PUT'],
                       'FCCO480X3.EX': [48, maturity_dec23, 'PUT'],
                       'FCCO460X3.EX': [46, maturity_dec23, 'PUT']
                      }
