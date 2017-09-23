import six.moves.cPickle as pickle
import gzip
import os
import numpy as np
from deep_nn import DeepNN
from deep_nn_momentum import DeepNNMomentum


def load_data(dataset):
    data_dir, data_file = os.path.split(dataset)

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        from six.moves import urllib
        origin = (
            'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
        )
        print('Downloading data from %s' % origin)
        urllib.request.urlretrieve(origin, dataset)

    print('... loading data')

    with gzip.open(dataset, 'rb') as f:
        try:
            train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
        except:
            train_set, valid_set, test_set = pickle.load(f)

    return train_set, valid_set, test_set


train_set, valid_set, test_set = load_data('./data/mnist.pkl.gz')

train_x = np.array(train_set[0]).T
train_y = np.array(train_set[1]).reshape(len(train_set[1]), 1).T

test_x = np.array(test_set[0]).T
test_y = np.array(test_set[1]).reshape(len(test_set[1]), 1).T

nn = DeepNNMomentum(train_x, train_y, iteration_count=1000)

nn.train(lambda i, cost: print(i, cost) if i % 1000 else None)

res = nn.predict_and_test(test_x, test_y)

print("succ: {}", res["rate"])

print(train_x.shape, train_y.shape)
