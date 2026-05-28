
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime
import xlwt
from django.http import HttpResponse


from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import datetime
import seaborn as sns
from sklearn.metrics import confusion_matrix

sns.set_style('darkgrid')



# Create your views here.
from Remote_User.models import ClientRegister_Model,Crime_details,Crime_type,detection_ratio,detection_accuracy


def serviceproviderlogin(request):
    if request.session.get('is_service_provider'):
        return redirect('View_Remote_Users')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            from django.contrib import messages
            messages.error(request, 'Please provide both username and password.')
            return render(request, 'SProvider/serviceproviderlogin.html')
        
        # Hardcoded admin credentials for now
        if username == "Admin" and password == "Admin":
            request.session['is_service_provider'] = True
            request.session['provider_name'] = 'Admin'
            from django.contrib import messages
            messages.success(request, 'Welcome, Admin!')
            return redirect('View_Remote_Users')
        else:
            from django.contrib import messages
            messages.error(request, 'Invalid credentials.')
    
    return render(request, 'SProvider/serviceproviderlogin.html')

def serviceprovider_logout(request):
    if 'is_service_provider' in request.session:
        del request.session['is_service_provider']
    if 'provider_name' in request.session:
        del request.session['provider_name']
    from django.contrib import messages
    messages.success(request, 'Logged out successfully!')
    return redirect('index')

def Find_Crime_Type_Ratio(request):
    if not request.session.get('is_service_provider'):
        from django.contrib import messages
        messages.error(request, 'Unauthorized access. Please login as service provider.')
        return redirect('serviceproviderlogin')
    
    detection_ratio.objects.all().delete()
    ratio = ""
    kword = 'Theft'
    print(kword)
    obj = Crime_type.objects.all().filter(Q(CTYPE=kword))
    obj1 = Crime_type.objects.all()
    count = obj.count();
    count1 = obj1.count();
    ratio = (count / count1) * 100
    if ratio != 0:
        detection_ratio.objects.create(names=kword, ratio=ratio)

    ratio1 = ""
    kword1 = 'Damage to Private Property'
    print(kword1)
    obj1 = Crime_type.objects.all().filter(Q(CTYPE=kword1))
    obj11 = Crime_type.objects.all()
    count1 = obj1.count();
    count11 = obj11.count();
    ratio1 = (count1 / count11) * 100
    if ratio1 != 0:
        detection_ratio.objects.create(names=kword1, ratio=ratio1)

    ratio12 = ""
    kword12 = 'Drugs Consuption'
    print(kword12)
    obj12 = Crime_type.objects.all().filter(Q(CTYPE=kword12))
    obj112 = Crime_type.objects.all()
    count12 = obj12.count();
    count112 = obj112.count();
    ratio12 = (count12 / count112) * 100
    if ratio12 != 0:
        detection_ratio.objects.create(names=kword12, ratio=ratio12)

    ratio123 = ""
    kword123 = 'Robbery or Threats'
    print(kword123)
    obj123 = Crime_type.objects.all().filter(Q(CTYPE=kword123))
    obj1123 = Crime_type.objects.all()
    count123 = obj123.count();
    count1123 = obj1123.count();
    ratio123 = (count123 / count1123) * 100
    if ratio123 != 0:
        detection_ratio.objects.create(names=kword123, ratio=ratio123)

    ratio1234 = ""
    kword1234 = 'Assult or Accident or Harassment'
    print(kword1234)
    obj1234 = Crime_type.objects.all().filter(Q(CTYPE=kword1234))
    obj11234 = Crime_type.objects.all()
    count1234 = obj1234.count();
    count11234 = obj11234.count();
    ratio1234 = (count1234 / count11234) * 100
    if ratio1234 != 0:
        detection_ratio.objects.create(names=kword1234, ratio=ratio1234)

    ratio12341 = ""
    kword12341 = 'Shoplifting or Weapon Carring'
    print(kword12341)
    obj12341 = Crime_type.objects.all().filter(Q(CTYPE=kword12341))
    obj112341 = Crime_type.objects.all()
    count12341 = obj12341.count();
    count112341 = obj112341.count();
    ratio12341 = (count12341 / count112341) * 100
    if ratio12341 != 0:
        detection_ratio.objects.create(names=kword12341, ratio=ratio12341)

    ratio333 = ""
    kword123412 = 'Fire or Injury or Accident'
    print(kword123412)
    obj111 = Crime_type.objects.all().filter(Q(CTYPE=kword123412))
    obj1111 = Crime_type.objects.all()
    count222 = obj111.count();
    count2222 = obj1111.count();
    ratio333 = (count222 / count2222) * 100
    if ratio333 != 0:
        detection_ratio.objects.create(names=kword123412, ratio=ratio333)

    obj = detection_ratio.objects.all()
    return render(request, 'SProvider/Find_Crime_Type_Ratio.html', {'objs': obj})

def View_Remote_Users(request):
    if not request.session.get('is_service_provider'):
        from django.contrib import messages
        messages.error(request, 'Unauthorized access. Please login as service provider.')
        return redirect('serviceproviderlogin')
    
    obj = ClientRegister_Model.objects.all()
    return render(request, 'SProvider/View_Remote_Users.html', {'objects': obj})

