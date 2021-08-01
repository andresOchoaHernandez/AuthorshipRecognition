%% TEST SET PROJECTION - PCA
load 'test_set'
load 'train_set'
load 'PCA_train_set'

centered_test_set = test_set - repmat(mean_vec,1,size(test_set,2));
projected_test_set = eigen_vectors' * centered_test_set;

%% NEIGHBORS
neighbors = 100;

%% CLASSIFICATION WITH KNN - PCA + LDA
load 'LDA_train_set.mat'

accuracy = zeros(1,neighbors);
for k = 1: neighbors
    correct = 0;
    wrong = 0;

    for i=1:size(projected_test_set,2)
        class = KNN(train_set_LDA,train_set_labels,W'*projected_test_set(:,i),k);

        if class == test_set_labels(i)
            correct = correct + 1;
        else
            wrong = wrong + 1 ;
        end
    end

    accuracy(k)=correct/(correct + wrong)*100;
end

plot(1:neighbors,accuracy);
[y,x]= max(accuracy);
text(x,y,'max');
xlabel('k neighbors');
ylabel('accuracy');

%% CLASSIFICATION WITH WEIGTHED KNN - PCA + LDA
load 'LDA_train_set.mat'

accuracy = zeros(1,neighbors);
for k = 1: neighbors
    correct = 0;
    wrong = 0;

    for i=1:size(projected_test_set,2)
        class = wKNN(train_set_LDA,train_set_labels,W'*projected_test_set(:,i),k);

        if class == test_set_labels(i)
            correct = correct + 1;
        else
            wrong = wrong + 1 ;
        end
    end

    accuracy(k)=correct/(correct + wrong)*100;
end

hold on;
plot(1:neighbors,accuracy);
[y,x]= max(accuracy);
text(x,y,'max');
xlabel('k neighbors');
ylabel('accuracy');

legend('PCA + LDA + KNN','PCA + LDA + wKNN','Location','southwest')