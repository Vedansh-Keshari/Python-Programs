import matplotlib.pyplot as plt
# plt.plot([1,2,3,4,5])
# plt.plot([1,2,3,4,5],[2,4,6,8,10])
# plt.plot([1,2,3,4,5],[2,4,6,8,10],'ro')
# plt.plot([1,2,3,4,5],[2,4,6,8,10],'r--')
# plt.plot([1,2,3,4,5],[2,4,6,8,10],'bs')
# plt.plot([1,2,3,4,5],[2,4,6,8,10],'g^')
import statistics
Estimates=[23,34,45,56,67,78,79,23,45,65,34,12,46,87,34,23,45,87,3,2,57,51,52,83,92,59,90]
y=[]
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([375],[5],'g^')