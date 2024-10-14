#include <iostream>
using namespace std;
int square(int a,int b){
    //Данная вункция получает на вход 2 параметра : длинну и ширину прямоугольника, на выход она выдает площадь
    return(a*b);
}
int perimetr(int a,int b){
    //Данная вункция получает на вход 2 параметра : длинну и ширину прямоугольника, на выход она выдает периметр
    return((a+b)*2);
}
int main(){
    int a,b,c,d;
    cin>>a>>b;
    c = square(a,b);
    d = perimetr(a,b);
}