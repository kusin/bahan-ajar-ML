import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# function of lineplot
def timeseries_matplotlib(df, nm_labels):

  # create lineplot
  fig, ax = plt.subplots(figsize = (8,4))
  for x in range(len(nm_labels)):
    ax.plot(df.iloc[:, 0:1], df.iloc[:, x+1:x+2], label=nm_labels[x], linewidth=2.5)

  # set label-labels
  ax.set_title("", fontsize=12)
  ax.set_xlabel("", fontsize=10)
  ax.set_ylabel("", fontsize=10)
  ax.legend(loc="best")
  ax.grid(True)
  
  # show lineplot
  plt.show()
# ----------------------------------------------------------------------------------------

# func timeseries plot
def lineplot_matplotlib1(x1, y1, label1):

  # create lineplot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x1, y1, color="tab:blue", label=label1, linewidth=2.5)
  
  # set label-labels
  ax.set_title("", fontsize=12)
  ax.set_xlabel("", fontsize=10)
  ax.set_ylabel("", fontsize=10)
  ax.legend(loc="best")
  ax.grid(True)
  
  # show lineplot
  plt.show()
# ----------------------------------------------------------------------------------------

# func timeseries plot
def lineplot_matplotlib2(x1, y1, label1, x2, y2, label2, title):

  # create lineplot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x1, y1, color="tab:blue", label=label1, linewidth=2.5)
  ax.plot(x2, y2, color="tab:red", label=label2, linewidth=2.5)
  
  # set label-labels
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=10)
  ax.set_ylabel("", fontsize=10)
  ax.legend(loc="best")
  ax.grid(True)
  
  # show lineplot
  plt.show()
# ----------------------------------------------------------------------------------------

# func timeseries plot
def lineplot_matplotlib3(x1, y1, label1, x2, y2, label2, title):

  # create lineplot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x1, y1, color="tab:blue", label=label1, linewidth=2.5)
  ax.plot(x2, y2, color="tab:red", label=label2, linewidth=2.5)
  
  # set label-labels
  ax.xaxis.set_major_formatter(DateFormatter("%Y"))
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=10)
  ax.set_ylabel("", fontsize=10)
  ax.legend(loc="best")
  ax.grid(True)
  
  # show lineplot
  plt.show()
# ----------------------------------------------------------------------------------------