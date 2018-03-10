Algorithm         | Parameters              |Training time | Predicting time | accuracy |
Nearet neightbors | default                 |0.001         |0.002            |0.92      |
Nearet neightbors | n_neighbors=1           |0.001         |0.001            |0.94      |
Nearet neightbors | n_neighbors=10          |0.002         |0.002            |0.932     |
Nearet neightbors | n_neighbors=30          |0.002         |0.005            |0.928     |
Adaboost          | default                 |0.098         |0.005            |0.924     |
Adaboost          | n_estimators=100        |0.193         |0.009            |0.924     |
Adaboost          | n_estimators=100, learning_rate=0.5        |0.191         |0.009            |0.916     |
Adaboost          | n_estimators=100, learning_rate=2          |0.19          |0.01             |0.904     |
Random forest     | default 1st time        |0.023          |0.001           |0.92      |
Random forest     | default 2nd time        |0.025          |0.001           |0.916     |
Random forest     | n_estimators=20         |0.046          |0.002           |0.912     |
Random forest     | n_estimators=5          |0.013          |0.001           |0.928     |
Random forest     | n_estimators=5, min_samples_split=50       |0.015         |0.001           |0.928     |
