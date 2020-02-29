from pathlib import Path
import os
import unittest
import pandas as pd
import csv
import subprocess


def add_missing_comma(file_name):
    awk_prgm = "../utils/add_comma.awk "
    cmd = '''awk -F, -v OFS=, -f ''' + awk_prgm + file_name
    # cmd = "awk -F, -v OFS=, '{for(i=NF;i<=12;i++){$i=$i""}print}' " + file_name + " > " + file_name
    # cmd.replace("\\", "")
    try:
        output = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).stdout.read()
        with open(file_name, "w", encoding='utf-8', newline='') as csvfile:
            decode_output = output.decode("utf-8")
            writer = csv.writer(csvfile)
            writer.writerow([decode_output])
    except ValueError:
        return False
    else:
        return True


# Option 1
def read_csv_pandas(file_name):
    try:
        fs = pd.read_csv(
            file_name,
            error_bad_lines=False,
        )
        pass
    except ValueError:
        return False
    else:
        return True


class PandasCSVTest(unittest.TestCase):
    def test_to_read_defective_csv(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = Path(current_dir).parent
        file_name = 'UBER-Key-Ratios.csv'
        file_path = os.path.join(parent_dir, 'data', file_name)
        if add_missing_comma(file_path):
            self.assertTrue(read_csv_pandas(file_name))
        else:
            pass


# Option 3
def read_csv_python(file_name):
    try:
        data = csv.DictReader(open(file_name))
        # with open(file_name, 'rt')as f:
        #     data = csv.reader(f)
    except ValueError:
        return False
    else:
        print_csv(data)
        return True


def print_csv(data):
    for row in data:
        print(row)


class PythonCSVTest(unittest.TestCase):
    def test_to_read_defective_csv(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = Path(current_dir).parent
        file_name = os.path.join(parent_dir, 'data', 'TSLA_from_Numbers.csv')
        # file_name = os.path.join(parent_dir, 'data', 'TSLA-Key-Ratios.csv')
        self.assertTrue(read_csv_python(file_name))

# def fun(x):
#     return x + 1
#
#
# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 4)
