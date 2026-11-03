import numpy as np
import casadi as ca

opti = ca.Opti()

waypoints=np.array([np.array([1,1]), np.array([0.9, 2]), np.array([0.9, 3]), np.array([1,4.1]), np.array([1.7,5]), np.array([2.3,6])])
w1 = waypoints[2]
w2 = waypoints[3]
dist= w2-w1
l = np.hypot(dist[0], dist[1])
theta_d=np.arctan2(dist[1], dist[0])

pos0 = np.array([0.1,3.1, np.pi/2])
v0=5.5
v_d=10
a_g=1.3
w_g=0.23

a = opti.variable(3)
w = opti.variable(3)

x, y, theta, v = pos0[0], pos0[1], pos0[2], v0

J=0
for i in range(3):
    theta += w[i] * 0.02
    v += a[i] * 0.02
    x += v * ca.cos(theta) * 0.02
    y += v * ca.sin(theta) * 0.02
    
    e_heading = theta - theta_d # initial: 0.09, squared: 0.0018
    e_cte = (dist[0] * (w1[1] - y) - (w1[0] - x) * dist[1]) / l  # initial: -0.8, squared = 0.16
    e_v = v - v_d # initial: -4.5, squared = 20.25
    
    J += 20*(e_heading**2) + 2.5*(e_cte**2) + 0.1*(e_v**2)
f_J = ca.Function('f', [a, w], [J])
J_0 = float(f_J(np.full(3, a_g), np.full(3, w_g)))

opti.minimize(J)
opti.set_initial(a, a_g)
opti.set_initial(w, w_g)
opti.subject_to(opti.bounded(-13.0, a, 13.0))
opti.subject_to(opti.bounded(-2, w, 2))

opti.solver('ipopt', {"expand": True}, {"print_level": 0})
sol = opti.solve()

print(f"\n\nActive segment found : {w1} -> {w2}\n")
print(f"J before optimisation: {J_0:.6f}")
print(f"J after optimisation : {sol.value(J):.6f}")
print(f"Optimal a*           : {sol.value(a)} m/s^2")
print(f"Optimal w*           : {sol.value(w)} rad/s")
