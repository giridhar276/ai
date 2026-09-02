# Install first: pip install seaborn matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x=["Python", "SQL", "Excel"], y=[30, 25, 20])
plt.title("Students per Course")
plt.show()
