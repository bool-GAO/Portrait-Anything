import cv2
import numpy as np

class BackgroundReplacer:
    def __init__(self):
        pass
    
    def replace(self, image, mask, background):
        # 调整背景大小以匹配原始图像
        background = cv2.resize(background, (image.shape[1], image.shape[0]))
        
        # 确保掩码是单通道的
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        
        # 创建掩码的三通道版本
        mask_3channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        
        # 归一化掩码
        mask_3channel = mask_3channel / 255.0
        
        # 融合前景和背景
        foreground = image * mask_3channel
        background = background * (1 - mask_3channel)
        result = foreground + background
        
        # 转换回 uint8 类型
        result = result.astype(np.uint8)
        
        return result
