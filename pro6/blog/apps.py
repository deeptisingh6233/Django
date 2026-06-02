from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = "blog"

    class BlogConfig(AppConfig):
        default_auto_field=
        name="Blog"

        def ready(self):
            import blog.signals
    
    
