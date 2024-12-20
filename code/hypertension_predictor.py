# -*- coding: utf-8 -*-
"""proyecto_ia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d_6opiT_TqfQpkjtMy032xp4qothEy7C

#Hypertension prediction

Tomas Giovanny Gonzalez Romero -2190197 E2
Ashley Michelle Calderón Villamizar - 2162101 F1

![hipertension.jpeg](data:image/jpeg;base64,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)

https://huggingface.co/datasets/jadaprojects/Hospital_Mortality_Prediction
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, KFold
import tensorflow as tf
from tensorflow import keras

data = pd.read_csv('https://drive.google.com/uc?export=download&id=1kBYjvHQr0_HdSGZdAlMX-GvNYa3uj17h')

"""Se eliminan columnas las cuales no son necesarias o estan sesgadas, ademas se eliminan los registros con valores nulos"""

data = data.dropna()
data = data.drop("group", axis=1)
data = data.drop("ID", axis=1)
data = data.drop("EF", axis=1)
data = data.drop("outcome", axis=1)
data = data.drop("COPD", axis=1)
data.columns

"""# matriz de correlacion"""

plt.subplots(figsize=(25,25))
corr = data.corr()
sns.heatmap(corr, annot=True, fmt=".2f")

"""# Histogramas"""

num_columns = data.shape[1]

fig, axes = plt.subplots(23, 2, figsize=(20, 70))

x = 0
y = 0
for i, col in enumerate(data.columns):
  if i < num_columns/2:
    y = 0
    x = i
  else:
    y = 1
    x = int(i - num_columns/2)
  ax = axes[x,y]
  data.hist(ax=ax, column=col)

"""#ENTREGA 2

Les recuerdo los requisitos para la primera entrega de proyectos finales, que se llevará a cabo este jueves 21 de noviembre:

1. Deben utilizar TODOS los estimadores vistos en clase: DecisionTree, RandomForest, SupportVectorMachine, con PARÁMETROS POR DEFECTO.
Utilícelos según su tarea:
   - regresión (DecisionTreeRegressor, RandomForestRegressor, SVR)
   - clasificación (DecisionTreeClassifier, RandomForestClassifier, SVC)

2. Elija:
a) usando train_test_split:
Ejecute el siguiente tuning de parámetros (learning curves - notebook 10, "https://gitlab.com/bivl2ab/academico/cursos-uis/ai/ai-uis-student/-/blob/master/10_std_Notes_Regression.ipynb"):
   - DecisionTree (max_depth, criterion)
   - RandomForest (n_estimators, criterion)
   - SVC/R (kernel, gamma)

...ó b) cross_val_score:
Ejecute el siguiente tuning de parámetros (learning curves - notebook 10, "https://gitlab.com/bivl2ab/academico/cursos-uis/ai/ai-uis-student/-/blob/master/10_std_Notes_Regression.ipynb") para determinar el MEJOR número de folds para cada estimador, con parámetros por defecto:
   - DecisionTree
   - RandomForest
   - SVC/R

Al ejecutar las tareas a) ó b) usted obtiene un valor de 4.0 en ESE PUNTO.
Sin embargo...
c) Si desea la nota más alta posible (5.0) en ESE PUNTO, lleve a cabo las tareas (a) y (b).

3. Grafique los resultados de cada ejecución del ítem 2, con matplotlib, usando el gráfico adecuado (plot, bar, etc).

*Si tiene problemas con la ejecución de alguna de las tareas (colapsa colaboratory o algo similar), debe mostrarme la celda de código en donde ocurre el error, como evidencia.

*Cada sustentación durará máximo 10 minutos.

Cualquier inquietud quedo pendiente.

Saludos,

# Punto 1

## sparing data for train and test
"""

X = data.drop('hypertensive', axis=1).values
y = data['hypertensive'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)

"""##Desition Tree Classifier"""

est = DecisionTreeClassifier()
est.fit(X_train,y_train)
print(accuracy_score(est.predict(X_test), y_test))

"""##Random Forest Classifier

"""

