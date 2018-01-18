
lines = open('day20.txt').readlines()

def mag(vec3d):
    x,y,z = vec3d
    return x*x + y*y + z*z

# Parse particle list
particles = []
for line in lines:
    csv = "".join([c for c in line if c in "-0123456789,"])
    csv = tuple(map(int, csv.split(',')))
    pos, vel, acc = (csv[:3], csv[3:6], csv[6:9])
    particles.append((pos, vel, acc))

# Find closest to origin
acc_magnitudes = [(i,mag(acc)) for i,(pos,vel,acc) in enumerate(particles)]
i, min_acc = min(acc_magnitudes, key=lambda x: x[1]) # Lowest acceleration

vel_magnitudes = [(i,mag(vel)) for i,(pos,vel,acc) in enumerate(particles) if mag(acc) == min_acc]
i, min_vel = min(vel_magnitudes, key=lambda x: x[1]) # Lowest velocity

pos_magnitudes = [(i,mag(pos)) for i,(pos,vel,acc) in enumerate(particles) if mag(vel) == min_vel]
i, min_pos = min(pos_magnitudes, key=lambda x: x[1]) # Lowest distance

print("Closest to origin:", i) # = 364
