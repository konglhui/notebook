![mark](http://p6yio0wew.bkt.clouddn.com/blog/180529/A0LhGfFaj4.png)

## 3.2

```c++
	string s;    
	while(getline(cin,s))
        cout <<s<<endl;
        
    while(cin>>s)
        cout<<s<<endl;
```

## 3.3

string类的输入时判断段空白符就停止

getline的输入时判断换行符停止

## 3.4

```c++
    string s1,s2;
    cin >>s1>>s2;
    if(s1 != s2){
        if (s1>s2)
            cout<< s1<<endl;
        else{
            cout << s2<<endl;
        }

    }
    return 0;
//2
    string s1,s2;
    cin >>s1>>s2;
    if(s1.size() != s2.size()){
        if (s1.size()>s2.size())
            cout<< s1<<endl;
        else{
            cout << s2<<endl;
        }

    }
    return 0;
```

## 3.5

```c++
    string s1,s2,s3,s4;
    cin>>s1>>s2>>s3>>s4;
    s1 += s2;
    s1 += s3;
    s1 += s4;
    cout <<s1;

    return 0;
//2
    string s1,s2,s3,s4;
    cin>>s1>>s2>>s3>>s4;
    s1 = s1 +" "+s2;
    s1 = s1+" "+s3;
    s1 = s1+" "+s4;
    cout <<s1;

    return 0;
```



