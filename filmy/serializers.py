from rest_framework import serializers
from filmy.models import Film, Ocena, Aktor, ExtraInfo
from django.contrib.auth.models import User

# class FilmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Film
#         fields = ['id', 'tytul', 'rok', 'opis', 'premiera', 'imdb_pkts']
#
#     def create(self, validated_data):
#         return Film.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.tytul = validated_data.get('tytul', instance.tytul)
#         instance.rok = validated_data.get('rok', instance.rok)
#         instance.opis = validated_data.get('opis', instance.opis)
#         instance.premiera = validated_data.get('premiera', instance.premiera)
#         instance.imdb_pkts = validated_data.get('imdb_pkts', instance.imdb_pkts)
#         instance.save()
#         return instance
#
#
# class OcenaModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ocena
#         fields = ['id', 'recenzja', 'gwiazdki', 'film']
#
#     def create(self, validated_data):
#         return Ocena.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.recenzja = validated_data.get('recenzja', instance.recenzja)
#         instance.gwiazdki = validated_data.get('gwiazdki', instance.gwiazdki)
#         instance.film = validated_data.get('film', instance.film)
#         instance.save()
#         return instance

class FilmModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "is_superuser", "email", "is_staff", "is_active"]

class OcenaModelSerializer(serializers.ModelSerializer):
    film = FilmModelSerializer()
    class Meta:
        model = Ocena
        fields = '__all__'

class AktorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktor
        fields = '__all__'

class ExtraInfoSerializer(serializers.ModelSerializer):
    film = FilmModelSerializer()
    class Meta:
        model = ExtraInfo
        fields = '__all__'