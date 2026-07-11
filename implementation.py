import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class OptimalExecutionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(OptimalExecutionModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

def generate_dummy_data(num_samples, input_dim):
    # Generate random dummy data for testing
    X = np.random.rand(num_samples, input_dim).astype(np.float32)
    y = np.random.randint(0, 2, size=(num_samples,)).astype(np.int64)
    return X, y

def train_model(model, criterion, optimizer, X_train, y_train, epochs=100):
    for epoch in range(epochs):
        model.train()
        inputs = torch.tensor(X_train)
        labels = torch.tensor(y_train)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}/{epochs}, Loss: {loss.item()}")

def evaluate_model(model, X_test, y_test):
    model.eval()
    inputs = torch.tensor(X_test)
    labels = torch.tensor(y_test)
    outputs = model(inputs)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == labels).sum().item() / len(labels)
    print(f"Accuracy: {accuracy * 100:.2f}%")

if __name__ == '__main__':
    # Hyperparameters
    input_dim = 10  # Number of features
    hidden_dim = 32
    output_dim = 2  # Binary classification (buy/sell decision)
    learning_rate = 0.001
    epochs = 50
    num_samples = 1000

    # Generate dummy data
    X, y = generate_dummy_data(num_samples, input_dim)
    split = int(0.8 * num_samples)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # Initialize model, loss function, and optimizer
    model = OptimalExecutionModel(input_dim, hidden_dim, output_dim)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Train the model
    train_model(model, criterion, optimizer, X_train, y_train, epochs)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)