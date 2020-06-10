from django.db import migrations


def populate_colors(apps, schema_editor):
    Color = apps.get_model("cars", "Color")
    db_alias = schema_editor.connection.alias
    Color.objects.using(db_alias).bulk_create([
        Color(name="Green"),
        Color(name="Red"),
        Color(name="Blue"),
        Color(name="White"),
        Color(name="Black")
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('cars', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_colors)
    ]
