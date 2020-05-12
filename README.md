## 主要是通过基于电影内容（CB）的相似、用户电影协同过滤（CF）、电影热评分榜（HOT）三块做主要的召回，排序主要是三块召回内容再进行手工权重的分配排序

本次用的数据集是movielns 10M的，下载放在data目录下面就行，这是提供的百度网盘下载：https://pan.baidu.com/s/1w7lXqzWLODY075MoJ6l_6A  密码:t7n3

### 主要用的redis作为全部推荐结果的存储，所以需要提前配置
### 协调过滤用的是pyspark的als模型，内容推荐也可以使用词向量（doc2vec）

![image](https://github.com/lonngxiang/movielens_recommendation/blob/master/11.png)
