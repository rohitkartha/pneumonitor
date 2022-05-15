import torch
from torch import nn
import torchvision
import numpy as np
import torch.optim as optim
from preprocess import Data
from model_v1 import ResNet34
from model_v1 import ResBlock
from torch.utils.data import TensorDataset, DataLoader


dataobj = Data()
batch_size = 32
epochs = 25
X_train, y_train, X_test, y_test, X_val, y_val = dataobj.preprocess()


X_train = X_train.reshape((4325,150,150,1))
X_test = X_test.reshape((624,150,150,1))
X_val = X_val.reshape((624,150,150,1))


tensor_X_train = torch.Tensor(X_train)
tensor_y_train = torch.Tensor(y_train)
tensor_X_test = torch.Tensor(X_test)
tensor_y_test = torch.Tensor(y_test)
tensor_X_val = torch.Tensor(X_val)
tensor_y_val = torch.Tensor(y_val)

print(tensor_X_test.shape)
print(tensor_y_test.size(0))

train_set = TensorDataset(tensor_X_train, tensor_y_train)
train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)

test_set = TensorDataset(tensor_X_test, tensor_y_test)
test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=True)


net = ResNet34(150, ResBlock, outputs=1)

criterion = nn.BCELoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

for epoch in range(epochs):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        outputs = outputs.reshape([-1])
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 20 == 19:    # print every 2000 mini-batches
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.8f}')
            running_loss = 0.0

print('Finished Training')


PATH = './resnet34.pth'
torch.save(net.state_dict(), PATH)

correct = 0
total = 0
# since we're not training, we don't need to calculate the gradients for our outputs
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        # calculate outputs by running images through the network
        outputs = net(images)
        # the class with the highest energy is what we choose as prediction
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')