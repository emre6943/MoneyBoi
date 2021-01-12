from Genome.NN.Node import Node

class Layer:
    def __init__(self, ids):
        self.nodes = []
        self.next_layer = None
        for i in ids:
            self.nodes.append(Node(i))

    def make_bebe(self, parent, bebe_brain_layer, mutation):
        for i in range(len(self.nodes)):
            bebe_brain_layer.nodes[i] = self.nodes[i].make_bebe(parent.nodes[i], bebe_brain_layer.nodes[i], mutation)
        return bebe_brain_layer

    def normalize(self):
        sum = 0
        for n in self.nodes:
            sum += abs(n.get_input())
        if sum == 0:
            # print("hell")
            return
        for n in self.nodes:
            n.set_input(n.get_input()/sum)

    def add_next_layer(self, layer, weights, activators, constants):
        self.next_layer = layer
        for i in range(len(self.nodes)):
            self.nodes[i].connect_bunch(layer.nodes, weights[i], activators[i], constants[i])

    def add_layer_connections(self, layer):
        self.next_layer = layer
        for i in range(len(self.nodes)):
            self.nodes[i].add_just_connections(layer.nodes)

    def feed_forward(self):
        if(self.next_layer != None):
            for i in range(len(self.nodes)):
                self.nodes[i].feed_forward()


    def set_layer_input(self, data_in):
        if (len(data_in) != len(self.nodes)):
            print("Error input dimension not fiting to structure size: " + len(self.nodes) + " input size: " + len(data_in))
            return
        else:
            for i in range(len(self.nodes)):
                self.nodes[i].set_input(data_in[i])

    def get_layer_input(self):
        data = []
        for i in range(len(self.nodes)):
            data.append(self.nodes[i].get_input())
        return data

    def set_genes(self, genes):
        for i in range(len(self.nodes)):
            self.nodes[i].set_gene(genes[i])

    def get_genes(self):
        genes = []
        for i in range(len(self.nodes)):
            genes.append(self.nodes[i].get_gene())
        return genes




