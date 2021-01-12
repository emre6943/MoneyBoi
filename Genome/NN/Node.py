import numpy as np
import random

class Node:
    def __init__(self, id):
        self.id = id
        self.connections = []
        self.weights = []
        self.activations = []
        self.constants = []
        self.input = 0

    def connect_bunch(self, nodes, weights, activators, constants):
        assert len(nodes) == len(weights) == len(activators) == len(constants)
        self.connections = nodes
        self.weights = weights
        self.activations = activators
        self.constants = constants

    def add_connection(self, node, weight, activator, constant):
        self.connections.append(node)
        self.weights.append(weight)
        self.activations.append(activator)
        self.constants.append(constant)

    def add_just_connections(self, nodes):
        self.connections = nodes

    def feed_forward(self):
        for w in range(len(self.connections)):
            if(self.input >= self.activations[w]):
                self.connections[w].set_input(self.connections[w].get_input() + self.input * self.weights[w] + self.constants[w])

    def set_input(self, input):
        self.input = input

    def get_input(self):
        return self.input

    def set_weights(self, weights):
        self.weights = weights

    def get_weights(self):
        return self.weights

    def set_activators(self, activations):
        self.activations = activations

    def get_activators(self):
        return self.activations

    def set_constants(self, constant):
        self.constants = constant

    def get_constants(self):
        return self.constants

    def get_gene(self):
        return [self.activations, self.weights, self.constants]

    def set_gene(self, gene):
        self.activations = gene[0]
        self.weights = gene[1]
        self.constants = gene[2]

    def make_bebe(self, node, bebe_node, luck):
        gene = [np.add(self.activations, node.activations)/2, np.add(self.weights, node.weights)/2, np.add(self.constants, node.constants)/2]
        if (random.random() <= luck):
            mutation = random.randint(0, 2)
            mutation_amount = random.random() * 2 - 1
            gene[mutation] = np.add(gene[mutation], np.full((len(gene[mutation])), mutation_amount))
        bebe_node.set_gene(gene)
        return bebe_node
