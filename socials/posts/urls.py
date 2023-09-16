from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
    path("", views.PostList.as_view(), name="all"),
    path("", views.postAll.as_view, name="allPost"),
    path(
        "post/<int:post_id>/comment/",
        views.Comment.as_view(),
        name="view_comment",
    ),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path(
        "post/<pk>/add_comment/",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),
    path("by/<username>/", views.UserPosts.as_view(), name="for_user"),
    path("by/<username>/<int:pk>/", views.PostDetail.as_view(), name="single"),
    path("delete/<int:pk>/", views.DeletePost.as_view(), name="delete"),
    path("post/following/",views.Fyp.as_view(),name="post_following")
]
