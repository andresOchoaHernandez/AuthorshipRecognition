%% PCA
load 'train_set'

mean_vec = mean(training_set,2);
centered_data = training_set - repmat(mean_vec,1,size(training_set,2));
cov_matrix = cov(centered_data');

principal_components = 30;
[eigen_vectors,eigen_values ]= eigs(cov_matrix,principal_components);

projected_train_set = eigen_vectors' * centered_data;

plot(cumsum(diag(eigen_values))/sum(diag(eigen_values)));

figure;
scatter3(projected_train_set(1,:),projected_train_set(2,:),projected_train_set(3,:),10,train_set_labels)
title('training set after PCA');
for i=1:size(train_set_labels,2)
    text(projected_train_set(1,i),projected_train_set(2,i),projected_train_set(3,i),int2str(train_set_labels(i)))
end

clearvars -except mean_vec eigen_vectors projected_train_set
save('PCA_train_set')