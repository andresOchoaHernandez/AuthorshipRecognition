%% LDA
load 'PCA_train_set'
load 'train_set'

tot_classes = size(unique(train_set_labels),2);

means = cell(1,tot_classes);
covariances = cell(1,tot_classes);
Sb = cell(1,tot_classes);

for i=1:tot_classes
    means{i} = mean(projected_train_set(:,train_set_labels == i),2);
    covariances{i} = cov(projected_train_set(:,train_set_labels == i)');
end

Sw = zeros(size(projected_train_set,1));
for i = 1 : tot_classes
    Sw = Sw + covariances{i};
end

means_sum = zeros(size(projected_train_set,1),1);
for i = 1 : tot_classes
    means_sum = means_sum + means{i};
end
Mu = means_sum ./ size(means,2);

for i=1:tot_classes
   Sb{i} = size(projected_train_set(:,train_set_labels == i),2) .* (means{i} - Mu)*(means{i} - Mu)'; 
end

SB = zeros(size(Sb{1},1));
for i = 1 : tot_classes
    SB = SB + Sb{i};
end

MA = Sw \ SB;

principal_components = 20;
[W,D] = eigs(MA,principal_components);

train_set_LDA = W' * projected_train_set;

figure;
scatter3(train_set_LDA(1,:),train_set_LDA(2,:),train_set_LDA(3,:),10,train_set_labels)
title('training set after LDA');
for i=1:size(train_set_labels,2)
    text(train_set_LDA(1,i),train_set_LDA(2,i),train_set_LDA(3,i),int2str(train_set_labels(i)))
end

clearvars -except W train_set_LDA
save('LDA_train_set')