import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = { 'Subject': ['Math', 'Physics', 'Chemistry', 'Biology', 'English'], 
        'Avg_Score': [1, 2, 3, 4, 5], 
        'Hours_Studied': [6, 7, 8, 9, 10] }

df = pd.DataFrame(data)

plt.figure(figsize=(6, 4))
sns.barplot(x='Subject', y='Avg_Score', data=df, palette='viridis')
plt.title('Average Scores by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Scores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('average_scores_by_subject.png')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Hours_Studied', y='Avg_Score', data=df, hue='Subject', palette='viridis', s=100)
plt.title('Average Scores vs Hours Studied')
plt.xlabel('Hours Studied') 
plt.ylabel('Average Scores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('average_scores_vs_hours_studied.png')
plt.show()