est = RandomForestClassifier()
est.fit(X_train,y_train)
print(accuracy_score(est.predict(X_test), y_test))

"""## Support Vector Machine"""

est = SVC()
est.fit(X_train,y_train)
print(accuracy_score(est.predict(X_test), y_test))

"""# Puntos 2.a y 3a
# train_test_split

##Desition Tree Classifier (with params)
"""

#criterion{“gini”, “entropy”, “log_loss”}, default=”gini”
est = DecisionTreeClassifier(max_depth=2, criterion="entropy")
est.fit(X_train,y_train)
print(accuracy_score(est.predict(X_test), y_test))

"""##Random Forest Classifier (with params)"""

#criterion{“gini”, “entropy”, “log_loss”}, default=”gini”
est = RandomForestClassifier(n_estimators=85, criterion="entropy")
est.fit(X_train,y_train)
print(accuracy_score(est.predict(X_test), y_test))

"""##Support Vector Machine (with params)"""

#kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
# gamma{‘scale’, ‘auto’} or float, default=’scale’
est = SVC(kernel="poly", gamma="auto")
est.fit(X_train,y_train)
print(accuracy_score(est.predict(X_test), y_test))

"""## Performance of desition tree varing max_depth"""

means, stds = [], []

n_depths_range = range(1,50)
for depth in n_depths_range:
  est = DecisionTreeClassifier(max_depth=depth, criterion="entropy")
  s = cross_val_score(est, X, y, cv=None, scoring=make_scorer(mean_squared_error))
  means.append(np.mean(s))
  stds.append(np.std(s))

means = np.r_[means]
stds  = np.r_[stds]

plt.plot(n_depths_range, means, label="mean", color="black")
plt.fill_between(n_depths_range, means-stds, means+stds, color="blue", alpha=.5, label="std")
plt.xlabel("max_depth")
plt.ylabel("performance")
plt.legend()

"""## Performance of ramdom forest varing n_stimators"""

means, stds = [], []

n_estimators_range = range(1,30)
for n_estimators in n_estimators_range:
  est = RandomForestClassifier(n_estimators=n_estimators, criterion="entropy")
  s = cross_val_score(est, X, y, cv=None, scoring=make_scorer(mean_squared_error))
  means.append(np.mean(s))
  stds.append(np.std(s))

means = np.r_[means]
stds  = np.r_[stds]

plt.plot(n_estimators_range, means, label="mean", color="black")
plt.fill_between(n_estimators_range, means-stds, means+stds, color="blue", alpha=.5, label="std")
plt.xlabel("max_depth")
plt.ylabel("performance")
plt.legend()

"""## Performance of support vector machine varing kernel param"""

means, stds = [], []

svg_kernels = ["poly", "rbf", "sigmoid", "precomputed", "linear"]
for kernel in svg_kernels:
  print(kernel)
  est = SVC(kernel=kernel, gamma="auto")
  s = cross_val_score(est, X, y, cv=None, scoring=make_scorer(mean_squared_error))
  means.append(np.mean(s))
  stds.append(np.std(s))

means = np.r_[means]
stds  = np.r_[stds]

plt.plot(svg_kernels, means, label="mean", color="black")
plt.fill_between(svg_kernels, means-stds, means+stds, color="blue", alpha=.5, label="std")
plt.xlabel("max_depth")
plt.ylabel("performance")
plt.legend()

"""# Puntos 2.b y 3b
# cross_val_score

# Definir rango
"""

folds_range = range(2,10)

"""# Modelos"""

models = {
    "DecisionTree": DecisionTreeClassifier(),
    "RandomForest": RandomForestClassifier(),
    "SVC": SVC()
}

results = {}

for model_name, model in models.items():
    print(f"Evaluando: {model_name}")
    model_scores = []
    for n_folds in folds_range:
        kf = KFold(n_splits=n_folds, shuffle=True, random_state=21)
        scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
        mean_score = np.mean(scores)
        model_scores.append(mean_score)
        print(f"Folds: {n_folds}, Accuracy: {mean_score:.4f}")
    results[model_name] = model_scores

"""# Resultados"""

