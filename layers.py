import numpy as np


def affine_forward(x, w, b):
    """
    This function computes the forward pass for an affine (fully-connected) layer.

    The input x has shape (N, d) and contains a N data examples each of which has d attributes.

    Inputs:
    x: input data, an array of shape (N, d)
    w: weights, an array of shape (d, M)
    b: biases, an array of shape (M,)

    Outputs:
    out: output, an array of shape (N, M)
    cache: (x, w, b)
    """
    out = x.dot(w) + b

    cache = (x, w, b)

    return out, cache


def affine_backward(dout, cache):
    """
    This function computes the backward pass for an affine (fully-connected) layer.

    Inputs:
    dout: derivatives coming from the next layer, an array of shape (N, M)
    cache: Tuple of:
        - x: input data, an array of shape (N, d)
        - w: weights, an array of shape (d, M)
        - b: biases, an array of shape (M,)

    Outputs:
    dx: gradient with respect to x, an array of shape (N, d)
    dw: gradient with respect to w, an array of shape (d, M)
    db: gradient with respect to b, an array of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None

    N = x.shape[0]

    dx = np.dot(dout, w.T)
    dw = np.dot(x.T, dout)
    db = np.dot(dout.T, np.ones(N))

    return dx, dw, db


def relu_forward(x):
    """
    This function computes the forward pass for a layer of rectified linear units (ReLUs).

    Input:
    x: inputs, an array of any shape

    Outputs:
    out: Output, an array of the same shape as x
    cache: x
    """
    out = np.maximum(0, x)
    cache = x
    return out, cache


def relu_backward(dout, cache):
    """
    This function computes the backward pass for a layer of rectified linear units (ReLUs).

    Inputs:
    dout: derivatives coming from the next layer, an array of any shape
    cache: input x, an array of same shape as dout

    Outputs:
    dx: gradient with respect to x
    """

    dx, x = None, cache
    dx = dout.copy()
    dx[x <= 0] = 0
    return dx


def L2_loss(x, y):
    """
    This functin computes the loss and gradient using L2 norm.

    Inputs:
    x: input data, an array of shape (N,) where x[i] is the regression output for the ith input.
    y: vector of labels, an array of shape (N,) where y[i] is the label for x[i].

    Outputs:
    loss: scalar giving the loss
    dx: gradient of the loss with respect to x
    """
    # Reshape Y
    loss = None
    dx = None

    N = x.shape[0]

    loss = np.sum(1.0/(2*N) * np.square(y-x))
    dx = -1.0/N * (y-x)
    
    return loss, dx
