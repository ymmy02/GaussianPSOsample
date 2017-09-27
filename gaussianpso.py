import random
import numpy as np
import matplotlib.pyplot as plt

#############
# Constants #
#############
DIM = 2
POPULATION = 10
LOOPMAX = 10
SKIP = 1
STT = -5.0
END = 5.0
W = 0.5

class Particle(object):
  
  def __init__(self, pos, fitness):
    self.pos = pos
    self.vel = np.zeros(DIM)
    self.fitness = fitness
    self.pbest = pos.copy()      # Parsonal Best
    self.lbest = np.zeros(DIM)   # Local Best
    self.neighbors = []

def evaluate(pos):
  return np.sum(pos.dot(pos))   # {x_1}^2 + {x_2}^2

def advance(particle):
  rho1 = random.uniform(0,0.14)
  rho2 = random.uniform(0,0.14)
  nextpos = np.zeros(DIM)
  nextvel = np.zeros(DIM)

  nextpos = particle.pos + particle.vel
  nextvel = W*particle.vel
  nextvel = nextvel + rho1 * np.random.normal(particle.pbest - particle.pos)
  nextvel = nextvel + rho2 * np.random.normal(particle.lbest - particle.pos)

  return nextpos, nextvel
  

def does_end(loopcount):
  if loopcount > LOOPMAX:
    return True
  return False

def main():

  # Initialize
  swarm = []
  for _ in range(POPULATION):
    pos = np.random.rand(DIM)*(END-STT) + STT
    fitness = evaluate(pos)
    particle = Particle(pos, fitness)
    swarm.append(particle)

  for i in range(len(swarm)):
    swarm[i].neighbors = swarm[0:i] + swarm[i+1:]

  best_partice = swarm[0]
  for particle in swarm:
    if particle.fitness < best_partice.fitness:
      best_partice = particle
  for particle in swarm:
    particle.lbest = best_partice.pos.copy()

  # Main Loop
  loopcount = 0
  while not does_end(loopcount):
    ## Update Particle Positions and Velocity
    for particle in swarm:
      (particle.pos, particle.vel) = advance(particle)

    ## Update Parsonal Best
    for particle in swarm:
      particle.fitness = evaluate(particle.pos)
      if particle.fitness < evaluate(particle.pbest):
        particle.pbest = particle.pos.copy()

    ## Update Best Particle
    for particle in swarm:
      if particle.fitness < best_partice.fitness:
        best_partice = particle
    for particle in swarm:
      particle.lbest = best_partice.pos.copy()
    
    ## Output
    if loopcount % SKIP == 0:
      plt.clf()
      plt.xlim(STT,END)
      plt.ylim(STT,END)
      for particle in swarm:
        plt.scatter(particle.pos[0], particle.pos[1], c="blue", marker="o")
      plt.savefig("fig" + str(loopcount+1).zfill(3) + ".png")
    loopcount += 1
    
  # Output
  print best_partice.pos
  print "Best Fitness : " + str(best_partice.fitness)

if __name__ == "__main__":
  main()
