import torch
import torch.nn as nn
import torch.nn.functional as F

class LinearQNet(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        super(LinearQNet,self).__init__()
        self.linear1 = nn.Linear(input_size,hidden_size)
        self.linear2 = nn.Linear(hidden_size,output_size)

    def forward(self,x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
    
    def save(self,file_name="model.pth"):
        torch.save(self.state_dict(),file_name)