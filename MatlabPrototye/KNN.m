function class = KNN(train_set,train_set_labels,test_point,k)

if k >= size(train_set,2)
    error('k must be less than the available points')
end

if size(train_set,2) ~= size(train_set_labels,2)
    error('labels does not match the samples');
end

distance_vector = zeros(1,size(train_set,2));
for i = 1 : size(distance_vector,2)
    distance_vector(i)= sqrt(sum((test_point - train_set(:,i)) .^ 2));
end

[~,indexes] = sort(distance_vector);
indexes_k_nearest = indexes(1:k);
labels_k_nearest = train_set_labels(indexes_k_nearest);


class = mode(labels_k_nearest);
end
