import gym
import ma_gym
import time

env = gym.make('ma_gym:Combat-v0')
done_n = [False for _ in range(env.n_agents)]
ep_reward = 0

obs_n = env.reset()
while not all(done_n):
    env.render()
    obs_n, reward_n, done_n, info = env.step(env.action_space.sample())

    ep_reward += sum(reward_n)
    print("reward:" + str(sum(reward_n)))
    time.sleep(1)
env.close()