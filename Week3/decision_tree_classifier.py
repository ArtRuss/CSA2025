import pandas as pd
import seaborn as sns
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import dtreeviz

df = pd.read_excel("DataCollection_Responses.xlsx")
df = df.drop(['Timestamp', 'Email Address'], axis=1)
df_cats = df.iloc[:, [0,4,8]].copy()
df_cats['class'] = 'cat'
df_cats.rename(columns={'How many legs do they have? [Cat]': 'Number of legs',
                        'Do they have tails? [Cat]': 'Tail',
                        'What is the size of cats in inches?': 'Size (in)'}, inplace=True)
df_horses = df.iloc[:, [1,5,9]].copy()
df_horses['class'] = 'horse'
df_horses.rename(columns={'How many legs do they have? [Horse]': 'Number of legs',
                        'Do they have tails? [Horse]': 'Tail',
                        'What is the size of horses in inches?': 'Size (in)'}, inplace=True)
df_frogs = df.iloc[:, [2,6,10]].copy()
df_frogs['class'] = 'frog'
df_frogs.rename(columns={'How many legs do they have? [Frog]': 'Number of legs',
                        'Do they have tails? [Frog]': 'Tail',
                        'What is the size of frogs in inches?': 'Size (in)'}, inplace=True)
df_flamingos = df.iloc[:, [3,7,11]].copy()
df_flamingos['class'] = 'flamingo'
df_flamingos.rename(columns={'How many legs do they have? [Flamingo]': 'Number of legs',
                        'Do they have tails? [Flamingo]': 'Tail',
                        'What is the size of flamingos in inches?': 'Size (in)'}, inplace=True)
df = pd.concat([df_cats,df_horses,df_frogs,df_flamingos]).reset_index()
df = df.drop(["index"], axis=1)

df.loc[df['Tail']=="Yes", 'Tail'] = 1
df.loc[df['Tail']=="No",  'Tail'] = 0

df_data = df.iloc[:, 0:3]
df_labels = df.iloc[:, 3]


# Create Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
clf.fit(df_data, df_labels)

# Classifier Visualization
text_representation = tree.export_text(clf)
print(text_representation)

"""
Remember DTC??
- Build a package/module able to fit data into a
decision tree classifier:
- Use IFs and Loops!
- Use PEP 8
- Use modularity
- Build tests:
- Create random sets of 2D points.
- Test with fixed seed.
- Test with the zoo_classifier data.
"""
