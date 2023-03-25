changing = str(input('Lütfen değiştirmek istediğiniz harfi seçin: ')) # Kullanıcıdan değiştirilecek harf istenir ve değişkene atanır
changed = str(input('Harfinizi hangi harf ile değiştirmek istersiniz: ')) # Kullanıcıdan harfin ne ile değiştirileceği istenir ve değişkene atanır

class Key:
    def __init__(self,changing,changed):
        self.changing = changing # değiştirilecek harfi tutan değişken
        self.changed = changed # değiştirilecek harfin yerine kullanılacak olan harfi tutan değişken
        self.file1 = [] # değiştirilecek dosyanın içeriğini tutan liste

    def open_file(self):
       file = open('deneme.txt','r',encoding='utf-8') # 'deneme.txt' dosyası açılır ve içeriği okunur
       for x in file:
            self.file1.append(x.replace(self.changing,self.changed)) # dosyanın içindeki belirli harf, diğer harfle değiştirilir ve değiştirilmiş veri "file1" listesine eklenir
       
    def change_file(self):
        self.open_file() # "open_file" fonksiyonu çağrılır
        file2 = open('deneme.txt','r+',encoding='utf-8') # 'deneme.txt' dosyası hem okunup hem de yazılabilir modda açılır
        file3=''.join(map(str,self.file1)) # "file1" listesi birleştirilerek tek bir string haline getirilir
        file2.write(file3) # değiştirilmiş veri, 'deneme.txt' dosyasına yazılır
        
work = Key(changing,changed) # Key sınıfından bir nesne oluşturulur
work.change_file() # "change_file" fonksiyonu çağrılır
