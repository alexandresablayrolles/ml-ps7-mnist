import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer

from data import read_dataset
import model

def getAccuracy(x, y, keep_prob, binarizer, acc, dataset, sess):
    dataset_accuracy = 0
    # TODO: Compute accuracy on the dataset
    return dataset_accuracy

def train():
    tr, va, te = read_dataset('../mnist.pkl.gz')
    binarizer = LabelBinarizer().fit(range(10))

    x = tf.placeholder(tf.float32, [None, 784])
    y = tf.placeholder(tf.float32, [None, 10])
    keep_prob = tf.placeholder(tf.float32)
    preds = model.inference(x, keep_prob)
    loss, total_loss = model.loss(preds, y)
    acc = model.evaluation(preds, y)
    # learning rate: 0.1
    train_op = model.training(total_loss, 0.1)

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    for i in xrange(10000):
        batch_xs, batch_ys = tr.next_batch(50)
        if i % 100 == 0:
            train_acc = acc.eval(feed_dict={
                x:batch_xs, y:binarizer.transform(batch_ys),
                keep_prob: 1.0}, session=sess)
            print "step: {0}, training accuracy {1}".format(i, train_acc)
            validation_accuracy = getAccuracy(x, y, keep_prob, binarizer, acc, va, sess)
            print("Validation accuracy : {0}".format(validation_accuracy))
        train_op.run(feed_dict={
            x:batch_xs, y:binarizer.transform(batch_ys), keep_prob: 0.5},
                     session=sess)

    test_accuracy = getAccuracy(x, y, keep_prob, binarizer, acc, te, sess)
    print("Test accuracy : ", test_accuracy)

if __name__ == '__main__':
    train()
