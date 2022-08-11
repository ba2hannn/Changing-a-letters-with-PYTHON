'''Lütfen kodun üzerindeki "deneme.txt" adlı yazıyı kendi dosyanızın ismi ile değiştirmeyi unutmayınız.'''

changing = str(input('Lütfen değiştirmek istediğiniz harfi seçin: '))
changed = str(input('Harfinizi hangi harf ile değiştirmek istersiniz: '))
class Key:
    def __init__(self,changing,changed):
        self.changing = changing
        self.changed = changed
        self.file1 = []

    def open_file(self):
       file = open('deneme.txt','r',encoding='utf-8')
       for x in file:
            self.file1.append(x.replace(self.changing,self.changed))
       
    def change_file(self):
        self.open_file()
        file2 = open('deneme.txt','r+',encoding='utf-8')
        file3=''.join(map(str,self.file1))
        file2.write(file3)
        
work = Key(changing,changed)
work.change_file()
