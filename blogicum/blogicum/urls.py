from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("blog.urls", namespace="blog")),
    path("pages/", include("pages.urls", namespace="pages")),
    path("admin/", admin.site.urls),
]

# handler403 = "pages.views.csrf_failure"
# handler404 = "pages.views.page_not_found"
# handler500 = "pages.views.server_error"
