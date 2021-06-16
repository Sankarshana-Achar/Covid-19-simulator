import matplotlib.pyplot as plt

def generate(sim,lis):
    x= []
    for i in range(len(lis)):
        x.append(i)
    y = lis
    plt.plot(x, y)
    plt.show()