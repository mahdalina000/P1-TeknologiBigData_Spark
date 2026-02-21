from pyspark.sql import SparkSession

# Inisialisasi Spark
spark = SparkSession.builder.appName("FinalTest").getOrCreate()

# Membuat data super simpel agar tidak Stack Overflow
df = spark.range(5).toDF("Nomor_Antrian")

print("\n" + "!"*30)
print("SAY HELLO TO BIG DATA!")
print("!"*30)

# Menampilkan tabel
df.show()

print("!"*30)
spark.stop()