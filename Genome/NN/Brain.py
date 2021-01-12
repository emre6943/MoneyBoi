from Genome.NN.Layer import Layer
import numpy as np
import pickle


class Brain:
    def __init__(self, brain_structure):
        self.brain_structure = brain_structure
        self.layers = []
        self.id = 0

        # First layer added here
        ids = []
        genes = []
        for i in range(brain_structure[0]):
            ids.append(self.id)
            self.id += 1
            genes.append([np.random.rand(brain_structure[1]), np.random.rand(brain_structure[1]), np.random.rand(brain_structure[1])])
        layer = Layer(ids)
        layer.set_genes(genes)
        self.layers.append(layer)

        for i in range(1, len(brain_structure)):
            if i == (len(brain_structure) - 1):
                self.add_last_layer(brain_structure[-1])
            else:
                self.add_random_layer(brain_structure[i], brain_structure[i + 1])


    def add_random_layer(self, node_count, next_node_count):
        ids = []
        genes = []
        for i in range(node_count):
            ids.append(self.id)
            self.id += 1
            genes.append([np.random.rand(next_node_count), np.random.rand(next_node_count), np.random.rand(next_node_count)])
        layer = Layer(ids)
        layer.set_genes(genes)
        self.layers[-1].add_layer_connections(layer)
        self.layers.append(layer)

    def add_last_layer(self, node_count):
        ids = []
        for i in range(node_count):
            ids.append(self.id)
            self.id += 1
        layer = Layer(ids)
        self.layers[-1].add_layer_connections(layer)
        self.layers.append(layer)

    def set_data(self, data):
        self.layers[0].set_layer_input(data)

    def feed_forward(self):
        for l in range(len(self.layers)):
            if l != 0:
                self.layers[l].normalize()
            self.layers[l].feed_forward()

    def make_bebe(self, partner, mutation_rate):
        bebe = Brain(self.brain_structure)
        for i in range(len(self.layers)):
            bebe.layers[i] = self.layers[i].make_bebe(partner.layers[i], bebe.layers[i], mutation_rate)
        return bebe

    def get_answer(self):
        return self.layers[-1].get_layer_input()

    def save_model(self, file):
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(self, config_dictionary_file)

    @staticmethod
    def load_model(file):
        with open(file, 'rb') as config_dictionary_file:
            brain = pickle.load(config_dictionary_file)
            return brain

    def print_genes(self):
        print("The genes od the brain")
        for layer in self.layers:
            print(layer.get_genes())

#
# brain = Brain(16, 32)
# brain.add_random_layer(32, 32)
# brain.add_random_layer(32, 48)
# brain.add_last_layer(2)
# brain.save_model("../Models/first_baby")

# brain = Brain.load_model("../Models/first_baby")
# print(len(brain.layers))
# brain.print_genes()
#
# brain.set_data(list(range(0, 16)))
# brain.feed_forward()
# print(brain.get_answer())

