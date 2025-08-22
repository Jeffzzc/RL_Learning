import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")

state = env.reset()

print(env.action_space)

for _ in range(1000):
    env.render()
    
    action = env.action_space.sample()
    
    observation, reward, terminated, truncated, info = env.step(action)
    print(observation, reward, terminated, truncated, info)
    
    if terminated or truncated:
        print("Episode finished")
        break
    
env.close()