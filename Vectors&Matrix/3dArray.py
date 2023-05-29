import matplotlib.pyplot as plt

r=[255,0,0]
g=[0,255,0]
b=[0,0,255]
w=[255,255,255]
bl=[0,0,0]

img= np.array([[r,r,b,b],
               [r,r,b,b],
               [g,g,b,b],
               [w,w,b,b],
               [k,k,bl,bl]])

plt.grid()
plt.imgshow(img)
