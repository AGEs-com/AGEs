from django.db import models
from datetime import datetime
#import subprocess

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.category_name
    
#from django.template.defaultfilters import slugify
class Item(models.Model):
    category = models.ForeignKey(Category)
    item_name = models.CharField(max_length=128, unique=True) #同じ名前は二度登録できない
    num_of_pictures = models.IntegerField(default=0) #画像数
#     slug = models.SlugField(unique=True) #項目を押下したときのリンクURLに必要
#     
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.item_name) #「nagasawa　masami」ならば「nagasawa_masami」になる
#         super(Item, self).save(*args, **kwargs) # TODO: なにをしているかイマイチ理解していない。。。
#         
#     # slugify()はアルファベット以外はエラーになるから変える必要あり
#     def changeKanjiToAlphabet(self, item_name):
#         # Kakasiを使って名前をローマ字sss
#         slug = subprocess.getstatusoutput('echo "%s" | nkf -e | kakasi -Ha' %item_name)
    
    def __str__(self):
        return self.item_name
    
class Picture(models.Model):
    item = models.ForeignKey(Item)
    picture_name = models.CharField(max_length=128)
    register_date = models.DateField(default=datetime.now) # model登録時に自動的に現在時刻を設定する
    age = models.IntegerField(default = 0)
    description = models.CharField(max_length=200)
    # pictureを保存するフォルダはItemインスタンスのitem_nameとする
    picture_folder = 'picture' #item.filepath().item_name TODO Item別にフォルダ名を変えたいがうまくいかず。。。
    # mediaフォルダのpicture_folderに画像を保存するように設定、空の値を設定したい場合はblank=Trueを設定
    image = models.ImageField(upload_to=picture_folder, blank=True)
    
    def __str__(self):
        return self.picture_name