# YOLOv8 Lightweight

基于 Ultralytics YOLO 的轻量化目标检测代码库，集成了 MobileNetV4 主干网络和 SE（Squeeze-and-Excitation）注意力模块，便于在资源受限设备上进行实验与部署。

## 主要改动

- 集成 MobileNetV4 卷积型和混合型主干：
  - `MobileNetV4ConvSmall`
  - `MobileNetV4ConvMedium`
  - `MobileNetV4ConvLarge`
  - `MobileNetV4HybridMedium`
  - `MobileNetV4HybridLarge`
- 集成 `SEAttention` 通道注意力模块。
- 在 Ultralytics 模型解析流程中注册上述模块，可直接在模型 YAML 中使用。
- 保留 Ultralytics 8.4.23 的训练、验证、预测、跟踪和导出能力。

## 目录结构

```text
ultralytics/
├── cfg/                 # 训练和模型配置
├── data/                # 数据集处理
├── engine/              # 训练、验证和预测引擎
├── models/              # YOLO、RT-DETR 等模型实现
├── nn/
│   ├── modules/
│   │   ├── MobileNetV4.py
│   │   └── SE.py
│   └── tasks.py         # 模块注册和模型解析
├── trackers/            # 多目标跟踪
└── utils/               # 通用工具
```

## 安装依赖

建议使用 Python 3.11，并按硬件环境安装 PyTorch。基础依赖包括：

```bash
pip install torch torchvision ultralytics-thop numpy opencv-python pillow matplotlib polars psutil pyyaml requests scipy
```

在本仓库根目录运行时，Python 会优先加载当前目录下的 `ultralytics` 包：

```bash
python -c "import ultralytics; print(ultralytics.__version__)"
```

## 使用自定义模块

在模型 YAML 中将模块名称写入网络结构，即可由 Ultralytics 解析器创建。例如：

```yaml
backbone:
  - [-1, 1, MobileNetV4ConvSmall, []]
  - [-1, 1, SEAttention, [16]]
```

具体层数、通道数和 `reduction` 参数应根据输入尺寸及任务进行调整。

## 许可证与致谢

本项目基于 [Ultralytics](https://github.com/ultralytics/ultralytics)，遵循其 AGPL-3.0 许可证。请在再分发和商业使用前阅读上游许可证及相关条款。

MobileNetV4 和 SE 模块的集成代码位于 `ultralytics/nn/modules/`，解析器注册逻辑位于 `ultralytics/nn/tasks.py`。

## CIFAR-10 分类训练

仓库提供了使用 MobileNetV4 和 SEAttention 的 CIFAR-10 分类配置：

```bash
python main.py
```

`main.py` 会加载 `yolov8-mbv4-se-cls.yaml`，并调用 `model.train(data="cifar10")`。首次运行时，Ultralytics 会尝试准备 CIFAR-10 数据集；如果当前版本的资源中没有自动下载包，也可以先将 CIFAR-10 整理为 `train/<类别>/图片` 和 `test/<类别>/图片` 的目录结构，再把 `data` 改为该目录路径。