def ViewTrendings(request):
    topic = Crime_type.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def charts(request,chart_type):
    chart1 = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def charts1(request,chart_type):
    chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def Predict_Crime_Type(request):
    if not request.session.get('is_service_provider'):
        from django.contrib import messages
        messages.error(request, 'Unauthorized access. Please login as service provider.')
        return redirect('serviceproviderlogin')
    
    obj = Crime_type.objects.all()
    return render(request, 'SProvider/Predict_Crime_Type.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts =detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})


def Download_Trained_DataSets(request):

    response = HttpResponse(content_type='application/ms-excel')
    # decide file name
    response['Content-Disposition'] = 'attachment; filename="TrainedData.xls"'
    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')
    # adding sheet
    ws = wb.add_sheet("sheet1")
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True
    # writer = csv.writer(response)
    obj = Crime_type.objects.all()
    data = obj  # dummy method to fetch data.
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.INCIDENT_NUMBER, font_style)
        ws.write(row_num, 1, my_row.OFFENSE_CODE, font_style)
        ws.write(row_num, 2, my_row.OFFENSE_CODE_GROUP, font_style)
        ws.write(row_num, 3, my_row.OFFENSE_DESCRIPTION, font_style)
        ws.write(row_num, 4, my_row.DISTRICT, font_style)
        ws.write(row_num, 5, my_row.REPORTING_AREA, font_style)
        ws.write(row_num, 6, my_row.OCCURRED_ON_DATE, font_style)
        ws.write(row_num, 7, my_row.YEAR, font_style)
        ws.write(row_num, 8, my_row.MONTH, font_style)
        ws.write(row_num, 9, my_row.DAY_OF_WEEK, font_style)
        ws.write(row_num, 10, my_row.Hour, font_style)
        ws.write(row_num, 11, my_row.UCR_PART, font_style)
        ws.write(row_num, 12, my_row.STREET, font_style)
        ws.write(row_num, 13, my_row.Lat, font_style)
        ws.write(row_num, 14, my_row.Long1, font_style)
        ws.write(row_num, 15, my_row.Location, font_style)
        ws.write(row_num, 16, my_row.CTYPE, font_style)
    wb.save(response)
    return response

