import matplotlib.pyplot as plt
activity=("home work","sports","online gaming","reading","self study")
time_spent=(2,3,1,1,3)
plt.pie(time_spent,labels=activity,autopct="%1.1f%%",startangle=50)
plt.title("relation between the activity and time_spent")
plt.show()