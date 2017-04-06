import pandas as pd
from os import remove

from main_handler import MainHandler


class FileDataHandler(MainHandler):
    def get(self, file_param):
        df = pd.read_csv(UPLOAD_DIR + '/' + file_param)

        cols = df.columns.tolist()
        res = {'columns': cols, 'rows': []}

        for index, row in df.iterrows():
            row_dict = {}
            for col in cols:
                row_dict[col] = row[col]
            res['rows'].append(row_dict)

        self.write(res)

    def post(self, file_param):
        try:
            remove(UPLOAD_DIR + '/' + file_param)
        except OSError:
            raise 'delete error'

        self.write({'status': 'OK'})