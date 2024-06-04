import numpy as np
import math

class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Inicializando os pesos
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Pesos e bias da camada de entrada para a oculta
        self.weights_input_hidden = np.random.randn(hidden_size, input_size)
        self.bias_hidden = np.random.randn(hidden_size)
        
        # Pesos e bias da camada oculta para a de saída
        self.weights_hidden_output = np.random.randn(output_size, hidden_size)
        self.bias_output = np.random.randn(output_size)
        
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def _sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def _heaviside(self, x):
        return 1 if x >= 0.5 else 0
    
    def forward_pass(self, x):
        self.hidden_input = np.dot(self.weights_input_hidden, x) + self.bias_hidden
        self.hidden_output = self._sigmoid(self.hidden_input)
        
        self.final_input = np.dot(self.weights_hidden_output, self.hidden_output) + self.bias_output
        self.final_output = self._sigmoid(self.final_input)
        
        return self.final_output
    
    def backward_pass(self, x, y, output):
        # Cálculo do erro
        error = y - output
        
        # Gradiente da camada de saída
        d_output = error * self._sigmoid_derivative(output)
        
        # Erro na camada oculta
        error_hidden = d_output.dot(self.weights_hidden_output)
        
        # Gradiente da camada oculta
        d_hidden = error_hidden * self._sigmoid_derivative(self.hidden_output)
        
        # Atualização dos pesos e bias
        self.weights_hidden_output += self.learning_rate * np.outer(d_output, self.hidden_output)
        self.bias_output += self.learning_rate * d_output
        
        self.weights_input_hidden += self.learning_rate * np.outer(d_hidden, x)
        self.bias_hidden += self.learning_rate * d_hidden
    
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            for xi, target in zip(X, y):
                output = self.forward_pass(xi)
                self.backward_pass(xi, target, output)
    
    def predict(self, x):
        output = self.forward_pass(x)
        return self._heaviside(output)

# Dados da porta XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Criação e treinamento da rede neural
mlp = MLP(input_size=2, hidden_size=2, output_size=1, learning_rate=0.1)
mlp.train(X, y, epochs=10000)

# Teste da rede neural
for xi in X:
    print(f"Input: {xi} Output: {mlp.predict(xi)}")
