def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    while steps>0:
        x0-=lr*(2*a*x0+b)
        steps-=1
    return x0

    pass