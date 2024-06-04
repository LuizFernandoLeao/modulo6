import torch
import torch.nn as nn
import torch.optim as optim

# Definição da classe MLP
class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        self.hidden = nn.Linear(input_size, hidden_size)
        self.output = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.hidden(x))
        x = self.sigmoid(self.output(x))
        return x

# Dados da porta XOR
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Inicializando a rede neural
input_size = 2
hidden_size = 2
output_size = 1
learning_rate = 0.1
num_epochs = 10000

model = MLP(input_size, hidden_size, output_size)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Treinamento da rede neural
for epoch in range(num_epochs):
    outputs = model(X)
    loss = criterion(outputs, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 1000 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# Teste da rede neural
with torch.no_grad():
    for xi in X:
        output = model(xi)
        predicted = (output >= 0.5).float()
        print(f'Input: {xi.tolist()} Output: {predicted.item()}')
