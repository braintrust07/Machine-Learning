from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
yp=n.predict(x2)
print(confusion_matrix(y2,yp))
print(precision_score(y2,yp))
print(recall_score(y2,yp))
print(f1_score(y2,yp))