import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_reward(rewards, window, x_label='episodes', y_label='reward'):
    """
    Function to plot rewards with a rolling mean and standard deviation.
    """
    steps = window

    df = pd.DataFrame({'rewards': rewards})
    m = df.rolling(steps, center=True).agg({'mean':'mean', 'std':'std'})
    m.columns = m.columns.droplevel(1)
    ax = m['mean'].plot()
    ax.fill_between(m.index, m['mean'] - m['std'], m['mean'] + m['std'],
                    alpha=.25)
    plt.tight_layout()
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.show()
    
def get_epsilons(epsilon_range, n_steps):
    """
    Linear decay of epsilon in n_steps.
    """
    epsilon = np.linspace(epsilon_range[0], epsilon_range[1], n_steps)
    return epsilon

def get_exp_epsilons(epsilon_range, epsilon_decay, n_steps):
    """
    Exponential decay of epsilon in n_steps.
    """
    tmp_epsilon = epsilon_range[0]
    min_epsilon = epsilon_range[1]
    epsilons = []
    for i in range(n_steps):
        epsilons.append(max([tmp_epsilon, min_epsilon]))
        tmp_epsilon *= epsilon_decay
        
    return epsilons