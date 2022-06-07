from collections import defaultdict

from search_py3.search import GraphProblem
from search_py3.search import Graph
from search_py3.search import breadth_first_search

WORDS = set(i.lower().strip() for i in open('./words.txt'))

class WordLadder(GraphProblem):
    """
    Express Word Ladder problem in an undirected graph form, and using DFS to solve it.
    
    First check the length of start and goal words, then check if they are valid words
    Then generate all the possible intermediate words with the same length
    Construct an undirected graph and apply BFS to it.
    """
    
    def __init__(self, start, goal):
        try:
            self.process(start, goal, WORDS)
            super().__init__(start, goal, self.graph)

        except AssertionError as err: print(err)

    def solve(self):
        return breadth_first_search(self).solution()

    def is_valid_word(self, word):
        return word in WORDS

    def process(self, start, goal, WORDS):
        assert len(start) == len(goal), "Length of start and goal words is different!"
        assert self.is_valid_word(start), "Not a valid start word"
        assert self.is_valid_word(goal), "Not a valid goal word"
        
        self.length = len(start)
        print(f"Valid Problem! Word length: {self.length}")

        self.word_vocab = self.generate_word_dictionary(WORDS) # build the word vocabulary
        self.graph = self.generate_word_graph(self.word_vocab) # build the graph of the problem
        return self.graph
    
    def generate_word_dictionary(self, WORDS):
        word_vocab = defaultdict(list)
        
        for word in WORDS:
            if len(word) == self.length:  # take only valid word with the same length
                for i in range(self.length):
                    key = word[:i] + "*" + word[i+1:]
                    word_vocab[key].append(word)
                    # {*EST : [VEST, REST, ...], ...}
        
        return word_vocab
    
    def generate_word_graph(self, word_vocab):
        graph = defaultdict(dict)
        for inter_word in word_vocab.keys():
            for i in word_vocab[inter_word]:
                for j in word_vocab[inter_word]:
                    if i != j:
                        graph[i][j] = 1 # form an edge between the words in the graph
                        # {'arum': {'alum': 1, 'drum': 1}, ...}, ...}
        return Graph(graph, directed = False)
        


if __name__ == "__main__":
    test_cases = [
        ("cars", "cats") ,
        ("cold","warm"),
        ("best","math")
    ]

    for start, goal in test_cases:
        problem = WordLadder(start, goal)
        solution = problem.solve()
        print(f"{start} -> {solution} -> {goal}")

    start_input = input("Please input a starting word: \t").lower()
    goal_input = input("Please input a goal word: \t").lower()

    problem_input = WordLadder(start_input, goal_input)
    solution_input = problem_input.solve()
    print(f"{start_input} -> {solution_input} -> {goal_input}")


