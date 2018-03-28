nm = raw_input("Masukan Nama\n: ")
uts = input("Masukan Nilai UTS\n: ")
uas = input("Masukan Nilai UAS\n: ")
tgs = input("Masukan Nilai TUGAS\n: ")
print "\n"
print "Nama           : ", nm
print "Nilai UTS      : ", uts
print "Nilai UAS      : ", uas
print "Nilai TUGAS    : ", tgs
akhir = (uts+uas+tgs)/3
print "Nilai Akhir    : ", akhir
print "\n"
if akhir >= 80:
    print"Nilai Huruf   : A"
    print"Keterangan    : Lulus"
elif akhir >= 70 and akhir < 79:
    print"Nilai Huruf   : B"
    print"Keterangan    : Lulus"
elif akhir >= 50 and akhir < 69:
    print"Nilai Huruf   : C"
    print"Keterangan    : Tidak Lulus"
elif akhir >= 40 and akhir < 49:
    print"Nilai Huruf   : D"
    print"Keterangan    : Tidak Lulus"
elif akhir >= 0 and akhir < 39:
    print"Nilai Huruf   : E"
    print"Keterangan    : Tidak Lulus"

