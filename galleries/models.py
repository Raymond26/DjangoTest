from django.db import models
from django.db.models.signals import post_save

def image_file_name(instance, filename):
    return '/'.join(['images', str(instance.owner_id), filename])
def thumbnail_file_name(instance, filename):
    return '/'.join(['images', str(instance.owner_id), "thumb_" + filename])

class ImageModel(models.Model):
    view_count = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('members.Member', related_name='member_images', null=True)
    image = models.ImageField(upload_to=image_file_name)
    thumbnail = models.ImageField(upload_to=thumbnail_file_name)
    filename = models.CharField(blank=True, null=True,max_length=130)
    filesize = models.IntegerField(default=0)
    title = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=500, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    is_public = models.BooleanField(default=True)

    comment_tree = models.ForeignKey('galleries.PhotoCommentTree', related_name='owner_image', null=True)

    def __unicode__(self):
        return self.image.name

    def increment_view_count(self):
        self.view_count += 1
        models.Model.save(self)

'''
def image_post_save(sender, instance, created, **kwargs):
    instance.filename = instance.image.name
    instance.filesize = instance.image.size

post_save.connect(image_post_save, sender=ImageModel)
'''

class Gallery(models.Model):
    title = models.CharField(max_length=75)
    title_slug = models.SlugField(unique=True)
    is_public = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    photos = models.ManyToManyField('ImageModel', related_name='linked_galleries',
                                    null=True, blank=True)
    # rating = null when there are no ratings yet
    rating = models.PositiveSmallIntegerField(null=True)

    def __unicode__(self):
        return self.title

class UserGallery(Gallery):

    owner = models.ForeignKey('members.Member', related_name='member_galleries', null=True)

    def __unicode__(self):
        return self.title

    def add_photo(self, photo):
        self.photos.add(photo)

class UserPublicGallery(UserGallery):

    def __unicode__(self):
        return self.title

class UserPrivateGallery(UserGallery):
    is_public = models.BooleanField(default=False)

'''
class FavoritesGallery(Gallery):
'''

class PhotoCommentTree(models.Model):
    # owner_photo = models.OneToOneField(ImageModel, related_name='comment_tree_2')
    # test = models.CharField(null=True, blank=True, max_length=50)

    def __unicode__(self):
        return str(self.pk)

class PhotoComment(models.Model):
    owner = models.ForeignKey('members.Member', related_name='member_comments', null=True)
    posted_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    tree = models.ForeignKey('galleries.PhotoCommentTree', related_name='comments', null=True)

    def __unicode__(self):
        return str(self.tree.pk) + "_" + str(self.pk)