## Vanishing/exploding gradients

var(w)  = 1/n

w = np.random.randn(shape) * np.sqrt(2/(n(l-1)))			---(relu as activation)

w = np.random.randn(shape) * np.sqrt(1/(n(l-1)))			---(tanh as activation)

w = np.random.randn(shape) * np.sqrt(1/(n(l-1)    + n(l)))	---else

## Numerical approximation of gradient 

- checking your derivative computation

  - (f(theta+epsilon) - f(theta - epsilon))/2*epsilon = g(theta)

- grad check

  - ```
    for each i:
    	d_theta_i = J(theat_1,teta_2,...theta_i+epsilon,...) - J(theat_1,teta_2,...theta_i+epsilon,...)
    	= d_theta_i = d_J/d_theta_i
    ```

## gradient checking implementation notes

- don't use in training -only to debug
- if algorithm fails grad check ,look as components to try to identify bug.
- remember regularization .
- doesn't work with dropout.