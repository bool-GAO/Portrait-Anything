import cv2
import numpy as np

class BeautyEnhancer:
    def __init__(self):
        pass
    
    def enhance(self, image, mask):
        # 确保掩码是单通道的
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        
        # 创建模糊版本的图像（磨皮效果）
        blurred = cv2.GaussianBlur(image, (15, 15), 0)
        
        # 创建掩码的三通道版本
        mask_3channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        mask_3channel = mask_3channel / 255.0
        
        # 只在人像区域应用模糊效果
        result = image * (1 - mask_3channel) + blurred * mask_3channel
        result = result.astype(np.uint8)
        
        # 美白效果
        brightness = 1.1  # 亮度调整因子
        contrast = 1.2    # 对比度调整因子
        result = cv2.convertScaleAbs(result, alpha=contrast, beta=brightness*50)
        
        return result
