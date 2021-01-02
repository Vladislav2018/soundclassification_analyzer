import pandas as pd
import datetime
import json

def parse_txt_report(path: str, path_tpl:str, separators: tuple = (':', ',')):
    report = {}
    with open(path) as file:
        tpl = pd.read_csv(path_tpl)
        for row in tpl['predicted_class']:
            report.update({row: []})
        for line in file:
            act_cls = line[line.find(separators[0])+2 : line.find(separators[1])]
            pred_class = line[line.find(separators[1])+2 : ]
            pred_class = pred_class[pred_class.find(separators[0]) + 2:]
            if pred_class.endswith('\n'):
                pred_class = pred_class[:-1]
            tpl_act_cls_row = tpl.loc[tpl['actual_class'] == act_cls]
            tpl_pred_class = tpl_act_cls_row['predicted_class'].values[0]
            if(pred_class == tpl_pred_class):
                report[tpl_pred_class].append(1)
            else:
                report[tpl_pred_class].append(0)
    with open('stat/' + "corresponds" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt', 'w') as file:
        file.write(json.dumps(report))
    return report

def analyze(data):
    vals = data.values()
    k_s = list(data.keys())
    short_report = {}
    i = 0
    for val in vals:
        accurancy = sum(val)/len(val)
        short_report.update({k_s[i]:accurancy})
        i += 1
    with open('stat/' + "short_report" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt', 'w') as file:
        file.write(json.dumps(short_report))
if __name__ == '__main__':
    analyze(parse_txt_report("reports/report_lstm.txt", 'templates/sa_tpl.csv'))