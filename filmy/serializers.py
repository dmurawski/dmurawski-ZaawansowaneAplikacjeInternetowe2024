from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Film, ExtraInfo, Ocena, Aktor

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


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'



class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania', 'gatunek', 'rezyser', 'filmy']


class OcenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocena
        fields = ['recenzja','gwiazdki','film']


class AktorSerializer(serializers.ModelSerializer):
    filmy = serializers.SlugRelatedField(slug_field='tytul', queryset = Film.objects.all(), many=True)
    class Meta:
        model = Aktor
        fields = ['id','imie','nazwisko','filmy']


class FilmModelSerializer(serializers.ModelSerializer):
    extrainfo = serializers.StringRelatedField()
    ocena_set = OcenaSerializer(read_only=True,many=True)
    aktor_set = serializers.StringRelatedField(read_only=True, many= True)
    class Meta:
        model = Film
        fields = ['id', 'tytul', 'rok','imdb_points','premiera','opis','owner','extrainfo','ocena_set','aktor_set']


class UserSerializer(serializers.ModelSerializer):
    filmy = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())
    einfo = serializers.PrimaryKeyRelatedField(queryset=ExtraInfo.objects.all())
    oceny = serializers.PrimaryKeyRelatedField(many=True, queryset=Ocena.objects.all())
    aktorzy = serializers.PrimaryKeyRelatedField(many=True, queryset=Aktor.objects.all())
    class Meta:
        model = User
        fields = ['id','username', 'filmy']

class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        password = validated_data.get('password', None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user
