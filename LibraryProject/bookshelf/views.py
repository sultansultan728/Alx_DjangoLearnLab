from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Article


@permission_required('advanced_features_and_security.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/article_list.html", {"articles": articles})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Article.objects.create(
            title=title,
            content=content,
            created_by=request.user
        )
        return redirect("article_list")

    return render(request, "articles/create_article.html")


@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.save()
        return redirect("article_list")

    return render(request, "articles/edit_article.html", {"article": article})


@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.delete()
        return redirect("article_list")

    return render(request, "articles/confirm_delete.html", {"article": article})

