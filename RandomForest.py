class Classifiers:
  def __init__(self,dataset,x,classval,a,b,normalize=True,encode=False,encodeval=0):
        global X,y,X_train,y_train,X_test,y_test
        if encode==True:
            from sklearn.preprocessing import LabelEncoder   
            le = LabelEncoder()
            encodeval1=data.columns[1 ]
            print(encodeval1)
            dataset[encodeval1]= le.fit_transform(dataset[encodeval1]) 
            from sklearn.preprocessing import OneHotEncoder 
            onehotencoder = OneHotEncoder(categorical_features = [0])
            global encoded
            encoded=dataset[encodeval1]
            encoded= onehotencoder.fit_transform(encoded).toarray()
            print(encoded)
            encoded=np.reshape(encoded,(np.size(encoded,axis=1),np.size(encoded,axis=0)))
            #print(temp)
            #print(dataset)
            X = dataset.iloc[:, a:b+1].values
            #X=np.delete(X,encodeval,axis=1)
            X=np.append(X,encoded,axis=1)
            y = dataset.iloc[:, classval].values
            print(X)
        else:
            X = dataset.iloc[:, a:b+1].values
            y = dataset.iloc[:, classval].values
        from sklearn.preprocessing import Imputer
        imputer = Imputer(missing_values = "NaN", strategy = 'mean', axis = 0)
        imputer = imputer.fit(X[:, a:b])
        X[:, a:b] = imputer.transform(X[:, a:b])
        X
        pca=PCA(n_components=4)
        X=pca.fit_transform(X)
        print(pca.explained_variance_ratio_)
        #from sklearn.cross_validation import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
  def RandomForest(self, n_estimators=300, criterion="gini", max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0., max_features="auto", max_leaf_nodes=None, min_impurity_decrease=0., min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None):
        rf=RandomForestClassifier(n_estimators, criterion, max_depth, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_features, max_leaf_nodes, min_impurity_decrease, min_impurity_split, bootstrap, oob_score, n_jobs, random_state, verbose, warm_start, class_weight)
        rf.fit(X_train,y_train)
        y_pred=rf.predict(X_test)
        acc=accuracy_score(y_test,y_pred)
        cm=confusion_matrix(y_test,y_pred)
        y_pred_prob=rf.predict_proba(X_test)
        return y_pred,acc,cm,y_pred_prob
data1=input("Enterdata set")
x=input("enter")
classval=int(input("enter"))
a=int(input("enter"))
b=int(input("enter"))
data=pd.read_csv(data1)
print(data)
c=Classifiers("hepaititis.data",x=30,classval=0,a=1,b=20)
c.knn()
