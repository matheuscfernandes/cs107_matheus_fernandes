import P3
import matplotlib.pyplot as plt

npq=P3.timeit(pqclass=P3.NaivePriorityQueue)
hpq=P3.timeit(pqclass=P3.HeapPriorityQueue)
ppq=P3.timeit(pqclass=P3.PythonHeapPriorityQueue)

ns=[10, 20, 50, 100, 200, 500]
plt.figure()
L=5
plt.plot(ns,npq,label='Naive PQ',lw=L)
plt.plot(ns,hpq,label='Heap PQ',lw=L)
plt.plot(ns,ppq,label='Python Heap PQ',lw=L)
plt.legend()
plt.title('Figure Showing Performace of Different PQ Implementations')
plt.xlabel('Number of Lists Merged [-]')
plt.ylabel('Elapsed Average Time [s]')
plt.savefig('P3-C.png',format='png',dpi=300)
plt.show()