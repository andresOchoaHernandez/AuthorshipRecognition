function class = wKNN(train_set,train_set_labels,test_point,k)
if k > size(train_set,2)
    error('k must be less than the available points')
end

if size(train_set,2) ~= size(train_set_labels,2)
    error('labels does not match the samples');
end

distance_vector = zeros(1,size(train_set,2));
for i = 1 : size(distance_vector,2)
    distance_vector(i) = norm(test_point - train_set(:,i));
end

WL = [1./distance_vector; train_set_labels];
[~,indexes] = sort(distance_vector);
indexes_k_nearest = indexes(1:k);
k_n = WL(:,indexes_k_nearest);

unique_classes = unique(k_n(2,:));
wf = zeros(1,size(unique_classes,2));
for i = 1: size(unique_classes,2)
    indexes_of_w = k_n(2,:) == unique_classes(i);
    wf(i) = sum(k_n(1,indexes_of_w));
end

[~,x] = max(wf);
class = unique_classes(x);
end
