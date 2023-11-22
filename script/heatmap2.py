import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, BoundaryNorm

plt.rcParams['font.family'] = 'Courier New'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['axes.labelsize'] = 20

# data2 = np.array([
#     [0.102201916,0.066296656,	0.066790672	,0.070626851,	0.084136979	,0.04765599 ],
#     [0.023132547,	0.02759932	,0.031957021,	0.038787963	,0.030901133
#  , np.nan],
#     [0.017597789,	0.023152229,	0.024053883,	0.023070511
#  , np.nan, np.nan],
#     [0.0191358	,0.023566961	,0.022605644
#  , np.nan, np.nan, np.nan],
#     [0.020036347	,0.026184816
# , np.nan, np.nan, np.nan, np.nan],
#     [0.025183125 , np.nan, np.nan, np.nan, np.nan, np.nan]
# ])
# data =np.array([
#     [2.77980448,	3.541902671	,4.42513125,	6.737561908,	7.520222,	6.44389247
#  ],
#     [1.887837498	,2.4271786,	2.61920256	,2.749632956	,2.556932771
# , np.nan],
#     [1.769958925,	2.172402216,	2.25186255	,2.173863042
#  , np.nan, np.nan],
#     [1.923988122,	2.383719795,	2.367116749
# , np.nan, np.nan, np.nan],
#     [2.313748688,	2.870945172
#  , np.nan, np.nan, np.nan, np.nan],
#     [2.829729473
# , np.nan, np.nan, np.nan, np.nan, np.nan]
# ])

data2 =  np.array([
    [9.904354778	,8.912521267,	9.155492077,	8.886287361,	9.19280033	,7.418483793

 ],
    [8.036063426	,8.29523961,	9.168848531,	7.8114751,	6.535799847

 , np.nan],
    [7.785320866,	6.942586153	,7.76095731	,7.017071175

 , np.nan, np.nan],
    [6.301390677	,6.54877406,	6.618666948

, np.nan, np.nan, np.nan],
    [6.618666948,	6.46728567

 , np.nan, np.nan, np.nan, np.nan],
    [6.779197075
, np.nan, np.nan, np.nan, np.nan, np.nan]
])
data = 1/1000000 *np.array([
    [355813847.2,	386597460.3,	398952259.6,	379840419.6,	336949535,	339530192.2

],
    [359715631.1,	337628478.6,	343163473.4	,324023800.2,	298609574.9

 , np.nan],
    [327140260.7,	331781188.1,	315708555.7	,302367319

 , np.nan, np.nan],
    [299765976.6	,315561007.3,	318009256.5

 , np.nan, np.nan, np.nan],
    [355723654.5	,300653046.3

 , np.nan, np.nan, np.nan, np.nan],
    [315235922.5
, np.nan, np.nan, np.nan, np.nan, np.nan]
])
min_index = np.unravel_index(np.nanargmin(data), data.shape)
vmin1 = np.nanmin(data)
vmin2= np.nanmin(data2)
vmax1 = np.nanmax(data)
vmax2= np.nanmax(data2)
f_values = np.arange(6)
l_values = np.arange(6)
# 创建两个并排的子图
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# 在第一个子图上绘制第一个数据集的热图
# sns.heatmap(data, annot=True, cmap='RdBu', xticklabels=f_values, yticklabels=l_values, 
            # annot_kws={"weight": "bold", "size": 25}, fmt=".1f", ax=axes[0], vmin=vmin1, vmax=vmax1)

sns.heatmap(data, annot=True, cmap='RdBu', xticklabels=f_values, yticklabels=l_values, 
            annot_kws={"weight": "bold", "size": 25}, fmt=".1f", ax=axes[0], vmin=vmin1, vmax=vmax1)
axes[0].xaxis.tick_top()
axes[0].xaxis.set_label_position('top')
axes[0].set_xlabel('f : Max fan-out of adders$=2^f+1$')
axes[0].set_ylabel('l : Logic level of adders$=L+l$ ')
axes[0].texts[min_index[0]*len(f_values) + min_index[1]].set_weight('extra bold')
# axes[0].set_xlabel('f : Max fan-out$=2^f+1$')
# axes[0].set_ylabel('l : Logic level$=L+l$ ')
# 在第二个子图上绘制第二个数据集的热图
sns.heatmap(data2, annot=True, cmap='RdBu', xticklabels=f_values, yticklabels=l_values, 
            annot_kws={"weight": "extra bold", "size": 25}, fmt=".1f", ax=axes[1], vmin=vmin2, vmax=vmax2)
            # annot_kws={ "size": 25}, fmt=".1f", ax=axes[1], vmin=vmin2, vmax=vmax2)

axes[1].xaxis.tick_top()
axes[1].xaxis.set_label_position('top')
axes[1].set_xlabel('f : Max fan-out of adders $=2^f+1$')
axes[1].set_ylabel('l : Logic level of adders $=L+l$ ')
# axes[1].set_xlabel('f : Max fan-out$=2^f+1$')
# axes[1].set_ylabel('l : Logic level$=L+l$ ')
axes[0].text(0.4, -0.1, "a. ASAP7", transform=axes[0].transAxes, va='center', fontsize=25)
axes[1].text(0.4, -0.1, "b. CNFET7", transform=axes[1].transAxes, va='center', fontsize=25)
# 调整两个子图之间的间距

plt.subplots_adjust(wspace=0.8)
plt.savefig("figure_name.pdf") 

plt.tight_layout()
plt.show()
