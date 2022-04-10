# import graphviz
# from concepts import Context
import pandas as pd
import numpy as np
import re


patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y' ,
    '[.]': ''
}

def convert(text):
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return re.sub("\s\s+", " ", output.lower().strip())

file = pd.read_csv('input_location.csv', encoding = 'utf-8', sep = ';')
# print(f'DataFrame: \n',file)
np = file.to_numpy()
# print(f'Array: \n', np)
# print(f'Array Shape: ', np.shape)
list_symptom = [file.columns]
# print(f'Danh sach cot 2:', list_symptom)
#
df = pd.DataFrame(np, columns = list_symptom)
# print(f'Chuyen lai sang pandas: ',df)
# df.to_csv('patient_covid19_context_location.csv', index = False)
##
