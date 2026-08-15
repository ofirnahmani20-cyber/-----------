print("hia all")
import matplotlib.pyplot as plt
import numpy as np

# יצירת נתונים אקראיים לדוגמה
data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('היסטוגרם')
plt.xlabel('ערך')
plt.ylabel('תדירות')
plt.show()