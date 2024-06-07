import random

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack", "Katie", "Liam", "Mia",
         "Nathan", "Olivia", "Patrick", "Quinn", "Rachel", "Sam", "Tina"]

rankings = []
for name in names:
    ranking = {"name": name, "score": random.randint(0, 10)}
    rankings.append(ranking)


def add_ranking(player, score):
    new_ranking = {"name": player, "score": score}
    rankings.append(new_ranking)
    rankings.sort(key=lambda x: x['score'], reverse=True)
    return rankings[:10]
