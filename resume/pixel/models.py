from django.db import models
from django.urls import reverse
# Create your models here.
class Accounts(models.Model):
    typeofacc = models.CharField(max_length=255)
    codeacc = models.CharField(max_length=255)
    power = models.IntegerField(default=30,null=True)
    def __str__(self):
        return "{} . {} - {}".format(self.id,self.typeofacc,self.codeacc)
    class Meta:
        ordering = ['id']
    
class users(models.Model):
    username=models.CharField(max_length=255)
    image=models.ImageField(max_length=255,upload_to="posts-img",default='posts-img/upic.png')
    password=models.CharField(max_length=255,default=123)
    codeacc=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    tellNumber=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    location=models.TextField(max_length=500,null=True)
    age=models.IntegerField()
    birthday=models.DateField(max_length=100)
    about=models.TextField(default="",null=True)
    education=models.CharField(max_length=255,default="",null=True)
    langs=models.CharField(max_length=255,default="",null=True)
    t_p=models.IntegerField(default=0,null=True)
    cod_posti=models.CharField(max_length=255,default="",null=True)
    def __str__(self):
        return f"{self.codeacc} - {self.username}"

class pages(models.Model):
    uname=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    discriptions=models.TextField(max_length=3255)
    par=models.CharField(max_length=255,null=True,default="")
    projects=models.IntegerField(default=0,null=True)

class cards(models.Model):
    uname=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255,default='')
    datetime=models.CharField(max_length=255)
    resources=models.CharField(max_length=255)
    dis=models.TextField(max_length=3000)
    def __str__(self):
        return self.title

class projects(models.Model):
    uname=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    proNam=models.CharField(max_length=255)
    dis=models.TextField(max_length=255)
    def __str__(self) -> str:
        return self.uname

class skills(models.Model):
    uname=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    skilNam=models.CharField(max_length=255)
    range=models.IntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.skilNam}-{self.range}"
    
class contact(models.Model):
    uname=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    email=models.EmailField()
    title=models.CharField(max_length=255)
    mess=models.TextField(max_length=5000)

class categorise(models.Model):
    name = models.CharField(max_length=255)
    


class posts(models.Model):
    uname = models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    category = models.ManyToManyField(categorise, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts-img/',default='posts-img/project-6.png')
    p_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    cview = models.IntegerField(default=0)
    desc = models.TextField()
    
    def __str__(self):
        return f'{self.id}. {self.title}'
    
    def get_absolute_url(self):
        return reverse('pixel:single',kwargs={'post':self.id})

class comments(models.Model):
    uname = models.ForeignKey(users, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    c_date = models.DateTimeField()
    subject = models.TextField()
    post = models.ForeignKey(posts, on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title
