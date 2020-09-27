def update_physics(rover, tilemap, timestep):
    rover.position[0] += rover.velocity[0] * timestep
    rover.position[1] += rover.velocity[1] * timestep
