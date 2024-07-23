print(" *** Distance *** ")
u,a,t = input("Enter Velocity Acceleration Time: ").split(',')
s = float(u)* float(t) + ((0.5)* float(a)* float(t)* float(t))
print(f"Your Distance = {s:.2f}")