import json
import filepathgen as fg

### currencynames and exchangerates are saved in currencylist.json ###
### try to load json, if not existing or found, empty dict is created to save information ###
try:
    js_path = fg.current_directory+'/currencylist.json'
    with open(js_path, 'r', encoding='utf-8') as file:
        cur_dict = json.load(file)
except:
    cur_dict = {}

### add currencies and exchangerates to loaded json/dict or to empty dict ###
def currency_lister(name, rate):
    cur_dict[name.upper()] = rate
    json_dumper()

### save dict to json ###
def json_dumper():
    output_file = 'currencylist.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cur_dict, f, indent=4, ensure_ascii=False)

### extract names of currencies and save to list, return list ###
def currency_name_giver():
    cur_names = []

    for names in cur_dict.keys():
        cur_names.append(names)

    return cur_names

### return exchangerate of given currency (currency_name) ###
def exchangerate_giver(currency_name):
    return cur_dict[currency_name]

### save last used currency to list ###
def cur_saver(currency_name):
    last_dict = {'last_saved':currency_name}
    output_file = 'last_used_currency.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(last_dict, f, indent=4, ensure_ascii=False)
