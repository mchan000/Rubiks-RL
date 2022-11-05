from stable_baselines3 import PPO, DQN
from RubikScape import *
from stable_baselines3.common.env_checker import check_env

if __name__ == '__main__':
    env = RubiksEnv()

    super_count = 0

    n_moves = int(input("How many moves? "))
    shuf_seq = []

    print("For now I can solve up to 9 moves 80% of the time")
    print("0 = u")
    print("1 = u'")
    print("2 = d")
    print("3 = d'")
    print("4 = l")
    print("5 = l'")
    print("6 = r")
    print("7 = r'")
    print("8 = f")
    print("9 = f'")
    print("10 = b")
    print("11 = b'")

    for i in range(n_moves):
        tmp = int(input("Which move? "))
        shuf_seq.append(tmp)

    print("Shuffle seq: {}".format(shuf_seq))

    for i in range(1):
        episodes = 100

        PPO_Path = os.path.join('training', 'saved models', 'PPO_RLLY_RDM')
        model = PPO.load(PPO_Path, env=env)

        least_moves = 100
        solve_seq = []

        count = 0
        for episode in range(1, episodes + 1):
            obs = env.reset()
            obs = env.scramble(shuf_seq)
            done = False
            score = 0

            while not done:
                action, _ = model.predict(obs)
                obs, reward, done, info = env.step(action)
                score += reward
            if score == 1:
                count += 1
            # print('Episode:{} Score:{} Moves Made:{}'.format(episode, score, info.get(2)))
            if info.get(2) < least_moves:
                least_moves = info.get(2)
                solve_seq = info.get(1)

        if not solve_seq:
            print("Sorry, I couldn't solve it this time. Try running again")
        else:
            print('Solve sequence: {}'.format(convertToRNotation(solve_seq)))
            super_count += 1
