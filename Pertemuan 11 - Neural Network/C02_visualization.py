# lib data visualizations
import matplotlib.pyplot as plt
# --------------------------------------------------------------

def lineplot1(x, y, label):
  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x, y, color="tab:blue", label=label, linewidth=2.5)

  # membuat label-label
  ax.set_title("", fontsize=14)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="upper left")
  ax.grid(True)

  # return values
  return plt.show()
# --------------------------------------------------------------

def lineplot2(x1, y1, x2, y2, label1, label2):
  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x1, y1, color="tab:blue", label=label1, linewidth=2.5)
  ax.plot(x2, y2, color="tab:red", label=label2, linewidth=2.5)

  # membuat label-label
  ax.set_title("", fontsize=14)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="upper left")
  ax.grid(True)

  # return values
  return plt.show()
# --------------------------------------------------------------

def lineplot3(training, validation, title):
  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(training, color="tab:blue", label="Training", linewidth=2)
  ax.plot(validation, color="tab:orange", label="Validation", linewidth=2)

  # membuat label-label
  ax.set_title(title, fontsize=12)#
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # menampilkan plot
  return plt.show()
# --------------------------------------------------------------

def lineplot4(date, ytrue, ypred, title):
  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(date, ytrue, color="tab:blue", label="data actual", linewidth=2, linestyle="solid")
  ax.plot(date, ypred, color="tab:red", label="results predictions", linewidth=2, linestyle="dashed")

  # membuat label-label
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # menampilkan plot
  return plt.show()

def lineplot5(date, ytrue, ypred1, label1, ypred2, label2, title):
  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(date, ytrue, color="tab:blue", label="data actual", linewidth=2, linestyle="solid")
  ax.plot(date, ypred1, color="tab:red", label=label1, linewidth=2, linestyle="dashed")
  ax.plot(date, ypred2, color="tab:orange", label=label2, linewidth=2, linestyle="dashed")

  # membuat label-label
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # menampilkan plot
  plt.show()