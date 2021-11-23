import glob
import pandas as pd

list_files = glob.glob("mnist_10k_test_images/*png")
labels = [ f.split('num')[1][0] for f in list_files ]
df= pd.DataFrame(data=[list_files, labels],
                 index=['file', 'target']).T

df.to_csv('mnist_10k_test_images.csv', index=False)
print(df.head())
print(df.shape)
print(df.target.value_counts())