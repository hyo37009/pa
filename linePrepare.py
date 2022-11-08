import pandas as pd
from subway import *

allData = pd.read_excel('운영기관_역사_코드정보.xlsx')
newData = allData[['LN_NM', 'STIN_NM']]

line_3 = newData[newData['LN_NM'] == '3호선']
line_3 = line_3['STIN_NM'].tolist()

line_4 = newData[newData['LN_NM'] == '4호선']['STIN_NM'].tolist()
line_7 = newData[newData['LN_NM'] == '7호선']['STIN_NM'].tolist()


line3 = line('3호선', len(line_3))
line3.setline(line_3)

line4 = line('4호선', len(line_4))
line4.setline(line_4)

line7 = line('7호선', len(line_7))
line7.setline(line_7)

