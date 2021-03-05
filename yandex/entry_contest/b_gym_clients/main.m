D = readtable('gym_data.csv');
DM = table2array(D(:,3:12));

exited = find(DM(:,10)==1);
stayed = find(DM(:,10)==0);
Y = DM(:,end);

figure; 
a = 5; b = 2;
for c = 1:size(DM,2)
    subplot(a,b,c);
    histogram(DM(exited,c), 25, 'normalization', 'pdf'); hold on;
    histogram(DM(stayed,c), 25, 'normalization', 'pdf');
    title(join(split(D.Properties.VariableNames{c+2}, '_')));
end

relevant_predictors = [1,2,3,4,5,6,7,8,9];%[2,5,7,8];%[2,5,6,7,8,9];
disp('Relevant predictors:'); 
for i = 1:numel(relevant_predictors)
    disp(join(split(D.Properties.VariableNames{relevant_predictors(i)+2}, '_')));
end

[B,dev,stats] = mnrfit(DM(:,relevant_predictors), double(nominal(Y)));

%Performance on the training dataset
% train_pred = mnrval(B, DM(:,relevant_predictors));
% [~,train_pred] = max(train_pred, [], 2);
% train_pred = train_pred - 1;

SVMModel = fitcsvm(DM(:,relevant_predictors), Y, 'KernelFunction', 'rbf', 'KernelScale','auto', 'Standardize', true);
[train_pred,score] = predict(SVMModel,DM(:,relevant_predictors));

err_percent = sum(abs(train_pred - Y))/numel(Y);
rc = sum(train_pred(exited))/numel(exited);
pr = sum(train_pred(exited))/sum(train_pred);
F1 = 2 * pr * rc / (pr+rc);

% Testing dataset
T = readtable('gym_test_init.csv');
TM = table2array(T(:,3:11));

test_pred = mnrval(B, TM(:,relevant_predictors));
[~,test_pred] = max(test_pred, [], 2);
test_pred = test_pred-1;

T.Exited = test_pred;

%% SVM
[label,score] = predict(SVMModel,TM(:,relevant_predictors));
T.Exited = label;

writetable(T, 'gym_test.csv');


