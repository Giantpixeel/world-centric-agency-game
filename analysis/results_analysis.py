
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('logs.csv')

df['speed'] = (df.dx**2 + df.dy**2)**0.5

plt.boxplot(df.speed)
plt.title('Movement Speed Distribution')
plt.ylabel('Speed')
plt.show()
