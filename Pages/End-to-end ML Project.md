# End-to-end ML Project

- Popular data repositories:
  - [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/index.php)
  - [Registry of Open Data on AWS](https://aws.amazon.com/fr/datasets/)
  - [List of datasets for machine learning research - Wikipedia](https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research)
  - [Kaggle: Your Home for Data Science](http://kaggle.com/)

- Background: You're hired as a data scientist for a real estate investment company to analyze the housing market in California.
  - What can we do to help the firm invest better in real estate?
  - The dataset: [California Housing Prices \| Kaggle](https://www.kaggle.com/camnugent/california-housing-prices)
    - Based on US Census Bureau
    - Organized by district (600-3000 people)

## 8 Main Steps of a ML Project
1. Look at the big picture.
    - Questions that must be answered before starting
    - Ask the purpose of building a model -> frame your problems and objectives:
      - What do you expect, use, and benefit from this model?
      - What learning algorithm to use?
      - What performance measure to evaluate (metric)?
        - One option is **Mean Abosulte Error** ($|residual|$)
        - $MAE(X,h) = \frac{1}{m}\sum_{i=1}^m|h(x^{(i)})-y^{(i)}|$
        - $m$ is the number of instances, h is the hypothesis function
        - Another option is the **Root Mean Square Error**
        - $RMSE(X,h) = \sqrt{\frac{1}{m}\sum_{i=1}^m(h(x^{(i)})-y^{(i)})^2}$
      - How much effort to be spent?  
2. Get the data.
    - Load data from a .csv file with `df = pd.read_csv(csv_path)`
    - `df.head()` prints the first 5 rows in a dataframe
    - `df.info()` provides you an overview of the dataframe
    - `df.describe()` provides you with basic statistics
    - Create train and test sets with `train_set, test_set = train_test_split(df,test_size=TEST_PROP,random_state=SEED)` from `sklearn.model_selection`
3. Discover and visualize the data to gain insights
    - Plot a histogram with `df.hist()`
    - Discover and visualize the data with `df.plot(kind=?,x=X_COL,y=Y_COL)`
    - Look at correlations with `corr_matrix = df.corr()`
    - Check all correlations with `df.scatter_matrix()`
    - Experiment with Feature Extraction like so: `df["New feature"] = df["Feature 1"] <MATH OPERATION> df["Feature 2"]`
4. Prepare the data for Machine Learning algorithms (data cleaning)
    - Dectect missing values `incomplete_rows = df[df.isnull().any(axis=1)]`
    - Fill in missing values with `imputer = Imputer(strategy=?)` and then `arr = imputer.transform(df)`
    - Process categorical inputs, possibly by encoding the categories with `cat_encoder = OneHotEncoder(sparse=False)` and then `arr = cat_encoder.fit(df_category_columns)`
    - Use `Pipeline` for a sequence of transormations with `num_pipe = Pipeline([(STRATEGY 1),(STRATEGY 2),(STRATEGY 3...)])` followed by `arr = num_pipe.fit_transform(df_num_categories)`
5. Select a model and train it.
6. Fine-tune your model
7. Present your solution
8. Launch, Monitor,
