from django.db import models

# Create your models here.

class HomeSliderActive(models.Model):
    name1 = models.CharField('HomeSlider name1', max_length=30)
    name2 = models.CharField('HomeSlider name2', max_length=30)
    about = models.TextField('HomeSlider about')
    img = models.ImageField('HomeSlider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSliderActive'
        verbose_name_plural = 'HomeSlidersActive'


class HomeSlider(models.Model):
    name1 = models.CharField('HomeSlider name1', max_length=30)
    name2 = models.CharField('HomeSlider name2', max_length=30)
    about = models.TextField('HomeSlider about')
    img = models.ImageField('HomeSlider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'

class HomeInfo(models.Model):
    name = models.CharField('HomeInfo name', max_length=30)
    about = models.TextField('HomeInfo about')
    img = models.ImageField('HomeInfo image', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeInfo'
        verbose_name_plural = 'HomeInfos'



class HomeProduct(models.Model):
    name = models.CharField('Product name', max_length=30)
    img = models.ImageField('Product image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'

class HomeCustomerActive(models.Model):
    name = models.CharField('Customer name', max_length=30)
    about = models.TextField('Customer about')
    img = models.ImageField('Customer image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeCustomerActive'
        verbose_name_plural = 'HomeCustomersActive'


class HomeCustomer(models.Model):
    name = models.CharField('Customer name', max_length=30)
    about = models.TextField('Customer about')
    img = models.ImageField('Customer image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeCustomer'
        verbose_name_plural = 'HomeCustomers'



class About(models.Model):
    name = models.CharField('About name', max_length=30)
    about = models.TextField('About about')
    img = models.ImageField('About image', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Product(models.Model):
    name = models.CharField('Product name', max_length=30)
    img = models.ImageField('Product image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

