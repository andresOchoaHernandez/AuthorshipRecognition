%% EXTRACTING FEATURES - TRAINING SET
tic;
%% AUTHORS TO BE CONSIDERED

tot_authors_T = 83;

%%
train_set_dir = dir('training_set');
train_set_dir = train_set_dir(3:size(train_set_dir,1),:);

books_per_author_T = zeros(1,size(train_set_dir,1));
authors = cell(1,size(train_set_dir,1));
for author_number=1:size(train_set_dir,1)
    authors{author_number} = train_set_dir(author_number).name;                       
    books_per_author_T(author_number)= size(dir(strcat(train_set_dir(author_number).folder,'\',train_set_dir(author_number).name)),1) - 2;
end
books_tot = sum(books_per_author_T);

fprintf("TRAINING SET - BOOKS TO BE PROCESSED : %d\n",sum(books_per_author_T(1:tot_authors_T)));

training_set = zeros(47,sum(books_per_author_T(1:tot_authors_T)));

index = 1;
for author_number = 1 : tot_authors_T
    
    author_tot_books = books_per_author_T(author_number);
    books_dir = dir(strcat(train_set_dir(author_number).folder,'\',train_set_dir(author_number).name));
    books_dir = books_dir(3:size(books_dir,1));

    for i = 1 : author_tot_books
        training_set(:,index) = extract_features(strcat(books_dir(i).folder,'\',books_dir(i).name));
        index = index+1;
    end

end

train_set_labels = [];
for i = 1:tot_authors_T
    labels_tmp = ones(1,books_per_author_T(i))*i;
    train_set_labels = [train_set_labels labels_tmp];
end

clearvars -except books_per_author_T authors tot_authors_T training_set train_set_labels
save('train_set')
%% EXTRACTING FEATURES - TEST SET

%% AUTHORS TO BE CONSIDERED

tot_authors_Tt = 83;

%%
test_set_dir = dir('test_set');
test_set_dir = test_set_dir(3:size(test_set_dir,1),:);

books_per_author_Tt = zeros(1,size(test_set_dir,1));
authors = cell(1,size(test_set_dir,1));
for author_number=1:size(test_set_dir,1)
    authors{author_number} = test_set_dir(author_number).name;                       
    books_per_author_Tt(author_number)= size(dir(strcat(test_set_dir(author_number).folder,'\',test_set_dir(author_number).name)),1) - 2;
end
books_tot = sum(books_per_author_Tt);

fprintf("TEST SET - BOOKS TO BE PROCESSED : %d\n",sum(books_per_author_Tt(1:tot_authors_Tt)));

test_set = zeros(47,sum(books_per_author_Tt(1:tot_authors_Tt)));

index = 1;
for author_number = 1 : tot_authors_Tt
    
    author_tot_books = books_per_author_Tt(author_number);
    books_dir = dir(strcat(test_set_dir(author_number).folder,'\',test_set_dir(author_number).name));
    books_dir = books_dir(3:size(books_dir,1));

    for i = 1 : author_tot_books
        test_set(:,index) = extract_features(strcat(books_dir(i).folder,'\',books_dir(i).name));
        index = index+1;
    end

end

test_set_labels = [];
for i = 1:tot_authors_Tt
    labels_tmp = ones(1,books_per_author_Tt(i))*i;
    test_set_labels = [test_set_labels labels_tmp];
end

clearvars -except books_per_author_Tt tot_authors_Tt test_set test_set_labels
save('test_set')

clear;
toc;