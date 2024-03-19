import math

import matplotlib.pyplot as plt


class Agent:
    def __init__(self, x, y, personal_radius, sight_radius):
        self.x = x
        self.y = y
        self.personal_radius = personal_radius
        self.sight_radius = sight_radius

    def breach_personal_space(self, other_agent: 'Agent'):
        return math.dist((self.x, self.y),
                         (other_agent.x, other_agent.y)) <= self.personal_radius + other_agent.personal_radius



a1 = Agent(2, 1.5, 1, 0)
a2 = Agent(4, 3, 1.8, 0)

print(a1.breach_personal_space(a2))

figure, axes = plt.subplots()
dc1 = plt.Circle((a1.x, a1.y), a1.personal_radius)
dc2 = plt.Circle((a2.x, a2.y), a2.personal_radius)

axes.set_aspect(1)
axes.add_artist(dc1)
axes.add_artist(dc2)
plt.title('Colored Circle')
plt.xlim(0,20)
plt.ylim(0,20)
plt.show()



