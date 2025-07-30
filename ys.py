import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r"C:\Users\betp\Desktop\mtcars.csv")
print(df)
plt.hist(df['mpg'])
plt.show()
plt.scatter(df['wt'],df['mpg'])
plt.xlabel('wt')
plt.ylabel('mpg')
plt.show()
plt.bar(df['am'],df['hp'])
plt.xlabel('am')
plt.ylabel('hp')
plt.show()
plt.boxplot(df['mpg'])
plt.xlabel('mpg')
plt.ylabel('mpg')
plt.show()


