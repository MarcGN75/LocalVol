import import_data as ImpData
import import_data_param as ImpDataParam


rics_dict = ImpDataParam.rics_dict_call_dec23
maturity = 'DEC23'
option_type = 'CALL'
start = ImpDataParam.start
end = ImpDataParam.end

df_ubs_commo_index = ImpData.get_option_data_all_strikes(rics_dict, maturity, option_type, start, end)
ImpData.print_data_to_csv(df_ubs_commo_index, 'TEST UBS.csv')
