import pandas as pd

# إنشاء بيانات تجريبية
pd.DataFrame({
    "name": ["Ali", "Ali", None, " Sara ", "omar"],
    "sales": [100, 100, 50, None, 75],
}).to_csv("messy.csv", index=False)

# قراءة البيانات وتنظيفها
df = pd.read_csv("messy.csv")
df = df.dropna(subset=["name"])
df["name"] = df["name"].str.strip().str.title()
df["sales"] = df["sales"].fillna(0)
df = df.drop_duplicates()

# حفظ البيانات النظيفة
df.to_csv("clean.csv", index=False)

print(df)
