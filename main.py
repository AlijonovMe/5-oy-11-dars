from database import connect
from collections import namedtuple

# 1.1
connect.create_categories()

# 1.2
connect.create_news()

# 1.3
connect.create_comments()

# 2
connect.alter_news()
connect.alter_comments()

# 3
connect.insert_categories()
connect.insert_news()
connect.insert_comments()

# 4
connect.update_news()
connect.update_news_days()

# 5
connect.delete_comments()

# 6.1
AliasNews = namedtuple('AliasNews', ['news_id', 'news_title', 'category_name'])
aliasNews = connect.select_alias_news()

for news in aliasNews:
    alias = AliasNews(*news)
    print(f"{alias.news_id} | {alias.news_title} | {alias.category_name}")

print("\n- - - - - - - - - - - - - - - - - - - - -\n")

# 6.2
Technology = namedtuple('Technology', ['id', 'title', 'content', 'published_at', 'is_published', 'category_id', 'views'])
technology = connect.select_technology()

for techno in technology:
    tech = Technology(*techno)
    print(f"{tech.id} | {tech.title} | {tech.content} | {tech.published_at} | {tech.is_published} | {tech.category_id} | {tech.views}")

print("\n- - - - - - - - - - - - - - - - - - - - -\n")

# 6.3
isPublished = namedtuple('isPublished', ['id', 'title', 'content', 'published_at', 'is_published', 'category_id', 'views'])
ispublished = connect.select_is_published()

for publish in ispublished:
    isPublish = isPublished(*publish)
    print(f"{isPublish.id} | {isPublish.title} | {isPublish.content} | {isPublish.published_at} | {isPublish.is_published} | {isPublish.category_id} | {isPublish.views}")

print("\n- - - - - - - - - - - - - - - - - - - - -\n")

# 6.4
Views = namedtuple('Views', ['id', 'title', 'content'])
selectViews = connect.select_views()

if not selectViews:
    print("Ma'lumot topilmadi.")
else:
    for view in selectViews:
        View = Views(*view)
        print(f"{View.id} | {View.title} | {View.content}")

print("\n- - - - - - - - - - - - - - - - - - - - -\n")

# 6.5
Author = namedtuple('Author', ['id', 'author_name', 'comment_text'])
authors = connect.select_author_name()

for author in authors:
    auth = Author(*author)
    print(f"{auth.id} | {auth.author_name} | {auth.comment_text}")

print("\n- - - - - - - - - - - - - - - - - - - - -\n")

# 6.8
allCategories = namedtuple('allCategories', ['name', 'count'])
all_categories = connect.select_all_categories()

for category in all_categories:
    allCategory = allCategories(*category)
    print(f"{allCategory.name} | {allCategory.count}")

# 7

connect.unique_title()