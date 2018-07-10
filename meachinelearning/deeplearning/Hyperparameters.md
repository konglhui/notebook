## Hyperparameters

- alpha （重要性依次下降）
- beta,mini-batch size,hidden units
- learning rate decay，
- beta1 = 0.9,beta2 = 0.99,epsilon = 10的-8次方

try use random select hyperparameters.



### Normalizing inputs to speed up learning

$$
\mu = \frac{1}{m}\sum x^{(i)}\
$$

$$
x = x-\mu
$$

$$
\theta^2 = \frac{1}{m}\sum x^{(i)2}
$$

$$
x = \frac{x}{\theta^2}

$$



