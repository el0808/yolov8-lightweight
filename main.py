import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

from ultralytics import YOLO


def main():
    # CIFAR-10 is a 10-class image-classification dataset.
    model = YOLO("yolov8-mbv4-se-cls.yaml", task="classify")
    model.train(data="cifar10")


if __name__ == "__main__":
    main()
