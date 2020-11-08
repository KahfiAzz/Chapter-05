# program hitung syarat kelulusan

# input nilai

# Bahasa Indonesia
BahasaIndonesia = int(input('Nilai Bahasa Indonesia :'))
if(BahasaIndonesia < 0 or BahasaIndonesia > 100):
  print('Maaf input ada yang tidak valid')
    
# Matematika
Matematika = int(input('Nilai Matematika :'))
if(Matematika < 0 or Matematika > 100):
     print('Maaf input ada yang tidak valid')

# IPA
IPA = int(input('Nilai IPA :'))
if(IPA < 0 or IPA > 100):
    print('Maaf input ada yang tidak valid')

# Status Kelulusan
if(BahasaIndonesia > 60 and IPA > 60 and Matematika > 70):
  print('Status Kelulusan : LULUS')
else:
  print('Status Kelulusan : TIDAK LULUS')
  print('Sebab')
if(BahasaIndonesia < 60):
      print('- Nilai Bahasa Indonesia kurang dari 60')
if(Matematika < 70):
      print('- Nilai Matematika kurang dari 70')
