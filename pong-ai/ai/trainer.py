import torch

def train_step(model, optimizer, criterion, state, action, reward, next_state, done, gamma):
    state = torch.tensor(state, dtype=torch.float)
    next_state = torch.tensor(next_state, dtype=torch.float)
    action = torch.tensor(action, dtype=torch.long)
    reward = torch.tensor(reward, dtype=torch.float)
    done = torch.tensor(done, dtype=torch.bool)

    if len(state.shape) == 1:
        state = state.unsqueeze(0)
        next_state = next_state.unsqueeze(0)
        action = action.unsqueeze(0)
        reward = reward.unsqueeze(0)
        done = done.unsqueeze(0)

    pred = model(state)
    target = pred.clone()

    for idx in range(len(done)):
        Q_new = reward[idx]
        if not done[idx]:
            Q_new = reward[idx] + gamma * torch.max(model(next_state[idx]))

        target[idx][action[idx].argmax().item()] = Q_new

    optimizer.zero_grad()
    loss = criterion(target, pred)
    loss.backward()
    optimizer.step()