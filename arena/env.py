import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from agents.agent import Agent


class Environment:
    def __init__(self, length_x, length_y, number_agents, radius_agents: list, sights_radius: list):
        if not len(radius_agents) == number_agents:
            raise ValueError(f"Number of agents personal radius should equal number of agents")
        if not len(sights_radius) == number_agents:
            raise ValueError(f"Number of agents sight radius should equal number of agents")

        self.x = length_x
        self.y = length_y

        candidates = [Agent(0.5, 0.5, radius_agents[0], sights_radius[0])]
        i = 0
        while i < number_agents - 1:
            x = np.random.uniform(0, self.x)
            y = np.random.uniform(0, self.y)
            temp_agent = Agent(x=x, y=y, personal_radius=radius_agents[i + 1], sight_radius=sights_radius[i + 1])
            if not any([candidates[j].breach_personal_space(temp_agent) for j in range(len(candidates))]):
                candidates.append(temp_agent)
                i += 1
        self.agents = candidates

    def plot_environment(self):
        figure, axes = plt.subplots()

        for agent in self.agents:
            axes.add_artist(plt.Circle((agent.x, agent.y), agent.personal_radius,
                                       color=cm.jet(np.abs(math.sin(agent.x ** 2 + agent.y ** 2))),
                                       alpha=0.5))

        axes.set_aspect(1)
        plt.xlim(0, self.x)
        plt.ylim(0, self.y)
        plt.show()


env = Environment(10, 10, 5, [0.5, 0.5, 0.5, 0.5, 0.5], [1, 1, 1, 1, 1])
env.plot_environment()
print(len(env.agents))
print('done')
