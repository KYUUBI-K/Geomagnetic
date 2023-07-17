import matplotlib.pyplot as plt
from dataset import get_data



data = get_data()

plt.subplot(1,2,1)
plt.grid()
plt.scatter(data["DST"],data["Velocity"], s=0.1, c = 'b')
plt.xlabel('Velocity')
plt.ylabel('DST')


plt.subplot(1,2,2)
plt.grid()
plt.scatter(data['SSN'],data['f10'], s=0.1, c = 'b')
plt.xlabel('SSN')
plt.ylabel('f10')

plt.show()




