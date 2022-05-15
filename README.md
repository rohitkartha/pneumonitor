# pneumonitor

You can see the data that we used here: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
Our neural network architecture is based off of Resnet-18, a state-of-the-art image classifying neural network. Our network uses convolutional layers to aid with feature recognition, and residual blocks to allow for network depth without worrying about 

Model Architecture:
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 64, 75, 1]         470,464
         MaxPool2d-2            [-1, 64, 38, 1]               0
       BatchNorm2d-3            [-1, 64, 38, 1]             128
              ReLU-4            [-1, 64, 38, 1]               0
            Conv2d-5            [-1, 64, 38, 1]          36,928
       BatchNorm2d-6            [-1, 64, 38, 1]             128
            Conv2d-7            [-1, 64, 38, 1]          36,928
       BatchNorm2d-8            [-1, 64, 38, 1]             128
          ResBlock-9            [-1, 64, 38, 1]               0
           Conv2d-10            [-1, 64, 38, 1]          36,928
      BatchNorm2d-11            [-1, 64, 38, 1]             128
           Conv2d-12            [-1, 64, 38, 1]          36,928
      BatchNorm2d-13            [-1, 64, 38, 1]             128
         ResBlock-14            [-1, 64, 38, 1]               0
           Conv2d-15           [-1, 128, 19, 1]           8,320
      BatchNorm2d-16           [-1, 128, 19, 1]             256
           Conv2d-17           [-1, 128, 19, 1]          73,856
      BatchNorm2d-18           [-1, 128, 19, 1]             256
           Conv2d-19           [-1, 128, 19, 1]         147,584
      BatchNorm2d-20           [-1, 128, 19, 1]             256
         ResBlock-21           [-1, 128, 19, 1]               0
           Conv2d-22           [-1, 128, 19, 1]         147,584
      BatchNorm2d-23           [-1, 128, 19, 1]             256
           Conv2d-24           [-1, 128, 19, 1]         147,584
      BatchNorm2d-25           [-1, 128, 19, 1]             256
         ResBlock-26           [-1, 128, 19, 1]               0
           Conv2d-27           [-1, 256, 10, 1]          33,024
      BatchNorm2d-28           [-1, 256, 10, 1]             512
           Conv2d-29           [-1, 256, 10, 1]         295,168
      BatchNorm2d-30           [-1, 256, 10, 1]             512
           Conv2d-31           [-1, 256, 10, 1]         590,080
      BatchNorm2d-32           [-1, 256, 10, 1]             512
         ResBlock-33           [-1, 256, 10, 1]               0
           Conv2d-34           [-1, 256, 10, 1]         590,080
      BatchNorm2d-35           [-1, 256, 10, 1]             512
           Conv2d-36           [-1, 256, 10, 1]         590,080
      BatchNorm2d-37           [-1, 256, 10, 1]             512
         ResBlock-38           [-1, 256, 10, 1]               0
           Conv2d-39            [-1, 512, 5, 1]         131,584
      BatchNorm2d-40            [-1, 512, 5, 1]           1,024
           Conv2d-41            [-1, 512, 5, 1]       1,180,160
      BatchNorm2d-42            [-1, 512, 5, 1]           1,024
           Conv2d-43            [-1, 512, 5, 1]       2,359,808
      BatchNorm2d-44            [-1, 512, 5, 1]           1,024
         ResBlock-45            [-1, 512, 5, 1]               0
           Conv2d-46            [-1, 512, 5, 1]       2,359,808
      BatchNorm2d-47            [-1, 512, 5, 1]           1,024
           Conv2d-48            [-1, 512, 5, 1]       2,359,808
      BatchNorm2d-49            [-1, 512, 5, 1]           1,024
         ResBlock-50            [-1, 512, 5, 1]               0
AdaptiveAvgPool2d-51            [-1, 512, 1, 1]               0
          Flatten-52                  [-1, 512]               0
           Linear-53                    [-1, 1]             513
