import numpy as np

pos0=np.array([10, 5 , 30])
tm=0.2
v=5
a=1
w=np.radians(10)

cones={
    "B1":np.array([12, 7]),
    "B2":np.array([8, 6]),
    "Y1":np.array([13, 4]),
    "Y2":np.array([9, 3]) 
}

d= (v*tm) + (0.5*(tm**2))
x1= pos0[0]+d*np.cos(np.radians(pos0[2]))
y1= pos0[1]+d*np.sin(np.radians(pos0[2]))
theta1 = pos0[2]+(np.degrees(w)*tm)
pos1 = np.array([x1, y1, theta1])
print(f"Position 0: {pos0}\nPosition 1: {pos1}\n\n\nCone positions relative to car:-")

def g2cframe(ccp, cones, pos):
    print(f"In position {pos}:-")
    thet_rad=np.radians(ccp[2])
    R_inv = np.array([
        [ np.cos(thet_rad), np.sin(thet_rad)],
        [-np.sin(thet_rad), np.cos(thet_rad)]
    ])
    for name, pos in cones.items():
        rel = pos-np.array(ccp[0:2])
        print(f"Cone {name}: {R_inv@rel}")

g2cframe(pos0, cones, 0)
g2cframe(pos1, cones, 1)
