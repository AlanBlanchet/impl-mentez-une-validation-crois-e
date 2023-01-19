class GridSearchCV:
    def __init__(self, classif, param_grid, cv, scoring):
        self.classif = classif
        self.param_grid = param_grid
        self.cv = cv
        self.scoring = scoring

    def fit(self, X, y):
        Y = self.classif.fit(X, y)
        print(Y)
        return Y
