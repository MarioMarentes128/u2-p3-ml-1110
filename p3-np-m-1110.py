import numpy as np

n1110=np.array([10, 20, 30, 40, 50])
print (n1110)
print(n1110[0])
print(n1110[3])
print(n1110[-1])
print(n1110[-2])
print("------------------")
n1110=np.array([
      [10, 20, 30],
      [40, 50, 60]
])
print(n1110)
print(n1110[0, 0])
print(n1110[1, 2])
print(n1110[-1, -1])
print(n1110[-2, -2])
print("------------------")

n1110=np.array([
    #0
      [
          [10, 20, 30],
          [40, 50, 60]
      ],
    #1
      [
          [70, 80, 90],
          [100, 110, 120]
      ]

])
print(n1110)
print(n1110[0,0,0])
print(n1110[1,1,2])
print(n1110[-1,-1,-2])

print("Mario Yañez NC 1110")

     