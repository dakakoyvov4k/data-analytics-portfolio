import torch

x = torch.tensor([10.0], requires_grad=True)
target = 2.0
step = 0.1
for i in range(1, 10):
    loss = (x - target) ** 2

    loss.backward() # x.grad = 2*(x - target)

    with torch.no_grad():
        x -= step * x.grad

    x.grad.zero_()

    if i % 3 == 0:
        print(f'Шаг {i}: x = {x.item():.3f}')

print(f'Результат: x = {x.item():.3f} (цель была 2.0)')
