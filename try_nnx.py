# from neuralnetworkx import nnx
import neuralnetworkx as nnx 
import torch 
import torch.nn.functional as F 

class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        self.out = torch.nn.Linear(n_hidden, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))      # activation function for hidden layer
        x = self.out(x)
        return x

n_data = torch.ones(100, 3, dtype=torch.float32)
x0 = torch.normal(2*n_data, 1)      # class0 x data (tensor), shape=(100, 2)
x1 = torch.normal(-2*n_data, 1)     # class1 x data (tensor), shape=(100, 2)
x = torch.cat((x0, x1), 0)  # shape (200, 2) FloatTensor = 32-bit floating
# print(type(x))
net = Net(n_feature=3, n_hidden=10, n_output=2)     # define the network
out = net(x)


netG = nnx.Graph()
netG.from_torch(net)
# netG([3, 10, 2])

# netG.animation()
# netG.ani_show()dd()




# print(type(net))
# print(type(out.data))
# print(type(net.out.weight.data))
# print(out.data.shape)
# print(net.out.weight.shape)
# print(net.hidden.weight.shape)
# print(type(net.out.weight.data.numpy()))

# print(type(net.hidden))
# print(type(net))
# # print(dir(net))
# # print((net.modules))
# print('______________________________________')
# for idx, m in enumerate(net.named_modules()):
#     if idx:
#         # print(type(m[0]))
#         s = 'net.'+m[0]+'.weight.data.numpy()'
#         print(m[0])
#         a = eval(s)
#         print(type(a.shape))
#         print(a.shape)
# print(dir(net.hidden))


# import neuralnetworkx.nnx as nnx 
# network = nnx.Graph([2,10,2])

# # network.check()
# network.draw()
# network.show()
# nn = nnx.Graph([1,3,1])
# nn.show()













