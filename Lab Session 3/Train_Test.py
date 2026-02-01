from sklearn.model_selection import train_test_split
x1,x2,y1,y2=train_test_split(X,y,test_size=0.3)
print(x1.shape)
print(x2.shape)
