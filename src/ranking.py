import random

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack", "Katie", "Liam", "Mia",
         "Nathan", "Olivia", "Patrick", "Quinn", "Rachel", "Sam", "Tina"]

rankings = []
for name in names:
    ranking = {"name": name, "score": random.randint(0, 100)}
    rankings.append(ranking)


def add_ranking(user_name, score):
    new_ranking = {"name": user_name, "score": score}
    rankings.append(new_ranking)


top_ranks = sorted(rankings, key=lambda x: x['score'], reverse=True)[:10]
