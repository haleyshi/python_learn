import matplotlib.pyplot as plt
import pandas as pds

names = ["Bob", "Jenny", "Amy", "John"]
births = [503, 720, 1011, 330]

# Zip the lists
birthDS = list(zip(names, births))
print '###DataSet'
print birthDS

# Generated DataSet
df = pds.DataFrame(data=birthDS, columns=["Name", "Birth"])
print '###DataFrame Store to CSV'
print df

# Store DataSet to CSV
df.to_csv('births.csv', index=False, header=False)

# Read from CSV to DataSet
df1 = pds.read_csv(r'births.csv', names=["NAME", "BIRTH"])
print "###DataFrame 1 - Read From CSV"
print df1

# Check the data type
print "###DataTypes for DF"
print df.dtypes

print "###DataTypes for DF1"
print df1.dtypes

print "###DataTypes for DF['Birth']"
print df.Birth.dtype

# Data Analysis
sortedDf = df.sort_values(['Birth'], ascending=False)
print "###Sorted DataFrame, 'Birth', ascending=False"
print sortedDf

print "###Head 2 of Sorted DataFrame"
print sortedDf.head(2)

print "###Max 'Birth'"
print df['Birth'].max()
print "###Min 'Birth'"
print df['Birth'].min()

# Visualization
df['Birth'].plot(kind='bar')
maxBirth = df['Birth'].max()
maxName = df['Name'][df['Birth'] == maxBirth].values
text = str(maxBirth) + " - " + maxName
plt.annotate(text, xy=(1, maxBirth), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
print 'The most popular name'
print df[df['Birth'] == maxBirth]

plt.show()