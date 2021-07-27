%% CLASSIFICATION USING SVM
clear;clc;

load 'train_set'
load 'PCA_train_set'
load 'test_set'

%% fitcsvm trains an svm classifier with only 2 classes, ONE VS ALL

class_1 = projected_train_set(:,train_set_labels == 4);
class_2 = projected_train_set(:,train_set_labels ~= 4);

labels_c_1 = ones(1,size(class_1,2));
labels_c_2 = ones(1,size(class_2,2))*2;

dataset = [ class_1 class_2];
labels = [labels_c_1 labels_c_2];

% test_point belongs to class 1
test_point = eigen_vectors' * test_set(:,1:50);

%%PLOTS
scatter3(dataset(1,:),dataset(2,:),dataset(3,:),10,labels);
hold on;
scatter3(test_point(1,:),test_point(2,:),test_point(3,:));
%% MODEL
model = fitcsvm(dataset',labels','KernelFunction','polynomial','PolynomialOrder',3,'Standardize',true);

[p_label,score] = predict(model,test_point')