# Determinar el mejor número de folds para cada modelo
for model_name in results:
    best_idx = np.argmax(results[model_name])
    best_folds = folds_range[best_idx]
    best_score = results[model_name][best_idx]
    print(f"Mejor número de folds para {model_name}: {best_folds} con accuracy: {best_score:.4f}")

"""# Grafica DecisionTree"""

means = np.array(results["DecisionTree"])  # Promedios
stds = np.std(means)

plt.figure(figsize=(8, 5))
plt.plot(folds_range, means, label="Mean Accuracy", color="black", marker="o")
plt.fill_between(folds_range, means - stds, means + stds, color="blue", alpha=0.3, label="Std Dev")
plt.title("Performance vs Folds (DecisionTree)", fontsize=14)
plt.xlabel("Número de Folds (n_splits)", fontsize=12)
plt.ylabel("Precisión Promedio (Accuracy)", fontsize=12)
plt.xticks(folds_range)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

"""# Grafica RandomForest"""

means = np.array(results["RandomForest"])
stds = np.std(means)

plt.figure(figsize=(8, 5))
plt.plot(folds_range, means, label="Mean Accuracy", color="black", marker="o")
plt.fill_between(folds_range, means - stds, means + stds, color="blue", alpha=0.3, label="Std Dev")
plt.title("Performance vs Folds (RandomForest)", fontsize=14)
plt.xlabel("Número de Folds (n_splits)", fontsize=12)
plt.ylabel("Precisión Promedio (Accuracy)", fontsize=12)
plt.xticks(folds_range)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

"""# Grafica para SVC"""

means = np.array(results["SVC"])
stds = np.std(means)

plt.figure(figsize=(8, 5))
plt.plot(folds_range, means, label="Mean Accuracy", color="black", marker="o")
plt.fill_between(folds_range, means - stds, means + stds, color="blue", alpha=0.3, label="Std Dev")
plt.title("Performance vs Folds (SVC)", fontsize=14)
plt.xlabel("Número de Folds (n_splits)", fontsize=12)
plt.ylabel("Precisión Promedio (Accuracy)", fontsize=12)
plt.xticks(folds_range)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

"""3. Sustentación de proyectos finales:
Requisitos de la entrega:
- PARTE I: al notebook que ya tienen elaborado, agregarle la implementación de un perceptrón multicapa (TAL COMO SE VIÓ EN LOS NOTEBOOKS 11 y 12) con: 3 capas ocultas, 6 capas ocultas y 10 capas ocultas. Calcular el accuracy_score ó el mean_absolute_error (según su tarea) para cada uno de esos 3 casos.
- PARTE II: tener en cuenta las indicaciones de la sección "Proyecto funcional IA" del repositorio (https://gitlab.com/bivl2ab/academico/cursos-uis/ai/ai-uis-student/). Esta sección es OBLIGATORIA y debe enviarse al CORREO de su profesor EL DÍA ANTERIOR A LA SUSTENTACIÓN (miércoles 11 de diciembre).
*Fecha: jueves 12 de diciembre, en sus horarios de clase.

# Entrega 3

##1 perceptron multicapa con 3 capas ocultas
"""

unique_values = len(data["hypertensive"].unique())

model = tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=X_train[0].shape),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(unique_values, activation=tf.nn.softmax)
  ])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, verbose=1)
y_pred_prob= model.predict(X_test, verbose=1)
y_pred = np.argmax(y_pred_prob, axis=1)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

"""## 2 Perceptrón multicapa con 6 capas ocultas"""

model = tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=X_train[0].shape),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(unique_values, activation=tf.nn.softmax)
  ])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, verbose=1)
y_pred_prob= model.predict(X_test, verbose=1)
y_pred = np.argmax(y_pred_prob, axis=1)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

"""## 3 perceptrón multicapa con 9 capas ocultas"""

model = tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=X_train[0].shape),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(unique_values, activation=tf.nn.softmax)
  ])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, verbose=1)
y_pred_prob= model.predict(X_test, verbose=1)
y_pred = np.argmax(y_pred_prob, axis=1)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
