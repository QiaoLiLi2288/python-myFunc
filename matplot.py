# 绘图操作
import matplotlib.pyplot as plt
plt.axis("off") # 关闭轴显示
plt.imshow(data, cmap="Greys_r") # 绘图像
plt.tight_layout() #自适应面积
plt.savefig("data.png") # 保存图像
