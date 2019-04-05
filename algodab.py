import json

class AlgoDab(object):
    """docstring for algodab."""

    def __init__(self):
        super(AlgoDab, self).__init__()
        with open('algsource.json', 'r') as f:
            self.alg_data = json.load(f)

    def puzzles(self):
        return [*self.alg_data]

    def algsets(self,puzzle):
        return [*self.alg_data[puzzle]]

    def algorithms(self,puzzle,set):
        return [*self.alg_data[puzzle][set]]

    def algorithm_list(self,puzzle,set,name):
        return self.alg_data[puzzle][set][name]

    def algorithm(self,puzzle,set,name,selection = (lambda list:list[0])):
        alg_select = selection(self.algorithm_list(puzzle,set,name))
        newAlg = Algorithm(puzzle,set,name,alg_select)
        return newAlg



class Algorithm(object):
    """docstring for algorithm."""

    def __init__(self, puzzle, set, name, algorithm):
        super(Algorithm, self).__init__()
        self.puzzle = puzzle
        self.set = set
        self.name = name
        self.algorithm = algorithm
