import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dataset import get_data


def get_indices(data, index):
    # extract input as numpy
    input_indices = data.drop(index, axis=1)
    X = np.hstack([np.ones([input_indices.shape[0], 1]), input_indices.to_numpy()])

    # extract output as numpy
    y = data[index].to_numpy()

    return X, y


def get_coefficients(X, y):
    # compute coefficients
    coef = np.linalg.inv(X.T @ X) @ (X.T @ y)

    return coef


def regression(data, input_indices, index, timespan="H", intervals="M", lag="1H"):
    # extract input and output indices from dataset
    subset = data[input_indices + [index, "DateTime"]].set_index("DateTime").resample(timespan).mean()['2018':'2021':]

    # divide into intervals
    groups = [group for _, group in subset.groupby(pd.Grouper(freq=intervals))]

    # compute coefficients for every group
    coefficients = []
    coefficients_lagged = []
    y_hat = []
    y_hat_lagged = []
    me = []
    mad = []
    rmse = []
    for group in groups:
        try:
            l = group.index[0]
            r = group.index[-1]

            X1, y = get_indices(group, index)
            coef1 = get_coefficients(X1, y)
            pred1 = (coef1.T @ X1.T).flatten()

            td = pd.to_timedelta(lag)
            l -= td
            r -= td

            X2, _ = get_indices(subset[l:r], index)

            coef2 = get_coefficients(X2, y)
            pred2 = (coef2.T @ X1.T).flatten()

            coefficients.append(coef1)
            y_hat.append(pred1)

            coefficients_lagged.append(coef2)
            y_hat_lagged.append(pred2)

            me.append((y - pred2).mean())
            mad.append(np.abs(y - pred2).mean())
            rmse.append(np.sqrt(np.power(y - pred2, 2).sum()) / len(y))

        except np.linalg.LinAlgError:
            print(f"{l} to {r}:")
            print("Can't compute the coefficients, because the matrix can't be inverted.\n")
            coefficients.append(None)
            coefficients_lagged.append(None)
            y_hat.append(None)
            y_hat_lagged.append(None)
            me.append(None)
            mad.append(None)
            rmse.append(None)

        except ValueError:
            print(f"{l} to {r}:")
            print("Can't compute the coefficients, because of the lag data shape is invalid.\n")
            coefficients.append(None)
            coefficients_lagged.append(None)
            y_hat.append(None)
            y_hat_lagged.append(None)
            me.append(None)
            mad.append(None)
            rmse.append(None)

    # plot the interval
    i = 5
    X, y = get_indices(groups[i], index)

    labels = {
        "H": "hours",
        "D": "days",
    }

    plt.plot(y)
    plt.plot(y_hat[i], c="orange")
    plt.plot(y_hat_lagged[i], c="yellow")
    plt.xlabel(labels[timespan[-1]])
    plt.ylabel(index)ч
    plt.legend(["data", "regression", f"regression -{lag}"])

    plt.show()

    return groups, coefficients, y_hat, coefficients_lagged, y_hat_lagged, me, mad, rmse


data = get_data()
input_indices = ["Velocity"]

g1, c1, y_h1, cl1, y_hl1, *errors1 = regression(data, input_indices, "DST", timespan="H", intervals="M", lag="35H")

g2, c2, y_h2, cl2, y_hl2, *errors2 = regression(data, input_indices, "DST", timespan="D", intervals="6M", lag="42D")

i = 5
fig, ax = plt.subplots(1, 2)

_, y1 = get_indices(g1[i], "DST")

ax[0].hist(y1 - y_h1[i], bins=25, weights=np.ones_like(y1) / len(y1), edgecolor='k')
ax[0].set_title("ME: {:.3f}, MAD: {:.3f}, RMSE: {:.3f}".format(*[errors1[_][i] for _ in range(3)]))
ax[0].set_xlabel("residual")
ax[0].set_ylabel("probability")

_, y2 = get_indices(g2[i], "DST")
ax[1].hist(y2 - y_h2[i], bins=25, weights=np.ones_like(y2) / len(y2), edgecolor='k')
ax[1].set_title("ME: {:.3f}, MAD: {:.3f}, RMSE: {:.3f}".format(*[errors2[_][i] for _ in range(3)]))
ax[1].set_xlabel("residual")
ax[1].set_ylabel("probability")
print(len(g2))
plt.show()