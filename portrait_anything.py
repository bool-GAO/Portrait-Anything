import cv2
import numpy as np
from utils.sam2_inference import SAM2Model
from utils.background_replacement import BackgroundReplacer
from utils.beauty_enhancement import BeautyEnhancer

class PortraitAnything:
    def __init__(self, model_path):
        self.sam2_model = SAM2Model(model_path)
        self.background_replacer = BackgroundReplacer()
        self.beauty_enhancer = BeautyEnhancer()
    
    def process_frame(self, frame, background_image=None, enable_beauty=True):
        # 步骤1: 人像分割
        mask = self.sam2_model.segment_person(frame)
        
        # 步骤2: 美颜处理
        if enable_beauty:
            frame = self.beauty_enhancer.enhance(frame, mask)
        
        # 步骤3: 背景替换
        if background_image is not None:
            frame = self.background_replacer.replace(frame, mask, background_image)
        
        return frame, mask
    
    def run(self, background_path=None, enable_beauty=True):
        cap = cv2.VideoCapture(0)
        
        background_image = None
        if background_path:
            background_image = cv2.imread(background_path)
            if background_image is None:
                print(f"警告: 无法加载背景图片 {background_path}")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            result, mask = self.process_frame(frame, background_image, enable_beauty)
            
            # 显示结果
            cv2.imshow('Portrait Anything', result)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # 这里需要替换为实际的SAM 2模型路径
    model_path = "models/sam2.onnx"
    app = PortraitAnything(model_path)
    app.run(background_path="backgrounds/default.jpg", enable_beauty=True)
