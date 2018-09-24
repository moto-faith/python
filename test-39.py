import csv

def main():
    result = {}
    with open('survey.csv', 'r', newline='')as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            if i == 0:
                continue
            age = row[1]
            country = row[3]

            if country not in result:
                result[country] = [0,0]

            if int(age)<100 and int(age)>0:

                result[country][0]+=int(age)
                result[country][1]+=1



    with open('result2.csv', 'w', newline='')as f:
        w_result = csv.writer(f)
        w_result.writerow(['国家', '年龄'])
        for k, v in list(result.items()):
            w_result.writerow([k, v[0]/v[1] if v[1]>0 else 0])


if __name__ == '__main__':
    main()
