from django.shortcuts import render

# home画面遷移時のView
def home(request):
    #テンプレートエンジンにコンテキストとしてDictionaryを用意する
    #context_dict = {'boldmessage' : "Welcome to AGEs!!!"}
    context_dict = {}
    # Client側にレンダリングしたresponseを送る
    return render(request, 'AGEs/home.html', context_dict)

# about画面遷移時のView
def about(request):
    #テンプレートエンジンにコンテキストとしてDictionaryを用意する
    #context_dict = {'boldmessage' : "Welcome to AGEs!!!"}
    context_dict = {}
    # Client側にレンダリングしたresponseを送る
    return render(request, 'AGEs/whatsages.html', context_dict)
