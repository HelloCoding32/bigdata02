import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pr = pd.read_csv('product.csv')
pr['path'] = pr.groupby('product_id')['operator'].transform(
    lambda x : '_'.join(x)
)
pr['path'] = pr['factory'] + '_' + pr['path']
pr = pr.drop_duplicates('product_id')
pr = pr[['date','product_id','passfail','path']]
pr['factory'] = pr['path'].map(lambda x:x[0:2]) # 팩토리 코드만 추출
pr['path'] = pr['path'].map(lambda x:x[3:]) # 3열 부터 끝까지 추출
pr['path'] = pr['path'].map(lambda x:x.split('_'))
pr = pr.explode('path')
# print(pr)
process_map = {
    '1' : 'p1',
    '2' : 'p1',
    'V' : 'p2',
    'W' : 'p2',
    'X' : 'p3',
    'Y' : 'p3'
}
pr['process'] = pr['path'].map(process_map)
pr = pr.rename({'path' : 'operator'}, axis = 1)
print(pr)