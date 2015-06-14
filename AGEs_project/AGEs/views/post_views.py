from django.shortcuts import render
from AGEs.forms import PersonForm, PictureForm
from AGEs.views.person_views import person
from AGEs.models import Category, Item

def add_person(request):
    
    # FIXME: Personオブジェクトを取得する(このやり方はあまりよくない気がする）
    try:
        category = Category.objects.get(category_name='Person')
    except Category.DoesNotExist:
        category = None
        
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PersonForm(request.POST)
        
        # 妥当なFormの場合
        if form.is_valid():
            # TODO: Personをデータベースに保村する(イコールにする意味がわからない)
            # ここでFalseにするのがポイント？TrueだとCategoryを持ってないからエラーになる
            item = form.save(commit=False)
            
            # Personのcategoryに取得したcategoryをセットする
            if category:
                item.category = category
                item.num_of_pictures = 0
                # TOOD: DBへの保存については再度学習する必要あり
                # FIXME: person_nameとperson_idが同じだとエラーになる、なぜだかわからない。同時エラー処理も書かなくてはいけない
                item.save()
                # person_views.pyのpersonを呼び出す
                # UserはPersonが追加された画面を確認できる
                return person(request)
           
        else:
            # TODO: errorが表示される?
            print (form.errors)
            
    else:
        # TODO: もしリクエストがPOSTでない場合は、formを再表示する?
        form = PersonForm()
        
    # TODO: フォームがない場合は、再表示？    
    return render(request, 'AGEs/upload.html', {'form':form})

def add_picture(request, slug):
    # FIXME: Itemオブジェクトを取得する(このやり方はあまりよくない気がする）
    try:
        person = Item.objects.get(slug=slug)
    except Category.DoesNotExist:
        category = None
        
    # 登録が成功したかを示す変数（成功した場合はTrueになる）
    registered = False

    # HTTP POSTの時は下記処理に移る
    if request.method == 'POST':
        # PictureFormの情報を取得する
        form = PictureForm(data=request.POST)

        # formが有効ならば。。。
        if form.is_valid():
            # formのデータをDBに登録する
            picture = form.save()

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'image' in request.FILES:
                picture.image = request.FILES['picture']

            # Now we save the UserProfile model instance.
            picture.save()
            
            # FIXME: Pictureのitemに取得したpersonをセットする
            if person:
                picture.item = person
                # TOOD: DBへの保存については再度学習する必要あり
                picture.save()
            
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        form = PictureForm()

    # Render the template depending on the context.
    return render(request,
            'AGEs/upload_picture.html',
            {'form': form, 'registered': registered} )