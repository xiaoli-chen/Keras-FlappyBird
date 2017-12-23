# 使用说明
使用前需安装最新版本 Keras，建议backend使用tensorflow

# 文件说明：
该项目利用flappybird小游戏，训练强化学习模型，项目文件分几个部分，为游戏元素，游戏模拟器，强化学习模型
游戏元素：文件夹assets中的文件都是为复现flappybird的音效和视觉效果图片
游戏模拟：文件夹game中，flappy_bird_utils.py设定游戏对元素的调用，wrapped_flappy_bird.py中设定游戏进度，游戏方法，奖励机制等等
强化学习模型：qlearn.py是主程序，model.h5是训练完成后保存的神经网参数，model.json是其他参数数据，readme.md是原作者的说明文档


# 运行说明：
模型演示：解压后，使用terminal或者命令行工具进入文件夹/Keras-FlappyBird／，运行：python qlearn.py -m 'Run', 部分使用者会遇到警告信息: RuntimeWarning: compiletime version 3.5 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version 3.6
  return f(*args, **kwds) 不影响运行结果

模型训练：使用terminal或者命令行工具进入文件夹/Keras-FlappyBird／，将备用model.h5保存至ready_model文件夹，运行：python qlearn.py -m 'Train',在游戏空转3000次左右后，进入模型训练阶段，至此将占用计算机不少资源，画面会有所卡顿。训练完成后将产生新的model.h5文件。


# Keras-FlappyBird

A single 200 lines of python code to demostrate DQN with Keras

Please read the following blog for details

https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html

![](animation1.gif)

# Installation Dependencies:

* Python 2.7
* Keras 1.0 
* pygame
* scikit-image

# How to Run?

**CPU only**

```
git clone https://github.com/yanpanlau/Keras-FlappyBird.git
cd Keras-FlappyBird
python qlearn.py -m "Run"
```

**GPU version (Theano)**

```
git clone https://github.com/yanpanlau/Keras-FlappyBird.git
cd Keras-FlappyBird
THEANO_FLAGS=device=gpu,floatX=float32,lib.cnmem=0.2 python qlearn.py -m "Run"
```

If you want to train the network from beginning, delete the model.h5 and run qlearn.py -m "Train"
