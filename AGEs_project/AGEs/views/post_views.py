from django.shortcuts import render
from AGEs.forms import PersonForm, PictureForm
from AGEs.views.item_views import show_person, show_object
from AGEs.models import Category, Item
from django.core.exceptions import ValidationError

def add_person(request):
    
    # Categoryオブジェクトを取得する
    category = getCategory('Person')

    # HTTP POSTの場合
    if request.method == 'POST':
        # Formを取得する
        form = PersonForm(request.POST)
        
        # 入力値が妥当かどうかをチェック
        if form.is_valid():
            # Falseにすることインスタンスを取得する。TrueだとCategoryを持ってないからエラーになる
            item = form.save(commit=False)
            
            # Personのcategoryに取得したcategoryをセットする
            if category:
                item.category = category
                item.num_of_pictures = 0
                # TOOD: DBへの保存については再度学習する必要あり
                # FIXME: person_nameとperson_idが同じだとエラーになる、なぜだかわからない。同時エラー処理も書かなくてはいけない
                item.save()
                # item_views.pyのpersonを呼び出す
                # UserはPersonが追加された画面を確認できる
                return show_person(request)
           
        else:
            # TODO: errorが表示される?
            print (form.errors)
            
    else:
        # TODO: もしリクエストがPOSTでない場合は、formを再表示する?
        form = PersonForm()
        
    # TODO: フォームがない場合は、再表示？    
    return render(request, 'AGEs/person_upload.html', {'form':form})

def add_object(request):

    # Categoryオブジェクトを取得する
    category = getCategory('Object')

    # HTTP POSTの場合
    if request.method == 'POST':
        # Formを取得する
        form = PersonForm(request.POST)

        # 入力値が妥当かどうかをチェック
        if form.is_valid():
            # Falseにすることインスタンスを取得する。TrueだとCategoryを持ってないからエラーになる
            item = form.save(commit=False)

            # Personのcategoryに取得したcategoryをセットする
            if category:
                item.category = category
                item.num_of_pictures = 0
                # TOOD: DBへの保存については再度学習する必要あり
                # FIXME: person_nameとperson_idが同じだとエラーになる、なぜだかわからない。同時エラー処理も書かなくてはいけない
                item.save()
                # person_views.pyのobjectを呼び出す
                # UserはObjectが追加された画面を確認できる
                return show_object(request)

        else:
            # TODO: errorが表示される?
            print (form.errors)

    else:
        # TODO: もしリクエストがPOSTでない場合は、formを再表示する?
        form = PersonForm()

    # TODO: フォームがない場合は、再表示？
    return render(request, 'AGEs/object_upload.html', {'form':form})

def add_person_picture(request, id):
    # FIXME: Itemオブジェクトを取得する(このやり方はあまりよくない気がする）
    try:
        person = Item.objects.get(id=id)
    except Item.DoesNotExist:
        person = None
        
    # 登録が成功したかを示す変数（成功した場合はTrueになる）
    registered = False

    # HTTP POSTの時は下記処理に移る
    if request.method == 'POST':
        # PictureFormの情報を取得する、request.FILESを書かないとImageは取得できない
        form = PictureForm(request.POST, request.FILES)

        try:
            # formが有効ならば。。。
            if form.is_valid():
                # formのデータをDBに登録する
                picture = form.save(commit=False)

                # Itemオブジェクトのnum_of_picturesの値を1増やして、DBに保存する
                person.num_of_pictures += 1
                person.save()

                picture.item = person

                # Did the user provide a profile picture?
                # If so, we need to get it from the input form and put it in the UserProfile model.
                if 'image' in request.FILES:
                    picture.image = request.FILES['image']
                    # 画像サイズが2MBより大きい場合はエラー
                    if picture.image.size > 2*1024*1024:
                        raise ValidationError("Max file size is %sMB" % str(2))

                picture.save()
                # Update our variable to tell the template registration was successful.
                registered = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
            else:
                print (form.errors)

        except ValidationError:
            print (form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        form = PictureForm()

    # Render the template depending on the context.
    return render(request,
            'AGEs/person_picture_upload.html',
            {'form': form, 'registered': registered, 'id':id} )


def add_object_picture(request, id):
    # FIXME: Itemオブジェクトを取得する(このやり方はあまりよくない気がする）
    try:
        person = Item.objects.get(id=id)
    except Item.DoesNotExist:
        person = None

    # 登録が成功したかを示す変数（成功した場合はTrueになる）
    registered = False

    # HTTP POSTの時は下記処理に移る
    if request.method == 'POST':
        # PictureFormの情報を取得する
        form = PictureForm(request.POST, request.FILES)

        try:
            # formが有効ならば。。。
            if form.is_valid():
                # formのデータをDBに登録する
                picture = form.save(commit=False)

                # Itemオブジェクトのnum_of_picturesの値を1増やして、DBに保存する
                person.num_of_pictures += 1
                person.save()

                picture.item = person

                # Did the user provide a profile picture?
                # If so, we need to get it from the input form and put it in the UserProfile model.
                if 'image' in request.FILES:
                    picture.image = request.FILES['image']
                    # 画像サイズが2MBより大きい場合はエラー
                    if picture.image.size > 2*1024*1024:
                        raise ValidationError("Max file size is %sMB" % str(2))

                picture.save()
                # Update our variable to tell the template registration was successful.
                registered = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
            else:
                print (form.errors)

        except ValidationError:
            print (form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        form = PictureForm()

    # Render the template depending on the context.
    return render(request,
            'AGEs/object_picture_upload.html',
            {'form': form, 'registered': registered, 'id':id} )


def getCategory(categoryName):
    '''
    :param categoryName:
        引数の文字列からCategoryオブジェクトを取得し、返す
    :return:
        取得したcategory
    '''
    try:
        # PersonオブジェクトにセットするCategoryオブジェクトを取得する
        category = Category.objects.get(category_name=categoryName)
    except Category.DoesNotExist:
        # 取得できなかった場合はNoneをセットする
        category = None

    return category
