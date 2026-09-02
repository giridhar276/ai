# Install first: pip install matplotlib
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 138, 170, 190]
expenses = [90, 100, 105, 115, 125]

fig, axes = plt.subplots(2, 2, figsize=(10, 7))

axes[0, 0].plot(months, sales, marker="o", label="Sales")
axes[0, 0].plot(months, expenses, marker="s", label="Expenses")
axes[0, 0].set_title("Line Chart")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Amount")
axes[0, 0].legend()
axes[0, 0].grid(alpha=0.3)

axes[0, 1].bar(months, sales, color="steelblue")
axes[0, 1].set_title("Bar Chart")

axes[1, 0].scatter(sales, expenses, color="darkred")
axes[1, 0].set_title("Scatter Chart")
axes[1, 0].set_xlabel("Sales")
axes[1, 0].set_ylabel("Expenses")

axes[1, 1].pie([40, 30, 20, 10], labels=["Python", "SQL", "Excel", "Cloud"], autopct="%1.1f%%")
axes[1, 1].set_title("Pie Chart")

fig.suptitle("Frequently Used Matplotlib Charts")
plt.tight_layout()
plt.savefig("matplotlib_examples.png", dpi=150, bbox_inches="tight")
plt.show()
