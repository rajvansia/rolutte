"""Assess a betting strategy.

Copyright 2018, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 4646/7646

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as github and gitlab.  This copyright statement should not be removed
or edited.

We do grant permission to share solutions privately with non-students such
as potential employers. However, sharing with other current or future
students of CS 7646 is prohibited and subject to being investigated as a
GT honor code violation.

-----do not edit anything above this line---

Student Name: Raj Vansia
GT User ID: rvrv3
GT ID: 902918505
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


def author():
        return 'rvrv3' # replace tb34 with your Georgia Tech username.

def gtid():
	return 902918505 # replace with your GT ID number

def gamble(win_prob):
        episode_winnings =0
        i =0
        array_winnings = np.array([0])
        while  i < 1000:
            if episode_winnings >= 80:
                array_winnings = np.append(array_winnings,80)
                i = i+1
            else:
                won = False
                bet_amount = 1
                while won == False and i < 1000:
                    i = i+1
                    won = get_spin_result(win_prob)
                    if won == True:
                        episode_winnings = episode_winnings+bet_amount
                        array_winnings = np.append(array_winnings,episode_winnings)
                    else:
                        episode_winnings = episode_winnings - bet_amount
                        array_winnings = np.append(array_winnings,episode_winnings)
                        bet_amount = bet_amount*2

        return array_winnings
def gamble_foreal(win_prob):
        episode_winnings =0
        i =0
        array_winnings = np.array([0])
        while  i < 1000:
            if episode_winnings >= 80:
                array_winnings = np.append(array_winnings,80)
                i = i+1
            elif episode_winnings <= -256:
                array_winnings = np.append(array_winnings,-256)
                i = i+1
            else:
                won = False
                bet_amount = 1
                while won == False and i < 1000 and episode_winnings > -256:
                    i = i+1
                    won = get_spin_result(win_prob)
                    if won == True:
                        episode_winnings = episode_winnings+bet_amount
                        array_winnings = np.append(array_winnings,episode_winnings)
                    else:
                        episode_winnings = episode_winnings - bet_amount
                        array_winnings = np.append(array_winnings,episode_winnings)
                        if episode_winnings+256 < bet_amount*2:
                            bet_amount = episode_winnings+256
                        else:
                            bet_amount = bet_amount*2

        return array_winnings

def multiple_foreal_runs(win_prob,runs):
    winnings = np.array([])
    for i in range(0,runs):
        new_winnings = gamble_foreal(win_prob)
        if winnings.size == 0:
            winnings = new_winnings
        else:
            winnings = np.vstack((winnings, new_winnings))

    return winnings

def multiple_runs(win_prob,runs):
    winnings = np.array([])
    for i in range(0,runs):
        new_winnings = gamble(win_prob)
        if winnings.size == 0:
            winnings = new_winnings
        else:
            winnings = np.vstack((winnings, new_winnings))

    return winnings

def get_spin_result(win_prob):
	result = False
	if np.random.random() <= win_prob:
		result = True
	return result

def test_code():
    win_prob = 18.0/38 # set appropriately to the probability of a win
    np.random.seed(gtid()) # do this only oncNE
    # print get_spin_result(win_prob) # test the roulette spin

	# add your code here to implement the experiments
    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    test_runs_10 = multiple_runs(18.0/38,10)
    i =0
    for i in range(0,test_runs_10.shape[0]):
        plt.plot(test_runs_10[i], label=i+1)
        i = i+1
    plt.ylabel('winnings')
    plt.xlabel('bets')
    plt.title("Figure1")
    legend = plt.legend(loc='best', shadow=True, fontsize = 'medium')
    plt.savefig('Figure1')
    plt.clf()

    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    test_runs_1000 = multiple_runs(18.0/38,1000)
    test_run_mean = test_runs_1000.mean(axis=0)
    test_run_std = test_runs_1000.std(axis=0)
    plt.plot(test_run_mean, label='Mean')
    plt.plot(test_run_mean-test_run_std, label='Mean -std')
    plt.plot(test_run_mean+test_run_std, label='Mean +std')
    legend = plt.legend(loc='best', shadow=True, fontsize = 'medium')

    plt.ylabel('winnings')
    plt.xlabel('bets')
    plt.title("Figure2")
    plt.savefig('Figure2')
    plt.clf()

    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    test_run_median = np.median(test_runs_1000,axis=0)
    plt.plot(test_run_median, label='Median')
    plt.plot(test_run_median-test_run_std, label='Median -std')
    plt.plot(test_run_median+test_run_std, label='Median +std')
    legend = plt.legend(loc='best', shadow=True, fontsize = 'medium')

    plt.ylabel('winnings')
    plt.xlabel('bets')
    plt.title("Figure3")
    plt.savefig('Figure3')
    plt.clf()

    plt.xlim([0, 300])
    plt.ylim([-256, 100])

    test_foreal_runs_1000 = multiple_foreal_runs(18.0/38,1000)
    test_foreal_run_mean = test_foreal_runs_1000.mean(axis=0)
    test_foreal_run_std = test_foreal_runs_1000.std(axis=0)
    plt.plot(test_foreal_run_mean, label='Mean')
    plt.plot(test_foreal_run_mean-test_foreal_run_std, label='Mean -std')
    plt.plot(test_foreal_run_mean+test_foreal_run_std, label='Mean +std')
    legend = plt.legend(loc='best', shadow=True, fontsize = 'medium')
    plt.ylabel('winnings')
    plt.xlabel('bets')
    plt.title("Figure4")
    plt.savefig('Figure4')
    plt.clf()

    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    test_foreal_run_median = np.median(test_foreal_runs_1000,axis=0)
    plt.plot(test_foreal_run_median, label='Median')
    plt.plot(test_foreal_run_median-test_foreal_run_std, label='Median -std')
    plt.plot(test_foreal_run_median+test_foreal_run_std, label='Median +std')
    legend = plt.legend(loc='best', shadow=True, fontsize = 'medium')
    plt.ylabel('winnings')
    plt.xlabel('bets')
    plt.title("Figure5")
    plt.savefig('Figure5')
    plt.clf()
if __name__ == "__main__":
    test_code()