def train_model(request):
    if not request.session.get('is_service_provider'):
        from django.contrib import messages
        messages.error(request, 'Unauthorized access. Please login as service provider.')
        return redirect('serviceproviderlogin')
    
    detection_accuracy.objects.all().delete()


    df_codes = pd.read_csv('offense_codes.csv', encoding='ISO-8859-1')
    df_codes.head()
    df = pd.read_csv('crime.csv', encoding='ISO-8859-1')
    df.head()
    df.isnull().sum()
    df.drop(['DISTRICT', 'SHOOTING', 'UCR_PART', 'STREET', 'Lat', 'Long'], axis=1, inplace=True)
    sorted(df['REPORTING_AREA'].unique())[:10]
    ## replace empty reporting areas with '-1'
    df['REPORTING_AREA'] = df['REPORTING_AREA'].str.replace(' ', '-1')
    sorted(df['REPORTING_AREA'].unique())
    df['REPORTING_AREA'] = df['REPORTING_AREA'].astype(int)
    # code day of week to ints
    df['OCCURRED_ON_DATE'] = pd.to_datetime(df['OCCURRED_ON_DATE'])
    df['DAY_OF_WEEK'] = df['OCCURRED_ON_DATE'].dt.dayofweek
    df['OFFENSE_CODE_GROUP'].value_counts().plot(kind='bar', figsize=(20, 5), title='Offense Code Group Counts')
    df_new = df.copy(deep=True)
    df_new['MV'] = np.where(df_new['OFFENSE_CODE_GROUP'] == 'Motor Vehicle Accident Response', 1, 0)
    df_new.head()
    df_mv = df_new[['MV', 'REPORTING_AREA', 'YEAR', 'MONTH', 'DAY_OF_WEEK', 'HOUR']]
    df_mv.head()

    # LogisticRegression

    print("Logistic Regression")
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import mean_squared_error, r2_score
    # shuffle the data if you want
    df_mv = df_mv.sample(frac=1).reset_index(drop=True)
    X = df_mv[df_mv.columns[1:]]
    y = df_mv['MV']
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
    y_pred = reg.predict(X_test)

    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix, f1_score

    print("ACCURACY")
    print(accuracy_score(y_test, y_pred) * 100)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, y_pred))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, y_pred))

    detection_accuracy.objects.create(names="Logistic Regression",ratio=accuracy_score(y_test, y_pred) * 100)

    # SVM Model
    print("SVM")
    from sklearn import svm
    lin_clf = svm.LinearSVC()
    lin_clf.fit(X_train, y_train)
    predict_svm = lin_clf.predict(X_test)
    svm_acc = accuracy_score(y_test, predict_svm) * 100
    print(svm_acc)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, predict_svm))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, predict_svm))
    detection_accuracy.objects.create(names="SVM",ratio=svm_acc)

    ## To get more output about coefficients of logistic regression use statsmodels to perform same logistic regression

    import statsmodels.discrete.discrete_model as sm
    from statsmodels.tools.tools import add_constant

    # statsmodels doesn't include a constant by default
    # sklearn.linear_model DOES include a constant by default
    X_ols = add_constant(X)

    sm.Logit(y, X_ols).fit().summary()
    df_knn = df[df['OFFENSE_CODE_GROUP'].isin(list(df['OFFENSE_CODE_GROUP'].value_counts()[:3].index))].copy(deep=True)

    # KNeighborsClassifier

    print("KNeighbors Classifier::")

    from sklearn.preprocessing import LabelEncoder
    from sklearn.neighbors import KNeighborsClassifier

    lb_make = LabelEncoder()
    df_knn['office_code_lbl'] = lb_make.fit_transform(df_knn['OFFENSE_CODE_GROUP'])

    df_knn = df_knn[['office_code_lbl', 'REPORTING_AREA', 'YEAR', 'MONTH', 'DAY_OF_WEEK', 'HOUR']]

    X = df_knn[['REPORTING_AREA', 'YEAR', 'MONTH', 'DAY_OF_WEEK', 'HOUR']]
    y = df_knn['office_code_lbl']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    neighbors_list = np.arange(1, 5)
    scores = []
    for n_neighbors in neighbors_list:
        knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        knn.fit(X_train, y_train)
        knn_pred = knn.predict(X_test)
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import confusion_matrix, f1_score
        if (n_neighbors == 1):
            print("Accuracy::")
            print(accuracy_score(y_test, knn_pred) * 100)
            print("CLASSIFICATION REPORT")
            print(classification_report(y_test, knn_pred))
            print("CONFUSION MATRIX")
            print(confusion_matrix(y_test, knn_pred))
            detection_accuracy.objects.create(names="KNeighbors Classifier",ratio=accuracy_score(y_test, knn_pred) * 100)


    ct=''
    obj1 = Crime_details.objects.values('INCIDENT_NUMBER',
    'OFFENSE_CODE',
    'OFFENSE_CODE_GROUP',
    'OFFENSE_DESCRIPTION',
    'DISTRICT',
    'REPORTING_AREA',
    'OCCURRED_ON_DATE',
    'YEAR',
    'MONTH',
    'DAY_OF_WEEK',
    'Hour',
    'UCR_PART',
    'STREET',
    'Lat',
    'Long1',
    'Location')
    Crime_type.objects.all().delete()
    for t in obj1:

        INCIDENT_NUMBER= t['INCIDENT_NUMBER']
        OFFENSE_CODE= t['OFFENSE_CODE']
        OFFENSE_CODE_GROUP= t['OFFENSE_CODE_GROUP']
        OFFENSE_DESCRIPTION= t['OFFENSE_DESCRIPTION']
        DISTRICT= t['DISTRICT']
        REPORTING_AREA= t['REPORTING_AREA']
        OCCURRED_ON_DATE= t['OCCURRED_ON_DATE']
        YEAR= t['YEAR']
        MONTH= t['MONTH']
        DAY_OF_WEEK= t['DAY_OF_WEEK']
        Hour= t['Hour']
        UCR_PART= t['UCR_PART']
        STREET= t['STREET']
        Lat= t['Lat']
        Long1= t['Long1']
        Location= t['Location']


        for f in OFFENSE_DESCRIPTION.split():
            if f in ('THEFT','LOST','LARCENY'):
                ct = 'Theft'
            elif f in ('VANDALISM','DAMAGE'):
                ct = 'Damage to Private Property'
            elif f in ('FIRE','INJURY','ACCIDENT','INJURED'):
                ct = 'Fire or Injury or Accident'
            elif f in ('DRUGS'):
                ct = 'Drugs Consuption'
            elif f in ('ROBBERY','THREATS','FRAUD'):
                ct = 'Robbery or Threats'
            elif f in ('ASSAULT','ACCIDENT','HARASSMENT','BURGLARY','TRESPASSING'):
                ct = 'Assult or Accident or Harassment'
            elif f in ('SHOPLIFTING','WEAPON'):
                ct = 'Shoplifting or Weapon Carring'


        Crime_type.objects.create(
            INCIDENT_NUMBER=INCIDENT_NUMBER,
            OFFENSE_CODE=OFFENSE_CODE,
            OFFENSE_CODE_GROUP=OFFENSE_CODE_GROUP,
            OFFENSE_DESCRIPTION=OFFENSE_DESCRIPTION,
            DISTRICT=DISTRICT,
            REPORTING_AREA=REPORTING_AREA,
            OCCURRED_ON_DATE=OCCURRED_ON_DATE,
            YEAR=YEAR,
            MONTH=MONTH,
            DAY_OF_WEEK=DAY_OF_WEEK,
            Hour=Hour,
            UCR_PART=UCR_PART,
            STREET=STREET,
            Lat=Lat,
            Long1=Long1,
            Location=Location,
            CTYPE=ct)

    obj = detection_accuracy.objects.all()
    return render(request,'SProvider/train_model.html', {'objs': obj})