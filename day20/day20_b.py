from collections import Counter

# Functions #########################################################

def add(va, vb):
    a_x, a_y, a_z = va
    b_x, b_y, b_z = vb
    return (a_x + b_x, a_y + b_y, a_z + b_z)

# Entry Point #######################################################

lines = open('day20.txt').readlines()
#lines = open('day20_test.txt').readlines()

# Parse particle list
particles = []
for line in lines:
    csv = "".join([c for c in line if c in "-0123456789,"])
    csv = tuple(map(int, csv.split(',')))
    pos, vel, acc = (csv[:3], csv[3:6], csv[6:9])
    particles.append((pos, vel, acc))

# Simulate particles
while True:

    # Update positions
    for i, (pos,vel,acc) in enumerate(particles):
        vel = add(vel, acc)
        pos = add(pos, vel)
        particles[i] = (pos,vel,acc)

    # Resolve collisions
    before = len(particles)
    positions = Counter([pos for (pos,vel,acc) in particles])
    particles[:] = [(pos,vel,acc) for (pos,vel,acc) in particles if positions[pos] == 1]
    
    removed = before - len(particles)
    if removed > 0:
        print('Removed:', removed)
        print('Remaining:', len(particles))
