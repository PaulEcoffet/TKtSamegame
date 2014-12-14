"""
Module gérant les scores du jeu
"""

import pickle


class Highscores:
    """
    Contient et trie tous les scores
    """
    def __init__(self, score_file_name=None):
        self.scores = {}
        self.score_file_name = score_file_name
        if score_file_name:
            self.load_scores(score_file_name)

    def add_score(self, name, game):
        """
        Ajoute le score obtenu lors de la partie `game` avec le nom `name`.

        add_score trie ensuite les scores par ordre décroissant
        """
        key = (game.nb_line, game.nb_col, game.nb_colors)
        try:
            self.scores[key].append((name, game.score))
        except KeyError:
            self.scores[key] = [(name, game.score)]
        self.scores[key].sort(key=lambda x: x[1], reverse=True)
        if self.score_file_name:
            self.save_scores(self.score_file_name)

    def get_scores(self, nb_line, nb_col, nb_colors):
        """Retourne tous les scores pour la catégorie donnée"""
        try:
            return self.scores[(nb_line, nb_col, nb_colors)]
        except KeyError:
            return None

    def load_scores(self, score_file_name):
        """
        Charge les score d'un fichier
        """
        try:
            with open(score_file_name, 'rb') as score_file:
                self.scores = pickle.load(score_file)
        except FileNotFoundError:
            pass

    def save_scores(self, score_file_name):
        """
        sauvegarde les score dans un fichier.
        """
        with open(score_file_name, 'wb') as score_file:
            pickle.dump(self.scores, score_file)
