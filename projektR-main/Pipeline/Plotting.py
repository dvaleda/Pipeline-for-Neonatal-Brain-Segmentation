import matplotlib.pyplot as plt

from Hyperparams import categories, colors
from pathlib import Path
import csv

class ResultPlotter:
    '''Class for plotting training results
    
    Attributes:
        results (Dict[str, List]): training results (loss, dice)
        result_dir (pathlib.Path): path to result directory, newly created for each run
        mode (str): one of four possible training modes ('baseline', 'agePrediction', 'labelBudgeting', 'transfer')
    
    '''

    def __init__(self, results, result_dir, mode, val_interval):
        self.results = results
        self.result_dir = result_dir
        self.mode = 'baseline'
        self.val_interval = val_interval

    def plot_epoch_loss_val_dice(self):
        '''Saves down plot of mean losses and validation dice scores over epochs.'''

        plt.figure("train", (12, 6))

        plt.subplot(1, 2, 1)
        plt.title(f"Epoch Average Loss in mode: {self.mode}")
        x = [i + 1 for i in range(len(self.results["epoch_loss"]))]
        y = self.results["epoch_loss"]
        plt.xlabel("epoch")
        plt.plot(x, y, color="red")

        plt.subplot(1, 2, 2)
        plt.title("Val Mean Dice")
        x = [self.val_interval * (i + 1) for i in range(len(self.results["mean_dice"]))]
        y = self.results["mean_dice"]
        plt.xlabel("epoch")
        plt.plot(x, y, color="green")

        plt.savefig(self.result_dir / 'epoch_average_loss.png')

    def plot_tissue_dice(self):
        ''' Plot val mean dice per tissue class and save down figure.'''

        plt.figure("train", (18, 6))

        for i, tc in enumerate(categories):
            plt.subplot(2, 5, i+1)
            plt.title(f"Val Mean Dice {tc}")
            x = [self.val_interval * (i + 1) for i in range(len(self.results[tc]))]
            y = self.results[tc]
            plt.xlabel("epoch")
            plt.plot(x, y, color=colors[i])

        plt.tight_layout()
        plt.savefig(self.result_dir / 'dice_subplots.png')


file = '/home/tea/TecaGit/ProjektR/Pipeline/Pipeline/results/pixel_size_1_50_epoha/results.csv'
columns = []
with open(file,'rU') as f: 
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if columns:
            for i, value in enumerate(row):
                columns[i].append(value)
        else:
            # first row
            columns = [[value] for value in row]
# you now have a column-major 2D array of your file.
#results = {c[0] : c[1:] for c in columns}
results = {}
for c in columns:
    valueList = []
    for value in c[1:]:
        if value == '':
            valueList.append(float(0))
        else:
            valueList.append(float(value))
    results[c[0]]=valueList

#print(results)

if __name__ == "__main__":
    resultplotter = ResultPlotter(results, Path('/home/tea/TecaGit/ProjektR/Pipeline/Pipeline/results/pixel_size_1_50_epoha'), 'baseline', 1)
    resultplotter.plot_epoch_loss_val_dice()
    resultplotter.plot_tissue_dice()