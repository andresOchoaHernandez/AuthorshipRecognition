import numpy as np
from scipy import stats
from scipy.spatial import distance
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def KNN(train_set,train_set_labels,test_point,k):
    if k > train_set.shape[1]:
        print("K must be less than the available points");return

    if train_set.shape[1] != train_set_labels.shape[0]:
        print("Labels don't match the samples");return


    distance_vector = np.zeros(train_set.shape[1])
    for i in range(0,train_set.shape[1]):
        distance_vector[i] = distance.euclidean(test_point , train_set[:,i])

    sorted_indexes = np.argsort(distance_vector)
    indexes_k_nearest = sorted_indexes[0:k]
    labels_k_nearest = train_set_labels[indexes_k_nearest]

    return stats.mode(labels_k_nearest)[0][0]
        

def wKNN(train_set,train_set_labels,test_point,k):
    if k > train_set.shape[1]:
        print("K must be less than the available points");return

    if train_set.shape[1] != train_set_labels.shape[0]:
        print("Labels don't match the samples");return


    distance_vector = np.zeros(train_set.shape[1])
    for i in range(0,train_set.shape[1]):
        distance_vector[i] = distance.euclidean(test_point , train_set[:,i])

    WL = np.array([1./distance_vector,train_set_labels])

    sorted_indexes = np.argsort(distance_vector)
    indexes_k_nearest = sorted_indexes[0:k]
    k_n = WL[:,indexes_k_nearest]

    unique_classes = np.unique(k_n[1,:])
    wf = np.zeros(unique_classes.shape[0])

    for i in range(0,unique_classes.shape[0]):
        indexes_of_w = k_n[1,:] == unique_classes[i]
        wf[i] = np.sum(k_n[0,indexes_of_w])

    return unique_classes[np.argmax(wf)]

