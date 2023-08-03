
# Alpha testing primarily takes place within the organization 
# Beta testing takes place in the user’s environment
# Only functionality and usability are checked during Alpha
# Usability, functionality, security, and dependability are Beta

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

# Read data
soap = pd.read_csv("Projects/soap.csv")
soap

# Calculate weight loss
soap["wloss"] = soap["pre"] - soap["post"]
soap

# Some EDA
soap.groupby("level")["wloss"].mean()

soap.boxplot(column="wloss", by="level");

# H0 (Null Hypothesis) u1 = u2 = u3

# HA (Alternative Hypothesis) at least one ui != uj for some i != j

# Mindless SciPy one-way ANOVA test
soap1 = soap.loc[soap['level'] == 1, "wloss"]
soap2 = soap.loc[soap['level'] == 2, "wloss"]
soap3 = soap.loc[soap['level'] == 3, "wloss"]
stats.f_oneway(soap1, soap2, soap3)

# Imports from statsmodels
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# statsmodels follows the R pattern of using "formulas" to specify a model
# In order to specify a variable is categorical, use the C() function.
model = ols("wloss ~ C(level)", soap).fit()

# Can summarize this just like other statsmodels models
model.summary()

# ANOVA Test (F Score)
anova_lm(model)