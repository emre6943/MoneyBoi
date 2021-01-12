from Genome.NN.Brain import Brain
from Genome.Simulation.Gamer import Gamer, getMarketPerformance
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

def sort_depending_seecond(arr1, arr2):
    sortme = np.array(arr1)
    scores = np.array(arr2)
    inds = (-scores).argsort()
    sorted = sortme[inds]
    return sorted.tolist()

def simulate_model(model, start, end, money):
    gamer = Gamer(money, start.strftime("%d/%m/%Y"), end.strftime("%d/%m/%Y"))
    current = start
    while (current != end):
        date_str = current.strftime("%d/%m/%Y")
        in_data = gamer.get_data_for_choice(date_str)

        option = model.predict([in_data], verbose=2)

        gamer.translate_model_to_action(option, current.strftime("%d/%m/%Y"))
        current = current + datetime.timedelta(days=1)

    wining = gamer.get_wallet_USD_value(end.strftime("%d/%m/%Y"))
    print(gamer.wallet)

    names = ['bro', 'brain dead']
    values = [wining, money * getMarketPerformance(start.strftime("%d/%m/%Y"), end.strftime("%d/%m/%Y"))]

    plt.bar(names, values)
    plt.xlabel('Names')
    plt.ylabel('End Money')
    plt.title('MANEY BOI MODEL')
    plt.show()

class World:
    def __init__(self, brain_structure, mutation_rate, population, surviving_number, bebes_per_parent, from_date, end_date, money):
        self.brains = []
        self.gamers = []
        self.start_day = from_date
        self.current_day = from_date
        self.end_day = end_date
        self.start_money = money


        #Creating the population
        for x in range(population):
            brain = Brain(brain_structure)
            self.brains.append(brain)
            self.gamers.append(Gamer(money, self.current_day.strftime("%d/%m/%Y"), self.end_day.strftime("%d/%m/%Y")))

        self.surviving_num = surviving_number
        self.mutation_rate = mutation_rate
        self.bebes_per_parent = bebes_per_parent

    def next_day(self):
        for i in range(len(self.gamers)):
            ai = self.gamers[i]
            brain = self.brains[i]

            date_str = self.current_day.strftime("%d/%m/%Y")
            in_data = ai.get_data_for_choice(date_str)

            brain.set_data(in_data)
            brain.feed_forward()
            brain_choice = brain.get_answer()

            ai.translate_brain_to_action(brain_choice, date_str)

        self.current_day = self.current_day + datetime.timedelta(days=1)

    def hayat(self):
        scores = []
        for ai in self.gamers:
            scores.append(ai.rewardFunc())

        winner_brains = sort_depending_seecond(self.brains, scores)[:self.surviving_num]

        for i in range(len(winner_brains)):
            for b in range(self.bebes_per_parent):
                winner_brains.append(winner_brains[i].make_bebe(winner_brains[random.randint(0, len(winner_brains) - 1)], self.mutation_rate))

        self.brains = winner_brains
        self.current_day = self.start_day

    def save_brains(self):
        for b in range(len(self.brains)):
            self.brains[b].save_model("../Models/" + str(b) + "_brain")

    def load_brains(self, num):
        brains = []
        for i in range(num):
            file_name = "../Models/" + str(i) + "_brain"
            brains.append(Brain.load_model(file_name))
        self.brains = brains

    def simulate(self, generations, save):
        for i in range(generations):
            while (self.current_day != self.end_day):
                self.next_day()
            self.hayat()
            if(save):
                self.save_brains()
            self.show_succes(i)
            self.fresh_gamers()

    def fresh_gamers(self):
        gamers = []
        for i in range(len(self.brains)):
            gamers.append(Gamer(self.start_money, self.start_day.strftime("%d/%m/%Y"),
                                self.end_day.strftime("%d/%m/%Y")))
        self.gamers = gamers

    def show_succes(self, gen):
        winner_wallets = []
        for g in self.gamers:
            winner_wallets.append(g.get_wallet_USD_value(self.current_day.strftime("%d/%m/%Y")))
        winner_wallets.sort(reverse=True)

        names = ['first', 'second', 'third', 'brain dead']
        values = [winner_wallets[0], winner_wallets[1], winner_wallets[2], self.start_money * getMarketPerformance(self.start_day.strftime("%d/%m/%Y"), self.end_day.strftime("%d/%m/%Y"))]

        plt.figure(figsize=(9, 3))
        plt.bar(names, values)
        plt.xlabel('Names')
        plt.ylabel('End Money')
        plt.title('MANEY BOI GEN' + str(gen))
        plt.show()









# world = World([7,14,28,56,11,2], 0.03, 500, 250, 1, datetime.datetime.strptime("16/09/2017", "%d/%m/%Y"), datetime.datetime.strptime("14/12/2020", "%d/%m/%Y"), 500)
# world.load_brains(500)
# # world = World([7,14,28,56,11,2], 0.02, 10, 5, 1, datetime.datetime.strptime("16/09/2017", "%d/%m/%Y"), datetime.datetime.strptime("20/09/2017", "%d/%m/%Y"), 500)
# world.simulate(1, True)



