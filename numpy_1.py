import numpy as np

print(np.version.version)

print np.array([1,2,3,4])
print np.array((1.2,2,3,4))
print type(np.array((1.2,2,3,4)))
print np.array([[1,2],[3,4]])
print np.array((1.2,2,3,4), dtype=np.int32)

print np.arange(20)
print np.arange(15).reshape(3,5)
print np.linspace(1,3,9)

print np.zeros((3,4))
print np.ones((3,4))
print np.eye(3)
