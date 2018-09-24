import csv
from collections import Counter


def main():
    sex_m = [
        'CisMale',
        'CisMan',
        'M',
        'Mail',
        'maile',
        'Make',
        'Mal',
        'Male',
        'Male(CIS)',
        'Male-ish',
        'Malr',
        'Man',
        'msle','male','m']
    sex_w = [
        'CisFemale',
        'cis-female/femme',
        'femail',
        'Femake',
        'Female',
        'Female(cis)',
        'Woman','female','f']
    result = {}
    with open('survey.csv', 'r', newline='')as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            if i == 0:
                continue
            gender = row[2]
            country = row[3]
            gender = gender.replace(' ','')
            gender = gender.lower()
            if country not in result:
                result[country] = [0, 0]

            if gender in sex_w:
                result[country][0] += 1
            if gender in sex_m:
                result[country][1] += 1
    with open('result.csv', 'w', newline='')as f:
        w_result = csv.writer(f)
        w_result.writerow(['国家', '女', '男'])
        for k, v in list(result.items()):
            w_result.writerow([k, v[0], v[1]])


if __name__ == '__main__':
    main()
