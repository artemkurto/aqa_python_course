class TxtAdaptor:

    @staticmethod
    def csv_to_json(file_path):
        with open(file_path) as f:
            res = f.readlines()

            header = [k.strip() for k in res[0].split(',')]
            # headers = res[0] # string: name, age, position, salary
            # headers = headers.split(',') ## list: ['name', 'age', 'position', 'salary\n']
            #
            # for k in headers:
            #     k = k.strip()  # позбулись переноса строк
            # result = ['name', 'age', 'position', 'salary']

            rows = res[1:]

            res_list = []

            for row in rows:
                row = row.strip().split(',')  # ['Alex', '25', 'Support', '1000']
                res_list.append(dict(zip(header, row)))  # dict key from header, value from row
        return res_list

    @staticmethod
    def csv_to_xml(file_path):
        with open(file_path) as f:
            res = f.readlines()
            header = [k.strip() for k in res[0].split(',')]
            rows = res[1:]
            values_list = [[value.strip() for value in row.split(',')] for row in rows]
            res_list = []
            for line in values_list:
                result = '\n'.join([f'<{header}>{value}</{header}>' for header, value in zip(header, line)])
                res_list.append(result)
            final_result = '\n'.join(res_list)
        return final_result


# print(TxtAdaptor.csv_to_json('tst_file.txt'))
print(TxtAdaptor.csv_to_xml('tst_file.txt'))