if __name__ == "__main__":

    ### READING MATRICES ###
    n_features = 47
    n_samples = 2269

    # READING TRAINING SET MATRIX
    training_set_file = open('training_set.txt','r')

    training_set = np.zeros((n_features,n_samples))
    row = 0
    for line in training_set_file :
        col = 0
        for num in line.split(',') :
            training_set[row,col] = np.float64(num)
            col +=1
        row+=1

    training_set_file.close()

    # READING TRAINING SET LABELS ARRAY
    train_set_labels_file = open('train_set_labels.txt','r')

    train_set_labels = np.zeros(n_samples,dtype=np.int16)

    cols = 0
    for line in train_set_labels_file :
        for num in line.split(',') :
            train_set_labels[cols] = np.int16(num)
            cols+=1
            
    train_set_labels_file.close()


    # READING TEST SET MATRIX
    test_set_samples = 446

    test_set_file = open('test_set.txt','r')

    test_set = np.zeros((n_features,test_set_samples))
    
    row = 0
    for line in test_set_file :
        col = 0
        for num in line.split(',') :
            test_set[row,col] = np.float64(num)
            col +=1
        row+=1

    test_set_file.close()

    #READING TEST SET LABELS

    test_set_labels_file = open('test_set_labels.txt','r')

    test_set_labels = np.zeros(test_set_samples,dtype=np.int16)

    cols = 0
    for line in test_set_labels_file :
        for num in line.split(',') :
            test_set_labels[cols] = np.int16(num)
            cols+=1
            
    test_set_labels_file.close()


    #####################################################################


    ### PCA ###

    # MEAN VECTOR
    mean_vector = training_set.mean(1).reshape(n_features,1)
    centered_train_set = training_set - np.repeat(mean_vector,n_samples,axis=1)

    # COVARIANCE MATRIX
    cov_matrix = np.cov(centered_train_set)

    # EIGEN VALUES AND EIGEN VECTORS
    eigen_values,eigen_vectors = np.linalg.eig(cov_matrix)
    sorted_indexes = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[sorted_indexes]
    eigen_vectors = eigen_vectors[:,sorted_indexes]

    # PROJECTION INTO PRINCIPAL COMPONENTS
    components_PCA = 40
    
    projected_train_set = np.dot(eigen_vectors[:,0:components_PCA].T , centered_train_set)

    """
    # SCATTER OF PROJECTED TRAIN SET
    fig = plt.figure()
    ax = plt.axes(projection = "3d")

    colors = cm.rainbow(train_set_labels)

    ax.scatter(projected_train_set[0,:],projected_train_set[1,:],projected_train_set[2,:],color=colors)

    for i in range(0,n_samples):
        ax.text(projected_train_set[0,i],projected_train_set[1,i],projected_train_set[2,i],str(train_set_labels[i]))
    
    plt.title("TRAINING SET AFTER PCA")
    
    plt.show()

    """

    ### LDA ###
    tot_classes = np.unique(train_set_labels).shape[0]

    means = [None] * tot_classes
    covariances = [None] * tot_classes
    Sb = [None] * tot_classes

    for i in range(0,tot_classes):
        means[i] = projected_train_set[:,train_set_labels == (i+1)].mean(1).reshape(-1,1)
        covariances[i] = np.cov(projected_train_set[:,train_set_labels == (i+1)])

    SW = np.zeros((projected_train_set.shape[0],projected_train_set.shape[0]));
    for i in range(0,tot_classes):
        SW += covariances[i]

    means_sum = np.zeros((projected_train_set.shape[0],1))
    for i in range(0,tot_classes):
        means_sum+=means[i]
    Mu = means_sum/tot_classes

    for i in range(0,tot_classes):
        Sb[i] = projected_train_set[:,train_set_labels == (i+1)].shape[1] * np.dot((means[i] - Mu),(means[i] - Mu).T)

    SB = np.zeros((Sb[0].shape[0],Sb[0].shape[0]))
    for i in range(0,tot_classes):
        SB += Sb[i]
        
    MA = np.dot(np.linalg.inv(SW),SB)

    # EIGEN VALUES AND EIGEN VECTORS
    eigen_values_LDA,W = np.linalg.eig(MA)
    sorted_indexes = np.argsort(eigen_values_LDA)[::-1]
    eigen_values_LDA = eigen_values_LDA[sorted_indexes]
    W = W[:,sorted_indexes]

    # PROJECTION TO PRINCIPAL DISCRIMINATIVE COMPONENTS
    components_LDA = 30
    LDA_train_set = np.dot(W[:,0:components_LDA].T,projected_train_set)

    """
    # SCATTER OF TRAIN SET AFTER LDA
    fig = plt.figure()
    ax = plt.axes(projection = "3d")

    colors = cm.rainbow(train_set_labels)

    ax.scatter(LDA_train_set[0,:],LDA_train_set[1,:],LDA_train_set[2,:],color=colors)

    for i in range(0,n_samples):
        ax.text(LDA_train_set[0,i],LDA_train_set[1,i],LDA_train_set[2,i],str(train_set_labels[i]))
    
    plt.title("TRAINING SET AFTER PCA + LDA")
    
    plt.show()
    """

    ### CLASSIFICATION WITH KNN AND wKNN ###

    # PROJECT THE TEST
    centered_test_set = test_set - np.repeat(mean_vector,test_set.shape[1],axis=1)
    projected_test_set = np.dot(eigen_vectors[:,0:components_PCA].T,centered_test_set);

    #CLASSIFICATION USING KNN
    neighbors = 50;

    accuracy = np.zeros(neighbors)

    for k in range(0,neighbors):

        correct = 0
        wrong = 0

        for i in range(0,test_set.shape[1]):
            classification = KNN(LDA_train_set,train_set_labels,np.dot(W[:,0:components_LDA].T,projected_test_set[:,i]),k+1)
            if classification == test_set_labels[i]:
                correct+=1
            else :
                wrong+=1
        accuracy[k]=(correct/(correct + wrong))*100;


    plt.plot(range(1,neighbors+1),accuracy,label='KNN')
    plt.xlabel("K neighbors")
    plt.ylabel("accuracy")


    #CLASSIFICATION USING wKNN
    accuracy = np.zeros(neighbors)

    for k in range(0,neighbors):

        correct = 0
        wrong = 0

        for i in range(0,test_set.shape[1]):
            classification = wKNN(LDA_train_set,train_set_labels,np.dot(W[:,0:components_LDA].T,projected_test_set[:,i]),k+1)
            if classification == test_set_labels[i]:
                correct+=1
            else :
                wrong+=1
        accuracy[k]=(correct/(correct + wrong))*100;

    plt.plot(range(1,neighbors+1),accuracy,label='wKNN')
    plt.legend(loc='lower left')
    plt.show()
