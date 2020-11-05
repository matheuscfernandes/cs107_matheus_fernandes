import numpy as np
import matplotlib.pyplot as plt

#PART A
def numerical_diff(f,h):
    def diff(x):
        dd=(f(x+h)-f(x))/h
        return dd
    return diff

#PART B
ff = lambda x: np.log(x)
dfdx = lambda x: 1/x

xx = np.linspace(0.2,0.4,1000)

hh=[1E-15,1E-7,0.1]

plt.figure()

for ih in hh:
    ndiff=numerical_diff(ff,ih)
    dfdx_fd=ndiff(xx)
    plt.plot(xx,dfdx_fd, label='h='+str(ih),lw=4)

plt.plot(xx,dfdx(xx),'--',label='Analytical',lw=4)
plt.xlabel('X')
plt.ylabel('df/dx')
plt.legend()
plt.savefig('P1_fig.png',format='png',dpi=300)


#PART C
print('Answer to Q-a: The value of h=1e-7 most closely approximates the value of the true derivative. If the value of h is too small we see that the approximation is very bad due to the numerical computation being limited by computer prescision. If the value of h is too large, then we get a poor approximation as we are not reflecting the limit as h->0 in the finite difference scheme. The jump in the derivative approximation between two pooints is too far, so the tangent line has the wrong angle and thus the approximation is incorrect.')
print('')
print('Answer to Q-b: Automatic differentiation addresses this by not having a variable h in the scheme. Because Automatic differentiaction uses small recursive analytical sub evaulations, the accuracy of the method is as good as the accuracy of the computers compuation of each of these operation evaluations. Therefore, the algorithm is able to compute the derivative at computer precision automatically without requiring a hyperparameter.')

plt.show()