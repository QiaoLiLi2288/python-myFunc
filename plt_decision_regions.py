# 利用色度图绘制决策域
from matplotlib.colors import ListedColormap
def plt_decision_regions(x, y, classfer):
    markers = ["*", "s", "x", "o"]
    colors = ["red", "blue", "lightgreen", "gray"]
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = x[:, 0].min()-1, x[:, 0].max()+1
    x2_min, x2_max = x[:, 1].min()-1, x[:, 1].max()+1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.02), np.arange(x2_min, x2_max, 0.02))
    z = classfer.prediction(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.3, cmap = cmap)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    for idx,c1 in enumerate(np.unique(y)):
        plt.scatter(x=x[y==c1,0],y=x[y==c1,1],alpha=0.8,c=colors[idx],marker=markers[idx],label=c1,edgecolor="black" )
    plt.legend(loc="upper left")
    plt.xlabel("sepal legenth [cm]")
    plt.ylabel("prtal length [cm]")
    plt.show()
