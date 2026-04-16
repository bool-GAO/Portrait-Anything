# Portrait-Anything

基于 SAM 2 的实时人像分割+背景替换工具，专注人像场景，提供美颜+虚拟背景一体化功能。

## 功能特性

- 实时人像分割
- 背景替换
- 美颜效果（磨皮+美白）
- 简单易用的命令行接口

## 技术栈

- Python
- ONNX Runtime
- OpenCV
- NumPy
- PyTorch (可选)

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/Portrait-Anything.git
cd Portrait-Anything
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 下载模型

将 SAM 2 模型文件放在 `models` 目录下。

## 使用方法

### 基本使用

```bash
python portrait_anything.py
```

### 自定义背景

将背景图片放在 `backgrounds` 目录下，然后修改 `portrait_anything.py` 中的 `background_path` 参数。

### 禁用美颜

修改 `portrait_anything.py` 中的 `enable_beauty` 参数为 `False`。

## 项目结构

```
Portrait-Anything/
├── models/            # 模型文件
├── utils/             # 工具模块
│   ├── sam2_inference.py       # SAM 2 模型推理
│   ├── background_replacement.py  # 背景替换
│   └── beauty_enhancement.py     # 美颜功能
├── backgrounds/       # 背景图片
├── portrait_anything.py  # 主入口文件
├── requirements.txt   # 依赖文件
└── README.md          # 说明文档
```

## 技术原理

1. **人像分割**：使用 SAM 2 模型进行实时人像分割，生成人像掩码。
2. **背景替换**：根据分割结果，将人像与新背景融合。
3. **美颜效果**：对人像区域应用磨皮和美白效果。

## 性能优化

- 使用 OpenCV 进行高效的图像处理
- 合理使用 GPU 加速（如果可用）
- 优化模型推理速度

## 未来计划

- 添加更多美颜效果
- 支持更多背景替换方式
- 提供 GUI 界面
- 优化模型性能

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
