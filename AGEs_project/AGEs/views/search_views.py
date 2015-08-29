from django.shortcuts import render
from AGEs.forms import PersonSearchForm
from AGEs.forms import PictureSearchForm

#Search後のPerson画面遷移時のView
from AGEs.models import Item, Category
def search_person(request):
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PersonSearchForm(request.POST)

        item_list = None
        # 入力データが適切かどうかを判断
        if form.is_valid():
            name = form.cleaned_data['item_name']
            person = Category.objects.filter(category_name = 'Person')
            try:
                # 入力された名前からDBを検索(categoryがpersonのものだけ、__icontainsでlike検索(大小区別しない))
                items = Item.objects.filter(category = person).filter(item_name__icontains = name)\
                    .order_by('-num_of_pictures')
                item_list = items
            except Exception: # FIXME: 例外レベルが高いから修正の必要あり
                pass

        context_dict = {'items' : item_list}

    return render(request, 'AGEs/person.html', context_dict)

from AGEs.models import Picture
def search_person_picture(request, id):
    # コンテキスト用の辞書を準備
    context_dict = {}
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PictureSearchForm(request.POST)

        picture_list = None
        # 入力データが適切かどうかを判断
        if form.is_valid():
            age = form.cleaned_data['age']
            try:
                item = Item.objects.get(id=id)
                context_dict['item_name'] = item.item_name
                context_dict['id'] = id
                pictures = Picture.objects.filter(age = age).order_by('-age')
                picture_list = pictures
            except Exception: # FIXME: 例外レベルが高いから修正の必要あり
                pass

        context_dict['pictures'] = picture_list

    # TODO: フォームがない場合は、再表示？
    return render(request, 'AGEs/person_pictures.html', context_dict)

#Search後のPerson画面遷移時のView
def search_object(request):
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PersonSearchForm(request.POST)

        item_list = None
        # 入力データが適切かどうかを判断
        if form.is_valid():
            name = form.cleaned_data['item_name']
            person = Category.objects.filter(category_name = 'Object')
            try:
                # 入力された名前からDBを検索(categoryがpersonのものだけ、__icontainsでlike検索(大小区別しない))
                items = Item.objects.filter(category = person).filter(item_name__icontains = name)\
                    .order_by('-num_of_pictures')
                item_list = items
            except Exception: # FIXME: 例外レベルが高いから修正の必要あり
                pass

        context_dict = {'items' : item_list}

    return render(request, 'AGEs/object.html', context_dict)

def search_object_picture(request, id):
    # コンテキスト用の辞書を準備
    context_dict = {}
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PictureSearchForm(request.POST)

        picture_list = None
        # 入力データが適切かどうかを判断
        if form.is_valid():
            age = form.cleaned_data['age']
            try:
                item = Item.objects.get(id=id)
                context_dict['item_name'] = item.item_name
                context_dict['id'] = id
                pictures = Picture.objects.filter(age = age).order_by('-age')
                picture_list = pictures
            except Exception: # FIXME: 例外レベルが高いから修正の必要あり
                pass

        context_dict['pictures'] = picture_list

    # TODO: フォームがない場合は、再表示？
    return render(request, 'AGEs/object_pictures.html', context_dict)
